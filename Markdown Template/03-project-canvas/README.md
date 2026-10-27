# Project Canvas

Red cells must completed for the first version of your project canvas.

*Cells marked with \* are the red cells.*

| [Scope\*](01-project-executive-summary.md) | [Milestones\*](02-milestones.md) | [Assumptions & Constraints\*](03-assumptions-and-constraints.md) |
|---|---|---|
| • An information assistant on the EU AI Act (Regulation (EU) 2024/1689) for technical teams at EdTech providers, used through a web page<br>• Covers the four education use cases in Annex III point 3 and the provisions that decide whether and how such a system is regulated, from the consolidated text of 27/07/2026<br>• Objectives: O1 Search time, O2 Evidence, O3 Understanding, O4 Safety<br>• No legal advice, compliance verdict or implementation guidance | • M1–M3 (28/10/2026): Charter v1, sources and first design, development starts<br>• M4–M6 (18/11/2026): baseline on the validation questions, Charter v2, go/no-go for the beta<br>• M7–M8 (09/12/2026): beta runs end to end, go/no-go for the pilot<br>• M9–M10 (30/12/2026): pilot measured, release candidate approved | • Assumptions A-01 to A-09, each with a basis, a dated check, an owner and a linked risk<br>• Constraints C-01 to C-10, for example: one source text, English only, a RAG chatbot with an open-source quantized model, CPU only, a $100 credit, four students, information and not legal advice, no personal data requested |

| [Major Activities](04-major-activities.md) | [Deliverables\*](05-deliverables.md) | [Dependencies](06-dependencies.md) |
|---|---|---|
| • In scope: spikes, source preparation, evaluation questions, baseline, experiments, beta, pilot, release candidate and documentation<br>• Out of scope: model training or fine-tuning, user accounts and saved history, hosted cloud deployment | • Sprint 1: D1 Charter v1, D3 Source Inventory and Manifest, D4 System Design (27/10/2026)<br>• Sprint 2: D2 Q&A Dataset v1, D5 Preprocessing Report, D6 Alpha Release, D7 Charter v2 (11–14/11/2026)<br>• Sprint 3: D8 Q&A Dataset v2, D9 Beta Release (05/12/2026)<br>• Sprint 4: D10 Pilot Evaluation Report, D11 Release Candidate and Final Evaluation (30/12/2026) | • Work that waits for other work, each with a critical date and a named contact<br>• For example: question adaptation waits for the selected benchmark scenarios; the baseline evaluation waits for the index and the D2 `val` questions; the final evaluation waits for the frozen `test` questions |

| [Cost & Funding](07-cost-and-funding.md) | [Project Organization\*](08-project-organization.md) | [Facilities and Resources](09-facilities-and-resources.md) |
|---|---|---|
| • Funding: the course's $100 Google Cloud credit, kept as a reserve (C-06)<br>• The system runs on the team's own computers and free tools (Google Colab, Hugging Face, Weights & Biases) | • Product Owner: Yeşim · Scrum Master: Yaren · Data Scientists: Kaan, Gözde Nur<br>• Project Review Committee: the course instructors<br>• AI customer: the course instructors and peer groups · AI users: pilot proxy users · Data provider: EUR-Lex · AI partner: Hugging Face | • The team's own computers (CPU only), Google Colab, the reserve Google Cloud credit<br>• Open-source quantized LLM and embedding model run locally; Chroma vector store<br>• GitHub, Jira, Confluence and Weights & Biases<br>• Pilot and final demo in person on a team computer |

| [Release Plan](10-release-plan.md) | [Risks](11-risks.md) | Result |
|---|---|---|
| • Alpha 0.1 (Sprint 2): the baseline<br>• Beta 0.5 (Sprint 3): the MVP, Features 1–4, with the one-page web interface<br>• Release candidate 1.0 (Sprint 4): Check the source and application dates; used in the pilot, then fixed for the final demo | • 12 risks (R-01–R-11) in five layers: data, model, infrastructure, integration, people/process<br>• Each risk has a probability, impact, score, owner and links to the assumptions and constraints<br>• 1 High (R-03 too few pilot users), 7 Medium, 4 Low | • **Problem:** technical teams building AI systems for education must find which EU AI Act provisions apply to their use case in a long, already amended text, or wait for a legal review<br>• **Value:** they find the relevant provisions faster than with a manual search (O1), with the cited source and its version date (O2), explained in plain language (O3), and with no legal verdict (O4)<br>• **Impacted:** the technical teams (AI users), the legal and compliance team (AI customer), and the students and teachers who use their products<br>• **Conflicts:** developers want a yes-or-no answer, the legal team wants no automated legal decisions; the assistant shows the relevant articles and conditions and never gives a classification or compliance verdict |

## Subpages

- [Project Executive Summary](01-project-executive-summary.md)
- [Milestones](02-milestones.md)
- [Assumptions & Constraints](03-assumptions-and-constraints.md)
- [Major Activities](04-major-activities.md)
- [Deliverables](05-deliverables.md)
- [Dependencies](06-dependencies.md)
- [Cost & Funding](07-cost-and-funding.md)
- [Project Organization](08-project-organization.md)
- [Facilities & Resources](09-facilities-and-resources.md)
- [Release Plan](10-release-plan.md)
- [Risks](11-risks.md)
