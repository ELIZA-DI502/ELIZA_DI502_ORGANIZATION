# Major Activities

Expand on the scope definition by outlining the major activities required to complete the project. Structure these around the AI system life cycle stages of ISO/IEC 5338 [1], listed below.

Include activities such as project management, feature engineering, model training, performance evaluation and analysis.

Mark each activity as In Scope or Out of Scope to reduce ambiguity.

Add rows as required. The table should give a summary view; add narrative explanation below it where more detail is needed. Activities can be linked to Jira from this page.

## Life cycle stages
 
Give every activity one stage from this table. The stage names and the processes in each stage come from ISO/IEC 5338 [1]; the typical activities are paraphrased for this course.
 
| Stage | Typical activities | ISO/IEC 5338 processes in this stage |
|---|---|---|
| **Inception** | Define the problem, the AI customer's needs and the success criteria; set model requirements; decide whether AI is needed at all | 6.4.1 Business or mission analysis; 6.4.2 Stakeholder needs and requirements definition; 6.4.3 System requirements definition |
| **Design and development** | Architecture and design; acquire, label, explore, clean and prepare data; protect sensitive data; feature engineering; train and tune models; integrate components | 6.4.4–6.4.6; 6.4.7 Knowledge acquisition; 6.4.8 AI data engineering; 6.4.9 Implementation; 6.4.10 Integration |
| **Verification and validation** | Test the model and system before deployment; check them against the AI customer's needs | 6.4.11 Verification; 6.4.13 Validation |
| **Deployment** | Move the model and system into the environment where AI users reach it | 6.4.12 Transition |
| **Operation and monitoring** | Run the system; fix and retrain it when needed | 6.4.15 Operation; 6.4.16 Maintenance |
| **Continuous validation** | Monitor data drift, concept drift and other changing requirements after deployment; decide when to retrain | 6.4.14 Continuous validation |
| **Re-evaluation** | Review results against the original needs; feed changes back to Inception or Design and development | 6.3.8 Quality assurance; 6.4.2; 6.4.13 |
| **Retirement** | Decommission the system and its data | 6.4.17 Disposal |
 
Project management work (sprint planning, documentation, reviews, risk tracking) runs across every stage, as risk management and governance do in the standard [1]. Write **All stages** for these rows.
 
Stages group work in a rough order, but they need not happen one after another. In agile work, stages can run at the same time and can repeat [1].

## In Scope and Out of Scope

| Status | What it means | Question it answers |
|---|---|---|
| **In Scope** | Work the team will do | What will we build or carry out? |
| **Out of Scope** | Work the team will not do at all | What are we deliberately not building? |

An out-of-scope activity is not the same as a constraint. A constraint is a rule that limits how the in-scope work is done; it goes in [Assumptions & Constraints](03-assumptions-and-constraints.md). If you want to show that the project's scope is narrow (for example, you plan no information-elicitation phase), list that here as Out of Scope. Limits on the system's inputs, such as a user-input boundary or English-only text, are constraints.

## Activities that come from a constraint

Many constraints create work and remove work at the same time. Write the decision as three statements, one per place, each pointing to the others:

| Where | What it says | Example wording |
|---|---|---|
| Constraint ([Assumptions & Constraints](03-assumptions-and-constraints.md)) | The rule the system must obey | "The system shall not persist personally identifiable information (e.g., names, email addresses, national ID numbers) in any database, log, or vector index." |
| In Scope (this page) | The work you do because of the constraint | "Implement PII detection and masking on user inputs before logging." "Configure logs to retain only anonymised interaction data." |
| Out of Scope (this page) | The features you give up because of it | "User accounts, personal profiles, and saved conversation history linked to an identity." |

**Do not skip the In Scope row.** Users will type names, emails or account numbers into a chatbot whether you invite them to or not. A rule such as "no PII stored" is not true just because you did not build a profile feature; enforcing it takes work. That work belongs here, in the backlog and in the estimates. Count its effort in [Cost & Funding](07-cost-and-funding.md).

The uncertain part becomes a risk in [Risks](11-risks.md), and the in-scope activity is its mitigation. For the example above, the risk is "Users submit PII in free-text queries, and it ends up in logs or the retrieval index".

## Knock-on effect on user stories

Once a constraint is in the charter, a user story that contradicts it is an external inconsistency between documents. For example, "As a returning analyst, I want to see my previous questions" contradicts a no-PII rule. Either drop such a story, or rewrite it so the history lives only in the session and is not stored.

## Rules

1. Every activity has exactly one stage from the life cycle table above, spelled as there, or **All stages** for project management work.
2. Every activity is marked In Scope or Out of Scope.
3. Every Out of Scope row says why in its Description, as row 2 below does.
4. Every constraint in [Assumptions & Constraints](03-assumptions-and-constraints.md) that creates work has at least one In Scope row here, and every constraint that removes features has at least one Out of Scope row here.
5. Rows created by a constraint name the constraint ID in their Description (for example "Because of C-03").
6. User authentication and PII storage, if you do not plan them, are listed as Out of Scope.
7. Activities do not increase the scope of the project beyond the first proposal.

## What doesn't belong here

- **Rules the system must obey** go in [Assumptions & Constraints](03-assumptions-and-constraints.md) as constraints.
- **What could go wrong** with an activity goes in [Risks](11-risks.md).
- **The order in which activities must happen**, when one blocks another, goes in [Dependencies](06-dependencies.md).
- **Effort in person-hours** goes in [Cost & Funding](07-cost-and-funding.md).

## Activities
 
The activities below expand the Scope Definition in the [Project Executive Summary](01-project-executive-summary.md) and are grouped by ISO/IEC 5338 life cycle stage. Rows created by a constraint name its ID from [Assumptions & Constraints](03-assumptions-and-constraints.md); rows that mitigate a risk name its ID from [Risks](11-risks.md); deliverable numbers refer to [Deliverables](05-deliverables.md). The Jira column gives the user stories that deliver the activity (each story holds its sub-tasks), or the epic for Sprint 1 project work (KAN-27 Project charter and sprint reporting, KAN-29 Source corpus, KAN-30 System design and delivery).

| # | Stage | Activity | Description | Status | Jira Task |
|---|---|---|---|---|---|
| 1 | Inception | Define the problem, users, objectives and success criteria | Completed in the Project Charter (Executive Summary, D1): technical teams at EdTech providers as AI users, objectives O1–O4 with success criteria. | In Scope | KAN-27 |
| 2 | Inception | Market or competitive analysis of existing legal-information tools | Not needed for an academic proof of concept; the comparison that matters is manual search of the official text, which O1 measures in the pilot. | Out of Scope | |
| 3 | Inception | Build the evaluation question set and rubric | Q&A Generation-Dataset v1 with 20–30 questions over the four Annex III point 3 use cases, safety questions, at least 5 questions taken or adapted from published work on the EU AI Act, `val`/`test` split, cross-check by a second member, the evaluation rubric and the data card written following Gebru et al. (D2). Validates A-03; mitigation for R-11. | In Scope | KAN-65, KAN-83 |
| 4 | Inception | Select the in-scope provisions and record the source manifest | Because of C-01 and C-09. Provision list (core, supporting, boundary, if-time) mapped to the D2 questions; manifest with URL, CELEX, version date, reuse basis under Commission Decision 2011/833/EU and file hash (D3). By 18/11/2026: the in-scope provisions affected by amendments are identified from the consolidation markers and the listed amending acts, and these together with Annex III point 3, Article 6 and Article 113 are compared word for word with the Official Journal texts; the identifiers and completeness of the remaining in-scope provisions are checked against the original Official Journal text; discrepancies are recorded. Validates A-01; mitigation for R-01. | In Scope | KAN-29 |
| 5 | Design and development | Architecture design and decision records | System Architecture Design Document v1 in the course template, with the first architecture diagram showing every component, ADRs for chosen technologies, spike notes for open choices, and one learning spike note per team member (D4). | In Scope | KAN-30 |
| 6 | Design and development | Model selection spike | Because of C-03, C-05 and C-07. Feasibility check, not a benchmark: run at least two open-source quantized models on CPU only (Colab CPU runtime or a team member's computer) on the same sample questions and record the answer time, and read each candidate's licence; throw-away notebook, no production code, no retrieval integration; result in a spike note and an ADR (D4). Validates A-07 and A-10; mitigation for R-13. | In Scope | KAN-57 |
| 7 | Design and development | Source parsing spike | Because of C-07. Check that the EUR-Lex HTML marks Articles, paragraphs and Annex points so that they can be extracted with their identifiers; spike note, no production code (D4). Validates A-05; mitigation for R-12. | In Scope | KAN-30 |
| 8 | Design and development | Parse and chunk the regulation text | Because of C-01. Extract the in-scope provisions from the stored source file, one chunk per Article paragraph or Annex point, each with its identifier and the version date; report the share of chunks corrected by hand (D5). | In Scope | KAN-86 |
| 9 | Design and development | Retrieval pipeline | Because of C-03. Embedding, vector store and retriever over the chunks of row 8; chunking and retrieval parameters in `config/rag.yaml`; the baseline answers show the retrieved provisions with their Article/Annex reference and the version date (D6). | In Scope | KAN-87, KAN-8 |
| 10 | Design and development | Answer generation with citations and version date | Because of C-03, C-08 and C-09. Open-source quantized model used as-is with fixed prompt templates; plain-language answer based only on retrieved provisions; Article/Annex reference and source version date shown with every answer; citation-ID check against the retrieved chunks; note that only the Official Journal text is authentic (citations in D6; plain-language answers in D9; application-date answers in D11). | In Scope | KAN-8, KAN-4, KAN-19, KAN-3 |
| 11 | Design and development | Out-of-scope and legal-decision notices | Because of C-04 and C-08. Notices for out-of-scope questions, missing evidence and requests for a legal decision; the out-of-scope notice names what the assistant covers (C-04); refusal of evasion, concealment and prohibited-practice requests with a one-sentence reason (Feature 4, D9). | In Scope | KAN-2, KAN-5, KAN-23, KAN-24 |
| 12 | Design and development | Input and output safety checks | Because of C-08 and C-10. Rule-based checks before the model call (prompt-injection and evasion patterns) and after it (decision phrases and compliance verdicts), with a fixed system prompt (D9). | In Scope | KAN-24, KAN-2 |
| 13 | Design and development | Personal-data reminder and input check | Because of C-10. A reminder on the page not to enter personal data, and a rule-based input check for e-mail addresses and phone numbers; this is not comprehensive personal-data detection. Independently of that check, application and error logs are configured not to record user questions or conversation content, the vector index holds only the source text, and the conversation of a session is deleted from the session database when the session ends; these controls are the actual privacy safeguard. They are verified by sending a marked test question to the system used for the pilot, searching the logs and the vector index for it, and checking that it is no longer in the database after the session ends (D9). | In Scope | KAN-26 |
| 14 | Design and development | One-page web interface | Because of C-08. Question box, answer view with citations and a permanent "not legal advice" notice; a mockup in D6, the working page calling the whole pipeline in D9 (Features 1–4). | In Scope | KAN-21, KAN-25, KAN-168 |
| 15 | Design and development | Check the source, and the features built only if time allows | Check the source: the wording of each cited provision under the answer, with a link to EUR-Lex (Feature 6, D11). Guided start (Feature 5) and follow-up questions within one session (Feature 7) are not committed and stay in the backlog; if follow-up questions are built, the session context is discarded when the session ends, because of C-04 and C-10. | In Scope | KAN-22 (KAN-20, KAN-6 in the backlog) |
| 16 | Design and development | Software Bill of Materials and pinned dependencies | `10-software-bill-of-materials.md` with every model tried: exact version, provider, licence (A-10), source model card, accesser and access date, method of interaction and experiment card; the model file is stored with its version and hash; the corpus version, prompt templates and `config/rag.yaml` version are recorded in the experiment cards; `requirements.txt` fully pinned (D6, updated every sprint and in D11). Mitigation for R-07. | In Scope | KAN-88, KAN-203 |
| 17 | Design and development | Model training or fine-tuning | Because of C-03 and C-05: models are used as-is; no GPU is available and no team-written model card is needed. | Out of Scope | |
| 18 | Design and development | Knowledge outside the designated source | Because of C-01: GDPR, national law, other EU acts and Commission guidelines are not added to the knowledge base (single source). | Out of Scope | |
| 19 | Design and development | Answers in Turkish or other languages | Because of C-02: questions and the source text are English only. | Out of Scope | |
| 20 | Design and development | Topics outside the education use cases | Because of C-04: non-education domains, deployer obligations, GPAI model provider obligations, enforcement and penalties receive an out-of-scope notice (row 11) and are not answered. | Out of Scope | |
| 21 | Design and development | User accounts, authentication, personal profiles and saved conversation history | Because of C-04 and C-10: these would require storing personal data and history across sessions. | Out of Scope | |
| 22 | Design and development | Legal advice, compliance decisions and implementation guidance | Because of C-08: the assistant identifies and explains provisions only; it gives no high-risk classification, compliance verdict or guidance on how to implement the requirements. | Out of Scope | |
| 23 | Verification and validation | Evaluation runs on the `val` split | Baseline (alpha): Recall@5 and the comparison without and with retrieval required by D6 criterion 5 (an analysis result, not a pass level). Beta: O2 (a)–(d) and O4 per safety category on the frozen `val` split, reported against the target levels as required by D9 criteria 2–4 (O4 also as correct responses / questions evaluated). Logged in Weights & Biases, the experiment cards and the sprint's technical summary. The release candidate is scored on the `test` split instead (row 27). | In Scope | KAN-87, KAN-169 |
| 24 | Verification and validation | Answer review against the rubric | One reviewer reviews every in-scope answer against the rubric for O2 (b), and a second reviewer checks a sample; disagreements are resolved against the rubric, then by a third member, and logged (D9, D11). | In Scope | KAN-169, KAN-77 |
| 25 | Verification and validation | Extend the question set | Q&A Generation-Dataset v2: at least 40 questions, including new questions from the baseline errors, and at least 16 safety questions. The held-out `test` split is preserved: the original `test` questions stay unchanged, and new `test` questions are fixed by 05/12/2026 and never used for prompt, retrieval or rule tuning. The `val` split is frozen on 01/12/2026 so that the beta can be scored on it by 05/12/2026 (internal date, [Release Plan](10-release-plan.md)) (D8). | In Scope | KAN-170 |
| 26 | Verification and validation | Pilot: timed search task and survey | At least 5 proxy users (named by 18/11/2026) do timed tasks manually and with the assistant, in person on a team computer between 16/12 and 23/12/2026, with tasks balanced across the four use cases over all participants and with task sets and method order counterbalanced, then a survey; results without names (D10). Validates A-04 and A-08; mitigation for R-03 and R-09. | In Scope | KAN-202, KAN-72 |
| 27 | Verification and validation | Final evaluation on the held-out test split | O2 (a)–(d) and O4 per category on the `test` split of the release candidate, with links to the Weights & Biases runs (D11). | In Scope | KAN-77, KAN-75 |
| 28 | Deployment | Run the system locally from `README.md` | Because of C-05. The baseline (D6), the beta (D9) and the release candidate (D11) run on a team computer, installed only from `README.md`; each sprint, a team member who did not build the system installs and runs it from the README. No hosted deployment is needed (row 31). | In Scope | KAN-87, KAN-168, KAN-203 |
| 29 | Deployment | Prepare the pilot and demo computer | Because of C-05. The team computer used for the pilot and the final demo is set up from `README.md`; the answer time on it is measured on the `val` questions and recorded against the answer-time limit in the design document by 09/12/2026, before the pilot (D9, D10). Mitigation for R-10 and R-13. | In Scope | KAN-163, KAN-206 |
| 30 | Operation and monitoring | Run the pilot version unchanged and log problems | Keep the version used in the pilot unchanged 16/12–23/12/2026 so that all pilot users evaluate the same version; log problems as they occur, without user questions (C-10); fix them in the release candidate: errors only, no new features (D11). | In Scope | KAN-209, KAN-210 |
| 31 | Deployment | Hosted cloud deployment and cost tracking | Because of C-05 and C-06: the course does not require a hosted deployment, and the pilot and the final demo run on a team computer (rows 28, 29), so no cloud instance, billing alerts or cost tracking are planned. The course's Google Cloud credit is kept as a reserve (A-07). | Out of Scope | |
| 32 | Continuous validation | Check for a newer consolidated version | At the start of each sprint from Sprint 2, check EUR-Lex for an amendment to the in-scope provisions; a change of the designated version needs Product Owner approval and an ADR. Validates A-02; mitigation for R-02. | In Scope | KAN-157, KAN-187, KAN-213 |
| 33 | Continuous validation | Monitoring and retraining after 30/12/2026 | The project ends on 30/12/2026 and no model is trained; the maintenance trigger (a new consolidated version) is documented in R-02 for anyone who continues the work. | Out of Scope | |
| 34 | Re-evaluation | Charter update | Project Charter v2: answers to the Sprint 1 review comments, O1/O3 target review and the Committee's feedback on the O2/O4 levels (D7). From Sprint 3 on, feature status and objective results are reported in each sprint's technical summary, not in a new charter version. Mitigation for R-04. | In Scope | KAN-89 |
| 35 | Re-evaluation | Separate final report and lessons-learned register | Not required by the course: the final results are reported in the Sprint 4 technical summary (D11) and the lessons in each sprint's retrospective (row 37). | Out of Scope | |
| 36 | Retirement | Keep the final version reproducible | After the final demo, the code, configuration, `README.md`, the submitted Git commit and the anonymised evaluation results stay in the project repository; nothing keeps running after 30/12/2026, so there are no resources to shut down. | In Scope | KAN-212 |
| 37 | All stages | Scrum events and sprint reports | Sprint planning, daily check-ins, reviews and retrospectives; Definition of Ready and Done agreed before each sprint; Jira board, burndown chart and impediment list; at each upload, the sprint folder's welcome page (sprint goal, results, links, submitted Git commit) and the Jira backlog export (`docs/backlog/`). Mitigation for R-06 and R-08. | In Scope | KAN-44, KAN-91, KAN-171, KAN-204 |
| 38 | All stages | Risk and assumption tracking | Review the risk register and the assumption checks at each sprint start; update triggers and owners in [Risks](11-risks.md). Mitigation for R-06. | In Scope | KAN-14 |
| 39 | All stages | Production code in Sprint 1 | Because of C-07: Sprint 1 produces documents, the source manifest and spike notes only (rows 4–7). | Out of Scope | |
| 40 | Verification and validation | Test cases for the user stories | For each user story, a test of its acceptance criteria (input or steps, and the expected result), written next to the story in its story requirements page in Sprint 2; the tests of every story built so far are run and reported as pass or fail in the technical summary in Sprints 3 and 4. | In Scope | KAN-90, KAN-214 |

### Constraint coverage

| Constraint | In Scope rows | Out of Scope rows |
|---|---|---|
| C-01 Single source | 4, 8 | 18 |
| C-02 English only | — (no work created) | 19 |
| C-03 RAG with open-source quantized model | 6, 9, 10 | 17 |
| C-04 Education use cases; follow-ups within one session | 11, 15 | 20, 21 |
| C-05 No GPU; the system runs on a team computer | 6, 28, 29 | 17, 31 |
| C-06 $100 Google Cloud credit (kept as a reserve) | — (no work created) | 31 |
| C-07 Team, duration, no production code in Sprint 1 | 6, 7 | 39 |
| C-08 Information, not legal advice | 10, 11, 12, 14 | 22 |
| C-09 Reuse with source acknowledgement | 4, 10 | — |
| C-10 No personal data requested; conversation deleted when the session ends | 12, 13, 15, 30 | 21 |

## Example (illustrative only)
 
An excerpt from a longer table for a legal research assistant (a RAG chatbot over legal documents). It shows the rows created by constraints C-03 and C-04 in the example on `03-assumptions-and-constraints.md`.
 
| # | Stage | Activity | Description | Status | Jira Task |
|---|---|---|---|---|---|
| 7 | Design and development | Mask PII in user inputs before logging | Because of C-03. Detect names, emails and ID numbers in queries and mask them before any log write. Mitigation for R-03. | In Scope | (link) |
| 8 | Deployment | Configure logs to keep only anonymized interaction data | Because of C-03. | In Scope | (link) |
| 12 | Design and development | User accounts, personal profiles and saved conversation history | Because of C-03: these would require storing PII. | Out of Scope | |
| 13 | Design and development | Multi-turn dialogue memory | Because of C-04: the system handles single-turn questions only. | Out of Scope | |

## Checklist before submitting

- [x] Every activity has one ISO/IEC 5338 life cycle stage, or All stages (rule 1)
- [x] Every activity is marked In Scope or Out of Scope (rule 2)
- [x] Every Out of Scope row says why (rule 3)
- [x] Every work-creating constraint in [Assumptions & Constraints](03-assumptions-and-constraints.md) has an In Scope row, and every feature-removing constraint has an Out of Scope row (rule 4)
- [x] Rows created by a constraint name its ID (rule 5)
- [x] User authentication and PII storage are listed as Out of Scope if you do not plan them (rule 6)
- [x] No activity goes beyond the first proposal's scope (rule 7)
