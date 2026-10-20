# Release Plan

Provide a high-level release plan showing the project's deliverables mapped against a sprint timeline. For example, indicate how many sprints are planned in each release, along with the start and end dates for each sprint.

A **release** is the distribution of the final version, or the newest version, of a software application. In agile development, it is a deployable software package built over several iterations [1]. Define your releases using the release stages below: alpha, beta, release candidate, and so on.

A weak plan has one release at the end. A strong plan shows what each sprint puts in someone's hands. Write "Sprint 3 — Beta — D6 Beta release for five pilot users", not "Sprints 1–4 — Chatbot" (examples illustrative only).

## Sprint calendar

The project has four sprints.

| Sprint | Start | End |
|---|---|---|
| Sprint 1 | 14/10/2026 | 28/10/2026 |
| Sprint 2 | 04/11/2026 | 18/11/2026 |
| Sprint 3 | 25/11/2026 | 09/12/2026 |
| Sprint 4 | 16/12/2026 | 30/12/2026 |

## Release stages

| Stage | What it means [1] | Who uses it [1] |
|---|---|---|
| **Pre-alpha** | Work before testing starts, such as designing and analysing new features | The development team |
| **Alpha** | The beginning of software testing, done by the development team | The development team |
| **Beta** | Major fixes are done. The version goes to specific customers or testers for feedback on remaining bugs and enhancements. | Named customers or testers |
| **Release candidate** | The final version, prepared for official release to end users | End users |

A release can also be classed as **major** (wide-ranging changes and new features), **minor** (small improvements to existing features) or an **emergency fix** (urgent issues) [1]. You may use these labels, for example "Beta 1.1 (minor)".

## How to fill in each row

Write one row per sprint.

| Field | What it means | When it applies | Question it answers |
|---|---|---|---|
| **#** | A running number | Every row | Which row is this? |
| **Release** | The release that this sprint builds or ships: a stage from the table above, with an optional version label (e.g., "Alpha 0.1") | Every row | Which release? |
| **Sprint** | Sprint 1, 2, 3 or 4 | Every row | When is it built? |
| **Start Date** | The sprint's start date from the calendar | Every row | From? |
| **End Date** | The sprint's end date from the calendar | Every row | To? |
| **Key Deliverable(s)** | Deliverables from [Deliverables](03-project-canvas_v2/05-deliverables.md) due in this sprint, given by number and name | Every row with a deliverable due in it | What is handed over? |

A release can span more than one sprint. Then it appears in more than one row, and the table shows how many sprints the release takes.

## Rules

Each rule is a condition you can check with yes or no.

1. All four sprints appear in the table.
2. Start and end dates are not modified.
3. Every Release names a release stage (pre-alpha, alpha, beta or release candidate) [1].
4. Every Key Deliverable exists in [Deliverables](03-project-canvas_v2/05-deliverables.md) under the same number and name.
5. Every Key Deliverable's due date falls within the dates of the sprint it is listed in.
6. A release does not combine items that [Deliverables](03-project-canvas_v2/05-deliverables.md) defines as separate deliverables under one new name; list the deliverable numbers instead.
7. The plan has more than one release, spread over the sprints, not a single delivery at the end.
8. Every beta names who receives it: which customers or testers [1]. The same people appear as Stakeholders of the beta deliverable in [Deliverables](03-project-canvas_v2/05-deliverables.md).

## Test: two consistency checks

1. **Against [Deliverables](03-project-canvas_v2/05-deliverables.md).** Pick each Key Deliverable. Is its due date inside the sprint's dates, and is its name the same as in 05?
2. **Against [Milestones](03-project-canvas_v2/02-milestones.md).** Does every milestone in [Milestones](03-project-canvas_v2/02-milestones.md) fall in the sprint where its deliverable is listed here, or in the gap just after it?

## Not this / this

Each corrected entry fixes only the named defect. All examples are illustrative.

| Not this | This | Defect |
|---|---|---|
| One "Chatbot Prototype" release that covers two capabilities, while [Deliverables](03-project-canvas_v2/05-deliverables.md) lists them as two deliverables | Key Deliverable(s): "D2 Functional core chat application; D5 Chatbot prototype" | Release plan and Deliverables disagree |
| "Release 1 — Sprints 1–4 — Final product" | Four rows: pre-alpha (S1), alpha (S2), beta (S3), release candidate (S4) | A single release at the end |
| Dates written as "Mid-Sprint 2" | "04/11/2026 – 18/11/2026" | Start and end dates are required for each sprint |
| "Beta — given to users" | "Beta — given to five pilot students from the target user group" | A beta goes to specific customers or testers [1] |

## Patterns to use if stuck

- **One stage per sprint:** pre-alpha in Sprint 1 (charter and design), alpha in Sprint 2, beta in Sprint 3, release candidate in Sprint 4 [1]. Adjust if your team needs two sprints for one stage.
- **A checkpoint before each beta or release candidate**, in the gap between sprints, where the Product Owner decides go or no-go (record it in [Milestones](03-project-canvas_v2/02-milestones.md)).
- **Minor releases for fixes:** if a beta needs fixes, plan "Beta 1.1 (minor)" in the next sprint rather than redoing the stage [1].

## What doesn't belong on this page

| Item | Where it belongs |
|---|---|
| Milestones and checkpoints | [Milestones](03-project-canvas_v2/02-milestones.md) |
| Deliverable descriptions, acceptance criteria and approvers | [Deliverables](03-project-canvas_v2/05-deliverables.md) |
| Which user stories are built in which sprint | The User Story Map, which can show sprints on its horizontal axis |
| Activities and their scope | [Major Activities](03-project-canvas_v2/04-major-activities.md) |

## Release table

The product is released in three stages after a pre-alpha design sprint: Alpha 0.1 (Sprint 2), Beta 0.5 (Sprint 3) and Release candidate 1.0 (Sprint 4, after the pilot with Beta 0.5). Deliverable numbers and names match [Deliverables](05-deliverables.md); checkpoints are recorded in [Milestones](02-milestones.md). Feature numbers refer to the Scope Definition in the [Project Executive Summary](01-project-executive-summary.md).

| # | Release | Sprint | Start Date | End Date | Key Deliverable(s) |
|---|---|---|---|---|---|
| 1 | Pre-alpha | Sprint 1 | 14/10/2026 | 28/10/2026 | D1 Project Charter v1; D2 Q&A Generation-Dataset v1; D3 Source Inventory and Manifest v1; D4 System Design v1 |
| 2 | Alpha 0.1 | Sprint 2 | 04/11/2026 | 18/11/2026 | D5 Preprocessing Report v1; D6 Alpha Release; D7 Project Charter v2 |
| 3 | Beta 0.5 | Sprint 3 | 25/11/2026 | 09/12/2026 | D8 Q&A Generation-Dataset v2; D9 Beta Release; D10 Project Charter v3 |
| 4 | Release candidate 1.0 (following the Beta 0.5 pilot) | Sprint 4 | 16/12/2026 | 30/12/2026 | D11 Pilot Evaluation Report; D12 Release Candidate and Final Evaluation; D13 Project Charter v4; D14 Final Report and Lessons Learned |

Beta 0.5 is built in Sprint 3 and kept unchanged during the Sprint 4 pilot (16/12–23/12, D11), so that all participants evaluate the same version. Problems found during the pilot are recorded as they occur and fixed in the release candidate, which is built from the beta. The held-out `test` split is not used to guide fixes. The release candidate adds no new features.

### What each release contains and who receives it

| Release | Content | Received by |
|---|---|---|
| Pre-alpha | No production code (C-07): evaluation questions (including questions taken or adapted from published work), rubric, source manifest, provision list, System Architecture Design Document v1 with its diagram, ADRs, technical spike notes and one learning spike note per member | Development team; Project Review Committee (charter and design review) |
| Alpha 0.1 | Core MVP, features 1–4: ask in their own words, find the relevant provisions with version date, plain-language answer, boundary notices; one-page web interface with a "not legal advice" notice | Development team (testing on the `dev` split); AI customer (course instructors and peer groups) at the Sprint 2 review |
| Beta 0.5 | Alpha fixes plus features 5–7: guided start, check the source, follow-up questions in the same session; rule-based input and decision-phrase checks; deployed on Google Cloud with logs that do not record user questions (C-10). A beta feature that cannot be completed is deferred with a reason and the Product Owner's agreement (D9 criterion 5) | AI users: at least 5 technical proxy users representing EdTech developers and ML engineers (technical professionals working on software or AI, named in A-04); AI customer: course instructors and peer groups, acting as academic proxies for the legal and compliance team of an EdTech provider |
| Release candidate 1.0 | Beta 0.5 with the fixes from the pilot; no new features | AI customer (course instructors and peer groups) at the final demonstration; Project Review Committee |

### Gaps between sprints

| Gap | Dates | Checkpoint in [Milestones](02-milestones.md) |
|---|---|---|
| Sprint 1 → Sprint 2 | 29/10/2026 – 03/11/2026 | M3 Checkpoint: Sprint 1 reviewed, development starts (02/11/2026) |
| Sprint 2 → Sprint 3 | 19/11/2026 – 24/11/2026 | M6 Checkpoint: go/no-go for the beta (20/11/2026) |
| Sprint 3 → Sprint 4 | 10/12/2026 – 15/12/2026 | M8 Checkpoint: go/no-go for the pilot and the release candidate (11/12/2026) |

### Fixed dates inside the sprints

| Date | What is fixed | Why |
|---|---|---|
| 28/10/2026 | `test` split of D2 frozen | Held-out questions are not used while tuning (D2 criterion 8) |
| 18/11/2026 | 5 named pilot participants and their dates confirmed | Assumption A-04 |
| 27/11/2026 (at the latest) | Trial cloud deployment with a smoke test from outside the team's network done | Access and answer-time problems surface before the beta deployment ([Major Activities](04-major-activities.md) row 28; R-10, R-15) |
| 04/12/2026 | D8 `dev` questions frozen | Leaves 5 days to score the beta on the D8 `dev` split before 09/12 (D9) |
| 09/12/2026 | New D8 `test` questions frozen | D8 criterion 4 |
| 16/12 – 23/12/2026 | Pilot with Beta 0.5 | Leaves one week to fix the release candidate and finish D11–D14 before 30/12 |

## Example (illustrative only)

The project and deliverable numbers are invented. They match the examples in [Milestones](03-project-canvas_v2/02-milestones.md) and [Deliverables](03-project-canvas_v2/05-deliverables.md).

| # | Release | Sprint | Start Date | End Date | Key Deliverable(s) |
|---|---|---|---|---|---|
| 1 | Pre-alpha | Sprint 1 | 14/10/2026 | 28/10/2026 | D1 Project Charter v1 |
| 2 | Alpha 0.1 | Sprint 2 | 04/11/2026 | 18/11/2026 | D2 Q&A Generation-Dataset v1; D3 Baseline experiment card; D4 Alpha prototype; D5 Project Charter v2 |
| 3 | Beta 0.5 | Sprint 3 | 25/11/2026 | 09/12/2026 | D6 Beta release (five pilot students) |
| 4 | Release candidate 1.0 | Sprint 4 | 16/12/2026 | 30/12/2026 | D7 Pilot feedback report; D8 Release candidate; D9 Final report |

## Checklist before submitting

- [x] All four sprints appear (Rule 1)
- [x] All start and end dates match the sprint calendar (Rule 2)
- [x] Every row names a release stage (Rule 3)
- [x] Every Key Deliverable exists in [Deliverables](03-project-canvas_v2/05-deliverables.md) under the same number and name (Rule 4)
- [x] Every Key Deliverable is due within its sprint's dates (Rule 5)
- [x] No release merges separate deliverables under a new name (Rule 6)
- [x] There is more than one release across the sprints (Rule 7)
- [x] Every beta names its customers or testers, and they match those in [Deliverables](03-project-canvas_v2/05-deliverables.md) (Rule 8)

## References

[1] Hanna, K. T. (2022, March 17). *What is a software release?* TechTarget. Retrieved October 1, 2026, from https://www.techtarget.com/it-infrastructure/definition/release
