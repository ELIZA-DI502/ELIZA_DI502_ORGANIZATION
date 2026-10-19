# Spike 01: Technology options for each part of ELIZA

**Status:** Open. Options are listed and the tests are planned; no measurement has been made yet.
**Date:** 18/10/2026 · **Feeds:** [design.md](../design.md), D4 System Design v1

## Question

Which tool do we use for each part of the system, given our constraints?

The tools must fit these limits from [Assumptions & Constraints](../../Markdown%20Template/03-project-canvas/03-assumptions-and-constraints.md):

- **C-03:** RAG with an open-source, quantized language model
- **C-05:** no GPU; runs on our own computers or on a Google Cloud CPU instance
- **C-06:** $100 Google Cloud credit
- **C-01:** one source, the consolidated text of 27/07/2026
- **A-06:** the model licence must allow use in this project

## Options per component

| # | Component | What it does | Options | Proposed | Why (basis) | How we test it | Status |
|---|---|---|---|---|---|---|---|
| 1 | Ingestion and parsing | Reads the EUR-Lex text and splits it by Article, paragraph and Annex point | BeautifulSoup on the EUR-Lex HTML; PDF text extraction | BeautifulSoup on HTML | The HTML marks Articles, paragraphs and Annex points as separate elements (A-05) | Count the chunks and compare with the table of contents; count chunks without an identifier (target: 0, D5) | Open |
| 2 | Chunking | One chunk per paragraph or Annex point, with metadata (Article, paragraph, version date) | Paragraph-level chunks; Article-level chunks | Paragraph level | A test split of the 27/07/2026 text gave 188 provision-level chunks for 19 Articles and Annex III | Compare Recall@5 for paragraph-level and Article-level chunks on the `dev` questions | Open |
| 3 | Embedding model | Turns text into vectors for meaning search | bge-small-en-v1.5; e5-small-v2; all-MiniLM-L6-v2 | bge-small-en-v1.5 | Small models run on a CPU | Recall@5 on the `dev` questions; time to embed all chunks. e5-small-v2 is tested with its "query:" and "passage:" prefixes, as its model card advises | Open |
| 4 | Keyword search | Finds exact references such as "Article 6(3)" | BM25 (rank_bm25 library) | BM25 | Users often type Article numbers, which meaning search can miss | Recall@5 with and without BM25 | Open |
| 5 | Vector store | Stores the vectors and finds the closest ones | Chroma; FAISS | Chroma | Runs locally as a file; no server needed | Works on a team laptop and on the cloud instance (yes/no) | Open |
| 6 | LLM | Writes the answer from the retrieved provisions | Qwen3-4B; Phi-3.5-mini-instruct (3.8B); Llama-3.2-3B-Instruct; a 7B model only if the 3–4B models are fast enough | Start with a 3–4B model, 4-bit quantized | Smaller models answer faster on a CPU, and 4-bit quantization lowers memory use (R-10, C-03) | First check: median and 95th-percentile answer time on 10 `dev` questions. Decision: all `dev` questions, scored on retrieval (expected provision in the top 5) and on the answer (supported by the cited text, correct citation, no verdict) | Open |
| 7 | Running the LLM | Loads the quantized model and serves it | Ollama; llama.cpp | Ollama with 4-bit GGUF files (Q4_K_M) | Runs 4-bit quantized models on a CPU with one install command | Same answer-time test as row 6, on a laptop and on the cloud instance. The exact model file and quantization level are recorded in `ai-bom.yaml` | Open |
| 8 | Input check | Detects out-of-scope, legal-decision and personal-data questions | Keyword rules; a short classification prompt to the LLM; both | Both | Rules are fast; the prompt catches cases that rules miss (R-05, R-12, R-13) | Share of out-of-scope and legal-decision `dev` questions handled as expected | Open |
| 9 | Output check | Checks that every cited ID is a retrieved chunk; blocks verdict phrases; adds source, version date and notice | Python code after the LLM | Python code | A code check is deterministic, so it can meet "100% of citations match retrieved IDs" (D6) | Run on all `dev` answers; count mismatches (target: 0). A matching ID does not prove the text supports the claim, so a sample of answers is also checked by a reviewer | Open |
| 10 | User interface | Web chat page with the "not legal advice" notice | Gradio; Streamlit | Gradio `ChatInterface` | Suggested in the course register ("Chat interface"); one Python file; keeps the conversation in the session, so no personal data is stored (C-10) | A team member who did not build it can run it from `README.md` (D6) | Open |
| 11 | Hosting | Runs the system for the pilot and the demo | Google Cloud Compute Engine CPU instance; team laptops | Cloud instance, stopped when not in use | Fits the $100 credit (A-07, R-08) | Cost per running hour and total cost of the pilot from the billing report; disk and IP address costs continue while the instance is stopped | Open |
| 12 | Evaluation and tracking | Scores every version and logs the results | Weights & Biases; RAGAS for faithfulness | Weights & Biases + our own scripts | W&B is the course tool; Recall@5 and citation checks are simple scripts | Every reported number links to a W&B run (D12) | Open |

## Licences to check (A-06)

Check each licence on the model's own model card before its ADR is written, and record it in `ai-bom.yaml`.

| Model | Licence to confirm on the model card |
|---|---|
| Qwen3-4B | Apache 2.0 |
| Phi-3.5-mini-instruct | MIT |
| Llama-3.2-3B-Instruct | Llama 3.2 Community License (extra terms) |
| bge-small-en-v1.5 | MIT |
| e5-small-v2 | MIT |
| all-MiniLM-L6-v2 | Apache 2.0 |

## Next steps

1. Run the answer-time test (rows 6–7) on one laptop and on the cloud instance, by 28/10/2026.
2. Run the parsing and chunking test (rows 1–2), by 28/10/2026.
3. Run Recall@5 for rows 3–5 once D2 has `dev` questions, in Sprint 2.
4. When a row is decided, write an ADR in `docs/adr/` and change its status here to "Decided".
