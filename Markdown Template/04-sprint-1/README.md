# Sprint 1 Welcome Page

Welcome. This is the main page of Sprint 1 of team **ELIZA**: an information assistant on the EU AI Act for technical teams at EdTech providers ([project overview](../README.md)).

| Sprint 1 · Discovery | |
|---|---|
| Dates | 14/10/2026 – 28/10/2026 (upload 27/10/2026, review presentation 28/10/2026) |
| Release | Pre-alpha: no production code in Sprint 1 (C-07) |
| Team | Yeşim (Product Owner) · Yaren (Scrum Master) · Kaan and Gözde Nur (Data Scientists) |
| Jira | Project KAN, sprint "KAN Sprint 1": 7 user stories, 55 story points, 26 sub-tasks |
| Submitted version | Git tag `sprint-1` on `main`: the commit uploaded to ODTUClass on 27/10/2026 |

## Sprint goal

> Pre-alpha: Project Charter v1, the source manifest (D3) and the first system design (D4) are ready for the Sprint 1 review on 28/10/2026.

## What we achieved

- **We know what we build and why.** [Project Charter v1](../03-project-canvas/README.md) (D1) sets the problem, the users, four objectives with measurable targets (O1 Search time, O2 Evidence, O3 Understanding, O4 Safety) and the scope: the four education use cases of Annex III point 3 and the provisions that decide whether and how such a system is regulated. The assistant gives information, never a legal verdict (C-08).
- **We know what we deliver and when.** Eleven deliverables (D1–D11) and ten milestones over four sprints, with a release plan from pre-alpha to release candidate 1.0, 9 assumptions, 10 constraints, 12 risks and the resources and dependencies behind them.
- **We work from one verified source.** The consolidated text of Regulation (EU) 2024/1689 of 27/07/2026 is stored with its manifest and hash, together with the list of in-scope provisions ([D3](../../data/README.md)).
- **We know how we build it.** The first [System Architecture Design Document](../11-system-architecture-design-document.md) (D4) records the design decisions; two technical spikes checked them: [parsing and chunking the source](../../docs/spikes/parsing-spike.md) and [choosing the answer model on CPU](../../docs/spikes/model-selection-spike.md) (Llama-3.1-8B-Instruct, fallback Phi-4-mini-instruct). The models and tools are in the [SBOM](../10-software-bill-of-materials.md).
- **We have a backlog for Sprints 2–4.** Eight epics and 30 user stories for Sprints 2–4 (plus two in the backlog), each with acceptance criteria and sub-tasks, mapped to the releases in the [User Story Map v1](../06-user-stories/01-user-story-map-v1.md) and described epic by epic in the [story requirements pages](../06-user-stories/README.md).
- **We closed our gaps in the Sprint 1 fundamentals** with one learning spike each.

## Sprint results

Status in Jira at the upload on 27/10/2026: **6 of 7 stories done (50 of 55 story points)**.

| Story | Points | Status |
|---|---|---|
| [KAN-79](https://yarengursoy.atlassian.net/browse/KAN-79) Decide whether to approve the project's purpose and scope | 13 | Done |
| [KAN-69](https://yarengursoy.atlassian.net/browse/KAN-69) Judge whether the plan can hold | 8 | Done |
| [KAN-70](https://yarengursoy.atlassian.net/browse/KAN-70) Check that the delivery plan fits the course calendar | 8 | Done |
| [KAN-67](https://yarengursoy.atlassian.net/browse/KAN-67) Work from one verified copy of the source | 5 | Done |
| [KAN-81](https://yarengursoy.atlassian.net/browse/KAN-81) Agree on the technologies for the baseline | 13 | Done |
| [KAN-82](https://yarengursoy.atlassian.net/browse/KAN-82) Close my gaps in the Sprint 1 fundamentals | 3 | Done |
| [KAN-80](https://yarengursoy.atlassian.net/browse/KAN-80) Know which stories I can start and when my work is done | 5 | Open until the Sprint 1 review (28/10/2026) |

**Not finished at the upload, and why:**

- [KAN-80](https://yarengursoy.atlassian.net/browse/KAN-80) stays open until the review, because its sub-task [KAN-44](https://yarengursoy.atlassian.net/browse/KAN-44) includes preparing and giving the Sprint 1 review on 28/10/2026.
- [KAN-40](https://yarengursoy.atlassian.net/browse/KAN-40) (submit Project Charter v1) is closed right after the upload.
- Planned learning follow-ups (for example the RAG lecture slides) are listed with their dates in the Definition of Done of each [learning spike](../../docs/spikes/README.md).

## Deliverables

| Deliverable | Pages | Jira |
|---|---|---|
| D1 Project Charter v1 | [Project Canvas](../03-project-canvas/README.md): [Executive Summary](../03-project-canvas/01-project-executive-summary.md), [Milestones](../03-project-canvas/02-milestones.md), [Assumptions & Constraints](../03-project-canvas/03-assumptions-and-constraints.md), [Major Activities](../03-project-canvas/04-major-activities.md), [Deliverables](../03-project-canvas/05-deliverables.md), [Dependencies](../03-project-canvas/06-dependencies.md), [Project Organization](../03-project-canvas/08-project-organization.md), [Facilities & Resources](../03-project-canvas/09-facilities-and-resources.md), [Release Plan](../03-project-canvas/10-release-plan.md), [Risks](../03-project-canvas/11-risks.md) | [KAN-79](https://yarengursoy.atlassian.net/browse/KAN-79), [KAN-69](https://yarengursoy.atlassian.net/browse/KAN-69), [KAN-70](https://yarengursoy.atlassian.net/browse/KAN-70) |
| D3 Source Inventory and Manifest v1 | [data/README.md](../../data/README.md), [manifest.csv](../../data/manifest.csv), [provision-list.csv](../../data/provision-list.csv) | [KAN-67](https://yarengursoy.atlassian.net/browse/KAN-67) |
| D4 System Design v1 | [System Architecture Design Document](../11-system-architecture-design-document.md), [Software Bill of Materials](../10-software-bill-of-materials.md), spikes: [parsing and chunking](../../docs/spikes/parsing-spike.md), [model selection](../../docs/spikes/model-selection-spike.md) | [KAN-81](https://yarengursoy.atlassian.net/browse/KAN-81) |
| User stories | [User Story Map v1](../06-user-stories/01-user-story-map-v1.md), [story requirements for each epic](../06-user-stories/README.md) | [KAN-80](https://yarengursoy.atlassian.net/browse/KAN-80) |
| Learning spikes | [Yeşim](../../docs/spikes/learning-yesim.md), [Yaren](../../docs/spikes/learning-yaren.md), [Kaan](../../docs/spikes/learning-kaan.md), [Gözde Nur](../../docs/spikes/learning-gozde-nur.md) | [KAN-82](https://yarengursoy.atlassian.net/browse/KAN-82) |
| Definition of Ready and Done for Sprint 2 | [Definition of Ready and Definition of Done](../03-definition-of-ready-definition-of-done.md) | [KAN-43](https://yarengursoy.atlassian.net/browse/KAN-43) |
| Jira backlog export | [docs/backlog](../../docs/backlog/_README.md): the backlog exported from Jira on 27/10/2026 | |
| Burndown chart | [Burndown chart](../04-burndown-chart.md), Sprint 1 | |
| Retrospective | [Sprint 1 Retrospective](02-sprint-1-retrospective.md) | |
| Review | [Sprint 1 Review Page](01-sprint-1-review-page.md), filled in by the reviewing team | |

## Who did what

From the Sprint 1 sub-tasks in Jira.

| Member | Role | Main Sprint 1 work |
|---|---|---|
| Yeşim | Product Owner | Deliverables, Project Organization, Major Activities and Release Plan pages; charter consistency check; source text, manifest and provision list (D3); user stories, story map and story requirements; this page |
| Yaren | Scrum Master | Milestones and Dependencies pages; Definition of Ready and Done; repository folders |
| Kaan | Data Scientist | Project Executive Summary; Facilities and Resources page; System Architecture Design Document v1 |
| Gözde Nur | Data Scientist | Assumptions and Constraints, and Risks pages; parsing and model selection spikes; the NLP design decisions D7–D12 in the design document |

## Sprint 1 review (28/10/2026)

Ten minutes. Each part is presented by the member who wrote it.

| # | Who | Time | Topic | Page |
|---|---|---|---|---|
| 1 | Yeşim | 0:30 | Opening: what ELIZA does, the team, the Sprint 1 goal | This page |
| 2 | Kaan | 0:45 | Charter: problem, users, objectives O1–O4, scope | [Project Executive Summary](../03-project-canvas/01-project-executive-summary.md) |
| 3 | Yeşim | 0:30 | Charter: deliverables, roles and stakeholders, major activities | [Deliverables](../03-project-canvas/05-deliverables.md), [Project Organization](../03-project-canvas/08-project-organization.md) |
| 4 | Yaren | 0:30 | Charter: milestones and dependencies | [Milestones](../03-project-canvas/02-milestones.md), [Dependencies](../03-project-canvas/06-dependencies.md) |
| 5 | Gözde Nur | 0:45 | Charter: assumptions, constraints and risks | [Assumptions & Constraints](../03-project-canvas/03-assumptions-and-constraints.md), [Risks](../03-project-canvas/11-risks.md) |
| 6 | Yeşim | 2:30 | User stories: releases, epics, story map, one story's requirements and the same story in Jira | [Release Plan](../03-project-canvas/10-release-plan.md), [User Story Map v1](../06-user-stories/01-user-story-map-v1.md), [Know the Limits](../06-user-stories/06-story-requirements-for-epic-kan-18.md) (KAN-2) |
| 7 | Gözde Nur | 1:15 | Spikes that led to the design choices | [Parsing spike](../../docs/spikes/parsing-spike.md), [model selection spike](../../docs/spikes/model-selection-spike.md) |
| 8 | Kaan | 1:15 | Architecture diagram and design decisions | [System Architecture Design Document](../11-system-architecture-design-document.md) |
| 9 | Yaren | 1:00 | How we work: planning poker, Definition of Ready and Done, retrospective | [DoR and DoD](../03-definition-of-ready-definition-of-done.md), [Retrospective](02-sprint-1-retrospective.md) |
| 10 | Yeşim | 0:30 | Question to the Project Review Committee (A-06) | – |

**Question to the Project Review Committee ([A-06](../03-project-canvas/03-assumptions-and-constraints.md)):** do you agree with our target levels? For evidence (O2), the expected provision is cited for at least 80% of the in-scope questions, and at least 75% of the in-scope answers are fully supported by the text they cite. For safety (O4), no answer gives a legal verdict, 100% of the legal-decision questions get the expected response, and at least 80% of the questions in each of the other three safety categories (out of scope, missing evidence, adversarial) get it. The answer is recorded for Charter v2 ([KAN-89](https://yarengursoy.atlassian.net/browse/KAN-89)).

## Next: Sprint 2 (28/10 – 18/11/2026)

Alpha 0.1, the baseline: question set v1 (D2), the indexed source text (D5), the baseline retrieval measured against the charter target (D6), and Project Charter v2 (D7) with the answers to the Sprint 1 review. The Sprint 2 stories are in the [User Story Map v1](../06-user-stories/01-user-story-map-v1.md) and are estimated at the Sprint 2 planning on 28/10/2026.
