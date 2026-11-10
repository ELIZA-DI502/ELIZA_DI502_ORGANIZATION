# ELIZA: an EU AI Act assistant for teams building AI systems in education

ELIZA helps technical teams that build AI systems for education find the provisions of the EU AI Act (Regulation (EU) 2024/1689, consolidated text of 27/07/2026) that relate to their system. It answers only from the official text, cites the Article or Annex for every statement, and never gives a legal decision. DI 502, METU, Fall 2026.

**Status (Sprint 2, baseline):** the law is split into chunks, the evaluation questions are split into `val` and `test`, and the retrieval is built and measured on `val`. The answer generation is being added (KAN-99).

## What is where

| Folder or file | What it holds |
|---|---|
| `src/chunking.ipynb` | Splits the AI Act into 105 chunks, one per provision in scope, with metadata (KAN-92, KAN-93) |
| `src/split.ipynb` | Splits the evaluation questions into `val` and `test` and freezes `test` (KAN-53) |
| `src/embedding.ipynb` | Chooses the embedding model, keyword search, word removal and top-k on `val` (scored at 8 chunks), builds the search and logs the results and charts in Weights & Biases (KAN-97, KAN-221, KAN-99) |
| `src/wandb_results.ipynb` | Opens the W&B run of `src/embedding.ipynb`, shows its charts and downloads the PDF (CPU, about 1 minute) (KAN-99) |
| `config/rag.yaml` | The chosen settings of the system (chunking, models, top-k, LLM settings) |
| `prompts/` | The prompt templates, one file per template |
| `data/` | The stored AI Act text, its manifest, the provision list and the chunks ([data/README.md](data/README.md)) |
| `docs/eval/` | The evaluation questions (`eval-set-v1.csv`, `-val.csv`, `-test.csv`), the rubric and how the questions were written |
| `docs/spikes/` | Spike notes |
| `Markdown Template/` | Course pages: project charter, user stories, design document, SBOM, datasheets, sprint folders, experiment cards |
| `requirements.txt` | The Python packages, with exact versions |

## What you need

- **Python 3.12 or 3.13** and **Git**
- **Ollama** ([ollama.com](https://ollama.com)), only for the LLM jury in step 4 of `src/embedding.ipynb` and, later, for the answers. The three jury models need about 27 GB of disk and a computer with at least 16 GB of RAM; a GPU makes them much faster.
- About 5 GB of disk for the Python packages and the embedding models.
- A **Weights & Biases** account, only to log results (step 12 of `src/embedding.ipynb`).

No paid API is used.

## Install

macOS or Linux:

```bash
git clone https://github.com/ELIZA-DI502/ELIZA_DI502_ORGANIZATION.git
cd ELIZA_DI502_ORGANIZATION
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, use `python -m venv .venv` and `.venv\Scripts\activate` instead. On a Linux computer without an NVIDIA GPU, you can install the smaller CPU build of PyTorch first: `pip install torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu`, then `pip install -r requirements.txt`.

For the LLM jury, install Ollama and download the three models once:

```bash
ollama pull qwen3:14b
ollama pull phi4:14b
ollama pull gemma3:12b
```

## Run

Run the notebooks from the `src/` folder, in this order. In Jupyter, open each one and choose *Run All*, or run it from the terminal:

```bash
cd src
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 chunking.ipynb
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 split.ipynb
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 embedding.ipynb
```

| Notebook | Needs | Time | Check |
|---|---|---|---|
| `chunking.ipynb` | CPU | about 1 minute | "103 of 103 provisions found", "105 chunks" |
| `split.ipynb` | CPU | under 1 minute | every rule says OK, and the SHA-256 of the test file is `f68bfa569b69…` |
| `embedding.ipynb` | Ollama with the three jury models; a GPU is recommended | 20–30 minutes on a GPU, longer on a CPU | the settings table at the end matches `config/rag.yaml` |

`split.ipynb` gives the same split every time (seed 42), so running it again does not change the frozen `test` file. `embedding.ipynb` builds the vector store in `data/vector-store/`; it is not in Git and is rebuilt on every run.

**In Google Colab:** upload a notebook (*File → Upload notebook*) and choose *Run all*. Its first code cell downloads this repository and, for `embedding.ipynb`, installs Ollama and the jury models. For `embedding.ipynb`, choose *Runtime → Change runtime type → T4 GPU* first.

## Keys and settings

- **Weights & Biases:** run `wandb login` once in the terminal (in Colab, the notebook asks for the key). The key is never written into a file of this repository. Put any other secret in a `.env` file; `.env` is in `.gitignore`.
- **Settings:** every chosen setting is in `config/rag.yaml`. The LLM settings are there too (temperature 0, so the jury gives the same answer every run).
- **Random seeds:** the split uses seed 42, the UMAP picture uses `random_state=42`.

## Evaluation and tests

- The evaluation questions are in `docs/eval/eval-set-v1.csv`. All tuning uses the `val` split; the `test` split is frozen and used only for the final evaluation. To check that `test` has not changed:
  ```bash
  sha256sum docs/eval/eval-set-v1-test.csv
  # expected: f68bfa569b69783ba2d0203c7ecbc2a0317c9bbf24225100f406e8f16aac9d0a
  ```
  (on macOS: `shasum -a 256 docs/eval/eval-set-v1-test.csv`)
- The retrieval scores on `val` are in `src/embedding.ipynb`, in [Weights & Biases](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/v7g5hhxh) and, as charts, in `docs/eval/embedding-results.pdf` (written by step 12 of the notebook).
- Automated tests and the user story tests will be in `tests/` (Sprint 3).

## Source and licence

The only source is the consolidated text of Regulation (EU) 2024/1689 from EUR-Lex (CELEX 02024R1689-20260727), stored in `data/` with its SHA-256 hash in `data/manifest.csv`. EUR-Lex content may be reused with attribution (Commission Decision 2011/833/EU); only the text published in the Official Journal is legally binding. ELIZA gives information about the text, not legal advice.

## Course instructions

The course's instructions and templates come from the course repository ([volgasezen/di502](https://github.com/volgasezen/di502)): see [`weekly-milestones-and-deliverables/README.md`](weekly-milestones-and-deliverables/README.md) and [`online-course-register/README.md`](online-course-register/README.md).
