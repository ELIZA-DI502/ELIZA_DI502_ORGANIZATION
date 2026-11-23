"""One-off preparation (D5): embeds the chunks and writes the Chroma vector store to data/vector-store/.

Run once on the host, from the repository root, before the first `docker compose up`:

    pip install -r rag/requirements.txt
    python rag/ingest.py

It does the same as steps 8 and 9 of src/embedding.ipynb, with the settings of config/rag.yaml.
The chunks come from data/chunks.jsonl, written by src/chunking.ipynb (D7, D8); moving the chunking
itself into this script is still open.
"""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rag.app.config import CHUNKS_PATH, CONFIG, VECTOR_STORE_PATH  # noqa: E402

KEEP = ["ref", "parent", "kind", "number", "title", "heading", "version_date", "celex", "embed_text"]


def main():
    import chromadb
    from sentence_transformers import SentenceTransformer

    chunks = [json.loads(line) for line in CHUNKS_PATH.open(encoding="utf-8")]
    print(len(chunks), "chunks read from", CHUNKS_PATH.relative_to(CHUNKS_PATH.parents[1]))

    emb = CONFIG["embedding"]
    if emb.get("remove_before_embedding", "none") != "none":
        sys.exit("remove_before_embedding is not 'none' in config/rag.yaml; this script does not support it yet")
    model = SentenceTransformer(emb["model"], device="cpu")
    vectors = model.encode([c["embed_text"] for c in chunks], normalize_embeddings=True, show_progress_bar=True)
    print(emb["model"], "->", vectors.shape)

    shutil.rmtree(VECTOR_STORE_PATH, ignore_errors=True)       # start from an empty store, as the notebook does
    store = chromadb.PersistentClient(path=str(VECTOR_STORE_PATH))
    col = store.create_collection("chunks", metadata={"hnsw:space": "cosine"})   # D11
    col.add(ids=[c["chunk_id"] for c in chunks], embeddings=vectors.tolist(),
            documents=[c["text"] for c in chunks],
            metadatas=[{k: str(c.get(k, "")) for k in KEEP} for c in chunks])
    print(col.count(), "chunks stored in", VECTOR_STORE_PATH)


if __name__ == "__main__":
    main()
