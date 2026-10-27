# Learning spike: Aliye Yeşim Yaman

**Sprint:** 1 (14/10–28/10/2026) · **Goal:** close my gaps in the Sprint 1 fundamentals from the [Online Course Register](../../online-course-register/README.md) · **Jira:** [KAN-60](https://yarengursoy.atlassian.net/browse/KAN-60) · **Updated:** 27/10/2026

## Where I start

| Topic | My level before Sprint 1 | What I did in Sprint 1 |
|---|---|---|
| Git & GitHub | Known; I have used Git and GitHub for years | – |
| Markdown | Known | – |
| Python environment | Known | – |
| Evaluation basics | Basic knowledge | Learned through the work: the O2 targets, Recall@5 and the `val`/`test` split while writing the charter |
| Scrum basics | Basic knowledge | Read Scrum.org "What is Scrum?" and the Scrum Guide; Product Owner work in Sprint 1 |
| Jira | Basic knowledge | Built the KAN backlog: epics, stories, sub-tasks, sprints and releases |
| LLM basics | Basic knowledge; I had used LLMs to generate synthetic data | 14/10 workshop |
| Embeddings & vector search | New to me | 14/10 workshop; the embedding choice in the design document |
| RAG | New to me | Learned through the work: the design document and the team's parsing and model selection spikes. The RAG lecture slides are planned for the first week of Sprint 2 |
| Prompt engineering | Basic knowledge, from generating synthetic data | 14/10 workshop; the prompt of the model selection spike |
| Chat interface (Gradio) | New to me | Not needed: the team chose React (section 6) |

## 1. RAG

**Source:** the team's [design document](../../Markdown%20Template/11-system-architecture-design-document.md), [parsing spike](parsing-spike.md) and [model selection spike](model-selection-spike.md)

**Expected output:** I can describe the two phases of ELIZA's pipeline in my own words at the Sprint 1 review.

**What I learned:**

- **Indexing** happens before any question is asked, and again when the source text changes: the source text is split into small pieces (chunks), each piece is turned into a vector, and the vectors are stored.
- **Query** happens for every question: the question is turned into a vector, the closest pieces are found, and the model is told to write the answer only from those pieces.
- RAG can reduce hallucination because the model is given the relevant source text to answer from and can cite it. It does not guarantee that every statement is supported by the retrieved pieces, so ELIZA's answers are checked against their cited pieces (O2 (b)). It does not remove it, so ELIZA's answers are checked against their cited pieces (O2 (b)).

**In ELIZA:** one piece per Article paragraph or Annex point, with its reference and the version date (D5).

## 2. LLM basics

**Source:** 14/10 workshop

**Expected output:** I can explain what a token, the context window and temperature are, and why an LLM can make things up.

**What I learned:** the model reads and writes **tokens** (pieces of words); the **context window** is how many tokens fit in at once, so the question and the retrieved pieces must fit in it; a low **temperature** gives more repeatable answers; an LLM **hallucinates** because it writes the most likely continuation, not a checked fact.

**Hands-on:** I did not run a model in Colab myself; the team's model selection spike (KAN-57) ran the candidate open-source models on Colab and on a team computer.

## 3. Embeddings & vector search

**Source:** 14/10 workshop; decision D10 in the design document

**Expected output:** I can explain why a question in everyday words can find the right provision.

**What I learned:** an embedding turns a text into a vector, so that texts with a similar meaning are close to each other; vector search returns the stored pieces closest to the question. So "our AI grades exams" can find "evaluate learning outcomes" (Annex III point 3(b)) although the words differ.

## 4. Prompt engineering

**Source:** 14/10 workshop; the prompt in the model selection spike

**Expected output:** I can check the team's prompt against the acceptance criteria of my stories.

**What I learned:** give the retrieved pieces in a separate, marked part of the prompt; tell the model to answer only from them and to cite the Article or Annex; let it say that the pieces do not answer the question (KAN-23) and never give a legal verdict (KAN-2).

## 5. Scrum basics and Jira

**Sources:** Scrum.org ["What is Scrum?"](https://www.scrum.org/resources/what-scrum-module), the [Scrum Guide](https://scrumguides.org/scrum-guide.html), the course's [Jira sync guide](../JIRA_SYNC_SETUP.md)

**Expected output:** the KAN backlog, ready for Sprint 2 planning.

**What I learned:** the Product Owner orders the backlog and keeps the stories clear enough to start; a **user story** is a user's need with testable acceptance criteria, a **task** delivers part of a story, a **spike** is timeboxed learning like this note; story points go on the stories and hours on the sub-tasks (Model A of the sync guide).

**Result:** eight epics and their stories and sub-tasks, shown in the [User Story Map v1](../../Markdown%20Template/06-user-stories/01-user-story-map-v1.md).

## 6. Chat interface (Gradio)

Not needed: the team chose React with a Node.js backend (design document, decision D1), so I did not build the Gradio "hello world".

## My computer

Recorded for [Facilities & Resources](../../Markdown%20Template/03-project-canvas/09-facilities-and-resources.md) row 1. The system runs on CPU only; the GPU may be used only to speed up offline experiments (C-05).

| Item | Value |
|---|---|
| Computer | Dell Precision 7680 |
| Processor | Intel Core i7-13850HX (2.10 GHz) |
| Memory | 32 GB |
| Graphics | Intel UHD Graphics; NVIDIA GeForce RTX laptop GPU |
| Operating system | Windows 11 Enterprise 24H2 |

## Definition of Done

- [x] My starting knowledge and learning gaps are recorded in the topic table above.
- [x] I reviewed Scrum fundamentals and applied them as Product Owner while organizing the Jira backlog.
- [x] The LLM, embeddings, vector search, and prompt engineering concepts introduced in the 14/10 workshop are documented in sections 2–4.
- [x] The RAG concepts I learned through the team's technical documents are explained in section 1, and the evaluation concepts I learned while preparing the charter are recorded in the topic table.
- [x] The learning sources, relevant project artifacts, and activities not performed individually are clearly documented.
- [ ] I can explain ELIZA's indexing and query phases in my own words at the Sprint 1 review (28/10/2026).

**Planned follow-up (Sprint 2):**

- [ ] Review the RAG lecture slides during the first week of Sprint 2 (by 04/11/2026).
