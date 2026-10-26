# ELIZA: an EU AI Act assistant for EdTech teams

DI 502, Fall 2026 · METU Graduate School of Informatics

ELIZA is an information assistant on the EU AI Act (Regulation (EU) 2024/1689) for technical teams at EdTech providers. A developer, ML engineer or technical lead describes their education product and asks a question in their own words. ELIZA finds the relevant provisions in the consolidated text of 27/07/2026, explains them in plain language and shows each cited Article or Annex with its version date. It does not give legal advice, a high-risk classification or a compliance verdict; legal decisions stay with the company's legal team.

The assistant covers the four education use cases in Annex III point 3 (admission, assessment of learning outcomes, level placement and exam monitoring) and the provisions that decide whether and how such a system is regulated. It is a RAG chatbot with an open-source quantized language model, run locally from `README.md` on a team computer.

## Team

| Member | Role |
|---|---|
| Aliye Yeşim Yaman | Product Owner |
| Yaren Gürsoy | Scrum Master |
| Kaan Kocatürk | Data Scientist |
| Gözde Nur Özdemir | Data Scientist |

Project Review Committee: Tuğba Taşkaya Temizel (course instructor), Volga Sezen (teaching assistant). Details in [Project Organization](03-project-canvas/08-project-organization.md).

## Objectives

| # | Objective | Target (summary) |
|---|---|---|
| O1 | Search time | In the pilot, the median time to find the relevant provision is at least 20% shorter with the assistant than with a manual search |
| O2 | Evidence | The expected provision is cited for at least 80% of in-scope questions, and at least 75% of in-scope answers are fully supported by their cited passages |
| O3 | Understanding | At least 70% of pilot users rate the answers 4 or 5 out of 5 for understandability |
| O4 | Safety | 0 answers contain a classification or compliance verdict, and every legal-decision question is declined with a pointer to the relevant provisions |

The full success criteria are in the [Project Executive Summary](03-project-canvas/01-project-executive-summary.md).

## Timeline

| Sprint | Dates ([Release Plan](03-project-canvas/10-release-plan.md)) | Main deliverables |
|---|---|---|
| Sprint 1 | 14/10 – 28/10/2026 | D1 Project Charter v1, D3 Source Inventory and Manifest, D4 System Design |
| Sprint 2 | 04/11 – 18/11/2026 | D2 Q&A Dataset v1, D5 Preprocessing Report, D6 Alpha Release, D7 Project Charter v2 |
| Sprint 3 | 25/11 – 09/12/2026 | D8 Q&A Dataset v2, D9 Beta Release |
| Sprint 4 | 16/12 – 30/12/2026 | D10 Pilot Evaluation Report, D11 Release Candidate and Final Evaluation |

## Pages

- [Project Canvas](03-project-canvas/README.md): the project charter (scope, milestones, assumptions and constraints, activities, deliverables, dependencies, cost, organization, resources, release plan, risks)
- [Definition of Ready and Definition of Done](03-definition-of-ready-definition-of-done.md)
- [Sprint 1](04-sprint-1/README.md): review page and retrospective
- [User Stories](06-user-stories/README.md): user story map and story requirements
- [System Architecture Design Document](11-system-architecture-design-document.md)
- [Software Bill of Materials](10-software-bill-of-materials.md)
- [Datasheets](11-datasheets/) and [Experiment cards](12-experiment-cards/)

## Links

- Code and documents: GitHub, ELIZA-DI502/ELIZA_DI502_ORGANIZATION
- Backlog: Jira project KAN
- Source text: [Regulation (EU) 2024/1689, consolidated text of 27/07/2026 on EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727), reused under Commission Decision 2011/833/EU; only the Official Journal text is legally authentic.
