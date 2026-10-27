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
- **We know what we deliver and when.** Eleven deliverables (D1–D11) and ten milestones over four sprints, with a release plan from pre-alpha to release candidate 1.0, 10 assumptions, 10 constraints, 13 risks and the resources and dependencies behind them.
- **We work from one verified source.** The consolidated text of Regulation (EU) 2024/1689 of 27/07/2026 is stored with its manifest and hash, together with the list of in-scope provisions ([D3](../../data/README.md)).
- **We know how we build it.** The first [System Architecture Design Document](../11-system-architecture-design-document.md) (D4) records the design decisions; two technical spikes checked them: [parsing and chunking the source](../../docs/spikes/parsing-spike.md) and [choosing the answer model on CPU](../../docs/spikes/model-selection-spike.md) (Llama-3.1-8B-Instruct, fallback Phi-4-mini-instruct). The models and tools are in the [SBOM](../10-software-bill-of-materials.md).
- **We have a backlog for Sprints 2–4.** Eight epics and 30 user stories for Sprints 2–4 (plus two in the backlog), each with acceptance criteria and sub-tasks, mapped to the releases in the [User Story Map v1](../06-user-stories/01-user-story-map-v1.md) and described epic by epic in the [story requirements pages](../06-user-stories/README.md).
- **We closed our gaps in the Sprint 1 fundamentals** with one learning spike each.

## Deliverables

| Deliverable | Pages | Jira |
|---|---|---|
| D1 Project Charter v1 | [Project Canvas](../03-project-canvas/README.md): [Executive Summary](../03-project-canvas/01-project-executive-summary.md), [Milestones](../03-project-canvas/02-milestones.md), [Assumptions & Constraints](../03-project-canvas/03-assumptions-and-constraints.md), [Major Activities](../03-project-canvas/04-major-activities.md), [Deliverables](../03-project-canvas/05-deliverables.md), [Dependencies](../03-project-canvas/06-dependencies.md), [Project Organization](../03-project-canvas/08-project-organization.md), [Facilities & Resources](../03-project-canvas/09-facilities-and-resources.md), [Release Plan](../03-project-canvas/10-release-plan.md), [Risks](../03-project-canvas/11-risks.md) | [KAN-79](https://yarengursoy.atlassian.net/browse/KAN-79), [KAN-69](https://yarengursoy.atlassian.net/browse/KAN-69), [KAN-70](https://yarengursoy.atlassian.net/browse/KAN-70) |
| D3 Source Inventory and Manifest v1 | [data/README.md](../../data/README.md), [manifest.csv](../../data/manifest.csv), [provision-list.csv](../../data/provision-list.csv) | [KAN-67](https://yarengursoy.atlassian.net/browse/KAN-67) |
| D4 System Design v1 | [System Architecture Design Document](../11-system-architecture-design-document.md), [Software Bill of Materials](../10-software-bill-of-materials.md), spikes: [parsing and chunking](../../docs/spikes/parsing-spike.md), [model selection](../../docs/spikes/model-selection-spike.md) | [KAN-81](https://yarengursoy.atlassian.net/browse/KAN-81) |
| User stories | [User Story Map v1](../06-user-stories/01-user-story-map-v1.md), [story requirements for each epic](../06-user-stories/README.md) | [KAN-80](https://yarengursoy.atlassian.net/browse/KAN-80) |
| Learning spikes | [Yeşim](../../docs/spikes/learning-yesim.md), [Yaren](../../docs/spikes/learning-yaren.md), [Kaan](../../docs/spikes/learning-kaan.md), [Gözde Nur](../../docs/spikes/learning-gozde-nur.md) | [KAN-82](https://yarengursoy.atlassian.net/browse/KAN-82) |
| Definition of Ready and Done for Sprint 2 | [Definition of Ready and Definition of Done](../03-definition-of-ready-definition-of-done.md) | [KAN-43](https://yarengursoy.atlassian.net/browse/KAN-43) |
| Retrospective | [Sprint 1 Retrospective](02-sprint-1-retrospective.md) | |
| Review | [Sprint 1 Review Page](01-sprint-1-review-page.md), filled in by the reviewing team | |

## Who did what

From the Sprint 1 sub-tasks in Jira.

| Member | Role | Main Sprint 1 work |
|---|---|---|
| Yeşim | Product Owner | Deliverables, Project Organization, Major Activities and Release Plan pages; charter consistency check; source text, manifest and provision list (D3); user stories, story map and story requirements; this page |
| Yaren | Scrum Master | Milestones and Dependencies pages; Definition of Ready and Done; repository folders |
| Kaan | Data Scientist | Project Executive Summary; Facilities and Resources page; System Architecture Design Document v1 |
| Gözde Nur | Data Scientist | Assumptions and Constraints, and Risks pages; parsing and model selection spikes; design decisions in the design document |

## Next: Sprint 2 (28/10 – 18/11/2026)

Alpha 0.1, the baseline: question set v1 (D2), the indexed source text (D5), the baseline retrieval measured against the charter target (D6), and Project Charter v2 (D7) with the answers to the Sprint 1 review. The Sprint 2 stories are in the [User Story Map v1](../06-user-stories/01-user-story-map-v1.md) and are estimated at the Sprint 2 planning on 28/10/2026.
