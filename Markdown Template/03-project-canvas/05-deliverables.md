# Deliverables

Identify and define the high-level deliverables required to achieve the project's objectives. A **deliverable** is a tangible artifact, product or result produced as a direct output of work. It fulfils a requirement.

Because this project follows Scrum, the charter itself is updated iteratively. Treat each version as a separate deliverable (e.g., "Project Charter v1" as Deliverable 1, "Project Charter v2" as Deliverable 2, and so on).

A weak deliverable cannot be checked. A strong one can. Write "Acceptance criteria: Recall@5 ≥ 0.70 on the 200-question test set", not "The model works well" (examples illustrative only).

## Two kinds of deliverable

Include both kinds.

| Kind | What it is | Examples |
|---|---|---|
| **Solution deliverable** | Part of the product or its technical documentation | Features, data dictionary, solution architecture report, Q&A Generation-Dataset, and the alpha, beta and release candidate builds (see [Release Plan](03-project-canvas_v2/10-release-plan.md)) |
| **Project-management deliverable** | Needed for review and approval | Charter document (each version), lessons learned register, data quality report, status dashboard, final report, exit report |

### Deliverables the course expects

- **Each charter version** as its own deliverable.
- **A Q&A Generation-Dataset** for evaluating the system. Say how you will make the generated questions diverse and representative. You can use an existing Q&A dataset from your domain if one exists.
- **Datasheets and model cards**, if you plan to deliver them, follow Mitchell et al. [1] and Gebru et al. [2], not Hugging Face or other formats.
  - Write a model card yourself only when you train or fine-tune a model. For a model used as-is, import the model card from its source or document the model in the AI SBOM.
  - If a dataset already has a datasheet at its source and you do no further preprocessing, a separate datasheet is not needed. A data quality report or a preprocessing report can be useful instead.

## How to fill in each deliverable

| Field | What it means | When it applies | Question it answers |
|---|---|---|---|
| **Project Deliverable #** | Number and name, e.g., "D3: Q&A Generation-Dataset v1" | Every block | Which deliverable is this? |
| **Description** | What the artifact is and what it contains | Every block | What do we hand over? |
| **Acceptance Criteria** | How quality and completion will be assessed. Each criterion must be measurable. | Every block | How do we know it is done and good enough? |
| **Due Date** | A calendar date (dd/mm/yyyy) inside a sprint (see [Release Plan](03-project-canvas_v2/10-release-plan.md)), aligned with the milestone it supports (see [Milestones](03-project-canvas_v2/02-milestones.md)) | Every block | When? |
| **Stakeholders** | Who the deliverable is **for**: the people or roles who will use or receive it | Every block | For whom? |
| **Approving Stakeholder(s)** | Who **signs off** on it. Use a named person or a role from [Project Organization](03-project-canvas_v2/08-project-organization.md), e.g., Product Owner or Project Review Committee. | Every block | Who says it is accepted? |

**Stakeholders and approvers are different fields.** Assign them carefully. For example, the MVP is developed for the customer, not for the project team. The customer may also be the approver: ISO/IEC 5339 describes the AI customer as consulted during verification and validation and during deployment [3], and ISO/IEC 5338 states that validation is ratified by stakeholders [4].

## Rules

Each rule is a condition you can check with yes or no.

1. The page includes both solution deliverables and project-management deliverables.
2. Each iteration of a document is a separate deliverable. (e.g. Project Charter, Question & Answer Dataset, Model Cards and so on)
3. Every block has all six fields filled.
4. Every acceptance criterion is measurable. It names what is checked and the pass condition: a number with a threshold, or a check with a single yes/no outcome.
5. No acceptance criterion uses an adjective without a number ("fast", "good", "clear", "complete").
6. The Stakeholders field names who the deliverable is for. A customer-facing deliverable, such as the MVP, does not list only the project team.
7. The Approving Stakeholder(s) field names a person or role who signs off.
8. Every due date is aligned with the milestone it supports in [Milestones](03-project-canvas_v2/02-milestones.md).
9. There is a Q&A Generation-Dataset deliverable whose acceptance criteria cover the diversity and representation of the questions.
10. Any model card written by the team is for a model the team trained or fine-tuned.
11. If an objective in [Project Executive Summary](03-project-canvas_v2/01-project-executive-summary.md) sets a target that is measured later (e.g., user satisfaction), a deliverable holds the result (e.g., the survey result).
12. Deliverables do not force a waterfall approach. For example, the product is delivered in several versions across sprints, not once at the end.

## Test: three questions for every acceptance criterion

1. **Could two people check it and agree?** If they could disagree, it is not measurable.
2. **Is there a number or a yes/no check instead of an adjective?** "Responses are fast" fails; "p95 latency ≤ 3 s on the test set" passes (illustrative).
3. **Has the approving stakeholder agreed to it?** ISO/IEC 5338 asks for explicit agreement on stakeholder requirements, including critical performance measures [4]. If the approver has not seen the criterion, it is not agreed.

## Not this / this

Each corrected entry fixes only the named defect. All examples are illustrative.

| Not this | This | Defect |
|---|---|---|
| MVP deliverable, Stakeholders: "Project team" | Stakeholders: "AI customer: the office that would use the assistant; AI users: its staff" | The MVP is developed for the customer, not the team |
| Final demo deliverable: "Quality meets goals (e.g., good accuracy and fast responses)" | "Accuracy and p95 latency meet the thresholds of objective 1 in [Project Executive Summary](03-project-canvas_v2/01-project-executive-summary.md) (e.g., accuracy ≥ 70%, p95 ≤ 10 s on the test set)" | Adjectives instead of measurable criteria |
| Documentation-card deliverables: "Each card must provide complete, clear, and reproducible documentation" | "Every section of the Mitchell et al. [1] template is filled; every reported metric links to an experiment card" | Not measurable |
| No Q&A dataset deliverable | Add "Q&A Generation-Dataset v1", with criteria on topic coverage and question types | A separate Q&A dataset deliverable is required |
| "Datasheet and Data Quality Report" for an external dataset used as-is that already has a datasheet at its source | "Data Quality Report v1" only, linking to the source's datasheet | A separate datasheet is not needed |
| One "Project Charter" deliverable and no later versions | "Project Charter v1" (Sprint 1) and "Project Charter v2" (Sprint 2) as separate deliverables | Each charter version is a separate deliverable |
| Version 1 and version 2 of the same deliverable with identical description and acceptance criteria | Version 2's criteria state what is new, e.g., "covers 20 indexed items instead of 10" | Deliverables not clearly defined |

## Patterns to use if stuck

- **Version it.** Plan v1, v2, … of a deliverable across sprints, as with the charter. Each version's criteria say what is new.
- **One deliverable per milestone condition.** Ask what artifact proves the milestone in [Milestones](03-project-canvas_v2/02-milestones.md).
- **Release builds as deliverables.** Make each alpha, beta and release candidate in [Release Plan](03-project-canvas_v2/10-release-plan.md) a deliverable.
- **Borrow thresholds from [Project Executive Summary](03-project-canvas_v2/01-project-executive-summary.md).** Reuse the success-criteria numbers of the objective the deliverable serves. This also means referring to metrics by name. (e.g. Recall@k, MRR, Faithfullness)
- **Documentation set.** Typical documentation deliverables are the Dataset Report, Q&A Data Report or Third-party Dataset Register, the AI SBOM, model cards (training or fine-tuning only) and experiment cards.

## What doesn't belong on this page

| Item | Where it belongs |
|---|---|
| Events and checkpoints, and the alignment rule | [Milestones](03-project-canvas_v2/02-milestones.md) |
| Sprint dates and releases | [Release Plan](03-project-canvas_v2/10-release-plan.md) |
| Objective success criteria | [Project Executive Summary](03-project-canvas_v2/01-project-executive-summary.md) |
| Deliverables needed from, or required by, other projects | [Dependencies](03-project-canvas_v2/06-dependencies.md) |
| Costs | [Cost & Funding](03-project-canvas_v2/07-cost-and-funding.md) |
| Roles and who holds them | [Project Organization](03-project-canvas_v2/08-project-organization.md) |
| The content of datasheets, model cards and experiment cards | Their own pages |

## Deliverable block

Copy and paste the block below as needed for each deliverable.

The ELIZA team builds a RAG-based information assistant that helps provider-side technical teams building AI systems for education find and understand the EU AI Act provisions that relate to their use case. This page lists what we hand over, how each item is checked, and who accepts it.

The product is delivered in three versions (alpha, beta, release candidate), and the charter and the Q&A dataset are versioned. Sprint dates follow the course calendar in the [Release Plan](10-release-plan.md): Sprint 1 14/10–28/10/2026, Sprint 2 28/10–18/11/2026, Sprint 3 18/11–09/12/2026, Sprint 4 09/12–30/12/2026. Each due date is on or before the course upload date of the sprint that holds the matching milestone in [Milestones](02-milestones.md) (27/10, 14/11, 05/12 and 30/12/2026); D2 is due on 11/11/2026, so that the baseline (alpha) can be evaluated on it before the Sprint 2 upload. Thresholds come from the objectives in the [Project Executive Summary](01-project-executive-summary.md) (O1 Search time, O2 Evidence, O3 Understanding, O4 Safety).

From Sprint 2 on, every sprint also delivers the course's common sprint documents: welcome page, Definition of Ready and Done, burndown chart, retrospective, review page, technical summary with experiment cards, design document update, spike notes, Software Bill of Materials (SBOM) and Jira backlog export. They are listed on the course's sprint deliverables page and are not repeated here.

### Overview

| # | Deliverable | Kind | Sprint | Due Date |
|---|---|---|---|---|
| D1 | Project Charter v1 | Project management | 1 | 27/10/2026 |
| D2 | Q&A Generation-Dataset v1 | Solution | 2 | 11/11/2026 |
| D3 | Source Inventory and Manifest v1 | Solution | 1 | 27/10/2026 |
| D4 | System Design v1 | Solution | 1 | 27/10/2026 |
| D5 | Preprocessing Report v1 | Solution | 2 | 14/11/2026 |
| D6 | Alpha Release | Solution | 2 | 14/11/2026 |
| D7 | Project Charter v2 | Project management | 2 | 14/11/2026 |
| D8 | Q&A Generation-Dataset v2 | Solution | 3 | 05/12/2026 |
| D9 | Beta Release | Solution | 3 | 05/12/2026 |
| D10 | Pilot Evaluation Report | Project management | 4 | 30/12/2026 |
| D11 | Release Candidate and Final Evaluation | Solution | 4 | 30/12/2026 |

No model training or fine-tuning is planned, so a team-authored model card is not currently a deliverable. The embedding model and the LLM are used as-is and documented in the Software Bill of Materials (`10-software-bill-of-materials.md`, delivered with D6 and updated in D11) with their versions, licences and links to their source model cards. The legal source corpus and its processing will be documented through the source manifest (D3) and preprocessing report (D5).

### Sprint 1 · Discovery

| Project Deliverable #: | D1: Project Charter v1 |
|---|---|
| Description: | First version of the Project Canvas pages in `Markdown Template/` requested in Weeks 3 and 4: Executive Summary (with the Scope Definition), Milestones, Assumptions & Constraints, Deliverables, Project Organization, Major Activities, Dependencies, Facilities and Resources, Release Plan and Risks, plus the cover page (`Markdown Template/README.md`). |
| Acceptance Criteria: | 1. All ten pages are filled and every page passes its own "Checklist before submitting" (yes/no per item). 2. Every objective has at least one numeric success criterion; O1 Search time is stated relative to manual search of the official text and names D10 as the deliverable that holds its result. 3. Every milestone in [Milestones](02-milestones.md) has at least one associated deliverable on this page under the same number and name. 4. Scrum roles, including the Product Owner for Sprint 1, are named in [Project Organization](08-project-organization.md). |
| Due Date: | 27/10/2026 |
| Stakeholders: | Project Review Committee (course instructor and teaching assistant); project team |
| Approving Stakeholder(s): | Product Owner |

| Project Deliverable #: | D3: Source Inventory and Manifest v1 |
|---|---|
| Description: | `data/manifest.csv` and the list of provisions in the knowledge base. Primary source: consolidated text of Regulation (EU) 2024/1689 on EUR-Lex (CELEX 02024R1689-20260727). For each document: source URL, CELEX number, version date, reuse basis, file hash. The provision list is drawn from the scope in the Executive Summary and is mapped to the D2 questions when D2 is complete (11/11/2026). |
| Acceptance Criteria: | 1. Every document has all five manifest fields filled (URL, CELEX, version date, reuse basis, SHA-256 hash). 2. The reuse basis cites Commission Decision 2011/833/EU and notes that only the Official Journal text is legally binding. 3. 100% of gold sources in D2 appear in the provision list; checked when D2 is complete (11/11/2026), and any missing provision is added to the list then. 4. Every provision in the list is needed by at least one D2 question, or has a one-line reason for inclusion; checked when D2 is complete (11/11/2026). 5. The list marks each provision as core, supporting, boundary or if-time, as in the Executive Summary. 6. The hash in the manifest matches the stored file (yes/no). |
| Due Date: | 27/10/2026 |
| Stakeholders: | Project team; Project Review Committee |
| Approving Stakeholder(s): | Product Owner |

| Project Deliverable #: | D4: System Design v1 |
|---|---|
| Description: | System Architecture Design Document v1, written in the course template (`Markdown Template/11-system-architecture-design-document.md`), with the first architecture diagram, plus the ADRs and spike notes behind it (`docs/adr/`, `docs/spikes/`). |
| Acceptance Criteria: | 1. The design document fills every section of the course template (summary, goals and non-goals, diagram, components, design details, decisions, open design areas, change log) and contains the architecture diagram. 2. The diagram shows every component: ingestion, chunking, embedding, vector store, retriever, LLM, input and output checks, user interface. 3. Each component names its chosen technology, or is marked "open" and links to a spike note. 4. Every technology marked as chosen has an ADR; every open choice links to a spike note. 5. The chosen LLM is open-source and runs on CPU on a team member's computer, without a paid cloud instance (yes/no). 6. Spike notes exist for at least source parsing/chunking and running an open-source quantized LLM within the course resources. 7. Each team member has written one learning spike note in `docs/spikes/` on a topic from the course's Sprint 1 fundamentals. |
| Due Date: | 27/10/2026 |
| Stakeholders: | Project team (Data Scientists); Project Review Committee |
| Approving Stakeholder(s): | Product Owner |

### Sprint 2 · Alpha

| Project Deliverable #: | D2: Q&A Generation-Dataset v1 |
|---|---|
| Description: | `docs/eval/eval-set-v1.csv`: questions that a technical team building an education AI system would ask. Columns: question ID, question, question type, Annex III 3 use case, context (for a follow-up question: the ID of the question it follows), gold answer (the expected answer or its key conditions), gold source (Article/Annex and paragraph or point), expected behaviour (answer / abstain / refuse / redirect), origin (team-written, taken or adapted from related work), split (val / test). Used to test that in-scope questions can be answered from the provisions listed in D3, to show any gap, and to evaluate every release. Delivered with the evaluation rubric (`docs/eval/rubric.md`), which defines when an answer is fully supported by its cited passages and what counts as each expected behaviour, and with its data card (`Markdown Template/11-datasheets/03-qa-data-report.md`), written following Gebru et al. [2]. |
| Acceptance Criteria: | 1. The dataset contains 20–30 questions. 2. Each of the four Annex III point 3 use cases, (a) admission, (b) learning-outcome assessment, (c) level placement, (d) exam monitoring, has at least 3 questions. 3. Each question type has at least 2 questions: direct lookup, condition/exception, multi-provision (needs two or more provisions), follow-up, boundary case (e.g. Article 5(1)(f), Article 50(1)). Follow-up questions stay in the set; they count towards the O2 and O4 results only if Feature 7 is built, and otherwise their results are reported separately. 4. Safety questions (objective O4): at least 2 out-of-scope, 2 insufficient-evidence and 2 legal-decision questions, and at least 5 inappropriate or adversarial inputs (e.g. circumvention, concealment, prompt injection, requests that contain synthetic personal-data placeholders instead of real personal data); at least 11 in total. 5. Every in-scope question has a gold answer and at least one gold source; every other question has an expected behaviour. 6. Every question records its origin; if an LLM helped write questions, the model and prompt are recorded. 7. Every question is checked by a team member other than its author; 0 questions remain flagged as unresolved. 8. At least one third of the questions are marked `test` and are not used while tuning prompts, retrieval or rules. 9. 0 questions contain personal data. 10. Every question has a unique ID; every follow-up question names the ID of the question it follows, and both are in the same split. 11. The `test` split holds at least 1 question of each safety category. 12. The rubric defines "fully supported" and each expected behaviour, with at least one example for each (yes/no). 13. At least 5 questions are taken or adapted from published work on the EU AI Act (for example the AI Act Evaluation Benchmark), each with its source and attribution in the origin column; each adapted question is checked against the official text like any other question. 14. The data card fills every section of the course's Q&A data report template, following Gebru et al. [2]: it states how the questions were written, how their source provisions were chosen from the D3 provision list, and names the exact model for every question an LLM helped write (yes/no). |
| Due Date: | 11/11/2026 |
| Stakeholders: | Project team (Data Scientists); Project Review Committee |
| Approving Stakeholder(s): | Product Owner |

| Project Deliverable #: | D5: Preprocessing Report v1 |
|---|---|
| Description: | `docs/eval/preprocessing.md`: how the regulation text is turned into chunks (parsing, chunking by Article/paragraph, metadata), with counts. |
| Acceptance Criteria: | 1. 100% of provisions in the D3 list are present in the index. 2. 0 chunks lack a structural identifier: Article or Annex number, plus paragraph or point where the text has one. 3. Every chunk carries the version date of the source. 4. The source file hash matches D3 (yes/no). 5. Chunking parameters are in `config/rag.yaml`, not in the report text. 6. The report gives the share of chunks corrected by hand; assumption A-05 holds if it is at most 5%. A random sample of 20 chunks is compared word for word with the source text, and the number of discrepancies is recorded. |
| Due Date: | 14/11/2026 |
| Stakeholders: | Project team; Project Review Committee |
| Approving Stakeholder(s): | Product Owner |

| Project Deliverable #: | D6: Alpha Release |
|---|---|
| Description: | Baseline (Alpha 0.1): the most basic vector database and retriever over the in-scope provisions, with a generator only where it is needed to phrase the answer; every answer shows the retrieved provisions with their Article/Annex reference and the version date. Delivered with `README.md`, a pinned `requirements.txt`, the parameters in `config/rag.yaml`, the prompts in `prompts/`, the first Software Bill of Materials (`10-software-bill-of-materials.md`), a mockup of the user interface and the baseline experiment card (`Markdown Template/12-experiment-cards/E1-baseline.md`) comparing answers without and with retrieval |
| Acceptance Criteria: | 1. A team member who did not build it can install and run it from `README.md` (yes/no). 2. The baseline returns the top-5 retrieved provisions and an answer for 100% of the D2 `val` questions without runtime errors. 3. Every answer shows the Article/Annex reference of each provision it uses and the source-version date. 4. 100% of citations match the IDs of the retrieved chunks. 5. Recall@5 and the no-RAG vs RAG comparison on the `val` split are logged in Weights & Biases, recorded in the baseline experiment card and summarised in the Sprint 2 technical summary (`05-sprint-2/01-review-committee-technical-summary.md`), with the chosen metrics, why they were chosen and the target from this charter. 6. A mockup of the user interface shows the question box, the answer with citations and the version date, and the permanent "not legal advice" notice (yes/no). 7. At least one end-to-end example is shown for each of the four Annex III point 3 use cases. 8. Known failures on the `val` split are listed in the Sprint 2 technical summary. 9. The SBOM (`10-software-bill-of-materials.md`) lists every model tried, with its exact version, provider, licence, link to its source model card, accesser and access date, method of interaction and experiment card; the baseline experiment card records the corpus version from `data/manifest.csv`, the prompt templates and the `config/rag.yaml` version; `requirements.txt` has 0 unpinned packages |
| Due Date: | 14/11/2026 |
| Stakeholders: | AI customer: course instructors and peer groups, acting as academic proxies for the legal and compliance team of an EdTech provider; AI users: developers and ML engineers at EdTech providers, represented by our proxy users; project team |
| Approving Stakeholder(s): | Product Owner |

| Project Deliverable #: | D7: Project Charter v2 |
|---|---|
| Description: | Final version of the Project Canvas, updated after the Sprint 1 review and the baseline results. |
| Acceptance Criteria: | 1. A response table lists every Sprint 1 review comment as accepted (with the change) or not accepted (with a reason). 2. The final provision list from D3 is reflected in the Scope Definition of the Executive Summary. 3. The O1 and O3 target levels are reviewed once using the baseline results (planned review); any change is recorded with its reason. 4. The Project Review Committee's feedback on the O2 and O4 levels is recorded (assumption A-06); these levels change only if the Project Review Committee asks for it, and the change is recorded. A level for the difference between answers with and without retrieval is either set from the baseline results, with its reason, or left as a reported analysis result. 5. Risks lists at least one entry for each problem met in Sprint 2. 6. Each changed page states what is new compared with v1. |
| Due Date: | 14/11/2026 |
| Stakeholders: | Project Review Committee; project team |
| Approving Stakeholder(s): | Product Owner |

### Sprint 3 · Beta

| Project Deliverable #: | D8: Q&A Generation-Dataset v2 |
|---|---|
| Description: | `docs/eval/eval-set-v2.csv`: D2 extended with questions derived from the errors found in the baseline |
| Acceptance Criteria: | 1. At least 40 questions in total, including at least 5 new questions derived from the baseline evaluation findings. 2. The four education use cases and required question categories remain represented, including the questions taken or adapted from published work; each split holds at least 3 application-date questions (O2 (d)); the `val` split and the `test` split each hold at least 2 questions in each safety category (out-of-scope, insufficient-evidence, legal-decision, adversarial), at least 16 safety questions in total (objective O4). Every follow-up question names the question it follows, and both are in the same split. 3. Every retained in-scope question has a gold answer and gold source, and every other question has an expected behaviour. 4. Held-out `test` questions remain unchanged; if a correction is necessary, the affected item is identified and excluded from claims of untouched held-out evaluation. New `test` questions are fixed in the repository by 05/12/2026 and are not used while tuning prompts, retrieval or rules; the `val` split is frozen on 01/12/2026. 5. The `val`/`test` split remains identifiable. 6. A change log in the data card (`11-datasheets/03-qa-data-report.md`) lists every added, edited or excluded question and why; `eval-set-v1.csv` is kept unchanged |
| Due Date: | 05/12/2026 |
| Stakeholders: | Project team (Data Scientists); Project Review Committee |
| Approving Stakeholder(s): | Product Owner |

| Project Deliverable #: | D9: Beta Release |
|---|---|
| Description: | The whole pipeline, user interface included, running as one pipeline from `README.md` on a team computer: retrieval with citations and the version date, plain-language answers in the summary-then-conditions format, boundary notices and refusals, the rule-based input and output checks, and the personal-data reminder (Features 1–4). The baseline's known failures are fixed where possible, every experiment is tracked, and implemented and deferred features are documented |
| Acceptance Criteria: | 1. A team member who did not build it can install and run the whole pipeline, user interface included, from `README.md`, and a screenshot of the interface answering a question is in the sprint folder (yes/no). 2. On the frozen D8 `val` split, the four O2 Evidence results are reported separately against the target levels in the Executive Summary; any unmet level is recorded as a known limitation or a fix for Sprint 4, and final acceptance is decided on the held-out `test` split in D11: (a) the expected provision is cited for at least 80% of in-scope questions; (b) at least 75% of in-scope answers are fully supported by the cited passages (one reviewer reviews every in-scope `val` answer, and a second reviewer checks a sample); (c) 100% of substantive answers cite an Article/Annex with the version date; (d) at most one application-date question gets a date that is not from the designated source version. 3. The O4 Safety result is reported for each of the four categories (out-of-scope, insufficient-evidence, legal-decision, adversarial) as correct responses / questions evaluated and as a percentage, against the target levels (100% of the legal-decision questions and at least 80% of the questions in each of the other three categories); any unmet level is recorded as in criterion 2. 4. 0 answers on the `val` split contain a classification or compliance verdict (e.g. "your system is compliant"). 5. Features 1–4 are each marked implemented or deferred, with a reason for deferral and the Product Owner's agreement; the tests of every story built so far are reported as pass or fail in the Sprint 3 technical summary. 6. Every experiment has an experiment card and its runs are tracked in Weights & Biases; the best configuration is re-run with at least 3 seeds, reported as mean ± std and compared with the baseline on the same questions. 7. The median answer time on the computer used for the pilot is measured on the `val` questions and recorded against the answer-time limit in D4 (A-07). 8. Privacy check (C-10): a marked test question sent to the system used for the pilot is not found in the application or error logs or the vector index, and it is no longer in the database after the session ends (yes/no) |
| Due Date: | 05/12/2026 |
| Stakeholders: | AI customer: course instructors and peer groups, acting as academic proxies for the legal and compliance team of an EdTech provider; Project Review Committee; project team |
| Approving Stakeholder(s): | Product Owner |

### Sprint 4 · Release candidate

| Project Deliverable #: | D10: Pilot Evaluation Report |
|---|---|
| Description: | `docs/eval/pilot.md`: timed tasks, held in person on a team computer between 16/12 and 23/12/2026, in which the same pilot users find provisions both by searching the official text manually and with the assistant, plus a survey. Holds the results of O1 Search time and O3 Understanding |
| Acceptance Criteria: | 1. At least 5 pilot users (technical professionals acting as EdTech developers) take part. 2. Each user does at least 4 timed tasks from the `val` split, an equal number with manual EUR-Lex search and with the assistant; tasks are balanced across the four education use cases over all participants; the task sets and the method order are counterbalanced between participants, as evenly as the number of users allows (for example 3 and 2 with 5 users). 3. The report gives the median time and the share of tasks with the correct provision found for each condition, and states whether the O1 target from the Executive Summary is met (median time at least 20% shorter with the assistant, and the correct provision found in at least as many tasks as with manual search). 4. The survey reports the share of users rating answers at least 4 out of 5 for understandability and whether the O3 target (at least 70%, i.e. at least 4 of 5 users when there are 5) is met, the share who would use the assistant as their first step, and the share who correctly answer that the assistant gives no legal decisions (business outcomes of O3 and O4); the task log records, for each task done with the assistant, whether the user opened or searched for another provision before giving an answer (business outcome of O2; an observation of behaviour, not a check of legal correctness). 5. Raw results are stored without participant names (P1, P2, …). |
| Due Date: | 30/12/2026 |
| Stakeholders: | AI users: pilot proxy users; AI customer: course instructors and peer groups, acting as academic proxies for the legal and compliance team of an EdTech provider; Project Review Committee; project team |
| Approving Stakeholder(s): | Product Owner; Project Review Committee |

| Project Deliverable #: | D11: Release Candidate and Final Evaluation |
|---|---|
| Description: | Final version of the assistant: the beta plus Check the source (Feature 6) and the application-date answers, with the problems found in the pilot fixed (errors only, no new features); an updated SBOM (`10-software-bill-of-materials.md`); and the final results on the held-out `test` split in the Sprint 4 technical summary and its experiment cards |
| Acceptance Criteria: | 1. On the held-out `test` split, the four O2 Evidence results (a)–(d) are reported separately and each meets its level as confirmed in D7 (at least 80% for (a), at least 75% for (b), 100% for (c), and at most one application-date question with a date not from the designated source version for (d)); for (b), one reviewer reviews every in-scope `test` answer, and a second reviewer checks a sample. 2. The O4 Safety result is reported for each of the four categories (out-of-scope, insufficient-evidence, legal-decision, adversarial) as correct responses / questions evaluated and as a percentage, and meets the level confirmed in D7 (100% of the `test` legal-decision questions and at least 80% of the `test` questions in each of the other three categories get the expected response). 3. 0 answers on the `test` split contain a classification or compliance verdict. 4. Every reported number links to its Weights & Biases run. 5. The SBOM matches the release commit (yes/no). 6. The final demo on 30/12/2026 runs end to end from `README.md` on a team computer (yes/no). 7. Known limitations of the release are listed in `README.md`. 8. The tests of every user story are run and reported in the Sprint 4 technical summary, together with the final system compared with the baseline and the charter's success criteria; the data cards, SBOM, design document and `README.md` describe the system shown in the demo (yes/no). |
| Due Date: | 30/12/2026 |
| Stakeholders: | AI customer: course instructors and peer groups, acting as academic proxies for the legal and compliance team of an EdTech provider; AI users: developers and ML engineers at EdTech providers; Project Review Committee |
| Approving Stakeholder(s): | Product Owner; Project Review Committee |

## Example (illustrative only)

The project, names, numbers and dates are invented. They match the examples in [Milestones](03-project-canvas_v2/02-milestones.md) and [Release Plan](03-project-canvas_v2/10-release-plan.md). The project is a RAG assistant that answers students' questions about a university's course regulations.

| Project Deliverable #: | D1: Project Charter v1 |
|---|---|
| Description: | First version of the Project Canvas pages |
| Acceptance Criteria: | 1. All cells marked with * are filled. 2. Every objective has at least one numeric success criterion. 3. Every milestone in [Milestones](03-project-canvas_v2/02-milestones.md) has an associated deliverable on this page. |
| Due Date: | 28/10/2026 |
| Stakeholders: | Project Review Committee; project team |
| Approving Stakeholder(s): | Product Owner |

| Project Deliverable #: | D2: Q&A Generation-Dataset v1 |
|---|---|
| Description: | Question–answer pairs generated from the regulations corpus, used to evaluate retrieval and answers. Stored as a file in the Git repository. |
| Acceptance Criteria: | 1. At least 200 pairs. 2. Every regulation chapter has at least 10 questions. 3. At least 20% of questions need two or more passages to answer. 4. A sample of 40 pairs is checked by hand, with at least 90% judged correct. 5. The generator model and prompt are recorded. |
| Due Date: | 18/11/2026 |
| Stakeholders: | Project team (AI developer role) |
| Approving Stakeholder(s): | Product Owner |

| Project Deliverable #: | D6: Beta release |
|---|---|
| Description: | Assistant deployed for five pilot students, with a feedback button |
| Acceptance Criteria: | 1. All five pilot users can log in and receive an answer. 2. Recall@5 ≥ 0.70 and p95 latency ≤ 3 s on the D2 test questions. 3. Every answer shows at least one source link. |
| Due Date: | 09/12/2026 |
| Stakeholders: | AI customer: student affairs office; AI users: pilot students |
| Approving Stakeholder(s): | Product Owner; student affairs contact |

## Checklist before submitting

- [x] Both solution and project-management deliverables are listed (Rule 1)
- [x] Each charter version is a separate deliverable (Rule 2)
- [x] Every block has all six fields filled (Rule 3)
- [x] Every acceptance criterion is measurable (Rule 4)
- [x] No acceptance criterion relies on an adjective without a number (Rule 5)
- [x] Customer-facing deliverables list the customer or users as Stakeholders, not only the team (Rule 6)
- [x] Every block names an Approving Stakeholder (Rule 7)
- [x] Every due date is aligned with its milestone in [Milestones](03-project-canvas_v2/02-milestones.md) (Rule 8)
- [x] A Q&A Generation-Dataset deliverable exists, with diversity and representation criteria (Rule 9)
- [x] Any team-written model card is for a trained or fine-tuned model (Rule 10)
- [x] Every later-measured target in [Project Executive Summary](03-project-canvas_v2/01-project-executive-summary.md) has a deliverable that holds the result (Rule 11)
- [x] The product is delivered in more than one version across sprints (Rule 12)
- [x] The page is complete in the first version of the canvas (red cell)

## References

[1] Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT\* '19)* (pp. 220–229). Association for Computing Machinery. https://doi.org/10.1145/3287560.3287596

[2] Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12), 86–92. https://doi.org/10.1145/3458723

[3] International Organization for Standardization & International Electrotechnical Commission. (2024). *Information technology — Artificial intelligence — Guidance for AI applications* (ISO/IEC 5339:2024, 1st ed.). Prepared by ISO/IEC JTC 1/SC 42, Artificial intelligence. Edition used: British Standards Institution. (2024). *BS ISO/IEC 5339:2024* (published 31 January 2024). BSI Standards Limited. ISBN 978 0 539 15221 0.

[4] International Organization for Standardization & International Electrotechnical Commission. (2023). *Information technology — Artificial intelligence — AI system life cycle processes* (ISO/IEC 5338:2023, 1st ed.). Prepared by ISO/IEC JTC 1/SC 42, Artificial intelligence. Edition used: British Standards Institution. (2024). *BS ISO/IEC 5338:2023* (published 29 February 2024). BSI Standards Limited. ISBN 978 0 539 15220 3.
