# Learning spike: Aliye Yeşim Yaman

**Sprint:** 1 (14/10–28/10/2026) · **Goal:** close my gaps in the Sprint 1 fundamentals from the [Online Course Register](../../online-course-register/README.md) · **Jira:** KAN-60 · **Updated:** 26/10/2026

## Where I start

| Topic | My level before Sprint 1 | What I did in Sprint 1 |
|---|---|---|
| Git & GitHub | Known; I have used Git and GitHub for years | – |
| Markdown | Known | – |
| Python environment | Known | – |
| Evaluation basics | Known | – |
| Scrum basics | Basic knowledge | Scrum.org "What is Scrum?" and the Scrum Guide; Product Owner work in Sprint 1 |
| Jira | Basic knowledge | Built the KAN backlog: epics, stories, sub-tasks, sprints and releases |
| LLM basics | Basic knowledge | Workshop material (14/10) |
| Embeddings & vector search | Basic knowledge | Workshop material (14/10) |
| RAG | Need to learn | Lewis et al. (2020) and the lecture slides (section 1) |
| Prompt engineering | Basic knowledge | Workshop material |
| Chat interface (Gradio) | Need to learn | Not needed: the team chose React (section 6) |

## 1. RAG

**Source:** [Lewis et al. (2020)](https://arxiv.org/abs/2005.11401) and the lecture slides (resources given in the Online Course Register)

**Goal:** learn the indexing and query phases of a RAG pipeline and why RAG reduces hallucination.

**What I learned:**

- **Indexing** (once, and again when the source changes): parse the documents, split them into chunks, turn each chunk into a vector and store it with its metadata.
- **Query** (for every question): turn the question into a vector, retrieve the most similar chunks, put them in the prompt and generate an answer from them.
- RAG reduces hallucination because the model answers from passages it is given, and each statement can be traced back to a passage. It does not remove hallucination: the model can still misread a passage, so the answers are checked against their cited passages (O2 (b)).

**How it is used in ELIZA:** one chunk per Article paragraph or Annex point, with its identifier and the version date (D5); retrieval measured with Recall@5 on the `val` split (D6); answers cite only retrieved provisions. The provisions that can be retrieved are listed in the D3 provision list (`data/provision-list.csv`).

## 2. LLM basics

**Source:** workshop material (14/10)

**Goal:** understand tokens, the context window, prompts and temperature, and why LLMs hallucinate; run a small open-source model in Colab.

**What I learned:**

- A model reads and writes **tokens** (pieces of words); the **context window** is the number of tokens it can take in at once, so the prompt and the retrieved passages must fit in it.
- **Temperature** controls how random the next token is; a low temperature gives more repeatable answers, which ELIZA needs for evaluation.
- LLMs **hallucinate** because they generate the most likely continuation, not a checked fact.

**How it is used in ELIZA:** a small quantized model on CPU (C-03, C-05) needs short answers and few retrieved passages; the [model selection spike](model-selection-spike.md) measured the answer time of the candidate models (R-16).

**Hands-on:** Before the project, I used LLMs to generate synthetic data, so I have worked with prompts and checked model outputs myself. I did not run a separate small open-source model in Colab in Sprint 1; the model selection spike (KAN-57) ran the candidate open-source models on Colab and on a team computer.

## 3. Embeddings & vector search

**Source:** workshop material (14/10)

**Goal:** understand how a text becomes a vector and how similarity search finds the passages closest to a question.

**What I learned:** an embedding model turns a text into a vector so that texts with a similar meaning get vectors that are close to each other; similarity search returns the stored vectors closest to the question's vector (for example by cosine similarity).

**How it is used in ELIZA:** "our AI grades exams" can find the provision on "evaluate learning outcomes" (Annex III point 3(b)) although the words differ. A question that names "Article 6(3)" depends on an exact identifier, which keyword search finds better; this is why the design document plans hybrid search (vector and BM25) after the baseline.

## 4. Prompt engineering

**Source:** workshop material

**Goal:** write a prompt that tells the model to answer only from the given passages and to say when it does not know.

**What I learned:** put the retrieved passages in a separate, marked part of the prompt; tell the model to answer only from them and to cite the Article or Annex for every statement; allow it to say that the passages do not answer the question.

**How it is used in ELIZA:** the prompt is checked against the acceptance criteria of KAN-2 (no legal decision) and KAN-23 (insufficient evidence).

## 5. Scrum basics and Jira

**Sources:** Scrum.org ["What is Scrum?"](https://www.scrum.org/resources/what-scrum-module), the [Scrum Guide](https://scrumguides.org/scrum-guide.html), the course's [Jira sync guide](../JIRA_SYNC_SETUP.md)

**Goal:** understand the Product Owner's responsibilities and the difference between a user story, a task and a spike; plan sprints in Jira.

**What I learned:**

- The Product Owner is accountable for the Product Backlog: its order, and stories that are clear enough for the team to start.
- A **user story** is a need of a user with testable acceptance criteria; a **task** is a piece of work that delivers part of a story; a **spike** is timeboxed learning or research, like this note.
- In Jira, story points go on the stories and hours on their sub-tasks (Model A of the course's sync guide), so that the burndown chart shows progress during the sprint.

**Result:** the KAN backlog: eight epics (four product epics and four project epics), the user stories of Sprints 1–4 with their sub-tasks, and two stories in the backlog that are built only if time allows. Every story has acceptance criteria and a traceability section that links it to the charter (objectives, deliverables, milestones, risks). The stories are shown in the [User Story Map v1](../../Markdown%20Template/06-user-stories/01-user-story-map-v1.md).

## 6. Chat interface (Gradio)

**Source:** Gradio documentation, ["Creating a chatbot fast"](https://www.gradio.app/guides/creating-a-chatbot-fast)

**Outcome:** not needed. The team chose React with a Node.js backend for the interface (System Design Document, decision D1), so I did not build the Gradio "hello world".

## Definition of Done

- [ ] Explain the indexing and query phases of ELIZA's RAG pipeline at the Sprint 1 review (28/10/2026).
- [x] Close the gaps marked "Basic knowledge" and "Need to learn" in the table above (Gradio dropped, see section 6).
