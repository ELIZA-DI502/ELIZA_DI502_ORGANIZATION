# The RAG service against the notebook (KAN-122)

| Date | Author | Status |
|---|---|---|
| 17/11/2026 | Kaan | retrieval checked on Linux and on a Mac; answers checked on the Mac |

**Aim:** The search and the prompt of [`src/rag_vs_no_rag.ipynb`](../../src/rag_vs_no_rag.ipynb) (KAN-99, KAN-125) were moved into the RAG service ([`rag/app/retrieval.py`](../../rag/app/retrieval.py), [`rag/app/prompt.py`](../../rag/app/prompt.py), [`rag/app/llm.py`](../../rag/app/llm.py)). This page records that the service gives the notebook's results, so the demo answers with the baseline that was measured.

## Setup

- Questions: [`eval-set-v1-val.csv`](eval-set-v1-val.csv), 30 questions, 27 with `gold_ids` (SHA-256 starting `76f40134dae736ab`)
- Chunks: [`data/chunks.jsonl`](../../data/chunks.jsonl), 105 chunks of the consolidated text of 27/07/2026 (SHA-256 starting `375e9b2db6f6f956`)
- Reference: the chunks the notebook gave the model, column `retrieved` of [`answers/val-with-retrieval-llama-3-1-8b.csv`](answers/val-with-retrieval-llama-3-1-8b.csv) (commit `885800e`, 12/11/2026; SHA-256 starting `3d36bf69e6e30ca2`)
- Settings: [`config/rag.yaml`](../../config/rag.yaml): bge-m3, Chroma with cosine distance (D11), BM25 without stopwords and jury words, weighted RRF with dense weight 0.8, 20 candidates per list, `rrf_k` 60, top 8 (D13, D14)
- One change from the notebook: the service sorts the BM25 scores with a stable sort (`np.argsort(-scores, kind="stable")`), see *Ties in the BM25 ranking* below
- Vector store: written by [`rag/ingest.py`](../../rag/ingest.py) into `data/vector-store/`
- Computers (the notebook ran on a Colab T4 GPU), both with the versions of [`requirements.txt`](../../requirements.txt) (torch 2.15.0, sentence-transformers 6.2.0, transformers 5.22.2, chromadb 1.5.9, rank-bm25 0.2.2, scikit-learn 1.9.1, numpy 2.5.4):
  - Linux x86-64, CPU only, Python 3.13.18
  - MacBook Pro, Apple M3 Pro, CPU, Python 3.13 (`.venv` of the README)

## Results

| Check | Result | Expected |
|---|---|---|
| Same 8 chunks in the same order as the notebook | **28 of 30** val questions on both computers (C-03 and D-10 differ) | the others only where BM25 has a tie at rank 20 |
| Same chunks on Linux and on the Mac | **30 of 30** | 30 of 30 |
| Recall@8 on the 27 questions with `gold_ids` | **0.59** on both computers | 0.59 (notebook) |
| Dense top 20 from Chroma and from the notebook's in-memory search (`vectors @ query`) | same list in the same order for 30 of 30 | — |
| Tokens of the `no_rag` prompt (all 105 chunks, `prompts/answer.yaml`, one question), Llama 3.1 tokenizer | **8,743** | below `NUM_CTX_ALL_CHUNKS` = 12,288 |

Per question: [`answers/val-service-retrieval.csv`](answers/val-service-retrieval.csv) (notebook chunks, service chunks, same, BM25 tie at rank 20).

The notebook ran its search in memory, while the service searches the Chroma store of D11. On these 105 chunks both give the same dense list, so the store does not change the results.

## Ties in the BM25 ranking

The first run of the service used the notebook's sort (`np.argsort(-scores)`). It gave the notebook's chunks for 30 of 30 questions on Linux (Intel), but for 27 of 30 on a Mac (Apple M3 Pro, 17/11/2026): A-02, C-03 and D-10 were different, with the same Recall@8 (0.59).

These are the questions whose BM25 scores have a tie at the edge of the 20 candidates. In A-02 and C-03, 103 of the 105 chunks score 0 (no keyword of the question), in D-10 89. The keyword list is still filled up to 20, so 18 chunks without any keyword get RRF points, and which ones depends on how the sort orders equal scores. NumPy's default sort does this differently on Intel and ARM processors, so the notebook's list for these questions came from the Colab processor and cannot be repeated on a Mac.

The service now uses a stable sort: equal scores keep the order of `data/chunks.jsonl`, so every computer gets the same chunks. Measured on `val` (Linux):

| BM25 sort | Recall@8 | Same as the notebook | Same on every computer |
|---|---|---|---|
| Notebook (`np.argsort(-scores)`) | 0.588 | 30 of 30 on Intel, 27 of 30 on the Mac | no |
| **Stable (service)** | **0.588** | **28 of 30** | yes |
| Stable, chunks with score 0 left out of the keyword list | 0.588 | 28 of 30 | yes |

With the stable sort, C-03 gets the same 8 chunks with two of them in the other order (ART3-9 and ART10-3), and D-10 gets ART2-1 in place of ART3-3. Leaving the chunks with score 0 out would be a change to the retrieval design (D14), so it is left to the owner of the retrieval. If the notebook also uses `kind="stable"`, the notebook and the service give the same chunks everywhere; the saved answers of C-03 and D-10 would then have to be made again.

## Answers

`python rag/verify_val.py --answers --out docs/eval/answers/val-service-answers.csv` asked every `val` question with the service's prompt and options (temperature 0, `num_predict` 300, seed 42) on the Mac (Apple M3 Pro, Metal; Ollama 0.40.11; model `hf.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF:Q4_K_M`, pulled on 17/11/2026), 17/11/2026. Answers: [`answers/val-service-answers.csv`](answers/val-service-answers.csv).

**14 of 30 answers are word for word the notebook's.** The others start the same and then take another word, for example "tasks" / "capabilities" (A-02), "behavior" / "behaviour" (D-01), "might apply" / "is relevant" (A-06); from that word on, the answer goes on differently. With temperature 0 the model takes the most likely word at every step; the notebook ran on an NVIDIA GPU (CUDA) and the Mac computes on Metal, and the small differences in the sums decide between two words that are almost equally likely. C-03 and D-10 also got other chunks (*Ties in the BM25 ranking*). Word-for-word answers are therefore not expected across computers, and the answers are compared with the automatic checks of the notebook (cell `check`):

| Check | Notebook (Colab T4 GPU) | Service (Mac) |
|---|---|---|
| Cites a provision | 23 of 30 | 24 of 30 |
| Expected provision cited (strict) | 18 of 27 | 19 of 27 |
| Expected provision cited (lenient, O2 (a) in the E1 card) | 19 of 27 | 21 of 27 |
| Cites only the chunks in the prompt | 19 of 23 | 19 of 24 |
| Says "The provided text does not answer this question." | 10 of 30 | 8 of 30 |

The service scores as the notebook within two questions on every check, in both directions; with 27 to 30 questions this is the size of the change one different word can make, not a change of the system. The answer time on the Mac was 5.9 s (median) and at most 16.3 s per question.

`python rag/verify_val.py --score docs/eval/answers/val-service-answers.csv` prints this table again from the saved answers, without Ollama.

## How to run it again

From the repository root, in the environment of *Install* in the [README](../../README.md):

```bash
python rag/ingest.py
python rag/verify_val.py --retrieval-out docs/eval/answers/val-service-retrieval.csv
python rag/verify_val.py --answers --out docs/eval/answers/val-service-answers.csv   # with Ollama and the answer model
python rag/verify_val.py --score docs/eval/answers/val-service-answers.csv            # only the scores of saved answers
```

The script prints "28 of 30", "different without a BM25 tie at rank 20: 0", "Recall@8 on 27 val questions: 0.59" and "OK". Linux and the Mac printed the same (17/11/2026); please add a line here when it is run on another computer.
