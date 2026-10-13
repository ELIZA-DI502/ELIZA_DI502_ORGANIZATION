# Story Requirements for Epic DI-01

<!--
HOW TO USE THIS TEMPLATE
- Copy this file for each epic, e.g. docs/backlog/DI-01-document-qa.md.
  Files whose names start with "_" are never synced, so this template stays out of Jira.
- Leave every "Jira" cell empty. After your pull request is merged, the sync creates
  the issues and writes their keys into those cells. Do not edit or delete the keys.
- Owners are GitHub handles listed in .jira/team.yml. One owner per row.
- Pick ONE breakdown per story:
    "Sub-tasks" table -> Model A: the story carries the points; sub-tasks carry hours.
    "Tasks" table     -> Model B: the tasks carry the points; leave the story's Points cell empty.
  A story can also have no breakdown yet (Model A without sub-tasks).
- Status and sprint are managed in Jira, not here.
- The example rows below show both models. Replace them with your own.
-->

| Epic | Document Q&A |
|---|---|
| Summary | Users ask questions about uploaded reports and get cited answers. |
| Document Owner | @volga |
| Designer | @volga |
| Developers | @volga |
| Release Target (Sprint) | Sprint 3 |
| Jira | [DI-1](https://volga-sezen.atlassian.net/browse/DI-1) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

| # | User story title | User story description | Priority | Points | Notes | Jira |
|---|---|---|---|---|---|---|
| S1 | Upload a report and ask questions | As an AI user, I want to upload a report and ask questions about it, so that I can find key figures quickly. | High | 5 | | [DI-2](https://volga-sezen.atlassian.net/browse/DI-2) |
| S2 | Fine-tune the answer model | As an AI developer, I want a fine-tuned answer model, so that answers follow the source documents more closely. | Medium | | Takes more than one sprint, so it uses Tasks | [DI-5](https://volga-sezen.atlassian.net/browse/DI-5) |

## S1 · Upload a report and ask questions

**Acceptance criteria**

- When the user uploads a PDF under 20 MB, the system shall list it within 10 seconds.
- When the user asks a question about an uploaded report, the system shall cite the page it used.

**Sub-tasks**

| Sub-task | Owner | Estimate | Jira |
|---|---|---|---|
| Build upload widget | @volga | 4h | [DI-3](https://volga-sezen.atlassian.net/browse/DI-3) |
| Parse PDF into chunks | @volga | 6h | [DI-4](https://volga-sezen.atlassian.net/browse/DI-4) |

## S2 · Fine-tune the answer model

**Acceptance criteria**

- The fine-tuned model shall score above the base model on the evaluation set.

**Tasks**

| Task | Owner | Points | Jira |
|---|---|---|---|
| Prepare the training set | @volga | 3 | [DI-6](https://volga-sezen.atlassian.net/browse/DI-6) |
| Train and evaluate the adapter | @volga | 5 | [DI-7](https://volga-sezen.atlassian.net/browse/DI-7) |
