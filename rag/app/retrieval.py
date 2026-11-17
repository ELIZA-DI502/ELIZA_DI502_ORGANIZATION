"""Retriever (D11, D13, D14): the search of src/rag_vs_no_rag.ipynb (cell "search"), moved into a module.

Dense search: the question's bge-m3 vector against the Chroma store in data/vector-store/ (D11, cosine
distance), written once by rag/ingest.py. Keyword search: BM25 on the chunks' embed_text without stopwords
and jury words. The two lists are merged by weighted Reciprocal Rank Fusion with the settings of
config/rag.yaml. The steps and their order follow the notebook, so the same question gets the same chunks;
rag/verify_val.py checks this against docs/eval/answers/val-with-retrieval-llama-3-1-8b.csv.
"""
import os
import re
from collections import Counter

import numpy as np

from .config import CHUNKS, CONFIG, VECTOR_STORE_PATH

R = CONFIG["retrieval"]
words = lambda text: re.findall(r"[a-z0-9]+", text.lower())


class Retriever:
    def __init__(self, chunks=CHUNKS):
        # Heavy imports only here, so the service can start (and answer in no_rag mode) before they are loaded.
        import chromadb
        import torch
        from rank_bm25 import BM25Okapi
        from sentence_transformers import SentenceTransformer
        from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

        if not VECTOR_STORE_PATH.exists():
            raise FileNotFoundError(f"vector store not found at {VECTOR_STORE_PATH}; run rag/ingest.py first")
        self.col = chromadb.PersistentClient(path=str(VECTOR_STORE_PATH)).get_collection("chunks")
        stored = set(self.col.get(include=[])["ids"])
        if stored != {c["chunk_id"] for c in chunks}:
            raise RuntimeError("the vector store does not hold the chunks of data/chunks.jsonl; run rag/ingest.py again")

        self.chunks = chunks
        self.by_chunk = {c["chunk_id"]: c for c in chunks}
        self.ids = [c["chunk_id"] for c in chunks]
        self.remove = (set(ENGLISH_STOP_WORDS) - {"not", "no", "nor"}) | set(CONFIG["bm25"]["jury_words"])
        self.bm25 = BM25Okapi([[w for w in words(c["embed_text"]) if w not in self.remove] for c in chunks])
        device = os.environ.get("EMBED_DEVICE") or ("cuda" if torch.cuda.is_available() else "cpu")
        self.embedder = SentenceTransformer(CONFIG["embedding"]["model"], device=device)

    def search(self, question, k=None):
        """The k chunks of the chosen search (D14), best first."""
        k = k or R["top_k"]
        query = self.embedder.encode([question], normalize_embeddings=True)[0]
        dense = self.col.query(query_embeddings=[query.tolist()], n_results=R["candidates"])["ids"][0]
        keyword = [self.chunks[n]["chunk_id"] for n in np.argsort(-self.bm25.get_scores(
            [w for w in words(question) if w not in self.remove]))][:R["candidates"]]
        fused = Counter()
        for weight, ranked in ((R["dense_weight"], dense), (1 - R["dense_weight"], keyword)):
            for rank, cid in enumerate(ranked, 1):
                fused[cid] += weight / (R["rrf_k"] + rank)
        return [self.by_chunk[cid] for cid, _ in fused.most_common(k)]
