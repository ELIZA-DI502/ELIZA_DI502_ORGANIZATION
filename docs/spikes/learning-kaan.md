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
| Evaluation basics | Need to learn | This learning spike (KAN-63), by 28/10/2026 |
| Python environment | Known; I use virtual environments | – |
| Chat interface (React) | Known; I build JavaScript and React applications | – |

## 1. Evaluation basics

**Source:** lecture slides "Requirements, scope and acceptance criteria" (resource given in the Online Course Register)

**Goal:** learn what an evaluation set is, why it must be fixed before experiments, and what Recall@5 ("the gold provision is in the top 5 results") measures.

**Expected output:** I can explain how our D2 question set and the dev/test split (KAN-53) are used to compare retrieval settings in the alpha evaluation (KAN-8).

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

## Definition of Done

- [ ] Explain the topic at the Sprint 1 review.
- [ ] Close the gaps marked "Need to learn" in the table above.
