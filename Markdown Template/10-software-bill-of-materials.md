# Software Bill of Materials

<!--
Course template instructions:
- This register is where you will keep track of all third party libraries, tools and models to be used during development. For more information: Producing Software Bill of Materials a.k.a SBOMs for Atlassian - Inside Atlassian.
- syft is an open source project where you can supply your requirements.txt or docker image to generate an SBOM table.
- AI SBOM: third party models are documented here. For models hosted on huggingface, you can use AI SBom Generator to generate an AI SBOM in the CycloneDX 1.6 json format.
- When naming the model please specify all characteristics, including model version, size, and quantization. Include links to where you accessed the models weights and more details.
- Specify what purpose each model will satisfy, who accessed this model, and when.
- Finally mention the specific libraries used to interact with them, along with an associated experiment and the result, whether the model will be used or rejected and why.
-->

| Team  | Sprint | Last updated | Updated by | Jira |
| ----- | ------ | ------------ | ---------- | ---- |
| ELIZA | 2      | 2026-11-09   | Kaan       | [KAN-105](https://yarengursoy.atlassian.net/browse/KAN-105) |

Sources: the [model selection spike](../docs/spikes/model-selection-spike.md) (Sprint 1, KAN-57), [`src/embedding.ipynb`](../src/embedding.ipynb) and [`src/evaluation.ipynb`](../src/evaluation.ipynb) (Sprint 2, KAN-97, KAN-221), [`config/rag.yaml`](../config/rag.yaml), and the `model` column of [`eval-set-v1.csv`](../docs/eval/eval-set-v1.csv). The computers are described in [Facilities and Resources](03-project-canvas/09-facilities-and-resources.md), row 1.

## Software Bill of Materials

The versions are not pinned yet: the repository has no `requirements.txt` (D6 criterion 9, baseline). The libraries below are the ones the notebooks import. When `requirements.txt` is added, the versions and checksums are filled from it with syft.

| Package Name | Version | Description | License | Supplier | Package Checksum |
|---|---|---|---|---|---|
| sentence-transformers | not pinned yet | Embeds the chunks and the questions with the bge models (D10) | Apache-2.0 | Hugging Face (UKP Lab) | – |
| chromadb | not pinned yet | Vector store on disk, cosine distance (D11) | Apache-2.0 | Chroma | – |
| rank_bm25 | not pinned yet | BM25 keyword index for hybrid search (D12) | Apache-2.0 | Dorian Brown | – |
| llama-cpp-python | not pinned yet | Ran the quantized answer models in the model selection spike (Google Colab) | MIT | Andrei Betlen | – |
| pandas, numpy, scikit-learn, PyYAML, requests, beautifulsoup4, umap-learn, matplotlib | not pinned yet | Data handling, configuration, parsing the EUR-Lex HTML, scores and plots in the notebooks | BSD-3-Clause (pandas, numpy, scikit-learn, umap-learn); MIT (PyYAML, beautifulsoup4); Apache-2.0 (requests); Matplotlib License (matplotlib) | Their open-source projects | – |

**Tools and services that are not in `requirements.txt`**

| Tool or service | Version | Used for | License or terms | Who, where |
|---|---|---|---|---|
| Ollama | 0.40.11 (Kaan's computer); Gözde Nur's computer: TODO | Runs the LLMs locally on CPU: the answer-time measurement of the spike and the LLM jury of KAN-221; the system serves the answer model with it (D9) | MIT | Kaan (MacBook Pro M3 Pro, 25/10/2026); Gözde Nur (MacBook Pro M4, from 06/11/2026) |
| Google Colab (free tier) | – | Ran the five answer models of the model selection spike (CPU and T4 GPU runtimes) | Google terms of service | Gözde Nur, 25/10/2026 |
| Hugging Face Hub | – | Download of the embedding models and the GGUF files | Each model's own licence (below) | Gözde Nur |
| claude.ai | – | Drafting the D2 questions (see the last two rows of the AI SBOM) | Anthropic terms of service | Gözde Nur, Yeşim, Kaan, Yaren |

## AI Software Bill of Materials

Accesser and computer: Gözde Nur's MacBook Pro 14-inch (2024), Apple M4 (10-core CPU), 16 GB RAM, macOS Sequoia 15.1, CPU only, unless the row says otherwise. Kaan's MacBook Pro 16-inch (Nov 2023), Apple M3 Pro (12-core CPU), 36 GB RAM, was used for the answer-time measurement of 25/10/2026.

| Model (version, size, quantization) | Provider | Licence | Purpose | Accesser | Date of access | Method of interaction | Experiment and results | Used? Why |
|---|---|---|---|---|---|---|---|---|
| [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct), 8B, GGUF `Q4_K_M` (file: TODO); Ollama `llama3.1:8b-instruct-q4_K_M` (ID `46e0c10c039e`, 4.9 GB) for the timing | Meta | Llama 3.1 Community License | Answer generation | Gözde Nur (Colab); Kaan (timing) | 25/10/2026 | Local: `llama-cpp-python` on Google Colab (T4 GPU); Ollama on macOS, CPU only, for the answer time | [Model selection spike](../docs/spikes/model-selection-spike.md), runs 4–5: 7 of 8 questions passed; answer time 15.4 s on the M3 Pro | **Used** as the answer model: the best score, and the answer time is within the 60 s limit (D9) |
| [Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct), 3.8B, GGUF `Q4_K_M` (file: TODO); Ollama `phi4-mini:3.8b-q4_K_M` (ID `78fad5d182a7`, 2.5 GB) for the timing, `phi4-mini` in the jury | Microsoft | MIT | Answer generation (fallback); member of the LLM jury | Gözde Nur (Colab, jury); Kaan (timing) | 25/10/2026; jury 06/11/2026 | Local: `llama-cpp-python` on Colab (CPU and T4); Ollama on macOS | Spike, runs 1–4: 2 to 5 of 8 passed; answer time 10.2 s on the M3 Pro. Jury ([`evaluation.ipynb`](../src/evaluation.ipynb) step 4): answered KEEP for all 20 words | **Fallback** answer model (D9): faster, lower score. In the jury it did not tell the words apart |
| [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct), 3B, GGUF `Q4_K_M` (file: TODO) | Meta | Llama 3.2 Community License | Answer generation (candidate) | Gözde Nur | 25/10/2026 | Local: `llama-cpp-python` on Colab (CPU) | Spike, runs 1–2: 5 of 8 passed | **Not used**: lower score than Llama-3.1-8B |
| [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B), 4B, GGUF `Q4_K_M` (file: TODO), thinking turned off; Ollama `qwen3:4b` | Alibaba Cloud (Qwen team) | Apache-2.0 | Answer generation (candidate); member of the LLM jury | Gözde Nur | 25/10/2026; jury 06/11/2026 | Local: `llama-cpp-python` on Colab (CPU); Ollama on macOS | Spike, runs 1–2: 4 and 5 of 8 passed; in run 1 it helped a user avoid the rules (B-S1). Jury: in practice the deciding vote on the 11 words BM25 ignores | **Not used** as the answer model (lower score, one unsafe answer). **Used** in the jury: `bm25.remove: jury` in `config/rag.yaml` |
| [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B), 8B, GGUF `Q4_K_M` (file: TODO) | Alibaba Cloud (Qwen team) | Apache-2.0 | Answer generation (candidate) | Gözde Nur | 25/10/2026 | Local: `llama-cpp-python` on Colab (T4) | Spike, runs 4–5: 2 of 8 passed; it wrote only reasoning text and no answer | **Not used**: no answers |
| [Gemma 3 4B instruct](https://huggingface.co/google/gemma-3-4b-it), Ollama `gemma3:4b` | Google | Gemma Terms of Use | Member of the LLM jury | Gözde Nur | 06/11/2026 | Local: Ollama on macOS | Jury ([`evaluation.ipynb`](../src/evaluation.ipynb) step 4): answered IGNORE for 18 of 20 words | **Used** in the jury (majority vote of three model families), but it did not tell the words apart |
| [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5), 384 dimensions | BAAI | MIT | Embedding of the chunks and the questions | Gözde Nur | 06/11/2026; chosen 07/11/2026 | Local: `sentence-transformers`, vectors in `chromadb` | [`embedding.ipynb`](../src/embedding.ipynb) step 2 (dense, B-01–B-06): Recall@5 0.48, MRR 0.26. [`evaluation.ipynb`](../src/evaluation.ipynb) step 6 (hybrid): Recall@5 0.52, MRR 0.45 | **Used** (`embedding.model` in `config/rag.yaml`, KAN-221): higher Recall@5, D10's measure. Checked again on the `val` split in KAN-99 |
| [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5), 768 dimensions | BAAI | MIT | Embedding (Sprint 1 choice, D10) | Gözde Nur | 06/11/2026 | Local: `sentence-transformers`, `chromadb` | Dense: Recall@5 0.40, MRR 0.53. Hybrid: Recall@5 0.48, MRR 0.64 | **Not used** since 07/11/2026: lower Recall@5 than bge-small; tested again in KAN-99 |
| [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2), 384 dimensions | sentence-transformers | Apache-2.0 | Embedding (candidate in D10) | Gözde Nur | 06/11/2026 | Local: `sentence-transformers`, `chromadb` | Dense: the lowest Recall@5, MRR and Precision@5 of the three | **Not used**: the weakest on retrieval |
| Claude Opus 5.5 (`claude-opus-5-5`) | Anthropic | Proprietary (Anthropic terms of service) | Drafting D2 questions and gold answers, checked by their authors against the consolidated text | Gözde Nur; Yeşim; Kaan | Gözde Nur: 24/10, 05/11 and 07/11/2026 (B); Yeşim: 04/11/2026 (BM) and 08/11/2026 (A); Kaan: 08/11/2026 (C) | API-hosted, interactive chat on claude.ai | [`prompts-3b.md`](../docs/eval/prompts-3b.md), [`benchmark-selection.md`](../docs/eval/benchmark-selection.md), [`question-writing-method.md`](../docs/eval/question-writing-method.md) | **Used** for the evaluation set only; not part of the system |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | Anthropic | Proprietary (Anthropic terms of service) | Drafting D2 questions (EM) | Yaren | TODO: date | API-hosted, interactive chat on claude.ai | `model` column of [`eval-set-v1.csv`](../docs/eval/eval-set-v1.csv) (EM questions) | **Used** for the evaluation set only; not part of the system |

**Still to fill in:** the exact GGUF files used on Colab and the Ollama version and tags on her computer (Gözde Nur); Yaren's access date. Any model tried in the baseline (KAN-99, KAN-100) is added here before the upload on 14/11/2026.
