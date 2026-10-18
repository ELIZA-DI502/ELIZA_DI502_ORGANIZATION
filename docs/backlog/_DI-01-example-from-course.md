# Story Requirements for Epic DI-01

<!--
HOW TO USE THIS TEMPLATE
- Copy this file for each epic, e.g. docs/backlog/DI-01-document-qa.md.
  Files whose names start with "_" are never synced, so this template stays out of Jira.
- Leave every "Jira" cell empty. After your pull request is merged, the sync creates
  the issues and writes their keys into those cells. Do not edit or delete the keys.
- Owners are GitHub handles listed in .jira/team.yml. One owner per row.
  The Document Owner becomes the epic's assignee in Jira.
- Pick ONE breakdown per story:
    "Sub-tasks" table -> Model A: the story carries the points; sub-tasks carry hours.
    "Tasks" table     -> Model B: the tasks carry the points; leave the story's Points cell empty.
  A story can also have no breakdown yet (Model A without sub-tasks).
- Work that belongs to the epic but not to any story (setup, data pipelines, infrastructure)
  goes in the "Other tasks" table at the end. Delete that section if you don't need it.
- Every table and every "Tasks" / "Sub-tasks" / "Acceptance criteria" heading must sit in
  a story section or under "Other tasks". The pull request check flags anything the sync would skip.
- Sprint: a new story or task goes into the sprint in its Sprint cell, or, if that is empty,
  into the epic's Release Target. Write "Sprint 3" or "DI Sprint 3". Sub-tasks follow their story.
  This happens only when the issue is created. After that, plan sprints in Jira.
- Status is managed in Jira, not here.
- The example rows below show both models. Replace them with your own.
-->

| Epic | Document Q&A |
|---|---|
| Summary | Users ask questions about uploaded reports and get cited answers. |
| Document Owner | @volga |
| Designer | @volga |
| Developers | @volga, @volga |
| Release Target (Sprint) | Sprint 3 |
| Jira | [DI-16](https://volga-sezen.atlassian.net/browse/DI-16) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

| # | User story title | User story description | Priority | Points | Owner | Sprint | Notes | Jira |
|---|---|---|---|---|---|---|---|
| S1 | Upload a report and ask questions | As an AI user, I want to upload a report and ask questions about it, so that I can find key figures quickly. | High | 5 | @volga | | | [DI-17](https://volga-sezen.atlassian.net/browse/DI-17) |
| S2 | Fine-tune the answer model | As an AI developer, I want a fine-tuned answer model, so that answers follow the source documents more closely. | Medium | | @volga | | Takes more than one sprint, so it uses Tasks | [DI-20](https://volga-sezen.atlassian.net/browse/DI-20) |

## S1 · Upload a report and ask questions

**Acceptance criteria**

- When the user uploads a PDF under 20 MB, the system shall list it within 10 seconds.
- When the user asks a question about an uploaded report, the system shall cite the page it used.

**Sub-tasks**

| Sub-task | Owner | Estimate | Jira |
|---|---|---|---|
| Build upload widget | @volga | 4h | [DI-18](https://volga-sezen.atlassian.net/browse/DI-18) |
| Parse PDF into chunks | @volga | 6h | [DI-19](https://volga-sezen.atlassian.net/browse/DI-19) |

## S2 · Fine-tune the answer model

**Acceptance criteria**

- The fine-tuned model shall score above the base model on the evaluation set.

**Tasks**

| Task | Owner | Points | Sprint | Jira |
|---|---|---|---|---|
| Prepare the training set | @volga | 3 | Sprint 3 | [DI-21](https://volga-sezen.atlassian.net/browse/DI-21) |
| Train and evaluate the adapter | @volga | 5 | Sprint 4 | [DI-22](https://volga-sezen.atlassian.net/browse/DI-22) |

## Other tasks

| Task | Owner | Points | Sprint | Jira |
|---|---|---|---|---|
| Set up the evaluation pipeline in CI | @volga | 2 | | [DI-23](https://volga-sezen.atlassian.net/browse/DI-23) |
