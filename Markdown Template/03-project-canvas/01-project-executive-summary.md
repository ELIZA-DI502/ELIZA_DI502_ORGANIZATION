# Project Executive Summary

This section briefly summarizes the entire project charter, highlighting the significant points of interest to the reader. It includes all of the information required for approval by the key stakeholders. The summary should also include some background information on the project that:

- includes the reason(s) for creating the project (e.g., a business problem or opportunity, a legal requirement, etc.); and,
- the budget, duration and timeline of the project.

While filling in this page, focus on end-users: the people who use the system. Everything from objectives, project scope and the desired features should cater to end-users, not to developers (yourselves).

Write objectives as **outcomes for the people who use the system**, not as work your team will do. Write "By the end of Sprint 4, residents find their next collection day in under 1 minute, compared with about 5 minutes on the current city website" (illustrative numbers), not "Build a RAG chatbot".

In ISO/IEC 5338 terms, this page belongs to the Inception stage [1]. It covers the 6.4.1 Business or mission analysis process and the 6.4.2 Stakeholder needs and requirements definition process [1]. You do not need to write ISO process names or numbers in your charter.

Numbers in examples are illustrative only. Outside sources are cited by number, for example [1]; full references are at the end.

## How to fill in each part

| Part | What it means | When it applies | Question it answers |
|---|---|---|---|
| **Background** | The reason the project exists: a business problem, an opportunity or a legal requirement | Always; it opens the page | Why is this project needed? |
| **Budget, duration and timeline** | The fixed budget, the length of the project and its start and end dates | Always | How much, how long, and from when to when? |
| **Stakeholders** | The key stakeholders who will benefit from the project results, each labelled with its role (see possible roles from ISO 5339) | Always | Who gains from the result, and in which role? |
| **Project vision** | The future state the project creates for its end-users, in one or two sentences; see 2.1 | Once per charter; revise it with the charter | What will be different for end-users when the project is done? |
| **Objectives** | The project's business objectives: an overhead view of what the project aims for, written by the SMART method | Every row of the objectives table | What outcome do we commit to, for whom, by when? |
| **Success criteria** | Concrete, measurable criteria that confirm whether an objective has been met, written in plain language | Every objective, without exception | How will we know the objective is met, and who decides? |
| **Business outcomes** | Results expected at the end of the project | Every objective; expected at the end of the project | What measurable change do the stakeholders get? |
| **Scope definition** | A high-level description of the features and functions of the product, service or result | Written once here. This page is the project proposal, and later scope must not grow beyond it | What will the product do for its users? |

## Background, budget, duration and timeline

1. The background states why the project exists: a business problem, an opportunity or a legal requirement.
2. The budget line states the fixed budget: $100 of Google Cloud credits per project.
3. The duration states the number of sprints, and the timeline states the project's start and end dates.
4. Sprint-by-sprint dates go on the Release Plan page; cost items go on the Cost & Funding page.

## 1. Stakeholders

Identify the key stakeholders who will benefit from the project results. Label each one with its role (see possible roles from ISO 5339 below).

### Possible roles from ISO 5339

ISO/IEC 5339 defines two groups of stakeholders. It also sorts them into "make", "use" and "impact" perspectives [2].

**AI stakeholders**

| Role | Perspective | Who it is (paraphrased) |
|---|---|---|
| **AI producer** | Make | Designs, develops, tests and deploys products or services that use AI systems. Involved in all stages, from inception to retirement. |
| **AI developer** | Make | Builds the AI product or service for the AI producer: model and system design, implementation, verification and validation. Can be an employee, contractor or partner. |
| **Data provider** | Make | Collects and/or prepares the data for the AI model. |
| **AI application provider** | Shares part of the make perspective | Provides the AI system's capabilities as a product or service to internal or external customers. Mainly involved at deployment. |
| **AI partner** | (not assigned to a perspective) | Provides services to the AI producer and AI application provider within a business relationship. |
| **AI customer** | Use | Uses the AI product or service directly, or provides it to AI users. Has a business relationship with the AI application provider. |
| **AI user** | Use | Uses the AI product or service. Needs no business relationship, so a user need not be a customer. |

**Other stakeholders**

| Role | Perspective | Who it is (paraphrased) |
|---|---|---|
| **Community** | Impact | People affected by the application beyond its customers and users, such as consumers, families or neighbours. |
| **Regulators / policy makers** | Impact | Regulators have authority over AI use where the application is deployed. Policy makers set the legal requirements for that use. |

Your own team usually holds the make roles. Describe team roles on the Project Organization page, not here.

### Rules

1. Every stakeholder row names one role (see possible roles from ISO 5339).
2. Every stakeholder row states what that stakeholder gains from the project result, or, for an impact-perspective role such as a regulator, what its interest in the project is.
3. At least one row is an AI user (an end-user). If a different party buys or commissions the system, list it as the AI customer in its own row.
4. One row holds one role. The party who buys the system (AI customer), the party who uses it (AI user) and the party who runs it (AI application provider) are different roles, even when one organization holds two of them [2].
5. The list covers more than one stakeholder type, because narrow stakeholder views can introduce bias [1].
6. If the application affects a community beyond its users, consider listing that community [2].
7. If two stakeholders want conflicting things, the conflict is written down.

### Stakeholder test

Ask these three questions of every row:

1. **Which single 5339 role is this?** If you need two roles, split the row (rule 4).
2. **What do they gain, in one sentence?** If you cannot say it, they may not be a key stakeholder (rule 2).
3. **Does anyone else want the opposite?** If yes, write the conflict below the table (rule 7).

Each right-hand entry fixes only the named defect. 
| Not this | This |
|---|---|
| "Company / application provider: the company that buys the assistant and analyses usage trends." **Defect:** two 5339 roles merged in one row (rule 4). | Row 1: "City waste department, **AI customer**: buys the assistant for its residents." Row 2: "City IT unit, **AI application provider**: runs the assistant and reviews usage trends." |
| "Students: secondary end-user target audience; gain a learning tool." **Defect:** informal group name with no 5339 role (rule 1). | "Students, **AI user**: secondary end-user target audience; gain a learning tool." |

## 2. Project Vision and Objectives

This section describes the project vision and the project objectives, and links each objective to related measurable business outcomes. Measurement criteria must also be provided to confirm that an objective has been reached.

Keep in mind that objectives defined here should be an overhead view. Each objective should have concrete, measurable success criteria to confirm whether the objective has been met. Business outcomes are results expected at the end of the project. Add rows as required.

### 2.1 Project vision

The vision states, in one or two sentences, the future state the project creates for its end-users. The project uses RAG as its basic solution; this is a constraint set by the Project Review Committee, so the vision does not need to argue for it or mention it.

**Questions to ask before you write**
- Which problem should be solved?
- Which value or advantage will be created?
- Who is impacted by the project result?
- Are there conflicts between multiple stakeholders?

**Elements of a vision statement**

| # | Element | What to write |
|---|---|---|
| 1 | Problem or opportunity | The need that triggered the project [1]. |
| 2 | Who benefits, named specifically | The end-users from section 1, named as specific groups. |
| 3 | The change for them, not the artefact | The future state end-users experience, not the system you build. |
| 4 | No implementation detail | No model names, techniques or tools. |
| 5 | No metrics or thresholds | Measurable targets go in the success criteria (2.3). |
| 6 | Short and plain | One or two sentences that a stakeholder can repeat. |
| 7 | Traceable to the objectives | Each objective reads as a step toward the vision. The vision makes no claim the objectives cannot support. |

Check also whether AI-specific risks could block the vision: privacy limits on reusing personal data, data accessibility or data quality [1]. If one could, record it on the Risks page.

Do not confuse the vision with the strategic objective. The vision describes the future for end-users, with no numbers or dates. The strategic objective is row 1 of the objectives table: the broadest objective, written by SMART, with a date and measurable success criteria. Write both.

| Not this | This |
|---|---|
| "Provide an assistant that lets users explore and compare topics; the information will be data-driven, grounded and accurate." **Defect:** describes the artefact, not the change for end-users (element 3). | "Users settle a question about [topic] in one place, without searching several sites; the information will be data-driven, grounded and accurate." |
| "By combining retrieval-augmented generation with fine-tuned domain language models, the assistant will bridge real-time events and formal records." **Defect:** implementation detail (element 4). | "The assistant will bridge real-time events and formal records." |

### 2.2 Objectives

The objectives on this page are business objectives. Write each one by the SMART method: Specific, Measurable, Achievable, Realistic and Time-bound. An objective that fails any one of the five tests is not yet SMART [3].

| Letter | Meaning | Test |
|---|---|---|
| **S**pecific | Says who, what, where, when and why, so that a second reader knows what success looks like [3] | Give it to a classmate. If they must ask what counts as success, it is not specific [3] |
| **M**easurable | Has a quantitative or verifiable indicator. An experience becomes measurable through a proxy such as a rating or survey score [3] | Can you name the number or check that decides it? |
| **A**chievable | Within reach of your team's resources, skills and constraints. Achievable does not mean easy [3] | What must you do, get or change to make it possible? [3] |
| **R**ealistic | The target does not overclaim; "100% correct answers on all questions" is unrealistic | Would a reviewer believe this target for your domain and time frame? |
| **T**ime-bound | Has a deadline, or milestones at set intervals [3] | Is there a date or sprint? |

**Strategic objective and Phase-1 objective.** Row 1 is a broad, outcome-focused strategic objective. A narrower MVP objective follows as the Phase-1 objective. Both have measurable success criteria. A broad objective can stay ambitious while its success criteria stay precise [3].

**Rules for objectives**

1. The objective is an outcome, not an activity: "reduce time-to-answer", not "build a RAG system".
2. The objective has a date or sprint.
3. The objective names its target users and domain.
4. The objective names no model, tool or architecture. RAG is a given constraint, not an objective.
5. The objective serves end-users, not developers.
6. The objective contains no unmeasured adjectives or buzzwords such as "fast", "intuitive" or "real time".
7. One sentence holds one goal [3].
8. No target is unrealistic, such as "100% correct answers".
9. The objective is not a milestone. "Deploy MVP and conduct demo" is a milestone.
10. The objective is not a constraint. "The system will not store any PII" reads like a constraint.
11. Across all rows, the objectives cover quality, performance/cost, adoption/UX, and safety/compliance. Model performance is not always the target.
12. Every objective has matching content in the rest of the charter. For example, a user-satisfaction target needs a milestone and a deliverable for the survey result.

### 2.3 Success criteria

1. Each criterion is a measurable result, not an action. "The system will run on the provided cloud" is not a success criterion.
2. Each criterion has a date or sprint.
3. Each criterion names its measurement method and its acceptance owner [3].
4. Each criterion uses a plain-language measure that a stakeholder understands without technical background, such as the share of answers judged correct or the time needed to find something. It uses no convoluted metric such as Recall@k or RAG-triad scores.
5. Each criterion maps to one or more specific metrics. Technical metrics are defined in the experiment cards and model card; user-facing ones, such as survey scores, are defined in the criterion itself. The Risks page uses these metrics as triggers.
6. The team sets each target level for its own project and states where the level comes from.
7. A criterion that claims an improvement compares against the **baseline**. Here, the baseline is the default state: what users do or get today without the project. It is not a model baseline. Example: today, people find it hard to find restaurants that suit them (default state); with the app, they get more personalized recommendations. To turn this into a criterion, measure both states, for example the share of users who find a restaurant they like within 5 minutes, before and with the app (illustrative). (For other technical documentation the baseline refers to a naive approach such as retrieving the most commonly referred to document all the time. It should require little or no models and the performance should be with respect to this approach.)

### 2.4 Business outcomes

1. Each business outcome is a result expected at the end of the project.
2. Each business outcome is measurable.
3. Each business outcome uses no adjectives in place of numbers.
4. Each business outcome is a change for users or stakeholders. An approval is not a business outcome.
5. Each business outcome is not an activity of the team.

### Objective test

Ask these five questions of every row:

1. **Would your team do this as work?** If yes, it is an activity and belongs under Major Activities.
2. **Could a classmate tell, without asking you, whether it was met?**
3. **How does it move toward the vision, in one sentence?**
4. **Who accepts it, and by which method?**
5. **Where does it appear in Milestones and Deliverables?**

| Not this | This |
|---|---|
| Business outcome: "Building an assistant that answers users' questions using RAG." **Defect:** activity, not outcome (2.4 rule 5). | Business outcome: "Residents answer their own collection questions instead of calling the helpline." |
| Objective: "The system will provide scalability under limited academic resources." **Defect:** serves the developers, not end-users (2.2 rule 5). | Objective: "Residents can still use the assistant on collection-day mornings, when demand peaks." |
| Objective: "Provide an intuitive, responsive and trustworthy entry point for residents." **Defect:** adjectives instead of numbers (2.2 rule 6). | Objective: "Provide an entry point where residents get an answer within 3 seconds and rate it helpful in at least 80% of cases." |
| Success criterion: "Qualitative feedback collected from at least 2 stakeholder groups." **Defect:** an action, not a measurable result (2.3 rule 1). | Success criterion: "At least 70% of pilot residents rate the answers as clear in the feedback survey." |
| Success criterion: "At least 70% accuracy." **Defect:** no date and no measurement method (2.3 rules 2–3). | Success criterion: "By the end of Sprint 4, at least 70% accuracy, judged by the department's reviewer on a fixed set of 100 test questions." |
| Success criterion: "Faithfulness ≥ 0.75, relevance ≥ 0.80, grounding ≥ 0.80." **Defect:** convoluted metric names (2.3 rule 4). | Success criterion: "At least 75% of answers are supported by the sources they cite." |
| Business outcome: "Residents receive accurate, timely information from several sources without switching platforms." **Defect:** not measurable (2.4 rule 2). | Business outcome: "Residents use one source instead of three; average lookup time falls from about 5 minutes (default state, measured in Sprint 1) to under 1 minute." |
| Objective: "Deploy MVP and conduct demo." Business outcome: "Academic validation and project approval." **Defect:** a milestone, and an approval instead of an outcome (2.2 rule 9; 2.4 rule 4). | Objective: "By [date], validate problem–solution fit with an MVP assistant that delivers sourced, accurate answers and measurable time savings for [target users]". |

### If you are stuck

Use one of these patterns:

- **Template sentence:** "(By [date]), [verb] [outcome] for [target users] in [scope] to achieve [business value]."
- **Strategic plus Phase-1:** one broad objective for the whole project, then one narrower MVP objective; both with measurable success criteria.
- **From–to:** state today's value and the target, for example "raise X from 78% to 85% by [date]" [3]. Today's value is the default state.
- **Proxy measure:** make an experience measurable through a rating or survey score [3].
- **One row per family:** write one objective each for quality, performance/cost, adoption/UX and safety/compliance.

## 3. Project Scope

### 3.1. Scope Definition

Provide a high-level description of the features and functions that characterize the product, service or result to be delivered by the project. This page is the project proposal: do not grow the scope beyond it later.

Project scope sets the boundaries of a project: what is included and what is excluded [4]. Start from the goals, because every scope item should serve one [4]. A clear scope helps you spot scope creep, meaning features that were never part of the plan [4].

**Rules**

1. Each feature is described by what the user can do with it.
2. Each feature serves at least one objective.
3. No feature description names models, retrieval techniques, frameworks or architecture. The System Architecture Diagram page covers those.
4. No feature description uses unmeasured adjectives such as "simple", "easy to use" or "real time".
5. Excluded work is not described here. Mark it Out of Scope under Major Activities. Clear exclusions keep the team on the agreed objectives [4].

**Scope test** [4]**:** for each feature, name the objective row it serves. If you cannot, the feature is scope creep: drop it, or mark it Out of Scope under Major Activities.

Each right-hand entry fixes only the named defect, so it may still need other fixes.

| Not this | This |
|---|---|
| "The retriever uses vector similarity search to match queries to the most relevant text segments." **Defect:** implementation detail (rule 3). | "Residents ask a question in their own words and get the matching rule from the official collection guide." |
| "A simple, easy-to-use interface that gives responses in real time." **Defect:** unmeasured adjectives (rule 4). | "An interface where residents type a question and see the answer within 3 seconds." |

## What does not belong in this section

| Item | Where it belongs |
|---|---|
| Sprint-by-sprint start and end dates | Release Plan |
| Cost items and source of funding | Cost & Funding |
| Milestones, such as "deploy MVP and conduct demo" | Milestones |
| Deliverables and their approving stakeholders | Deliverables |
| RAG as the solution approach | Assumptions & Constraints, as a constraint set by the Project Review Committee |
| Other constraint-like statements: no PII, licensing, English only, input boundaries | Assumptions & Constraints |
| Activities, and features you will not deliver | Major Activities, marked In Scope or Out of Scope |
| Team members' roles and responsibilities | Project Organization |
| The risk that an objective is not met | Risks |
| Model names, architecture, retrieval design | System Architecture Diagram |
| Specific metrics behind each success criterion, such as Recall@k or RAG-triad scores | Experiment cards and model card |
| Product backlog | Not on this page |

## Fill-in tables

### Background

The EU AI Act (Regulation (EU) 2024/1689) sets requirements for AI systems within its scope and can apply to providers outside the EU that place AI systems on the EU market (Article 2). It lists four uses in education and vocational training in Annex III, point 3: admission, assessment of learning outcomes, level placement and exam monitoring; whether such a system is high-risk also depends on the conditions in Article 6. Technical teams building these systems have to work out which provisions apply to their use case, but today they either read a 151-page consolidated text that has already been amended (by Regulation (EU) 2026/1744), or wait for a legal review. This project lets them find the relevant provisions in less time than a manual search, understand them in plain language and check them against the official text before the legal review starts.

**Budget:** $100 of Google Cloud credits (course allocation; the system is built and run on the team's own computers and Google Colab, so the credit is kept as a reserve).\
**Duration:** 4 sprints.\
**Timeline:** 14/10/2026 to 30/12/2026.

### 1. Stakeholders

| # | Stakeholder | Role (see possible roles from ISO 5339) | Perspective (make / use / impact) | Relationship to project | Benefit from project |
| - | ----------- | --------------------------------------- | --------------------------------- | ----------------------- | -------------------- |
| 1 | Technical teams at EdTech providers: developers, ML engineers and technical leads building AI systems for education | AI user | Use | Ask which AI Act provisions relate to the education product they are building | Find the rules that relate to their product, what they require and from when, in one place and with the source |
| 2 | Legal and compliance team of an EdTech provider (representative scenario; in DI 502 the course instructors and peer groups review the project's outputs as academic proxies for this stakeholder; they do not act as legal experts) | AI customer | Use | Would adopt the assistant for the company's technical teams and receives their questions in legal reviews | Developers come to legal reviews already knowing the relevant articles, so reviews start from the right provisions |
| 3 | EUR-Lex (Publications Office of the European Union) | Data provider | Make | Publishes the official consolidated text of Regulation (EU) 2024/1689 that the assistant uses | Interest: its official text is reused with attribution and the correct version date (Commission Decision 2011/833/EU) |
| 4 | European Commission AI Office and national market surveillance authorities | Regulators / policy makers | Impact | Enforce Regulation (EU) 2024/1689 and supervise high-risk AI systems in education | Interest: the law is reproduced correctly, and users are not misled into treating answers as legal decisions |
| 5 | Students and teachers who use the EdTech provider's AI-based products | Community | Impact | Are admitted, assessed, placed or monitored by the education products these teams build | Interest: the teams building these products know which obligations apply to them |

Conflicts between stakeholders (if any):

| Developers (AI user) want | Legal team (AI customer) wants | How the project resolves it |
| ------------------------- | ------------------------------ | --------------------------- |
| A yes-or-no answer: "Is our product high-risk?" | No legal decisions made by an automated assistant | The assistant shows the relevant articles and conditions but never gives a classification or compliance verdict |
| An answer they can read in under a minute | All conditions and exceptions, e.g. Article 6(3) | A summary of at most three sentences first, then the conditions and exceptions |
| Plain language | The official wording of the law | A plain-language explanation together with the exact Article/Annex reference and the wording of the official text |

### 2. Project Vision

Teams building AI systems for education can find which EU AI Act rules relate to their system, what those rules require and from when, in one place and always with the official source. Legal reviews then start from the right provisions instead of from a 151-page regulation.

### 2. Objectives

In each Success Criteria cell, write for every criterion: the plain-language target with where the level comes from, the measurement method, the acceptance owner, the date or sprint, and the specific metric(s) it maps to.

| # | Objectives | Success Criteria | Business Outcomes |
| - | ---------- | ---------------- | ----------------- |
| 1 (strategic) · O1 Search time | By the end of Sprint 4, reduce the time technical teams building AI systems for education need to find the AI Act provisions that relate to their use case, compared with searching the official consolidated text themselves. | In the pilot, the median time to find the relevant provision for a scenario task is at least 20% shorter with the assistant than with manual search in the EUR-Lex consolidated text (default state, measured on the same users in the same pilot), and the correct provision is found in at least as many tasks. **Target level**: team target. With at least 5 users and 4 tasks each (D10), each condition has about 10 tasks, so a smaller difference could come from variation between users; the assistant's answer time, first measured in Sprint 1 (D4), must leave room for this gain (A-07, R-13). Reviewed once in Project Charter v2 (D7, end of Sprint 2), any change recorded with its reason, and fixed before the final evaluation. **Method**: timed search task with at least 5 pilot users (technical professionals acting as proxy EdTech developers); each user solves half of the tasks manually and half with the assistant, with the task sets swapped between users (D10 Pilot Evaluation Report). **Owner**: Product Owner. **Date**: end of Sprint 4. **Maps to**: median task completion time and task success rate in the pilot. | Developers arrive at a legal review already knowing the relevant articles, sooner: in the pilot, users name the correct Article/Annex in at least as many scenario tasks with the assistant as with manual search, in less time (default state, same users). |
| 2 (Phase-1 MVP) · O2 Evidence | By the end of Sprint 3, validate that an MVP assistant answers in-scope education questions from EdTech provider teams with evidence from the project's designated source version (27 July 2026 consolidated text). | On the fixed evaluation set: (a) the expected provision is among the cited sources for at least 80% of in-scope questions; (b) at least 75% of in-scope answers are judged fully supported by the passages they cite (every in-scope answer in the evaluated split is reviewed by one reviewer, and a second reviewer checks a sample); (c) 100% of substantive answers cite at least one Article/Annex with the version date; (d) at most one application-date question in the evaluated split (at least 3 such questions in each split of D8) gets a date that is not from the designated source version (for example from the original 2024 text). The same questions are also answered without access to the regulation text (measured with the Sprint 2 baseline, D6), and the difference is reported in the experiment cards; it is an analysis result, not a pass level, until a level is set from the baseline results in Project Charter v2 (D7). **Target level**: (a) follows the course's example acceptance criterion of 80% correctly cited provisions; (b) is set lower because an answer can add unsupported details even when the right provision is found; (c) is a fixed format rule, enforced in the answer template and checked on every answer; (d) is written as a count because there are only a few date questions in each split, where a percentage would move in large steps. The levels are confirmed with the Project Review Committee's feedback in Project Charter v2 (D7, A-06). **Method**: evaluation-set review against the expected evidence: one reviewer reviews every in-scope answer, and a second reviewer checks a sample; the evaluation set contains team-written questions and questions taken or adapted from published work on the EU AI Act, each with its origin recorded (D2, D8); validation (`val`) questions in the beta (D9), held-out `test` questions in the release candidate (D11). **Owner**: evaluation reviewers (team members acting for the AI customer; disagreements in the checked sample are resolved against the written evaluation rubric; if they remain, a third team member reviews the answer and the decision is logged). **Date**: end of Sprint 3 (`val` questions); confirmed on the held-out `test` questions by the end of Sprint 4. **Maps to**: expected-provision hit rate, answer support by cited text and citation coverage in the experiment cards. | In the pilot, users accept the cited provision without having to search the regulation for a different one in at least 70% of scenario tasks (pilot task log: the observer records whether the user opens or searches for another provision before giving an answer; this is an observation of user behaviour, not a check of legal correctness, D10). |
| 3 · O3 Understanding | By the end of Sprint 4, technical teams in the pilot understand the assistant's answers and can use them for their own education use case. | At least 70% of pilot users (at least 4 of 5 when there are 5 users) rate the answers 4 or 5 out of 5 for understandability. **Target level**: team target; with 5–8 pilot users each user is 12–20% of the result, so the level is read in whole users. Reviewed together with the O1 level in Project Charter v2 (D7). **Method**: post-task survey on a 5-point scale after the timed search task (D10 Pilot Evaluation Report). **Owner**: Product Owner. **Date**: end of Sprint 4. **Maps to**: survey scores. | At least 60% of pilot users say they would use the assistant as their first step before asking their legal team (post-task survey). |
| 4 · O4 Safety | By the end of Sprint 4, users who ask for a legal decision, ask something the assistant cannot answer from the in-scope provisions, or ask for help with evading the law get a notice instead of a verdict, an unsupported answer or harmful help. | On the safety questions of the evaluation set, in four categories (out-of-scope, insufficient-evidence, legal-decision and adversarial): at least 11 in D2 with at least 1 of each category in the held-out test questions, and at least 16 in D8 with at least 2 of each category in both the `val` and the held-out `test` questions: (a) 0 answers to the evaluated questions contain a classification or compliance verdict, checked on every answer (C-08); (b) 100% of legal-decision questions receive the expected response: the assistant declines the verdict and points to the relevant provisions; (c) at least 80% of the questions in each of the other three categories receive the expected response: it states that the question is out of scope, says that evidence is missing, or refuses an inappropriate request with a one-sentence reason. **Target level**: (a) and (b) follow the course's example acceptance criterion of 100% correct refusal and the hard limit in C-08; (c) is set at 80% because out-of-scope, missing-evidence and adversarial questions include borderline cases. The result holds for this test set and is not a general safety guarantee. **Method**: scripted evaluation-set review; `val` questions in the beta (D9), held-out `test` questions in the release candidate (D11). **Owner**: evaluation reviewers. **Date**: end of Sprint 4. **Maps to**: number of verdicts and expected-response rate per safety category in the experiment cards. | At least 80% of pilot users correctly answer that the assistant does not give legal decisions (post-task survey). |

Objectives 1–4 cover performance, quality, adoption/UX and safety in turn.

### 3.1. Scope Definition

An information assistant on the EU AI Act for provider-side technical teams in EdTech, used through a web page. Its knowledge is limited to the provisions that decide whether and how an education AI system is regulated, taken from the project's designated source version (consolidated text of 27 July 2026): the education use cases in Annex III point 3 (admission, assessment, level placement and exam monitoring), the high-risk classification rules and their exceptions (Article 6), the requirements for high-risk systems (Articles 8–15), the provider obligations (Article 16), the application dates (Article 113), the scope and definitions of the Act (Articles 2 and 3), and two boundary cases: emotion inference in education (Article 5(1)(f)) and telling users that they are interacting with an AI system (Article 50(1)). The assistant identifies and explains these provisions; it gives no legal advice, compliance verdict or implementation guidance. Questions about other parts of the Act receive an out-of-scope notice.

Provision priority: **core**: Annex III point 3, Article 6(2)–(3), Articles 8–15 (identify and explain the requirements, no implementation guidance), Article 16 (limited to identifying provider obligations) and Article 113; **supporting**: Article 2 (scope) and Article 3 (selected definitions); **boundary**: Article 5(1)(f) and Article 50(1) (explained with their conditions); **if time (not committed)**: Articles 4 and 4a of the same text. Commission guidelines and other documents are not added to the knowledge base (single source). The provision list in D3 records these provisions; the D2 questions test that in-scope questions can be answered from them and show any gap, which is added only within the scope above.

| # | Feature | What the user can do with it | Objective(s) it serves |
| - | ------- | ---------------------------- | ---------------------- |
| 1 | Ask in their own words | Describe their use case and ask their question in their own words | 1, 3 |
| 2 | Find the relevant provisions | See which of the in-scope provisions (education use cases, high-risk classification and its exceptions, requirements and provider obligations, the prohibition of emotion inference in education, AI-interaction disclosure and application dates) relate to their use case, with the exact Article/Annex reference and the version date of the text | 1, 2 |
| 3 | Plain-language answer | Read a summary first, then the conditions and exceptions, explained in plain language and based only on the provisions found | 2, 3 |
| 4 | Boundary notices | Get a notice when evidence is missing, when the question is out of scope, or when they ask for a legal decision; requests for help with evading the law, hiding decisions or building a prohibited practice are refused with a one-sentence reason and a pointer to the relevant provision | 4 |
| 5 | Guided start | Start from example questions, at least one for each of the four education use cases in Annex III point 3, and optionally pick their use case (admission, assessment, level placement, exam monitoring) from a list, without knowing legal terms | 1, 3 |
| 6 | Check the source | Open the wording of each cited provision under the answer, exactly as it stands in the consolidated text of 27 July 2026, with a link to the source on EUR-Lex | 2 |
| 7 | Follow-up questions | Ask a follow-up question in the same session (e.g. "What about human oversight?") without describing their system again; nothing is kept after the session ends | 1, 3 |

The alpha (Sprint 2) is the baseline: it retrieves the in-scope provisions and shows them with their Article/Annex reference and the version date (the first part of Feature 2). Features 1–4 form the MVP and are completed in the beta (Sprint 3); Feature 6 and the application-date answers of Feature 2 are added in the release candidate (Sprint 4). Features 5 and 7 are not committed: they stay in the backlog and are built only if time allows. A feature that has to be deferred is recorded with its reason and the Product Owner's agreement (see Deliverables, D9).

## Example (illustrative only)

Every name, number, date and target below is invented. None is a real project fact.

**Background.** City residents find waste-collection rules in three places: a PDF calendar, the city website and a telephone helpline. Residents miss collections, and the helpline receives many repeated questions.

**Budget:** $100 of Google Cloud credits (fixed, per project). **Duration:** 4 sprints. **Timeline:** 14/10/2026 - 30/12/2026

**1. Stakeholders**

| # | Stakeholder | Role (ISO 5339) | Perspective | Relationship to project | Benefit from project |
|---|---|---|---|---|---|
| 1 | City residents | AI user | Use | Ask questions about sorting and collection days | Correct answers in one place |
| 2 | City waste department | AI customer | Use | Commissions the assistant for residents | Fewer repeated helpline calls |
| 3 | City IT unit | AI application provider | Make (shared) | Runs the assistant after deployment | Sees which questions residents ask most |
| 4 | Collection contractor | Data provider | Make | Supplies the collection schedules | Fewer missed-collection complaints |
| 5 | Neighbours of missed bins | Community | Impact | Affected when bins are left out | Cleaner streets |

Conflicts: the department wants fewer helpline calls, but residents without internet access still need the helpline. The helpline stays. Replacing it will fall out of scope. (see Out of Scope under Major Activities).

**2. Project Vision.** Every resident can find out, in one place and in their own words, what goes in which bin and when it is collected, so fewer collections are missed.

**Objectives**

| # | Objectives | Success Criteria | Business Outcomes |
|---|---|---|---|
| 1 (strategic) | By the end of Sprint 4, reduce the time residents need to answer a waste-collection question, compared with the current website and helpline. | Median time to answer a test question falls from 5 minutes (default state, measured on the current website in Sprint 1) to under 1 minute. Method: timed usability test with 10 residents. Owner: Product Owner. End of Sprint 4. Maps to: task completion time in the usability test, supported by end-to-end response time and answer correctness. | During the pilot, residents in the test group make 20% fewer helpline calls about collection days than before the pilot. |
| 2 (Phase-1 MVP) | By the end of Sprint 3, validate that an MVP assistant gives correct, source-backed answers to common collection questions for residents. | At least 80% of answers judged correct on a fixed set of 100 test questions; at least 90% of answers link to the official source page (levels set from the team's own research). Method: review by the department. Owner: department reviewer. End of Sprint 3. Maps to: answer correctness, retrieval quality and citation metrics in the experiment cards. | Residents need no second source for 9 of 10 questions, measured in the pilot survey. |
| 3 | By the end of Sprint 4, residents in the pilot prefer the assistant to the current website for collection questions. | At least 70% of 20 pilot residents say they would use it again. Method: post-test survey. Owner: Product Owner. End of Sprint 4. Maps to: survey score. | At least half of pilot residents report using the assistant as their first source for collection questions in the follow-up survey. |
| 4 | By the end of Sprint 4, residents are not misled when they ask questions the assistant cannot answer. | The assistant declines and points to the helpline in at least 95% of 30 out-of-domain test questions. Method: scripted test set reviewed by the department. Owner: department reviewer. End of Sprint 4. Maps to: refusal rate on out-of-domain questions. | No pilot resident reports wrong advice. |

Objectives 1–4 cover performance, quality, adoption/UX and safety in turn.

**3.1. Scope Definition.** A question-answering assistant for the city's waste-collection rules, used by residents through a web page.

| # | Feature | What the user can do with it | Objective(s) it serves |
|---|---|---|---|
| 1 | Plain-language questions | Ask about sorting or collection in their own words and get an answer | 1, 2 |
| 2 | Source link | Open the official page each answer comes from | 2 |
| 3 | Collection day by street | Enter a street name and see the next collection day | 1 |
| 4 | Out-of-domain handling | Get a pointer to the helpline when the assistant cannot answer | 4 |

## Checklist before submitting

**Whole page**
- [x] The background gives the reason for the project, the budget ($100 of Google Cloud credits), the number of sprints, and the start and end dates
- [x] Nowhere on the page names a model, tool or technique, or uses an unmeasured adjective

**Stakeholders**
- [x] Each row has one ISO 5339 role and says what the stakeholder gains (or its interest, for impact roles)
- [x] At least one row is an AI user, and any conflict between stakeholders is written down

**Vision**
- [x] One or two sentences describe the change for end-users, with no metrics

**Objectives**
- [x] Row 1 is the strategic objective, and row 2 is the Phase-1 MVP objective
- [x] Each objective passes all five SMART tests, is an outcome for end-users, and is not a milestone or a constraint
- [x] Each objective is a step toward the vision and has a matching milestone and deliverable
- [x] Together, the objectives cover quality, performance/cost, adoption/UX and safety/compliance

**Success criteria and business outcomes**
- [x] Each success criterion is a measurable result in plain language, with a date or sprint, a method, an owner, the metric it maps to, and where its target level comes from
- [x] Each improvement claim compares against the default state
- [x] Each business outcome is a measurable change for users or stakeholders, not an approval or an activity

**Scope**
- [x] Each feature says what the user can do and which objective it serves

## References

[1] ISO/IEC JTC 1/SC 42, *ISO/IEC 5338:2023 Information technology — Artificial intelligence — AI system life cycle processes*, 1st ed. Geneva, Switzerland: International Organization for Standardization and International Electrotechnical Commission, Dec. 2023. UK implementation: BS ISO/IEC 5338:2023, London, UK: BSI Standards Limited, 2024.

[2] ISO/IEC JTC 1/SC 42, *ISO/IEC 5339:2024 Information technology — Artificial intelligence — Guidance for AI applications*, 1st ed. Geneva, Switzerland: International Organization for Standardization and International Electrotechnical Commission, Jan. 2024. UK implementation: BS ISO/IEC 5339:2024, London, UK: BSI Standards Limited, 2024.

[3] Swiss Education Group, "What Are SMART Goals? Components, Examples, and Benefits," HIM Business School, n.d. [Online]. Available: https://www.him-business-school.com/en/news/smart-goals/ (accessed Oct. 1, 2026).

[4] F. Grace, "How to define and create a project scope in 5 simple steps," Atlassian, n.d. [Online]. Available: https://www.atlassian.com/work-management/project-management/project-scope (accessed Oct. 1, 2026).
