# Learning spike: Kaan Kocatürk

**Sprint:** 1 (14/10–28/10/2026) · **Goal:** close my gaps in the Sprint 1 fundamentals from the [Online Course Register](../../online-course-register/README.md) · **Jira:** KAN-63

## Where I start

| Topic | My level before Sprint 1 | What I do in Sprint 1 |
|---|---|---|
| Git & GitHub | Known; I use Git in my own projects | – |
| Markdown | Basic knowledge | Review tables, code blocks and GitHub note boxes in GitHub's "Basic writing and formatting syntax" |
| Scrum basics | Need to learn | Read Scrum.org "What is Scrum?" |
| Jira | Need to learn | Work with stories, tasks and sprints in our KAN project |
| LLM basics | Known before the project | – |
| Embeddings & vector search | Need to learn | Workshop material (14/10) |
| RAG | Need to learn | Lewis et al. (2020) and the lecture slides |
| Prompt engineering | Need to learn | Workshop material |
| Evaluation basics | Need to learn | This learning spike (KAN-63) (done) |
| Python environment | Known; I use virtual environments | – |
| Chat interface (React) | Known; I build JavaScript and React applications | – |

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

## 3. RAG

**Source:** [Lewis et al. (2020)](https://arxiv.org/abs/2005.11401) and the lecture slides

**Goal:** understand the indexing and query phases of a RAG pipeline and why RAG reduces hallucination.

**Expected output:** I can explain each box of our [architecture diagram](../images/system-architecture-v1.png).

## 4. Prompt engineering

**Source:** workshop material

**Goal:** write a prompt that tells the model to answer only from the given passages and to say when it does not know.

**Expected output:** I can review the prompt in `prompts/` against KAN-23 (insufficient evidence) and KAN-2 (no legal decision).

## 5. Markdown, Scrum basics and Jira

**Sources:** GitHub Docs ["Basic writing and formatting syntax"](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), Scrum.org ["What is Scrum?"](https://www.scrum.org/resources/what-scrum-module)

**Goal:** write the charter and design pages in Markdown, and follow our sprints, stories and tasks in Jira.

**Expected output:** my charter pages and the design document are written in Markdown, and every branch and commit carries its Jira key (for example `KAN-59`).

## My computer

Recorded for [Facilities & Resources](../../Markdown%20Template/03-project-canvas/09-facilities-and-resources.md) row 1 (CPU only, C-05).

| Item | Value |
|---|---|
| Computer | MacBook Pro 16-inch (Nov 2023) |
| Chip | Apple M3 Pro (12-core CPU) |
| Memory | 36 GB |
| Operating system | macOS Tahoe 26 |

## Definition of Done

- [ ] Explain the topic at the Sprint 1 review.
- [ ] Close the gaps marked "Need to learn" in the table above.
