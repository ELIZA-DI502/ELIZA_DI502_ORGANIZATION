# Sprint 1 Retrospective

Retrospective meetings allow teams to identify points of strength, issues faced during the sprint, and let members discuss how to handle them next time. 

While holding the retrospective meeting, assess promised time-commitments outlined in the constraints/budget sections and evaluate whether these were fulfilled. Everyone must also individually comment on their learning journey and their ability to contribute in this sprint.

The table below is very basic, but feel free to follow a template from Miro. For holding the retro you can use [Scrum Powder | Retro](https://scrumpowder.com/retro).

**Sprint 1:** 14/10/2026 – 28/10/2026 · **Team:** ELIZA (Yeşim, Yaren, Kaan, Gözde Nur)

| What went well? | What went bad? | Action | Assigned to |
|---|---|---|---|
| All ten Project Canvas pages were written on time, each with one owner. | Pages were written separately, so IDs (A-xx, R-xx) did not match across pages and Jira. | Before each review, one person checks that IDs match on all pages and in Jira. | Yaren (Scrum Master) |
| Jira stories have acceptance criteria and traceability; epics and releases are set up. | Some stories were left without an epic or a sprint. | Every story gets an epic and a sprint at sprint planning. | Yeşim (Product Owner) |
| Feedback from the review was applied quickly. | Some pages were read differently from what the instructor expected (for example, what counts as a risk), so they were rewritten after feedback. | Share an early draft of each page and ask for feedback before the review. | Everyone |
| The GitHub–Confluence and Jira sync works. | The sync stopped once because of missing secrets. | Check the sync and the course template updates at the start of every sprint. | Kaan, Gözde Nur |
| The presentation for 21/10 was ready on time. | Many pages changed the night before the presentation, and not everyone saw the changes. | Freeze the pages 2 days before a review; announce changes that affect other pages in the group. | Everyone |

## Hot Air Balloon Retrospective

We also looked at Sprint 1 with the Hot Air Balloon retrospective on our [Miro board](https://miro.com/app/board/uXjVEWMJhwo=/?share_link_id=854607532110): sunny skies are the positive things ahead, hot air is what pushes us along, storm clouds are the problems coming up, and sandbags are what slows us down.

![Sprint 1 Hot Air Balloon Retrospective](hot-air-balloon-retro-sprint-1.png)

*Note added on 26/10/2026:* the storm cloud "Cloud budget or credit not ready (R-05, R-10)" was written before the hosted cloud deployment was removed from the plan on 25/10/2026. R-05 is now closed, and R-10 is now "The system does not install on the pilot computer" (see [Risks](../03-project-canvas/11-risks.md)).

| ☀️ Sunny Skies (positive things ahead) | 🔥 Hot Air (what pushes us along) | ⛈️ Storm Clouds (problems coming up) | 🎒 Sandbags (what slows us down) |
|---|---|---|---|
| M1: Charter v1 approved | One owner per page | Too few pilot users (R-03) | IDs did not match across pages and Jira |
| M2: Evaluation set, sources and first design | Clear constraints for Sprint 1 | Cloud budget or credit not ready (R-05, R-10) | Pages rewritten after feedback |
| Presentation on 21/10 was ready on time | Fast response to feedback | The law or its official reading changes (R-02) | Many changes the night before the presentation |
| | Working GitHub–Confluence and Jira sync | Work falls behind in Sprint 2 (R-08) | |

## Commitments check

| Commitment | Promised in | Fulfilled? | Notes |
|---|---|---|---|
| No production code is written in Sprint 1 | [Assumptions & Constraints](../03-project-canvas/03-assumptions-and-constraints.md), constraint C-07 (course rule) | Yes | Sprint 1 produced only documents, spike notes and the course's sync scripts. |
| Sprint 1 runs from 14/10 to 28/10/2026, as the first of 4 sprints | [Assumptions & Constraints](../03-project-canvas/03-assumptions-and-constraints.md), constraint C-07 (duration) | Yes | Sprint 1 started on 14/10/2026 as planned and ends with the sprint review on 28/10/2026; Sprint 2 starts on 28/10/2026, as in the course calendar updated on 23/10/2026. |
| The project is done by the four team members, with no new members | [Assumptions & Constraints](../03-project-canvas/03-assumptions-and-constraints.md), constraint C-07 (team) | Yes | All four members contributed in Sprint 1. |
| Development runs on Google Colab or the team members' own computers, and the system runs on CPU only; the $100 Google Cloud credit is kept as a reserve | [Assumptions & Constraints](../03-project-canvas/03-assumptions-and-constraints.md), constraints C-05 and C-06 | Yes | The Sprint 1 spikes ran on Google Colab and a team computer; no cloud credit was used. |

## Individual comments

**Yeşim (Product Owner):** I wrote the Deliverables, Project Organization, Major Activities and Release Plan pages, checked the consistency of all charter pages, and prepared the source manifest and the in-scope provision list (D3). As Product Owner, I rewrote the user stories in Jira and, after the course changes of 23/10, rebuilt the backlog as epics, stories and sub-tasks for Sprints 2–4, so that every story has acceptance criteria and traces back to the charter. I also wrote the User Story Map v1, the story requirements pages and the Sprint 1 welcome page. I came into the sprint already knowing Git, Markdown and Python. My learning was mostly about the Product Owner's responsibilities in Scrum, writing user stories with testable acceptance criteria and planning sprints in Jira. I learned the basics of evaluation and the indexing and query phases of RAG through the work, from the charter, the design document and the team's spikes; I will study the RAG lecture slides in the first week of Sprint 2. The main lesson for me is that the charter and Jira describe the same plan: when one changes, the other has to be updated the same day.

**Yaren (Scrum Master):** I wrote the Milestones and Dependencies pages and checked their dates, deliverables and contacts against the other charter pages.  I reviewed the user stories the team had written, wrote new ones with testable acceptance criteria, entered all of them in Jira, and rearranged every story and task so that each one links to a charter page. In this sprint I learned GitHub, Jira and RAG systems: how a team plans and tracks work with them, and how a RAG system finds passages in the documents and uses them to answer. I defined the Definition of Ready and the Definition of Done for Sprint 1, based on the rules the team really used.

**Kaan (Data Scientist):** I wrote the Project Executive Summary page and my learning spike, and I started the System Architecture Design Document v1 (KAN-59). I came into the sprint already knowing Git, Python and React, so my learning was mostly about Scrum, Jira, embeddings and vector search, RAG and evaluation basics. I learned why the evaluation set has to be fixed before experiments, and how each part of our architecture diagram fits into the RAG pipeline.

**Gözde Nur (Data Scientist):** I wrote the Assumptions & Constraints and Risks pages and my learning spike. I learned how assumptions, constraints, dependencies, and risks link to each other, and after the instructor's feedback I learned how the instructor separates a risk from a design task. I rewrote the Risks page based on that feedback. Also, I worked on the development of ELIZA’s NLP pipeline, including RAG implementation, information retrieval, and model selection.

## Lessons Learned

List lessons learned from the retrospective, with special emphasis on actions to be taken to improve, for example: the development environment, the process, or team collaboration.

- **Process:** Ask for feedback on an early draft. Most rework in Sprint 1 came from reading a template rule differently from the instructor.
- **Team collaboration:** Pages depend on each other. A change to one page (for example a risk number) must be announced, and IDs must be checked across all pages before a review.
- **Planning:** Finish and freeze the pages 2 days before a review, so the whole team can read the final version.
- **Development environment:** Check the GitHub–Confluence and Jira sync and the course template updates at every sprint start, so reviewers always see the current pages. Before coding starts in Sprint 2, agree on one Python version and a shared `requirements.txt`, so the code runs the same on Colab and on every laptop.
