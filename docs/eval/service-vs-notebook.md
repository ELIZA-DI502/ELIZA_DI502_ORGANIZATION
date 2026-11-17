# The RAG service against the notebook (KAN-122)

| Date | Author | Status |
|---|---|---|
| 17/11/2026 | Kaan | retrieval checked; answers not yet checked |

**Aim:** The search and the prompt of [`src/rag_vs_no_rag.ipynb`](../../src/rag_vs_no_rag.ipynb) (KAN-99, KAN-125) were moved into the RAG service ([`rag/app/retrieval.py`](../../rag/app/retrieval.py), [`rag/app/prompt.py`](../../rag/app/prompt.py), [`rag/app/llm.py`](../../rag/app/llm.py)). This page records that the service gives the notebook's results, so the demo answers with the baseline that was measured.

## Setup

- Questions: [`eval-set-v1-val.csv`](eval-set-v1-val.csv), 30 questions, 27 with `gold_ids` (SHA-256 starting `76f40134dae736ab`)
- Chunks: [`data/chunks.jsonl`](../../data/chunks.jsonl), 105 chunks of the consolidated text of 27/07/2026 (SHA-256 starting `375e9b2db6f6f956`)
- Reference: the chunks the notebook gave the model, column `retrieved` of [`answers/val-with-retrieval-llama-3-1-8b.csv`](answers/val-with-retrieval-llama-3-1-8b.csv) (commit `885800e`, 12/11/2026; SHA-256 starting `3d36bf69e6e30ca2`)
- Settings: [`config/rag.yaml`](../../config/rag.yaml): bge-m3, Chroma with cosine distance (D11), BM25 without stopwords and jury words, weighted RRF with dense weight 0.8, 20 candidates per list, `rrf_k` 60, top 8 (D13, D14)
- Vector store: written by [`rag/ingest.py`](../../rag/ingest.py) into `data/vector-store/`
- Computer: Linux x86-64, CPU only (the notebook ran on a Colab T4 GPU). Python 3.13.18 with the versions of [`requirements.txt`](../../requirements.txt): torch 2.15.0 (CPU build), sentence-transformers 6.2.0, transformers 5.22.2, chromadb 1.5.9, rank-bm25 0.2.2, scikit-learn 1.9.1, numpy 2.5.4

## Results

| Check | Result | Expected |
|---|---|---|
| Same 8 chunks in the same order as the notebook | **30 of 30** val questions | 30 of 30 |
| Recall@8 on the 27 questions with `gold_ids` | **0.59** | 0.59 (notebook) |
| Dense top 20 from Chroma and from the notebook's in-memory search (`vectors @ query`) | same list in the same order for 30 of 30 | — |
| Tokens of the `no_rag` prompt (all 105 chunks, `prompts/answer.yaml`, one question), Llama 3.1 tokenizer | **8,743** | below `NUM_CTX_ALL_CHUNKS` = 12,288 |

Per question: [`answers/val-service-retrieval.csv`](answers/val-service-retrieval.csv) (notebook chunks, service chunks, same).

The notebook ran its search in memory, while the service searches the Chroma store of D11. On these 105 chunks both give the same dense list, so the store does not change the results.

**Not yet checked:** the answers. `python rag/verify_val.py --answers` asks Ollama with the service's prompt and options (temperature 0, `num_predict` 300, seed 42, model of `config/rag.yaml`) and compares every answer with the saved one. An answer on another computer can differ in a few words from the notebook's (Colab T4 GPU), so the same chunks and the same prompt are the main check.

## How to run it again

From the repository root, in the environment of *Install* in the [README](../../README.md):

```bash
python rag/ingest.py
python rag/verify_val.py --retrieval-out docs/eval/answers/val-service-retrieval.csv
python rag/verify_val.py --answers        # with Ollama and the answer model on this computer
```

The script prints "30 of 30", "Recall@8 on 27 val questions: 0.59" and "OK" when the service retrieves exactly as the notebook.
