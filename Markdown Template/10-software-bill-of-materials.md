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
| ELIZA | 2      | 2026-11-10   | Kaan       | [KAN-105](https://yarengursoy.atlassian.net/browse/KAN-105) |

Sources: the [model selection spike](../docs/spikes/model-selection-spike.md) (Sprint 1, KAN-57), [`src/embedding.ipynb`](../src/embedding.ipynb) (Sprint 2, KAN-97, KAN-221, KAN-99), [`config/rag.yaml`](../config/rag.yaml), and the `model` column of [`eval-set-v1.csv`](../docs/eval/eval-set-v1.csv). The computers are described in [Facilities and Resources](03-project-canvas/09-facilities-and-resources.md), row 1.

## Software Bill of Materials

The versions are not pinned yet: the repository has no `requirements.txt` (D6 criterion 9, baseline). The libraries below are the ones the notebooks import. When `requirements.txt` is added, the versions and checksums are filled from it with syft.

| Package Name | Version | Description | License | Supplier | Package Checksum |
|---|---|---|---|---|---|
| sentence-transformers | not pinned yet | Embeds the chunks and the questions with the bge models (D13) | Apache-2.0 | Hugging Face (UKP Lab) | – |
| chromadb | not pinned yet | Vector store on disk, cosine distance (D11) | Apache-2.0 | Chroma | – |
| rank_bm25 | not pinned yet | BM25 keyword index in the hybrid search, weight 0.1, stopwords removed (D14) | Apache-2.0 | Dorian Brown | – |
| llama-cpp-python | not pinned yet | Ran the quantized answer models in the model selection spike (Google Colab) | MIT | Andrei Betlen | – |
| pandas, numpy, scikit-learn, PyYAML, requests, beautifulsoup4, umap-learn, matplotlib | not pinned yet | Data handling, configuration, parsing the EUR-Lex HTML, scores and plots in the notebooks | BSD-3-Clause (pandas, numpy, scikit-learn, umap-learn); MIT (PyYAML, beautifulsoup4); Apache-2.0 (requests); Matplotlib License (matplotlib) | Their open-source projects | – |

**Tools and services that are not in `requirements.txt`**

| Tool or service | Version | Used for | License or terms | Who, where |
|---|---|---|---|---|
| Ollama | 0.40.11 (Kaan's computer); 0.40.13 (Gözde Nur's computer) | Runs the LLMs locally: the answer-time measurement of the spike (CPU only), the first LLM jury (4B models, Gözde Nur's computer) and the second jury (12–14B models, Colab T4 GPU); the system serves the answer model with it (D9) | MIT | Kaan (MacBook Pro M3 Pro, 25/10/2026); Gözde Nur (MacBook Pro M4, from 06/11/2026) |
| Google Colab (free tier) | – | Ran the five answer models of the model selection spike (CPU and T4 GPU runtimes) and the 12–14B LLM jury (T4 GPU) | Google terms of service | Gözde Nur, 25/10/2026, 08/11/2026 and 09/11/2026 |
| Hugging Face Hub | – | Download of the embedding models and the GGUF files | Each model's own licence (below) | Gözde Nur |
| claude.ai | – | Drafting the D2 questions (see the last two rows of the AI SBOM) | Anthropic terms of service | Gözde Nur, Yeşim, Kaan, Yaren |

## AI Software Bill of Materials

Accesser and computer: Gözde Nur's MacBook Pro 14-inch (2024), Apple M4 (10-core CPU), 16 GB RAM, macOS Sequoia 15.1, CPU only, unless the row says otherwise. Kaan's MacBook Pro 16-inch (Nov 2023), Apple M3 Pro (12-core CPU), 36 GB RAM, was used for the answer-time measurement of 25/10/2026.

| Model (version, size, quantization) | Provider | Licence | Purpose | Accesser | Date of access | Method of interaction | Experiment and results | Used? Why |
|---|---|---|---|---|---|---|---|---|
| [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct), 8B, `Q4_K_M`: GGUF `bartowski/Meta-Llama-3.1-8B-Instruct-GGUF`, `Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf` (4.92 GB); Ollama `llama3.1:8b-instruct-q4_K_M` (ID `46e0c10c039e`, 4.9 GB) for the timing | Meta | Llama 3.1 Community License | Answer generation | Gözde Nur (Colab); Kaan (timing) | 25/10/2026 | Local: `llama-cpp-python` on Google Colab (T4 GPU); Ollama on macOS, CPU only, for the answer time | [Model selection spike](../docs/spikes/model-selection-spike.md), runs 4–5: 7 of 8 questions passed; answer time 15.4 s on the M3 Pro | **Used** as the answer model: the best score, and the answer time is within the 60 s limit (D9) |
| [Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct), 3.8B, `Q4_K_M`: GGUF `unsloth/Phi-4-mini-instruct-GGUF`, `Phi-4-mini-instruct-Q4_K_M.gguf` (2.49 GB); Ollama `phi4-mini:3.8b-q4_K_M` / `phi4-mini` (ID `78fad5d182a7`, 2.5 GB) | Microsoft | MIT | Answer generation (fallback); first LLM jury | Gözde Nur (Colab, jury); Kaan (timing) | 25/10/2026; jury 06/11/2026 | Local: `llama-cpp-python` on Colab (CPU and T4); Ollama on macOS | Spike, runs 1–4: 2 to 5 of 8 passed; answer time 10.2 s on the M3 Pro. Jury ([`src/embedding.ipynb`](../src/embedding.ipynb) step 4): the 4B-class models did not tell the words apart | **Fallback** answer model (D9): faster, lower score. Replaced in the jury by `phi4:14b` |
| [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct), 3B, `Q4_K_M`: GGUF `bartowski/Llama-3.2-3B-Instruct-GGUF`, `Llama-3.2-3B-Instruct-Q4_K_M.gguf` (2.02 GB) | Meta | Llama 3.2 Community License | Answer generation (candidate) | Gözde Nur | 25/10/2026 | Local: `llama-cpp-python` on Colab (CPU) | Spike, runs 1–2: 5 of 8 passed | **Not used**: lower score than Llama-3.1-8B |
| [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B), 4B, `Q4_K_M`: GGUF `Qwen/Qwen3-4B-GGUF` (`Q4_K_M`), thinking turned off; Ollama `qwen3:4b` (ID `359d7dd4bcda`, 2.5 GB) | Alibaba Cloud (Qwen team) | Apache-2.0 | Answer generation (candidate); first LLM jury | Gözde Nur | 25/10/2026; jury 06/11/2026 | Local: `llama-cpp-python` on Colab (CPU); Ollama on macOS | Spike, runs 1–2: 4 and 5 of 8 passed; in run 1 it helped a user avoid the rules (B-S1). Jury: see Phi-4-mini | **Not used**: lower score and one unsafe answer; replaced in the jury by `qwen3:14b` |
| [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B), 8B, `Q4_K_M`: GGUF `Qwen/Qwen3-8B-GGUF`, `Qwen3-8B-Q4_K_M.gguf` (5.03 GB) | Alibaba Cloud (Qwen team) | Apache-2.0 | Answer generation (candidate) | Gözde Nur | 25/10/2026 | Local: `llama-cpp-python` on Colab (T4) | Spike, runs 4–5: 2 of 8 passed; it wrote only reasoning text and no answer | **Not used**: no answers |
| [Gemma 3 4B instruct](https://huggingface.co/google/gemma-3-4b-it), Ollama `gemma3:4b` (ID `68ceab7e468a`, 3.4 GB) | Google | Gemma Terms of Use | First LLM jury | Gözde Nur | 06/11/2026 | Local: Ollama on macOS | Jury: see Phi-4-mini | **Not used**: replaced in the jury by `gemma3:12b` |
| [Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B), Ollama `qwen3:14b` | Alibaba Cloud (Qwen team) | Apache-2.0 | LLM jury: which frequent words are useless (instructor's request; a model other than the answer model) | Gözde Nur | 08/11/2026 and 09/11/2026 | Ollama on Google Colab (T4 GPU) | [`src/embedding.ipynb`](../src/embedding.ipynb) step 4: the jury (majority of three) chose 10 words to remove | **Not used**: removing the jury's words did not help; for BM25 the stopword list was better (step 5), and before embedding the MRR dropped (step 6b, D13) |
| [Phi-4](https://huggingface.co/microsoft/phi-4), 14B, Ollama `phi4:14b` | Microsoft | MIT | LLM jury | Gözde Nur | 08/11/2026 and 09/11/2026 | Ollama on Google Colab (T4 GPU) | Step 4: answered KEEP for all 20 words | **Not used**: as above |
| [Gemma 3 12B instruct](https://huggingface.co/google/gemma-3-12b-it), Ollama `gemma3:12b` | Google | Gemma Terms of Use | LLM jury | Gözde Nur | 08/11/2026 and 09/11/2026 | Ollama on Google Colab (T4 GPU) | Step 4: member of the majority vote | **Not used**: as above |
| [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5), 1,024 dimensions (1.34 GB) | BAAI | MIT | Embedding of the chunks and the questions | Gözde Nur | 09/11/2026 | Local: `sentence-transformers`, vectors in `chromadb` | [`src/embedding.ipynb`](../src/embedding.ipynb) step 6, 27 `val` questions, with a little BM25 (dense weight 0.9): Recall@5 0.48, MRR 0.69, the best; with top 8 (step 7): Recall@8 0.56; [W&B run](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/oyrsrqwf) | **Used** (`embedding.model` in `config/rag.yaml`, D13) |
| [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3), 1,024 dimensions (2.27 GB) | BAAI | MIT | Embedding (candidate) | Gözde Nur | 09/11/2026 | Local: `sentence-transformers`, `chromadb` | Step 6: Recall@5 0.48 (tied with bge-large), MRR 0.62 | **Not used**: same Recall@5 as bge-large-en-v1.5, lower MRR (D13) |
| [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5), 384 dimensions | BAAI | MIT | Embedding (candidate in D10) | Gözde Nur | 06/11/2026 | Local: `sentence-transformers`, `chromadb` | First check on B-01–B-06 (06–07/11/2026): the best Recall@5, so it was used from 07/11. Step 6 on `val`: Recall@5 0.45 | **Not used** since 09/11/2026: lower Recall@5 than bge-large-en-v1.5 (D13) |
| [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5), 768 dimensions | BAAI | MIT | Embedding (Sprint 1 choice, D10) | Gözde Nur | 06/11/2026 | Local: `sentence-transformers`, `chromadb` | Step 6 on `val`: Recall@5 0.45, MRR 0.51 | **Not used**: lower Recall@5 than bge-large-en-v1.5 (D13) |
| [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2), 384 dimensions | sentence-transformers | Apache-2.0 | Embedding (candidate in D10) | Gözde Nur | 06/11/2026 | Local: `sentence-transformers`, `chromadb` | Step 6 on `val`: Recall@5 0.39, the lowest of five models | **Not used**: the weakest on retrieval |
| Claude Opus 5.5 (`claude-opus-5-5`) | Anthropic | Proprietary (Anthropic terms of service) | Drafting D2 questions and gold answers, checked by their authors against the consolidated text | Gözde Nur; Yeşim; Kaan | Gözde Nur: 24/10, 05/11 and 07/11/2026 (B); Yeşim: 04/11/2026 (benchmark questions) and 08/11/2026 (A); Kaan: 08/11/2026 (C) | API-hosted, interactive chat on claude.ai | [`prompts-3b.md`](../docs/eval/prompts-3b.md), [`benchmark-selection.md`](../docs/eval/benchmark-selection.md), [`question-writing-method.md`](../docs/eval/question-writing-method.md) | **Used** for the evaluation set only; not part of the system |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | Anthropic | Proprietary (Anthropic terms of service) | Drafting D2 questions (D) | Yaren |  | API-hosted, interactive chat on claude.ai | `model` column of [`eval-set-v1.csv`](../docs/eval/eval-set-v1.csv) (D questions) | **Used** for the evaluation set only; not part of the system |
