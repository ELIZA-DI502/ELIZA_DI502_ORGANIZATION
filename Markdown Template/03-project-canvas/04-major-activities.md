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

An out-of-scope activity is not the same as a constraint. A constraint is a rule that limits how the in-scope work is done; it goes in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md). If you want to show that the project's scope is narrow (for example, you plan no information-elicitation phase), list that here as Out of Scope. Limits on the system's inputs, such as a user-input boundary or English-only text, are constraints.

## Activities that come from a constraint

Many constraints create work and remove work at the same time. Write the decision as three statements, one per place, each pointing to the others:

| Where | What it says | Example wording |
|---|---|---|
| Constraint ([Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md)) | The rule the system must obey | "The system shall not persist personally identifiable information (e.g., names, email addresses, national ID numbers) in any database, log, or vector index." |
| In Scope (this page) | The work you do because of the constraint | "Implement PII detection and masking on user inputs before logging." "Configure logs to retain only anonymised interaction data." |
| Out of Scope (this page) | The features you give up because of it | "User accounts, personal profiles, and saved conversation history linked to an identity." |

**Do not skip the In Scope row.** Users will type names, emails or account numbers into a chatbot whether you invite them to or not. A rule such as "no PII stored" is not true just because you did not build a profile feature; enforcing it takes work. That work belongs here, in the backlog and in the estimates. Count its effort in [Cost & Funding](03-project-canvas_v2/07-cost-and-funding.md).

The uncertain part becomes a risk in [Risks](03-project-canvas_v2/11-risks.md), and the in-scope activity is its mitigation. For the example above, the risk is "Users submit PII in free-text queries, and it ends up in logs or the retrieval index".

## Knock-on effect on user stories

Once a constraint is in the charter, a user story that contradicts it is an external inconsistency between documents. For example, "As a returning analyst, I want to see my previous questions" contradicts a no-PII rule. Either drop such a story, or rewrite it so the history lives only in the session and is not stored.

## Rules

1. Every activity has exactly one stage from the life cycle table above, spelled as there, or **All stages** for project management work.
2. Every activity is marked In Scope or Out of Scope.
3. Every Out of Scope row says why in its Description, as row 2 below does.
4. Every constraint in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md) that creates work has at least one In Scope row here, and every constraint that removes features has at least one Out of Scope row here.
5. Rows created by a constraint name the constraint ID in their Description (for example "Because of C-03").
6. User authentication and PII storage, if you do not plan them, are listed as Out of Scope.
7. Activities do not increase the scope of the project beyond the first proposal.

## What doesn't belong here

- **Rules the system must obey** go in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md) as constraints.
- **What could go wrong** with an activity goes in [Risks](03-project-canvas_v2/11-risks.md).
- **The order in which activities must happen**, when one blocks another, goes in [Dependencies](03-project-canvas_v2/06-dependencies.md).
- **Effort in person-hours** goes in [Cost & Funding](03-project-canvas_v2/07-cost-and-funding.md).

## Activities
 
The activities below expand the Scope Definition in the [Project Executive Summary](01-project-executive-summary.md) and are grouped by ISO/IEC 5338 life cycle stage. Rows created by a constraint name its ID from [Assumptions & Constraints](03-assumptions-and-constraints.md); rows that mitigate a risk name its ID from [Risks](11-risks.md); deliverable numbers refer to [Deliverables](05-deliverables.md). The Jira column gives the epic that holds the Sprint 1 tasks (D1 KAN-27, D2 KAN-28, D3 KAN-29, D4 KAN-30) or the user stories that deliver the activity; Sprint 2–4 tasks are added to the stories at sprint planning.

| # | Stage | Activity | Description | Status | Jira Task |
|---|---|---|---|---|---|
| 1 | Inception | Define the problem, users, objectives and success criteria | Completed in the Project Charter (Executive Summary, D1): technical teams at EdTech providers as AI users, objectives O1–O4 with success criteria. | In Scope | KAN-27 |
| 2 | Inception | Market or competitive analysis of existing legal-information tools | Not needed for an academic proof of concept; the comparison that matters is manual search of the official text, which O1 measures in the pilot. | Out of Scope | |
| 3 | Inception | Build the evaluation question set and rubric | Q&A Generation-Dataset v1 with 20–30 questions over the four Annex III point 3 use cases, safety questions, at least 5 questions taken or adapted from published work on the EU AI Act (A-11), `dev`/`test` split, cross-check by a second member, and the evaluation rubric (D2). Basis of A-03; mitigation for R-03 and R-21. | In Scope | KAN-28 |
| 4 | Inception | Select the in-scope provisions and record the source manifest | Because of C-01 and C-09. Provision list (core, supporting, boundary, if-time) mapped to the D2 questions; manifest with URL, CELEX, version date, reuse basis under Commission Decision 2011/833/EU and file hash (D3). By 18/11/2026: the in-scope provisions affected by amendments are identified from the consolidation markers and the listed amending acts, and these together with Annex III point 3, Article 6 and Article 113 are compared word for word with the relevant Official Journal texts; the identifiers and completeness of the remaining in-scope provisions are checked against the original Official Journal text; discrepancies are recorded. Validates A-01; mitigation for R-01 and R-18. | In Scope | KAN-29 |
| 5 | Design and development | Architecture design and decision records | System Architecture Design Document v1 in the course template, with the first architecture diagram showing every component, ADRs for chosen technologies, spike notes for open choices, and one learning spike note per team member (D4). | In Scope | KAN-30 |
| 6 | Design and development | Model selection spike | Because of C-03, C-05 and C-07. Short feasibility check, not a benchmark: run at least two open-source quantized models on CPU only (Colab CPU runtime or a short-lived Google Cloud instance of the planned type) on a few sample questions and record the answer time, and read each candidate's licence; throw-away notebook, no production code, no retrieval integration; result in a spike note and an ADR (D4). Validates A-10; mitigation for R-10, R-14 and R-19. | In Scope | KAN-30 |
| 7 | Design and development | Source parsing spike | Because of C-07. Check that the EUR-Lex HTML marks Articles, paragraphs and Annex points so that they can be extracted with their identifiers; spike note, no production code (D4). Validates A-05; mitigation for R-05 and R-14. | In Scope | KAN-30 |
| 8 | Design and development | Parse and chunk the regulation text | Because of C-01. Extract the in-scope provisions from the stored source file, one chunk per Article paragraph or Annex point, each with its identifier and the version date; report the share of chunks corrected by hand (D5). | In Scope | — |
| 9 | Design and development | Retrieval pipeline | Because of C-03. Embedding, vector store and retriever over the chunks of row 8; chunking and retrieval parameters in `config/rag.yaml` (D6). Mitigation for R-12. | In Scope | KAN-8 |
| 10 | Design and development | Answer generation with citations and version date | Because of C-03, C-08 and C-09. Open-source quantized model used as-is with fixed prompt templates; plain-language answer based only on retrieved provisions; Article/Annex reference and source version date shown with every answer; citation-ID check against the retrieved chunks; note that only the Official Journal text is authentic (D6). Mitigation for R-20. | In Scope | KAN-4, KAN-3, KAN-19 |
| 11 | Design and development | Out-of-scope and legal-decision notices | Because of C-04 and C-08. Notices for out-of-scope questions, missing evidence and requests for a legal decision; refusal of evasion, concealment and prohibited-practice requests with a one-sentence reason (Feature 4, D6). Mitigation for R-13. | In Scope | KAN-2, KAN-5, KAN-23, KAN-24 |
| 12 | Design and development | Input and output safety checks | Because of C-08 and C-10. Rule-based checks before the model call (prompt-injection and evasion patterns) and after it (decision phrases and compliance verdicts), with a fixed system prompt (D6, D9). Mitigation for R-13. | In Scope | KAN-24 |
| 13 | Design and development | Personal-data reminder and input check | Because of C-10. A reminder on the page not to enter personal data, and a limited rule-based input check for common patterns such as e-mail addresses and phone numbers; this is not comprehensive personal-data detection. Independently of that check, application, error and cloud logs are configured not to record user questions or conversation content, and no conversation is stored after the session ends; these controls are the actual privacy safeguard. They are verified by sending a marked test question to the deployed beta, searching the logs for it and checking that no conversation remains after the session ends (D9 criterion 8). Mitigation for R-11. | In Scope | KAN-26 |
| 14 | Design and development | One-page web interface | Because of C-08. Question box, answer view with citations and a permanent "not legal advice" notice (Features 1–3, D6). | In Scope | KAN-21, KAN-25 |
| 15 | Design and development | Beta features | Guided start (example questions, optional use-case selection), check the source (wording of each cited provision under the answer), follow-up questions within one session; because of C-04 and C-10, session context is discarded when the session ends (Features 5–7, D9). | In Scope | KAN-6, KAN-20, KAN-22 |
| 16 | Design and development | AI SBOM and pinned dependencies | `ai-bom.yaml` with every model version, licence (A-10) and source model card, corpus version, prompt templates and `config/rag.yaml` version; `requirements.txt` fully pinned (D6, updated in D12). | In Scope | — |
| 17 | Design and development | Model training or fine-tuning | Because of C-03 and C-05: models are used as-is; no GPU is available and no team-written model card is needed. | Out of Scope | |
| 18 | Design and development | Knowledge outside the designated source | Because of C-01: GDPR, national law, other EU acts and Commission guidelines are not added to the knowledge base (single source). | Out of Scope | |
| 19 | Design and development | Answers in Turkish or other languages | Because of C-02: questions and the source text are English only. | Out of Scope | |
| 20 | Design and development | Topics outside the education use cases | Because of C-04: non-education domains, deployer obligations, GPAI model provider obligations, enforcement and penalties receive an out-of-scope notice (row 11) and are not answered. | Out of Scope | |
| 21 | Design and development | User accounts, authentication, personal profiles and saved conversation history | Because of C-04 and C-10: these would require storing personal data and history across sessions. | Out of Scope | |
| 22 | Design and development | Legal advice, compliance decisions and implementation guidance | Because of C-08: the assistant identifies and explains provisions only; it gives no high-risk classification, compliance verdict or guidance on how to implement the requirements. | Out of Scope | |
| 23 | Verification and validation | Evaluation runs on the `dev` split | Alpha: Recall@5 and the comparison without and with retrieval required by D6 criterion 5 (an analysis result, not a pass level). Beta: O2 (a)–(d) and O4 per safety category, reported against the target levels as required by D9 criteria 2–4 (O4 also as correct responses / questions evaluated). Logged in Weights & Biases and `docs/eval/results.md`. The release candidate is scored on the `test` split instead (row 27). Mitigation for R-12 and R-13. | In Scope | — |
| 24 | Verification and validation | Answer review by two reviewers | Two team members review every in-scope answer against the rubric for O2 (b); disagreements are resolved against the rubric, then by a third member, and logged (D9, D12). | In Scope | — |
| 25 | Verification and validation | Extend the question set and rate its realism | Q&A Generation-Dataset v2: at least 40 questions, including new questions from proxy users and alpha errors, and at least 16 safety questions. The held-out `test` split is preserved: the original `test` questions stay unchanged, and new `test` questions are fixed by 09/12/2026 and never used for prompt, retrieval or rule tuning. The `dev` split is frozen on 04/12/2026 so that the beta can be scored on it by 09/12/2026 (internal date, [Release Plan](10-release-plan.md)). At least 5 proxy users rate 10 questions for realism (D8). Validates A-08; mitigation for R-08 and R-16. | In Scope | — |
| 26 | Verification and validation | Pilot: timed search task and survey | At least 5 proxy users (named by 18/11/2026) do timed tasks manually and with the assistant, with tasks balanced across the four use cases over all participants and with task sets and method order counterbalanced, then a short survey; results without names (D11). Validates A-04; mitigation for R-04. | In Scope | — |
| 27 | Verification and validation | Final evaluation on the held-out test split | O2 (a)–(d) and O4 per category on the `test` split of the release candidate, with links to the Weights & Biases runs (D12). | In Scope | — |
| 28 | Deployment | Trial cloud deployment | Because of C-05 and C-06. The alpha (D6) runs locally from `README.md`; a cloud deployment is not one of its acceptance criteria. In Sprint 2, if time allows, or at the latest by 27/11/2026 (start of Sprint 3), a short trial deployment on a Google Cloud instance of the planned type with a smoke test from outside the team's network, so that problems surface before the beta deployment (row 29); the answer time on this instance type is measured here (R-10). Mitigation for R-15 and R-10. | In Scope | — |
| 29 | Deployment | Deploy the beta for the pilot | Because of C-05 and C-06. Beta on Google Cloud, reachable by the pilot participants by 09/12/2026; the instance runs only in test, beta and pilot windows (D9). | In Scope | — |
| 30 | Operation and monitoring | Run the beta in the pilot and log problems | Keep the beta available and unchanged 16/12–23/12/2026 so that all pilot users evaluate the same version; log problems as they occur, without user questions (C-10); fix them in the release candidate: errors only, no new features (D12). Mitigation for R-17. | In Scope | — |
| 31 | Operation and monitoring | Cloud cost tracking | Because of C-06. Billing alerts at $25, $50 and $70; billing check at the end of Sprints 2 and 3. Validates A-07; mitigation for R-07. | In Scope | — |
| 32 | Continuous validation | Check for a newer consolidated version | At the start of each sprint from Sprint 2, check EUR-Lex for an amendment to the in-scope provisions; a change of the designated version needs Product Owner approval and an ADR. Validates A-02; mitigation for R-02. | In Scope | — |
| 33 | Continuous validation | Monitoring and retraining after 30/12/2026 | The project ends on 30/12/2026 and no model is trained; the maintenance trigger (a new consolidated version) is documented in R-02 for anyone who continues the work. | Out of Scope | |
| 34 | Re-evaluation | Charter updates | Project Charter v2, v3 and v4: answers to review comments, O1/O3 target review, Committee feedback on O2/O4, feature status and objective results (D7, D10, D13). | In Scope | — |
| 35 | Re-evaluation | Final report and lessons learned | Final report and lessons learned register built from the sprint reports (D14). | In Scope | — |
| 36 | Retirement | Release the cloud resources | Because of C-06. After the final demonstration and once the course's submission requirements are met, stop the Google Cloud resources that are no longer needed so that no further credit is used; the code, configuration and anonymised evaluation results stay in the project repository. | In Scope | — |
| 37 | All stages | Scrum events and sprint reports | Sprint planning, daily check-ins, reviews and retrospectives; Jira board and impediment list; sprint report after each sprint (`docs/sprints/sprint-N.md`). | In Scope | KAN-44 |
| 38 | All stages | Risk and assumption tracking | Review the risk register and the assumption checks at each sprint start; update triggers and owners in [Risks](11-risks.md). | In Scope | KAN-14 |
| 39 | All stages | Production code in Sprint 1 | Because of C-07: Sprint 1 produces documents, the question set, the source manifest and spike notes only (rows 3–7). | Out of Scope | |

### Constraint coverage

| Constraint | In Scope rows | Out of Scope rows |
|---|---|---|
| C-01 Single source | 4, 8 | 18 |
| C-02 English only | — (no work created) | 19 |
| C-03 RAG with open-source quantized model | 6, 9, 10 | 17 |
| C-04 Education use cases; follow-ups within one session | 11, 15 | 20, 21 |
| C-05 No GPU; paid cloud use within the course credit | 6, 28, 29 | 17 |
| C-06 $100 budget | 28, 29, 31, 36 | — |
| C-07 Team, duration, no production code in Sprint 1 | 6, 7 | 39 |
| C-08 Information, not legal advice | 10, 11, 12, 14 | 22 |
| C-09 Reuse with source acknowledgement | 4, 10 | — |
| C-10 No personal data persisted | 12, 13, 15, 30 | 21 |

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
- [x] Every work-creating constraint in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md) has an In Scope row, and every feature-removing constraint has an Out of Scope row (rule 4)
- [x] Rows created by a constraint name its ID (rule 5)
- [x] User authentication and PII storage are listed as Out of Scope if you do not plan them (rule 6)
- [x] No activity goes beyond the first proposal's scope (rule 7)
