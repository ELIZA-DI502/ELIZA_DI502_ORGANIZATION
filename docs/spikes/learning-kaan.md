# Learning spike: Kaan Kocatürk

**Sprint:** 1 (14/10–28/10/2026) · **Goal:** close my gaps in the Sprint 1 fundamentals from the [Online Course Register](../../online-course-register/README.md) · **Jira:** KAN-63

## Where I start

| Topic                      | My level before Sprint 1                         | What I do in Sprint 1                                                                                     |
| -------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Git & GitHub               | Known; I use Git in my own projects              | –                                                                                                        |
| Markdown                   | Basic knowledge                                  | Review tables, code blocks and GitHub note boxes in GitHub's "Basic writing and formatting syntax" (done) |
| Scrum basics               | Need to learn                                    | Read Scrum.org "What is Scrum?" (done)                                                                    |
| Jira                       | Need to learn                                    | Work with stories, tasks and sprints in our KAN project (done)                                            |
| LLM basics                 | Known before the project                         | –                                                                                                        |
| Embeddings & vector search | Need to learn                                    | Workshop material (14/10) (done)                                                                          |
| RAG                        | Need to learn                                    | Lewis et al. (2020) and the lecture slides (done)                                                         |
| Prompt engineering         | Need to learn                                    | Workshop material (done)                                                                                  |
| Evaluation basics          | Need to learn                                    | This learning spike (KAN-63) (done)                                                                       |
| Python environment         | Known; I use virtual environments                | –                                                                                                        |
| Chat interface (React)     | Known; I build JavaScript and React applications | –                                                                                                        |

## 1. Evaluation basics

**Source:** lecture slides "Requirements, scope and acceptance criteria" (resource given in the Online Course Register)

**Goal:** learn what an evaluation set is, why it must be fixed before experiments, and what Recall@5 ("the gold provision is in the top 5 results") measures.

**Expected output:** I can explain how our D2 question set and the `val`/`test` split (KAN-53) are used to compare retrieval settings in the alpha evaluation (KAN-8).

**What I learned:**

- An **evaluation set** is a fixed list of questions, each with its expected result: the gold source, a gold answer and the expected behaviour. Every version of the system answers the same questions, so the results can be compared. Our set is not finished yet: it is due with D2 (11/11/2026) as `docs/eval/eval-set-v1.csv`. The questions written so far (for example `eval-set-v1-3b.csv`) already have these columns (`gold_source`, `gold_answer`, `expected_behaviour`, `split`).
- The set must be **fixed before the experiments** (D2, before the Sprint 2 runs). If questions change between two runs, a difference in the result may come from the questions and not from the change we tested. The set is also split: settings are chosen on `val`, and `test` is not looked at until the final evaluation. A score on questions that were used to choose the settings is too optimistic.
- **Recall@5** is the share of in-scope questions whose gold provision is among the top 5 retrieved chunks: questions with a hit ÷ in-scope questions. Example (made-up numbers): if the gold provision is in the top 5 for 6 of 8 questions, Recall@5 = 6/8 = 75%.
- Recall@5 measures **only the retrieval step**, not the answer. It is an upper limit for O2 (a): a provision that is not retrieved cannot be cited. A larger k raises recall but makes the prompt longer, which costs answer time on a CPU and space in the 4,096-token context window.

**How it will be used in ELIZA:** once the set is fixed in D2, E1 (dense) and E2 (hybrid BM25 + dense) will be compared by Recall@k on the `val` split, and top-k will be chosen from 3, 5 and 8 (design decision D12) in Sprint 2. The `test` split will be used only for the final evaluation (D11). Open point for the scoring script: when a question has more than one gold provision (for example `B-01`), we must decide whether one hit is enough.

## 2. Embeddings & vector search

**Source:** workshop material (14/10)

**Goal:** understand how a text becomes a vector and how similarity search finds the passages closest to a question.

**Expected output:** I can explain why "our AI grades exams" can find the provision on "evaluate learning outcomes" (Annex III point 3(b)).

**What I learned:**

- An **embedding model** turns a text into a vector (a list of numbers). Texts with a similar meaning get vectors that are close to each other, even when they share no words.
- **Vector search** turns the question into a vector with the same model and returns the stored chunks whose vectors are closest, for example by cosine similarity.
- Vector search is weak on **exact identifiers** such as "Article 6(3)"; keyword search (BM25) finds these better. The two result lists can be merged, for example with Reciprocal Rank Fusion, which uses only the rank in each list.

**How it will be used in ELIZA:** each provision chunk will be embedded with bge-base-en-v1.5 and stored in Chroma with cosine distance (design decisions D10, D11). "Our AI grades exams" can find Annex III point 3(b) ("evaluate learning outcomes") because the meaning is close although the words differ. The baseline (E1) uses vector search only; E2 adds BM25 and merges the lists with RRF (D12).

## 3. RAG

**Source:** [Lewis et al. (2020)](https://arxiv.org/abs/2005.11401) and the lecture slides

**Goal:** understand the indexing and query phases of a RAG pipeline and why RAG reduces hallucination.

**Expected output:** I can explain each box of our [architecture diagram](<../../Markdown%20Template/11-system-architecture-design-document.md#3-system-architecture-diagram>).

**What I learned:**

- **Indexing** (once, and again when the source changes): parse the documents, split them into chunks, embed each chunk and store it with its metadata.
- **Query** (for every question): embed the question, retrieve the closest chunks, put them in the prompt and let the LLM write the answer from them.
- RAG reduces hallucination because the model answers from passages it is given and every statement can be traced to a passage. It does not remove hallucination: the model can still misread a passage, so answers must be checked against the passages they cite.

**How it will be used in ELIZA:** in the [architecture diagram](<../../Markdown%20Template/11-system-architecture-design-document.md#3-system-architecture-diagram>), the indexing boxes are ingestion and chunking (one chunk per Article paragraph or Annex point, with its identifier and version date, D7), the embedding model and the vector store. The query boxes are the input check, the retriever, the prompt builder, the LLM and the output check, which removes citations that are not among the retrieved chunks. Whether answers stay within their cited passages will be checked with O2 (b).

## 4. Prompt engineering

**Source:** workshop material

**Goal:** write a prompt that tells the model to answer only from the given passages and to say when it does not know.

**Expected output:** I can review the prompt in `prompts/` against KAN-23 (insufficient evidence) and KAN-2 (no legal decision).

**What I learned:**

- Put the retrieved passages in a separate, clearly marked part of the prompt, each with its identifier, so the model can cite them.
- Tell the model to answer only from these passages, to cite the Article or Annex for every statement, and to say so when the passages do not answer the question.
- One short example answer in the prompt shows the expected format better than a long description. A low temperature (0) gives repeatable answers, which evaluation needs.
- Rules in the prompt are not a guarantee; what must never happen (a legal verdict) is also checked by code after the model.

**How it will be used in ELIZA:** the prompt template will be kept in `prompts/` (not created yet) and reviewed against KAN-23 (say when the provisions do not answer) and KAN-2 (decline the decision, show the relevant provisions). The model selection spike already used a prompt with one example answer and temperature 0 (D9); the output check removes verdict sentences after the model.

## 5. Markdown, Scrum basics and Jira

**Sources:** GitHub Docs [&#34;Basic writing and formatting syntax&#34;](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), Scrum.org [&#34;What is Scrum?&#34;](https://www.scrum.org/resources/what-scrum-module)

**Goal:** write the charter and design pages in Markdown, and follow our sprints, stories and tasks in Jira.

**Expected output:** my charter pages and the design document are written in Markdown, and every branch and commit carries its Jira key (for example `KAN-59`).

**What I learned:**

- **Markdown:** tables, code blocks, relative links between pages, and Mermaid diagrams that GitHub draws from a code block.
- **Scrum:** work is done in sprints; each sprint has planning at the start and a review and a retrospective at the end. The Product Owner orders the backlog, the Scrum Master helps the team follow Scrum, and the Developers do the work.
- A **user story** is a need of a user with testable acceptance criteria; a **sub-task** is a piece of work for a story; a **spike** is timeboxed learning or research, like this note.
- **Jira:** story points go on the stories and hours on their sub-tasks; a Jira key in the branch name or commit message links the work in GitHub to the issue.

**Result:** my pages ([Project Executive Summary](<../../Markdown%20Template/03-project-canvas/01-project-executive-summary.md>), [Facilities &amp; Resources](<../../Markdown%20Template/03-project-canvas/09-facilities-and-resources.md>) and the [System Architecture Design Document](<../../Markdown%20Template/11-system-architecture-design-document.md>), with its Mermaid diagram) are written in Markdown, and my commits carry their Jira key (for example `KAN-59`, `KAN-38`, `KAN-63`).

## My computer

Recorded for [Facilities &amp; Resources](<../../Markdown%20Template/03-project-canvas/09-facilities-and-resources.md>) row 1 (CPU only, C-05).

| Item             | Value                          |
| ---------------- | ------------------------------ |
| Computer         | MacBook Pro 16-inch (Nov 2023) |
| Chip             | Apple M3 Pro (12-core CPU)     |
| Memory           | 36 GB                          |
| Operating system | macOS Tahoe 26                 |

## Definition of Done

- [X] My starting knowledge and learning gaps are recorded in the topic table above.
- [X] What an evaluation set is, why it is fixed before the experiments, and what Recall@5 measures are explained in section 1 (KAN-63).
- [X] The embeddings, vector search, RAG and prompt engineering concepts from the 14/10 workshop and Lewis et al. (2020) are documented in sections 2–4.
- [X] I reviewed Markdown, Scrum and Jira basics and applied them in my charter pages, the design document and my Jira-keyed commits (section 5).
- [X] The learning sources and the related project documents are linked, and what is planned but not built yet (the evaluation set D2, `prompts/`) is marked as planned.
- [ ] I can explain the evaluation basics and Recall@5 in my own words at the Sprint 1 review (28/10/2026).
