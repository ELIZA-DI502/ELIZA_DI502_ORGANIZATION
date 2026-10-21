# Learning spike: Aliye Yeşim Yaman

**Sprint:** 1 (14/10–28/10/2026) · **Goal:** close my gaps in the Sprint 1 fundamentals from the [Online Course Register](../../online-course-register/README.md) · **Jira:** KAN-60

## Where I start

| Topic | My level before Sprint 1 | What I do in Sprint 1 |
|---|---|---|
| Git & GitHub | Known; I have used Git and GitHub for years | – |
| Markdown | Known | – |
| Python environment | Known | – |
| Evaluation basics | Known | – |
| Scrum basics | Basic knowledge | Read Scrum.org "What is Scrum?" and the Scrum Guide |
| Jira | Basic knowledge | Work with epics, stories, tasks, releases and sprints in our KAN project |
| LLM basics | Basic knowledge | Workshop material (14/10) |
| Embeddings & vector search | Basic knowledge | Workshop material (14/10) |
| RAG | Need to learn | This learning spike (KAN-60), by 28/10/2026 |
| Prompt engineering | Basic knowledge | Workshop material |
| Chat interface (Gradio) | Need to learn | Gradio's ChatInterface guide |

## 1. RAG

**Source:** [Lewis et al. (2020)](https://arxiv.org/abs/2005.11401) and the lecture slides (resources given in the Online Course Register)

**Goal:** learn the indexing and query phases of a RAG pipeline and why RAG reduces hallucination.

- **Indexing** (once, and again when the source changes): parse the documents, split them into chunks, turn each chunk into a vector and store it with its metadata.
- **Query** (for every question): turn the question into a vector, retrieve the most similar chunks, put them in the prompt and generate an answer from them.

**Expected output:** I can explain each phase for ELIZA at the Sprint 1 review: one chunk per Article paragraph or Annex point with its identifier and version date (D5), top-5 retrieval measured with Recall@5 (D6), and answers that cite only retrieved provisions (R-20).

## 2. LLM basics

**Source:** workshop material (14/10)

**Goal:** understand tokens, the context window, prompts and temperature, and why LLMs hallucinate; run a small open-source model in Colab.

**Expected output:** I can explain why ELIZA answers only from retrieved provisions and why a small quantized model on CPU (C-03, C-05) needs short answers and few retrieved passages.

## 3. Embeddings & vector search

**Source:** workshop material (14/10)

**Goal:** understand how a text becomes a vector and how similarity search finds the passages closest to a question.

**Expected output:** I can explain why "our AI grades exams" can find the provision on "evaluate learning outcomes" (Annex III point 3(b)), and why a question that names "Article 6(3)" may also need keyword search.

## 4. Prompt engineering

**Source:** workshop material

**Goal:** write a prompt that tells the model to answer only from the given passages and to say when it does not know.

**Expected output:** I can check our prompt against the acceptance criteria of KAN-2 (no legal decision) and KAN-23 (insufficient evidence).

## 5. Scrum basics and Jira

**Sources:** Scrum.org ["What is Scrum?"](https://www.scrum.org/resources/what-scrum-module), the [Scrum Guide](https://scrumguides.org/scrum-guide.html)

**Goal:** understand the Product Owner's responsibilities and the difference between a user story, a task and a spike; plan sprints in Jira.

**Expected output:** the KAN backlog: four epics with 14 user stories for Sprints 2–3, four epics with the Sprint 1 tasks, and four releases matching the Release Plan.

## 6. Chat interface (Gradio)

**Source:** Gradio documentation, ["Creating a chatbot fast"](https://www.gradio.app/guides/creating-a-chatbot-fast)

**Goal:** build a "hello world" chat app with Gradio's `ChatInterface`.

**Expected output:** a working "hello world" chat app, by 28/10/2026.

## Definition of Done

- [ ] Explain the indexing and query phases of ELIZA's RAG pipeline at the Sprint 1 review.
- [ ] Close the gaps marked "Basic knowledge" and "Need to learn" in the table above.
