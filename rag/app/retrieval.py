"""Retriever (D13, D14): bge-m3 vector search in Chroma and BM25 keyword search, merged by weighted
Reciprocal Rank Fusion. The same search as step 10 of src/embedding.ipynb, with the settings of
config/rag.yaml. The keyword index is rebuilt from the vector store each time the service starts.
"""
import json
import re
from collections import Counter

import numpy as np

from .config import CHUNKS_PATH, CONFIG, VECTOR_STORE_PATH

words = lambda text: re.findall(r"[a-z0-9]+", text.lower())   # same tokenizer as the notebook


def _bm25_removed_words():
    from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
    remove = set()
    setting = CONFIG["bm25"]["remove"]
    if "stopwords" in setting:
        remove |= set(ENGLISH_STOP_WORDS) - {"not", "no", "nor"}
    if "jury" in setting:
        remove |= set(CONFIG["bm25"]["jury_words"])
    return remove


class Retriever:
    def __init__(self):
        # Heavy imports only here, so the service can start (and answer in no_rag mode) without them loaded.
        import chromadb
        from rank_bm25 import BM25Okapi
        from sentence_transformers import SentenceTransformer

        if not VECTOR_STORE_PATH.exists():
            raise FileNotFoundError(f"vector store not found at {VECTOR_STORE_PATH}; run rag/ingest.py first")
        self.col = chromadb.PersistentClient(path=str(VECTOR_STORE_PATH)).get_collection("chunks")
        stored = self.col.get(include=["documents", "metadatas"])
        if not stored["ids"]:
            raise RuntimeError("the vector store is empty; run rag/ingest.py first")

        # The notebook's store keeps only ref and version_date; the text that BM25 indexed (embed_text)
        # and the other fields come from data/chunks.jsonl when the store does not have them.
        extra = {}
        if CHUNKS_PATH.exists():
            extra = {c["chunk_id"]: c for c in map(json.loads, CHUNKS_PATH.open(encoding="utf-8"))}
        self.chunks = {}
        for cid, text, meta in zip(stored["ids"], stored["documents"], stored["metadatas"]):
            row = extra.get(cid, {})
            self.chunks[cid] = {
                "chunk_id": cid,
                "ref": meta.get("ref") or row.get("ref", cid),
                "version_date": meta.get("version_date") or row.get("version_date"),
                "text": text,
                "embed_text": meta.get("embed_text") or row.get("embed_text") or text,
            }
        # Same order as data/chunks.jsonl, so ties in BM25 break as in the notebook.
        self.ids = [cid for cid in extra if cid in self.chunks] + [cid for cid in self.chunks if cid not in extra]

        self.remove = _bm25_removed_words()
        self.bm25 = BM25Okapi([[w for w in words(self.chunks[i]["embed_text"]) if w not in self.remove] for i in self.ids])

        emb = CONFIG["embedding"]
        self.model = SentenceTransformer(emb["model"], device="cpu")
        # The bge v1.5 models expect the query instruction; bge-m3 uses none (D13).
        self.instruction = emb.get("query_instruction", "") if emb["model"].endswith("en-v1.5") else ""

        r = CONFIG["retrieval"]
        self.dense_weight = float(r["dense_weight"]) if r.get("mode", "hybrid") == "hybrid" else 1.0
        self.top_k, self.candidates, self.rrf_k = int(r["top_k"]), int(r["candidates"]), int(r["rrf_k"])

    def search(self, question, k=None):
        """The k most relevant chunks (dicts with chunk_id, ref, version_date, text), best first."""
        vector = self.model.encode([self.instruction + question], normalize_embeddings=True)[0]
        ranked = self.col.query(query_embeddings=[vector.tolist()], n_results=self.candidates)["ids"][0]
        if self.dense_weight < 1.0:
            scores = self.bm25.get_scores([w for w in words(question) if w not in self.remove])
            bm25_ids = [self.ids[n] for n in np.argsort(-scores)[:self.candidates]]   # as in the notebook
            fused = Counter()
            for weight, ids in ((self.dense_weight, ranked), (1 - self.dense_weight, bm25_ids)):
                for rank, cid in enumerate(ids, 1):
                    fused[cid] += weight / (self.rrf_k + rank)
            ranked = [cid for cid, _ in fused.most_common()]
        return [self.chunks[cid] for cid in ranked[:k or self.top_k]]
