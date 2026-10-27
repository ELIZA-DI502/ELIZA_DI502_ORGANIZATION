# Story Requirements for Epic KAN-30: System design and delivery

Version v1, end of Sprint 1 (27/10/2026). Source: Jira project KAN. Back to the [User Story Map v1](01-user-story-map-v1.md) · [all story requirements pages](README.md).

| Epic | System design and delivery |
|---|---|
| Summary | How the assistant is built and delivered, apart from its user-facing features: the System Architecture Design Document, ADRs and spikes (D4, Sprint 1, updated every sprint), and the non-feature work of each release: baseline experiment, the whole pipeline run from `README.md` on a team computer, `config/rag.yaml`, pinned requirements, SBOM, tracked experiments, user interface mockup, Git rules and the release candidate (D6, D9, D11). |
| Features | Design document and spikes (D4), alpha, beta, release candidate (D6, D9, D11) |
| Document Owner | Yeşim (Product Owner) |
| Designer | Gözde Nur (design decisions, KAN-58) and Kaan (design document, KAN-59) |
| Developers | Gözde Nur, Kaan, Yaren, Yeşim (Sprint 1); later stories are assigned at each sprint planning |
| Release Target (Sprint) | Sprint 1 (Pre-alpha); Sprint 2 (Alpha 0.1); Sprint 3 (Beta 0.5); Sprint 4 (Release candidate 1.0) |
| Traceability | Constraints: C-03, C-05. Major Activities rows 5–7, 9, 16. |
| Jira | [KAN-30](https://yarengursoy.atlassian.net/browse/KAN-30) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

| # | User story title | User story description | Priority | Points | Owner | Sprint | Notes | Jira |
|---|---|---|---|---|---|---|---|---|
| S1 | [Agree on the technologies for the baseline](#s1--agree-on-the-technologies-for-the-baseline) | As a Data Scientist, I want the architecture, the chosen technologies and the reasons behind them recorded before Sprint 2, so that I can start building the baseline on agreed technologies. | High | 13 | Gözde Nur | Sprint 1 | Release: Pre-alpha; Status: In progress (27/10/2026). | [KAN-81](https://yarengursoy.atlassian.net/browse/KAN-81) |
| S2 | [Close my gaps in the Sprint 1 fundamentals](#s2--close-my-gaps-in-the-sprint-1-fundamentals) | As a Data Scientist, I want to close my gaps in the Sprint 1 fundamentals with a learning spike, so that I can work on the RAG pipeline from Sprint 2. | Medium | 3 | Yaren | Sprint 1 | Release: Pre-alpha; Status: In progress (27/10/2026). | [KAN-82](https://yarengursoy.atlassian.net/browse/KAN-82) |
| S3 | [Measure how well the baseline retrieval finds the expected provisions](#s3--measure-how-well-the-baseline-retrieval-finds-the-expected-provisions) | As a Project Review Committee member, I want to see how often the most basic retrieval finds the expected provision, compared with the target in the charter, so that I can judge whether the project starts from a measured baseline. | High | – | – | Sprint 2 | Release: Alpha 0.1; Depends on [KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65) (question set v1) and [KAN-86](https://yarengursoy.atlassian.net/browse/KAN-86) (indexed source text). | [KAN-87](https://yarengursoy.atlassian.net/browse/KAN-87) |
| S4 | [Review the system design, the models used and the interface plan](#s4--review-the-system-design-the-models-used-and-the-interface-plan) | As a Project Review Committee member, I want the design document, the software bill of materials and the interface mockup to match the system as it is built in Sprint 2, so that I can review every decision and every model the team used. | High | – | – | Sprint 2 | Release: Alpha 0.1. | [KAN-88](https://yarengursoy.atlassian.net/browse/KAN-88) |
| S5 | [Run the whole pipeline from one README](#s5--run-the-whole-pipeline-from-one-readme) | As a Project Review Committee member, I want to install and run the whole assistant, user interface included, from one README, so that I can check that the pipeline works end to end. | High | – | – | Sprint 3 | Release: Beta 0.5. | [KAN-168](https://yarengursoy.atlassian.net/browse/KAN-168) |
| S6 | [Measure the beta against the baseline and the charter targets](#s6--measure-the-beta-against-the-baseline-and-the-charter-targets) | As a Project Review Committee member, I want every experiment compared with the Sprint 2 baseline and the beta measured against the charter targets on the same questions, so that I can see which configuration is best and whether the beta is ready for the pilot. | High | – | – | Sprint 3 | Release: Beta 0.5; Depends on [KAN-170](https://yarengursoy.atlassian.net/browse/KAN-170) (question set v2). | [KAN-169](https://yarengursoy.atlassian.net/browse/KAN-169) |
| S7 | [Use a release candidate with the pilot problems fixed](#s7--use-a-release-candidate-with-the-pilot-problems-fixed) | As an EdTech AI developer, I want to use a release candidate in which the problems found in the pilot are fixed, so that the system shown in the final demo is the one I can actually rely on. | High | – | – | Sprint 4 | Release: Release candidate 1.0; Depends on [KAN-202](https://yarengursoy.atlassian.net/browse/KAN-202) and [KAN-72](https://yarengursoy.atlassian.net/browse/KAN-72) (problems found in the pilot). | [KAN-203](https://yarengursoy.atlassian.net/browse/KAN-203) |

Priority, points, owner and sprint are as in Jira on 27/10/2026. Sprint 1 stories were estimated with planning poker; the other stories are estimated and assigned at their sprint planning, starting with Sprint 2 on 28/10/2026. A dash means not decided yet.

Test cases: KAN-8, KAN-2 and KAN-3 already have test cases; a test for every story (the input or steps and the expected result) is added next to it in Sprint 2 ([KAN-90](https://yarengursoy.atlassian.net/browse/KAN-90)).

## S1 · Agree on the technologies for the baseline

[KAN-81](https://yarengursoy.atlassian.net/browse/KAN-81) · Sprint 1 (Pre-alpha) · Priority High · Points 13 · Owner Gözde Nur

**Story:** As a Data Scientist, I want the architecture, the chosen technologies and the reasons behind them recorded before Sprint 2, so that I can start building the baseline on agreed technologies.

**Acceptance criteria**

1. The design document fills every section of the current course template and contains the architecture diagram with every component (ingestion, chunking, embedding, vector store, retriever, LLM, input and output checks, user interface).
2. Each component names its chosen technology and has an ADR, or is marked open and links to a spike note.
3. Spike notes exist for source parsing and for running an open-source quantized LLM on CPU, and the chosen models' licences are recorded.
4. The model spike note records the answer time of each candidate model on CPU, so that the chosen model can run on a team member's computer without a paid cloud instance (A-07; D4 criterion 5).
5. The design document records an answer-time limit (A-07, R-13) and describes the out-of-scope notice in its Interfaces section (C-04).

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Spike: parse and chunk the EUR-Lex HTML | A spike note in docs/spikes/ shows whether Articles, paragraphs and Annex points can be extracted with their identifiers, and proposes a first chunking rule (one chunk per Article paragraph or Annex point). Throw-away notebook, no production code. | Gözde Nur | – | Done | [KAN-56](https://yarengursoy.atlassian.net/browse/KAN-56) |
| Spike: run open-source quantized models on CPU, check their licences and record the answer time | At least two open-source quantized models run on CPU only (Colab CPU runtime or a team member's computer) on a few sample questions. The answer time and the licence of each are recorded in a spike note. Throw-away notebook, no production code. | Gözde Nur | – | Done | [KAN-57](https://yarengursoy.atlassian.net/browse/KAN-57) |
| Write the ADRs for the model, embedding, vector store and user interface choices | Every technology marked as chosen in the design document has an ADR in docs/adr/. Every open choice links to a spike note. The chosen LLM is open-source and runs on CPU on a team member's computer, without a paid cloud instance. | Gözde Nur | – | Done | [KAN-58](https://yarengursoy.atlassian.net/browse/KAN-58) |
| Write the System Architecture Design Document v1 with the architecture diagram | The design document fills every section of the course template (Markdown Template/11-system-architecture-design-document.md): summary, goals and non-goals, diagram, components, design details, decisions, open design areas, change log. The diagram shows every component: ingestion, chunking, embedding, vector store, retriever, LLM, input and output checks, user interface. Each component names its chosen technology or is marked "open" with a link to a spike note. The document states the session and privacy boundaries (C-04, C-10). | Kaan | – | To do | [KAN-59](https://yarengursoy.atlassian.net/browse/KAN-59) |

The story carries the points and its sub-tasks are not estimated separately (Model A of the course's [Jira sync guide](../../docs/JIRA_SYNC_SETUP.md)).

**Traceability**

Deliverable: D4 System Design v1 (due 27/10/2026)    
Milestone: M2 Sources and first design ready; M3 Checkpoint: Sprint 1 reviewed, development starts (28/10/2026)    
Assumptions / constraints / risks: A-07, A-10; C-03, C-04, C-05; R-13

## S2 · Close my gaps in the Sprint 1 fundamentals

[KAN-82](https://yarengursoy.atlassian.net/browse/KAN-82) · Sprint 1 (Pre-alpha) · Priority Medium · Points 3 · Owner Yaren

**Story:** As a Data Scientist, I want to close my gaps in the Sprint 1 fundamentals with a learning spike, so that I can work on the RAG pipeline from Sprint 2.

**Acceptance criteria**

1. Each team member has one learning spike note in `docs/spikes/` on topics from the course's Sprint 1 fundamentals.
2. Each note states the member's starting level, the sources used, the expected output and a Definition of Done.
3. The Sprint 1 page links all four notes.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Learning spike: RAG indexing and query phases | A learning spike note of at most one page is in docs/spikes/. It explains the indexing and query phases of a RAG pipeline and why RAG reduces hallucination. The member can explain the topic at the Sprint 1 review. Timeboxed; the member may choose another topic from the course's Sprint 1 fundamentals. | Yeşim | – | Done | [KAN-60](https://yarengursoy.atlassian.net/browse/KAN-60) |
| Learning spike: LLM basics and prompt engineering | A learning spike note of at most one page is in docs/spikes/. It covers tokens, context window, temperature and why LLMs hallucinate, and gives a prompt that answers only from the given passages and says when it does not know. The member can explain the topic at the Sprint 1 review. Timeboxed; the member may choose another topic from the course's Sprint 1 fundamentals. | Yaren | – | To do | [KAN-61](https://yarengursoy.atlassian.net/browse/KAN-61) |
| Learning spike: Scrum, Git and prompt engineering | A learning spike note of at most one page is in docs/spikes/ (`learning-gozde-nur.md`). It covers Scrum, Git and prompt engineering from the course's Sprint 1 fundamentals and states what the member learned for each topic; throw-away code only. The member can explain the topics at the Sprint 1 review. Timeboxed. | Gözde Nur | – | Done | [KAN-62](https://yarengursoy.atlassian.net/browse/KAN-62) |
| Learning spike: evaluation basics and Recall@5 | A learning spike note of at most one page is in docs/spikes/. It explains what an evaluation set is, why it must be fixed before experiments, and what Recall@5 measures. The member can explain the topic at the Sprint 1 review. Timeboxed; the member may choose another topic from the course's Sprint 1 fundamentals. | Kaan | – | To do | [KAN-63](https://yarengursoy.atlassian.net/browse/KAN-63) |

The story carries the points and its sub-tasks are not estimated separately (Model A of the course's [Jira sync guide](../../docs/JIRA_SYNC_SETUP.md)).

**Traceability**

Deliverable: D4 System Design v1, acceptance criterion 7 (due 27/10/2026)    
Milestone: M2 Sources and first design ready (28/10/2026)

## S3 · Measure how well the baseline retrieval finds the expected provisions

[KAN-87](https://yarengursoy.atlassian.net/browse/KAN-87) · Sprint 2 (Alpha 0.1) · Priority High · Points – · Owner –

**Story:** As a Project Review Committee member, I want to see how often the most basic retrieval finds the expected provision, compared with the target in the charter, so that I can judge whether the project starts from a measured baseline.

**Acceptance criteria**

1. The vector index covers every chunk from D5, and the retriever returns the top 5 passages for each D2 `val` question (course halfway check: by 11/11/2026 for a handful of test questions).
2. Recall@5 and the comparison of answers without and with retrieval on the `val` split are logged in Weights & Biases and recorded in `Markdown Template/12-experiment-cards/E1-baseline.md` (D6 criterion 5).
3. The baseline experiment card records the corpus version from `data/manifest.csv`, the prompt templates and the `config/rag.yaml` version (D6 criterion 9).
4. A team member who did not build it can install and run the baseline from `README.md`; `requirements.txt` has 0 unpinned packages; prompts are in `prompts/` (D6 criteria 1, 9).
5. The Sprint 2 technical summary names the chosen metrics and why, the baseline score, the target from the charter, and the known failures on the `val` split (D6 criteria 5, 8).

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Build the vector index and the retriever | The embedding model and vector store chosen in the design document index every D5 chunk, and the retriever returns the top 5 passages for a question; retrieval parameters are in `config/rag.yaml`. By 11/11/2026 retrieval returns passages for a handful of test questions (course halfway check). | – | – | To do | [KAN-97](https://yarengursoy.atlassian.net/browse/KAN-97) |
| Set up the README, pinned requirements and prompts folder | `README.md` explains setup and running; `requirements.txt` has 0 unpinned packages; prompts are in `prompts/`. A team member who did not build it runs it once from the README. | – | – | To do | [KAN-98](https://yarengursoy.atlassian.net/browse/KAN-98) |
| Run Recall@5 and the comparison without and with retrieval on the val split | Recall@5 and the answers without and with retrieval are logged in Weights & Biases for every D2 `val` question. | – | – | To do | [KAN-99](https://yarengursoy.atlassian.net/browse/KAN-99) |
| Write the baseline experiment card | `Markdown Template/12-experiment-cards/E1-baseline.md` records the baseline parameters, the corpus version from `data/manifest.csv`, the prompt templates, the `config/rag.yaml` version and the results. | – | – | To do | [KAN-100](https://yarengursoy.atlassian.net/browse/KAN-100) |
| Write the Sprint 2 technical summary | `Markdown Template/05-sprint-2/01-review-committee-technical-summary.md` gives the chosen metrics and why, the baseline score, the target from the charter and the known failures on the `val` split, and links the baseline experiment card. The metrics and their targets are drafted by 11/11/2026 (course halfway check). | – | – | To do | [KAN-101](https://yarengursoy.atlassian.net/browse/KAN-101) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverable: D6 Alpha Release (due 14/11/2026; criteria 1, 5, 8, 9)    
Milestone: M4 Baseline (alpha) runs on the full validation question set (18/11/2026)    
Objective: O2 Evidence (a)    
Major Activities: rows 9, 23, 28    
Dependencies: rows 6, 7    
Constraints: C-03 RAG chatbot with an open-source quantized model; C-05 No GPU

## S4 · Review the system design, the models used and the interface plan

[KAN-88](https://yarengursoy.atlassian.net/browse/KAN-88) · Sprint 2 (Alpha 0.1) · Priority High · Points – · Owner –

**Story:** As a Project Review Committee member, I want the design document, the software bill of materials and the interface mockup to match the system as it is built in Sprint 2, so that I can review every decision and every model the team used.

**Acceptance criteria**

1. The design document has a record for every decision taken in Sprint 2, and the diagram and RAG parameters as the system is at the upload date (course Sprint 2 deliverable).
2. The design document describes each RAG pipeline stage with its parameters, and names the user interface technology (course halfway check: chosen by 11/11/2026).
3. The SBOM lists every model tried, with its exact version, provider, licence, link to its source model card, accesser and access date, method of interaction, whether it is used and why, and its experiment card; it also lists tools and services not in `requirements.txt` (D6 criterion 9).
4. A mockup of the user interface is added as an image; it shows the question box, the answer with citations and version date, and the permanent notice (D6 criterion 6).
5. Every spike run in Sprint 2 has its note in `docs/spikes/`.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Update the design document for Sprint 2 | `11-system-architecture-design-document.md` describes each RAG pipeline stage with its parameters, has a decision record for every decision taken in Sprint 2, and shows the diagram as the system is at the upload date. | – | – | To do | [KAN-102](https://yarengursoy.atlassian.net/browse/KAN-102) |
| Choose the user interface technology | The user interface technology (for example Gradio or Streamlit) and the reason for the choice are recorded in the design document by 11/11/2026 (course halfway check). | – | – | To do | [KAN-103](https://yarengursoy.atlassian.net/browse/KAN-103) |
| Draw the user interface mockup | An image of the user interface shows the question box, an answer with Article/Annex citations and the version date, and the permanent "not legal advice" notice. It does not have to be connected to the system. | – | – | To do | [KAN-104](https://yarengursoy.atlassian.net/browse/KAN-104) |
| Write the Software Bill of Materials | `10-software-bill-of-materials.md` lists every model tried, with its exact version, provider, licence, link to its source model card, accesser and access date, method of interaction, whether it is used and why, and its experiment card; tools and services not in `requirements.txt` are also listed. | – | – | To do | [KAN-105](https://yarengursoy.atlassian.net/browse/KAN-105) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverable: D6 Alpha Release (due 14/11/2026; criteria 6, 9)        
Milestone: M4 Baseline (alpha) runs on the full validation question set (18/11/2026)        
Major Activities: rows 5, 14, 16        
Constraints: C-03 RAG chatbot with an open-source quantized model; C-08 Information, not legal advice        
Assumption / Risk: A-10 / R-07 The model or a library changes

## S5 · Run the whole pipeline from one README

[KAN-168](https://yarengursoy.atlassian.net/browse/KAN-168) · Sprint 3 (Beta 0.5) · Priority High · Points – · Owner –

**Story:** As a Project Review Committee member, I want to install and run the whole assistant, user interface included, from one README, so that I can check that the pipeline works end to end.

**Acceptance criteria**

1. The interface calls the full pipeline (retrieval, answer generation and the input and output checks) as one simple pipeline; by 02/12/2026 it does so even if some parts are still stubs (course Sprint 3 deliverable and halfway check).
2. A team member who did not build it can install and run the whole pipeline from `README.md`.
3. A screenshot of the interface answering a question is in the sprint folder.
4. The design document, spike notes and SBOM describe the system at the Sprint 3 upload.
5. Every branch name and commit message has a Jira key, branches are merged with `git merge --no-ff`, the repository follows the course structure, and the `.zip` is uploaded.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Connect the interface to the full pipeline | The interface calls retrieval, answer generation and the input and output checks as one pipeline; by 02/12/2026 it works even if some parts are still stubs (course halfway check). | – | – | To do | [KAN-172](https://yarengursoy.atlassian.net/browse/KAN-172) |
| Update the README for the full pipeline | `README.md` explains how to install and run the whole pipeline with its interface, and a team member who did not build it runs it once from the README. | – | – | To do | [KAN-173](https://yarengursoy.atlassian.net/browse/KAN-173) |
| Add a screenshot of the interface answering a question | A screenshot of the interface answering a question is in the Sprint 3 folder and linked from the welcome page. | – | – | To do | [KAN-174](https://yarengursoy.atlassian.net/browse/KAN-174) |
| Update the design document, spike notes and SBOM for Sprint 3 | The design document has a record for every Sprint 3 decision and shows the diagram and RAG parameters as the system is at the upload; every Sprint 3 spike has its note; the SBOM lists every model tried and the tools not in `requirements.txt`. | – | – | To do | [KAN-175](https://yarengursoy.atlassian.net/browse/KAN-175) |
| Follow the Git rules for Sprint 3 and upload the zip | Every branch name and commit message in Sprint 3 has a Jira key, branches are merged with `git merge --no-ff`, the repository follows the course structure, and the `.zip` is uploaded to ODTUClass by 05/12/2026. | – | – | To do | [KAN-176](https://yarengursoy.atlassian.net/browse/KAN-176) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverable: D9 Beta Release (due 05/12/2026)      
Milestone: M7 (09/12/2026)      
Major Activities: rows 5, 14, 16      
Constraints: C-03, C-05

## S6 · Measure the beta against the baseline and the charter targets

[KAN-169](https://yarengursoy.atlassian.net/browse/KAN-169) · Sprint 3 (Beta 0.5) · Priority High · Points – · Owner –

**Story:** As a Project Review Committee member, I want every experiment compared with the Sprint 2 baseline and the beta measured against the charter targets on the same questions, so that I can see which configuration is best and whether the beta is ready for the pilot.

**Acceptance criteria**

1. Each experiment has an experiment card with its question, parameter space and search method; every run is tracked in Weights & Biases; at least one improvement over the baseline is measured by 02/12/2026 (course Sprint 3 deliverable and halfway check).
2. The best combination from each experiment is re-run with at least 3 seeds and reported as mean ± std; `config/rag.yaml` holds only the chosen product configuration (D9 criterion 6).
3. On the frozen D8 `val` split, O2 (a)–(d) and O4 per safety category are reported against the charter targets, and 0 answers contain a classification or compliance verdict (D9 criteria 2–4).
4. Every in-scope `val` answer is reviewed against the rubric by one reviewer, and a second reviewer checks a sample; disagreements are logged.
5. The Sprint 3 technical summary compares the best configuration with the baseline, reports pass or fail for the test of every story built so far, and marks each feature as implemented or deferred (D9 criterion 5).

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Plan the experiments and their parameter space | Each planned experiment has its own card in `Markdown Template/12-experiment-cards/` with its question, what it is compared against (the baseline), the parameter space and the search method. | – | – | To do | [KAN-177](https://yarengursoy.atlassian.net/browse/KAN-177) |
| Run the experiments in Weights & Biases | Every experiment run is tracked in W&B, and at least one improvement over the baseline is measured by 02/12/2026, with a link to its W&B run (course halfway check). | – | – | To do | [KAN-178](https://yarengursoy.atlassian.net/browse/KAN-178) |
| Re-run the best configurations with at least 3 seeds | The best combination from each experiment is re-run with at least 3 seeds and reported as mean ± std; the best configuration is named and `config/rag.yaml` holds only that product configuration. | – | – | To do | [KAN-179](https://yarengursoy.atlassian.net/browse/KAN-179) |
| Report O2 and O4 on the frozen D8 val split | On the D8 `val` split frozen on 01/12/2026, O2 (a)–(d) and O4 per safety category (correct responses / questions evaluated and %) are reported against the charter targets; 0 answers contain a classification or compliance verdict; any unmet level is recorded as a known limitation or a Sprint 4 fix. | – | – | To do | [KAN-180](https://yarengursoy.atlassian.net/browse/KAN-180) |
| Review the in-scope val answers against the rubric | One reviewer checks every in-scope `val` answer against the rubric's "fully supported" definition (O2 (b)); a second reviewer checks a sample of the answers; disagreements are resolved against the rubric and logged. | – | – | To do | [KAN-181](https://yarengursoy.atlassian.net/browse/KAN-181) |
| Write the Sprint 3 technical summary | `Markdown Template/05-sprint-3/01-review-committee-technical-summary.md` compares the best configuration with the baseline on the same evaluation set, reports pass or fail for the test of every story built so far, and marks each feature as implemented or deferred. | – | – | To do | [KAN-182](https://yarengursoy.atlassian.net/browse/KAN-182) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverable: D9 Beta Release (due 05/12/2026)    
Milestone: M7 (09/12/2026)    
Objectives: O2 Evidence; O4 Safety    
Major Activities: rows 23, 24, 40

## S7 · Use a release candidate with the pilot problems fixed

[KAN-203](https://yarengursoy.atlassian.net/browse/KAN-203) · Sprint 4 (Release candidate 1.0) · Priority High · Points – · Owner –

**Story:** As an EdTech AI developer, I want to use a release candidate in which the problems found in the pilot are fixed, so that the system shown in the final demo is the one I can actually rely on.

**Acceptance criteria**

1. Every problem seen during the pilot is logged without asking participants for personal data (C-10).
2. The logged pilot errors are prioritised: every critical error (a wrong citation, a legal verdict, a stored personal-data item or a crash) is fixed, and every error that is not fixed is listed as a known limitation in the Sprint 4 technical summary; no new features are added after the pilot.
3. The README, SBOM, design document and data cards describe the release candidate shown in the final demo.
4. The Sprint 4 code follows the course Git rules, and the release is uploaded to ODTUClass as a zip.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Log the problems seen during the pilot | Every problem seen during the pilot is logged as a Jira bug or in the pilot log, without asking participants for personal data. | – | – | To do | [KAN-209](https://yarengursoy.atlassian.net/browse/KAN-209) |
| Fix the pilot errors without adding features | Every critical pilot error (a wrong citation, a legal verdict, a stored personal-data item or a crash) is fixed, every error that is not fixed is listed as a known limitation in the Sprint 4 technical summary, no new feature is added after the pilot, and the story tests still pass. | – | – | To do | [KAN-210](https://yarengursoy.atlassian.net/browse/KAN-210) |
| Update the final documents to describe the demo system | The README, SBOM, design document and data cards describe the release candidate shown in the final demo. | – | – | To do | [KAN-211](https://yarengursoy.atlassian.net/browse/KAN-211) |
| Follow the Git rules for Sprint 4 and upload the zip | The Sprint 4 code follows the course Git rules (branches, pull requests, tag) and the release is uploaded to ODTUClass as a zip. | – | – | To do | [KAN-212](https://yarengursoy.atlassian.net/browse/KAN-212) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Objective: O1–O4 (system used in the final evaluation)        
Deliverable: D11 Release Candidate and Final Evaluation (due 30/12/2026)        
Milestone: M10 (30/12/2026)        
Constraint: C-10
