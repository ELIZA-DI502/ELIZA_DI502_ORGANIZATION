# DI 502 — Sprint Deliverables

This page lists what your team delivers in each sprint. It replaces the weekly to-do lists for sprint 2 onwards. Changes are announced in class.

- **Deliverables** are assessed at the end of each sprint. Upload them to ODTUClass by the upload deadline, as Markdown files with images attached where needed. Code stays in Git.
- **Halfway checks** are a pace guide for the progress presentation. They are not graded.
- **Informal presentations** are perfectly fine. You can render your own markdown files as pdf presentations, or go over relevant pages.
- **Every week**, show your team's current burndown chart in class.

## Contents

- [Calendar](#calendar)
- [Every sprint (Sprints 2, 3 and 4)](#every-sprint-sprints-2-3-and-4)
  - [In the first week](#in-the-first-week)
  - [Deliverables](#deliverables)
    - [For sprints 3 and 4](#for-sprints-3-and-4)
  - [How the review works](#how-the-review-works)
- [Sprint 1 · Discovery](#sprint-1--discovery)
- [Sprint 2 · Baseline](#sprint-2--baseline)
  - [Deliverables, in addition to every sprint's](#deliverables-in-addition-to-every-sprints)
- [Sprint 3 · Pipeline](#sprint-3--pipeline)
  - [Deliverables, in addition to every sprint's](#deliverables-in-addition-to-every-sprints-1)
- [Sprint 4 · Product](#sprint-4--product)
  - [Deliverables, in addition to every sprint's](#deliverables-in-addition-to-every-sprints-2)
- [Reference](#reference)
  - [Working principles](#working-principles)
  - [Code and Git](#code-and-git)
  - [Repository structure](#repository-structure)
- [Appendix: lessons from last year's reviews](#appendix-lessons-from-last-years-reviews)

## Calendar

All classes are on Wednesdays.

| Sprint | Runs | Upload deadline (23:59) | Reviews | End-of-sprint presentation |
|---|---|---|---|---|
| 1 · Discovery | 14/10 – 28/10 | 27/10 | — | 28/10: charter and user stories |
| 2 · Baseline | 28/10 – 18/11 | 14/11 | 15/11 – 18/11 | 18/11: demo, reviews and rebuttals |
| 3 · Pipeline | 18/11 – 09/12 | 05/12 | 06/12 – 09/12 | 09/12: demo, reviews and rebuttals |
| 4 · Product | 09/12 – 30/12 | 30/12 | 30/12 (live) | 30/12: final product demo |

Teams who started early ran Sprint 1 from 07/10 to 21/10 and uploaded by 20/10. 

Final exam: 06/01/2027.

---

## Every sprint (Sprints 2, 3 and 4)

### In the first week

These are the minimum for your Definition of Ready; add your own items.

- [ ] Actions agreed on in the last sprint's retrospective have been carried out by the respective owners.
- [ ] From Sprint 3 on: every item from the last review is answered, and the accepted ones are addressed.
- [ ] The team has agreed on the Definition of Ready and Done checklists, and on a one-sentence sprint goal.
- [ ] Every relevant task and user story is moved to the current sprint, and each task has a story point estimate and an owner.

### Deliverables

Sprint pages go in the sprint folder: `Markdown Template/05-sprint-2/`, then `07-sprint-3/` and `08-sprint-4/`.

- [ ] **Welcome page** (`README.md` in the sprint folder): the sprint goal, what you achieved, links to the other deliverables, and the Git commit you submit.
- [ ] **Definition of Ready and Done** (`03-definition-of-ready-definition-of-done.md`).
- [ ] **Burndown chart** for the whole sprint, from Jira (`04-burndown-chart.md`).
- [ ] **Retrospective** (sprint folder): every "what went bad" row has an action and an owner.
- [ ] **Last sprint's review page**, if applicable (sprint folder): your answer to every item (accepted, accepted with rework, or rejected with a reason) and, for every accepted item, a link to its fix in the correction explanation.
- [ ] **Technical summary** (`01-review-committee-technical-summary.md` in the sprint folder), and one experiment card for each experiment run this sprint, in `Markdown Template/12-experiment-cards/`.
- [ ] **Design document** (`11-system-architecture-design-document.md`): a record for every decision taken this sprint, and the diagram and RAG parameters as the system is now.
- [ ] **Spike notes** (`docs/spikes/`), one per spike.
- [ ] **SBOM** (`10-software-bill-of-materials.md`): every model you tried, with its exact version, provider, licence, who accessed it and when, how you call it (API or local), whether you use it and why, and its experiment card. Also list tools and services that are not in `requirements.txt`.
- [ ] **Jira backlog export** (`docs/backlog/`): Markdown with the [Jira sync](../docs/JIRA_SYNC_SETUP.md), or `.xlsx` if the sync does not work.
- [ ] **Demo** in class at the end-of-sprint presentation, 10 minutes or less.

#### For sprints 3 and 4

- [ ] **Repository**, assessed at the end of the sprint against the [Code and Git](#code-and-git) rules.

### How the review works

**What to review:** the deliverables of that sprint, starting from the team's welcome page. From Sprint 3 on, also use the links in the correction explanations on their last review page to check that the items they accepted were fixed. Split the deliverables among your members so that everyone reviews something, and have one member install and run the system from its `README.md`.

1. During the review period, another team reviews your work on Confluence. They fill in your review page and may comment on your other pages, but they do not edit them. You review your assigned team the same way.
2. At the end-of-sprint presentation, the reviewers present their main points, and your team answers each one.
3. Afterwards, copy the completed review page, with your answers, into your sprint folder. It goes in your next upload. Before that upload, add a link to the fix in the correction explanation of every accepted item.
4. For the final sprint the reviews will be done in-class where everyone will comment on each project individually.

All members of all teams attend. Reviewer pairings are announced in class.

---

## Sprint 1 · Discovery

**Goal:** Know *what* you will build and *why*, and prepare everything needed to measure it. No production code is expected yet.

### Week 2 — 07/10 · Start of Sprint 1 (early)

**Deliverables**
* Project Executive Summary
* Mini presentations of project topics (10 min per team)

**Milestones**
* Open a Github repository and invite your peers. Clone this git repository inside. Please note that only the Project Executive summary has been manually checked and updated. Other pages will be updated by October 8th.

If you are not familiar with Git and GitHub, such as using issues, pull requests, reviewing changes etc. please follow Datacamp guides on Intermediate Git and Advanced Git.


### Week 3 — 14/10 · Start of Sprint 1
> [!IMPORTANT]
> **Sprint goal** Know *what* you will build and *why*, and prepare everything needed to measure it. No production code is expected in this sprint.

**Deliverables**

- [ ] [Project Canvas](Markdown%20Template/README.md) : Scope, Milestones, Assumptions & Constraints, Deliverables and Project Organization
- [ ] User stories in Jira (you may plan them in Miro first, but this is optional)
- [ ] Learning spike notes in `docs/spikes/`

**Your tasks**

- [ ] Check the *Sprint 1 fundamentals* table in [Online Course Register](online-course-register/README.md/#sprint-1-fundementals) individually and plan how to close your gaps. Git and Jira courses are important for this week but plan ahead as well.
- [ ] Create your team repository from the course template (Use this template) and your Jira project.
- [ ] Revise your topic and scope based on the feedback from Week 2.
- [ ] Assign the Scrum roles, including the Product Owner for Sprint 1.
- [ ] Choose your document sources and check their terms of use and licences.

**Presentation (10 minutes):** Each team presents, repository, charter draft and Jira setup, the Scrum roles, the revised topic and scope, and the document sources.

---

### Week 4 — 21/10 · Middle of Sprint 1 (Early end of Sprint 1)

- [ ] [Project Canvas](Markdown%20Template/README.md): Major Activities, Dependencies, Facilities and Resources, Release Plan, Risks, as well as the cover page (README.md)
- [ ] Updated user stories in Jira
- [ ] Initial system architecture diagram and design document (v1)
- [ ] Learning spike notes in `docs/spikes/`
- [ ] [Sprint 1 Retrospective](Markdown%20Template/04-sprint-1/02-sprint-1-retrospective.md): for teams who will finish this sprint early.

**Your tasks**

- [ ] Iterate on user stories based on feedback from Week 3.
- [ ] Assign stories/tasks within the scope of sprint 1 to relevant team members.
- [ ] If you haven't done so, invite the reviewer accounts shown [here](README.md/#adding-reviewer-accounts) to your Confluence and Jira pages.
- [ ] For teams who won't present next week, export your jira tasks as markdown files using the updated [Jira sync guide](docs/JIRA_SYNC_SETUP.md), and upload the requested documents in ODTUClass as Sprint 1 Deliverables.

**Presentation (10 minutes):** Each team presents their project charter, updated user stories, architecture design diagram and document, and relevant spikes that lead to those design choices. For teams who will finish the sprint, a look at their sprint retrospectives as well.

### Week 5 — 21/10 · End of Sprint 1

**Your tasks**

- [ ] Finalize your project charter, user epics and their story requirements.
- [ ] Iterate on the first version of your system architecture diagram and design document.
- [ ] Hold a sprint retrospective meeting and fill in the provided table/example [template](Markdown%20Template/04-sprint-1/02-sprint-1-retrospective.md).
- [ ] Decide on the sprint 2 definition of ready and done checklists
- [ ] Export your jira tasks as markdown files using the updated [Jira sync guide](docs/JIRA_SYNC_SETUP.md), and upload the requested documents in ODTUClass as Sprint 1 Deliverables.

---

## Sprint 2 · Baseline

**Goal:** The charter and user stories are finalized. A first baseline retrieves relevant documents to the user queries and its performance has been measured. Go further if your workload allows.

### Deliverables, in addition to every sprint's

- [ ] **Final charter (v2)**, revised after the Sprint 1 feedback.
- [ ] **Final user stories:** story map v2, story requirements for every epic, and a prioritized backlog estimated with planning poker. Take the roles from the ISO/IEC 5339 stakeholder categories.
- [ ] **Test cases for your user stories:** for each story, a short test that checks its success criteria: the input or steps, and the expected result. Put them in the story requirements, next to the story.
- [ ] **Baseline:** the most basic vector database and retrieval over your documents; add a generator only if needed. Its setup should be documented in `README.md`, with pinned `requirements.txt`, parameters in `config/rag.yaml`, and prompts, if any, in `prompts/`. Also record the baseline parameters in its experiment card, because `config/rag.yaml` will change.
- [ ] **Q&A dataset v1** in `docs/eval/eval-set-v1.csv` (question, type, gold source, gold answer), with its data card in [`03-qa-data-report.md`](../Markdown%20Template/11-datasheets/03-qa-data-report.md), following Gebru et al., *Datasheets for Datasets*.
- [ ] **Corpus datasheet:** your document sources' register entry or dataset report, completed.
- [ ] **In the technical summary:** the metrics you chose (for retrieval, if applicable), why, the baseline score and the target from the charter, plus the baseline experiment card.
- [ ] **In the design document:** the RAG pipeline (each stage and its parameters) and your user interface technology (for example Gradio or Streamlit).
- [ ] **A mockup of the user interface**, as an image. It does not have to be connected to the system yet.

### Halfway check (11/11)

- [ ] The Sprint 1 feedback is addressed.
- [ ] The documents are indexed, and retrieval returns passages for a handful of test questions.
- [ ] A first draft of `eval-set-v1.csv` exists.
- [ ] The metrics and their targets are drafted.
- [ ] The user interface technology is chosen.
- [ ] The charter and story revisions are in a pull request.

---

## Sprint 3 · Pipeline

**Goal:** The whole pipeline, user interface included, runs end to end and improves on the Sprint 2 baseline, with every experiment tracked.

### Deliverables, in addition to every sprint's

- [ ] **Full pipeline:** all components, the user interface included, run as one simple pipeline. Instructions of it's use are recorded in the `README.md`. Upload a screenshot of the interface answering a question.
- [ ] **Tracked experiments:** every experiment records the parameter space it tested in its experiment card, and its runs are tracked in W&B. `config/rag.yaml` holds only the product configuration.
- [ ] **In the technical summary:** the best combination from each experiment, compared with the Sprint 2 baseline on the same evaluation set, re-run with n seeds and reported as mean ± std, and the best configuration named.
- [ ] **Test results so far:** run the tests for every story you have built, and report pass or fail in the technical summary.
- [ ] **Q&A dataset v2** in `docs/eval/eval-set-v2.csv`. Keep v1, and say in the data card what changed and why.
- [ ] **Git**, assessed at the end of the sprint: a Jira key in every branch name and commit message, branches merged with `git merge --no-ff`, and the repository structure below. Upload a `.zip` file to ODTUClass. 

### Halfway check (02/12)

- [ ] At least one improvement is measured against the baseline, with a link to its W&B run.
- [ ] The user interface calls the pipeline, even if some parts are still stubs.
- [ ] A draft of the Q&A dataset v2 exists.

---

## Sprint 4 · Product

**Goal:** Assemble the final product, with all the improvements you and your reviewers judged necessary. Prepare a live-demo for the end-of-term presentation.

### Deliverables, in addition to every sprint's

- [ ] **Final test results:** every story's tests are run, and the results are in the technical summary.
- [ ] **In the technical summary:** the test results, and the final system against the baseline and the charter's success criteria.
- [ ] **Final documents:** the data cards, SBOM, design document and `README.md` describe the system you demo.
- [ ] **Git**, assessed at the end of the sprint: a Jira key in every branch name and commit message, branches merged with `git merge --no-ff`, and the repository structure below. Upload a `.zip` file to ODTUClass. 
- [ ] **Final demo** in class on 30/12.

### Halfway check (23/12)

- [ ] The improvements are in, and they are measured.
- [ ] The test cases for your user stories have been run.
- [ ] Everything you plan to demo is in Git.

---

## Reference

### Working principles

- **Everything lives in Git as Markdown**, and documents stay short: one or two pages each. Parameters live in `config/rag.yaml`, and results live in Weights & Biases.
- **Jira is for planning, GitHub is for code.**
- **Decisions are recorded when they are made**, in the design document.
- **Everything that affects an answer is versioned in Git**: code, prompts, configuration and the evaluation set. Python packages are pinned in `requirements.txt`; the SBOM lists models and other external tools.
- **After Sprint 1, the Markdown Template pages change only through pull requests.**

### Code and Git

These rules are assessed at the end of Sprints 3 and 4.

- **Branches:** one branch per Jira task, named with its key, for example `DI3-14-vector-store`. Before merging, a teammate reads the change and runs it. Merge with `git merge --no-ff` so the branch stays visible in the history.
- **Commits:** commit often and not all at once at the end of a sprint. Every commit message and pull request description has the Jira key and explains the change to someone outside the team; AI tools may help write them. Keep debug prints, API keys and large data files out of commits.
- **Code:** follow the repository structure below. Every function has a docstring explaining its inputs, outputs and parameters. Write tests as you build, in `tests/`.
- **Replicability:** anyone should be able to run the system from `README.md` without asking you. It gives the Python version, how to create a virtual environment and install `requirements.txt`, where API keys go, and how to start the system, run the evaluation and the tests. Set random seeds explicitly, and keep the LLM settings (temperature, and a seed if the API supports one) in `config/rag.yaml`.

### Repository structure

```
<team-repo>/
├── README.md               # How to install and run the system
├── .gitignore              # Keeps out secrets (.env), large data and virtual environments
├── requirements.txt        # Pinned dependencies (exact versions)
├── config/
│   └── rag.yaml            # Product configuration: chunking, models, top-k, prompt variant
├── prompts/                # Prompt templates, one file per template
├── data/                   # Raw and processed documents if their licence allows, otherwise a download script
├── src/                    # Code
├── tests/                  # Automated tests, including user story tests
├── Markdown Template/      # Course pages: charter, stories, design document, SBOM, datasheets
│   ├── 05-sprint-2/        # One folder per sprint (07-sprint-3/, 08-sprint-4/)
│   │   ├── README.md                       # Welcome page
│   │   │   ├── 01-review-committee-technical-summary.md  # The technical summary
│   │   │   ├── 02-sprint-2-retrospective.md
│   │   │   └── 03-sprint-2-review-page.md
│   │   ├── 02-sprint-2-retrospective.md
│   │   └── 03-sprint-2-review-page.md
│   └── 12-experiment-cards/  # Every experiment card of the project, one per file
│           ├── E1-baseline.md
│           └── E2-<short-name>.md
└── docs/
    ├── backlog/            # Jira export
    ├── spikes/             # Learning and hypothesis notes
    └── eval/
        └── eval-set-v1.csv # Question, type, gold answer, gold source
```



---

## Appendix: lessons from last year's reviews

These points come from the instructor's feedback on last year's sprints. They are not extra deliverables; use them to check your work before you upload it.

- **Definition of Ready and Done:** decide the lists before the sprint starts, not after.
- **Burndown chart:** the line should fall through the sprint, not drop on the last day. Do not remove stories mid-sprint. Points on subtasks stay hidden until the whole task is done, so put points on stories and tasks.
- **Retrospective:** each "what went bad" action says what the team will do differently next time.
- **Welcome page:** stating the sprint goal was appreciated.
- **Jira:** put documentation work on the board too, and assign tasks at the start of the sprint, not during it.
- **User stories:** story requirements list each story's tasks and success criteria, not only its priority. The story map shows actionable tasks, not qualities such as "fast" or "visually appealing", and can put the sprints on the horizontal axis. Each story says how it serves its role.
- **Q&A dataset:** keep the pairs in a file in Git. Write natural-language questions, not keyword matches. If a model generated them, name the exact model. Show a few example rows and how the source texts were sampled. Cover only documents that are in your retrieval set.
- **Corpus datasheet:** link the archived raw data, the processed data and the processing scripts in Git. If the data already has a card and you do no preprocessing, a short data-quality report is enough.
- **Experiment cards:** compare against something concrete. Runs with the same setup are one experiment. Give the measured numbers, not only the decision, and link public W&B runs. Keep a 0 score separate from a null result, and mark an experiment that a later one supersedes as deprecated. Break failures down by cause.
- **SBOM:** the accesser is the person who downloaded or deployed the model. Bold the models still under consideration. Do not list every subpackage.
