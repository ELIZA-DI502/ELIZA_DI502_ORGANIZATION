# Risks

Record here the strategic risks identified at the start of the project. Write each risk as an **event** that could happen, not as a general worry: "Recall@5 on the evaluation set stays below 0.60 at the end of Sprint 3", not "the model fails".

## Risks, assumptions and constraints

A risk is an uncertain event that would hurt the project if it happens. It is connected to two other entries in the charter:

- **Every assumption has a risk on its flip side.** Each assumption in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md) has an ID (A-01, …) and names its linked risk. Register that risk here, give it an ID (R-01, …), and write the assumption's ID in **Linked to**. The IDs must point both ways. Example: the assumption "the dataset covers the in-scope categories" has the risk "the dataset under-represents some categories, leading to poor performance on them".
- **The uncertain part of a constraint is a risk.** A constraint in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md) is a fixed limit, but complying with it can fail. The in-scope activity in [Major Activities](03-project-canvas_v2/04-major-activities.md) that enforces the constraint is the risk's mitigation. Example: the constraint "no PII is stored" has the risk "users submit PII in free-text queries, and it ends up in logs or the retrieval index"; PII masking is the mitigation.

A risk can also come from a dependency in [Dependencies](03-project-canvas_v2/06-dependencies.md), for example an external API that changes or becomes unavailable. Write the dependency's row number in **Linked to**.

## How to fill in each risk

Each risk has three parts that act at different times. Keep them separate.

| Field | When it acts | Question it answers |
|---|---|---|
| **Mitigation** | **Before** the risk happens | How do I lower its probability or impact? |
| **Contingency plan (B plan)** | **After** the risk happens | If it happens anyway, what will I do? |
| **Probability / Impact** | The situation **after** mitigation | Given the mitigation, how likely is it and how bad would it be? |

**Probability is residual probability:** what remains after the mitigation is applied. Do not write "we will try several models, so probability is 1". The mitigation is already counted. If your mitigation really brings the probability down to 1, the item is not a risk.

### Probability (1–5)

| Value | Meaning |
|---|---|
| 1 | Very low (&lt;10%): rare in the literature, no sign in pilot tests |
| 2 | Low (10–30%): possible, but only under special conditions |
| 3 | Medium (30–50%): seen in about half of similar projects |
| 4 | High (50–75%): typical in this area; it would be a surprise if it did not happen |
| 5 | Very high (>75%): almost certain. If it is basically going to happen, treat it as a constraint in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md). If some uncertainty remains, keep it as an assumption in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md) and link this risk to it |

Every probability value needs a **basis**, written next to it: a pilot measurement, the literature, a data profile (e.g., the class or category distribution), a third-party dependency, or team experience. "3, because it feels medium" cannot be defended. "3, because the pilot retrieval test gave Recall@5 = 0.52" can.

### Impact (1–5)

Rate impact by the **worst** of the three columns:

| Value | Schedule | Budget (incl. cloud credits) | Target / Scope |
|---|---|---|---|
| 1 | &lt;2 weeks | &lt;2% | Not noticeable |
| 2 | 2–4 weeks | 2–5% | A secondary metric is affected |
| 3 | 1–2 months | 5–10% | A technical requirement is partly unmet |
| 4 | 2–4 months | 10–20% | An acceptance criterion is not met |
| 5 | >4 months | >20% | The output is unacceptable; the objective is not achieved |

**A risk that threatens an acceptance criterion or success criterion has an impact of at least 4.**

### Risk score and what each band requires

**Risk score = Probability × Impact** (1–25).

| Score | Band | Required |
|---|---|---|
| 1–4 | Low | Monitoring is enough |
| 5–9 | Medium | Define a mitigation |
| 10–14 | High | Mitigation **and** trigger **and** contingency plan **and** named owner are all required |
| 15–25 | Critical | Review the project design. Also explain below the table when the risk will be re-evaluated and which early measurement will test it |

A healthy table has a few high risks, mostly medium ones and a few low ones. If every row is 1–2, it reads as "no risk analysis was done". If every row is 4–5, the project looks infeasible.

### Contingency plan: three-question test

Ask these three questions of every contingency plan:

1. **Would I have done this anyway?** If yes, it belongs in the Major Activities, not here. "Try different models", "tune hyperparameters" and "keep testing and optimizing" are not contingency plans.
2. **What is the trigger?** A contingency plan needs a **numeric threshold** and a **date or sprint**. Write "If groundedness on the evaluation set is &lt; 0.70 at the end of Sprint 4, …", not "If performance stays low, …".
3. **Who is the owner?** Name the person who decides to narrow the scope, switch the model or renegotiate the target with the AI customer. "The project team" is not an owner. Every member manages the project in some capacity, so an owner is always a named person, together with the role they hold in [Project Organization](03-project-canvas_v2/08-project-organization.md).

| Not a contingency plan | Contingency plan |
|---|---|
| "Different models will be compared." | "If the target is not met, the system is released only for the categories that meet it; the rest stay manual." |
| "Expert validation will be done." | "If label agreement is κ < 0.70, those classes are excluded from the evaluation and the AI customer is informed in writing." |
| "Hyperparameter optimization will be done." | "If GPU memory is not enough, a 4-bit quantized model is used and the latency target is renegotiated." |

If you are stuck, use one of these four patterns:

- **Narrow the scope:** release on the subset that meets the target and leave the rest manual.
- **Degrade gracefully:** give a narrower output instead of the full one (e.g., retrieved passages and a structured summary instead of a generated answer).
- **Hand over to a human (human-in-the-loop):** below a confidence threshold, the system stops producing output and routes the case to a person.
- **Renegotiate the target:** document what cannot be measured and revise the scope with the AI customer.

## Where risks come from

Do not write only "the model may not work". Write **at least one risk from each of the five layers**. A table with only technical risks is incomplete. The same five layers are used as the constraint categories in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md).

| Layer | Typical risks |
|---|---|
| **Data** | Label noise, class imbalance, delayed data access, distribution shift (data drift, concept drift) |
| **Model** | Target metric not met, collapse on rare classes, uncalibrated confidence scores, bias |
| **Infrastructure** | Not enough GPU or memory, latency target not met, failure to scale, fluctuation or loss of assigned resources |
| **Integration** | An external API changes, authorization or access is delayed |
| **People / process** | No domain expert available for labelling or evaluation, user acceptance not obtained, a team member leaves |

Across the layers, cover the whole life cycle: data preparation, model development, deployment and maintenance. Include model decay after deployment and say what will trigger maintenance.

**Not risks:**

- A fixed limit is a **constraint**. For example, "limited computational resources" belongs under Assumptions & Constraints. The resources fluctuating or failing *is* a risk.
- An **assumption** is logged in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md), not here. Its flip-side risk is registered here, with the assumption's ID in **Linked to**.
- Work the team will not do is an **out-of-scope activity** in [Major Activities](03-project-canvas_v2/04-major-activities.md).

## Risk register

Add rows as needed. Rows with a score of 10 or more also need a detail block (next section).

This page lists only uncertain events that the team cannot fully control. Design questions, such as how to split the text, which model to use or how fast it runs, are not listed here. They are answered in the spikes and recorded in the System Architecture Design Document (D4).

R-01 to R-07 and R-10 are the other side of the assumptions in [Assumptions & Constraints](03-assumptions-and-constraints.md). R-08, R-09 and R-11 come from constraints and from how the team, users and outside parties may act.

| # | Layer | Risk (event) | When / where | Probability | Impact | Score | Owner | Linked to |
|---|---|---|---|---|---|---|---|---|
| R-01 | Data | **Source text differs from the Official Journal.** The EUR-Lex text differs from the Official Journal in an in-scope article. | Sprint 2; development | 1: EUR-Lex builds this text from the Official Journal | 4: answers would quote a text that is not the official wording (O2) | 4 (Low) | Yeşim (Product Owner) | A-01; C-01; [Dependencies](06-dependencies.md) row 3 |
| R-02 | Data | **The law or its official reading changes (concept drift).** An in-scope article is amended, or the European Commission adopts its final guidelines on high-risk classification (Article 6), before 30/12/2026, so some answers describe outdated rules or miss the official reading. | Sprints 2–4; development and after deployment | 3: the Commission published draft Article 6 guidelines on 19/05/2026 and has said the final version will be adopted by the end of 2026; the last amendment (Regulation (EU) 2026/1744) is already in the 27/07/2026 version | 3: answers on the changed article or on Article 6 become partly wrong for users, so a technical requirement is partly unmet | 9 (Medium) | Yaren (Scrum Master) | A-02; C-01; [Major Activities](04-major-activities.md) rows 18, 32 |
| R-03 | People / process | **Too few pilot users.** Fewer than 5 people join the pilot (16/12–23/12/2026). | Sprints 3–4; validation | 3: holiday period; participation is voluntary and unpaid | 4: O1 and O3 need at least 5 users | 12 (High) | Gözde Nur (Development Team Member) | A-04; [Dependencies](06-dependencies.md) row 9 |
| R-04 | People / process | **Targets change after review.** The Project Review Committee asks for different targets or a different scope at a sprint review. | Sprints 1–2; planning | 2: the targets have not been reviewed yet | 2: questions, tests and charter pages need 2–4 weeks of changes | 4 (Low) | Yeşim (Product Owner) | A-06; [Dependencies](06-dependencies.md) row 5 |
| R-05 | Infrastructure | **Cloud budget runs out.** Google Cloud spending reaches $70 before 09/12/2026, so the $100 credit would run out before 30/12/2026. | Sprints 2–4; development and after deployment | 2: billing alerts are set, and the server is off when not in use | 5: the credit is fixed; if it runs out, the assistant stops before the pilot | 10 (High) | Kaan (Development Team Member) | A-07; C-05; C-06; [Dependencies](06-dependencies.md) row 8 |
| R-06 | People / process | **A team member leaves.** A team member leaves the course or cannot work for 2 weeks or more. | Sprints 1–4; development | 2: all four members are enrolled and active | 3: the other three members take over a quarter of the work; later deliverables move by 1–2 months | 6 (Medium) | Yaren (Scrum Master) | A-09; C-07 |
| R-07 | Model | **The model or a library changes.** The selected model or a library that the assistant uses is changed or removed by its authors during the project. | Sprints 2–4; development | 2: model files on these sites are updated by their authors without notice; the version used is recorded in each evaluation run | 2: another model or library must be chosen and the evaluation runs repeated; 2–4 weeks | 4 (Low) | Kaan (Development Team Member) | A-10; C-03; [Dependencies](06-dependencies.md) row 6; [Facilities & Resources](09-facilities-and-resources.md) rows 4–6 |
| R-08 | People / process | **Work falls behind.** A sprint ends with planned work not done, so the next release starts at least 1 week late. | Sprints 1–4; development | 3: four part-time students; every sprint has a fixed end date | 2: a delay of 1 week in each sprint adds up to 4 weeks | 6 (Medium) | Yaren (Scrum Master) | C-07; [Release Plan](10-release-plan.md); [Dependencies](06-dependencies.md) rows 2, 4, 7, 10–16 |
| R-09 | People / process | **Answers are used as legal advice.** A pilot user says they would make a legal decision based only on the assistant's answer. | Sprint 4 and after deployment; validation | 2: every answer states that it is information, not legal advice | 4: the O4 goal is not met | 8 (Medium) | Yeşim (Product Owner) | C-08; [Major Activities](04-major-activities.md) rows 11, 14 |
| R-10 | People / process | **Pilot users do not match the target users.** Fewer than 3 of the pilot users have worked on an AI or education software product, so the pilot results do not represent the target users. | Sprints 2–4; validation | 2: the contacts work in software and AI, but few of them work on education products | 3: O1 and O3 are measured, but on users outside the target group | 6 (Medium) | Gözde Nur (Development Team Member) | A-08; [Dependencies](06-dependencies.md) row 9 |
| R-11 | Integration | **Cloud credit is late.** The Google Cloud credit is not available to the team by the start of the trial deployment (18/11/2026). | Sprint 2; deployment | 2: the credit is given through the course, and its date is set outside the team | 2: the beta and the pilot run from a team laptop instead; 2–4 weeks of extra work | 4 (Low) | Kaan (Development Team Member) | C-06; [Dependencies](06-dependencies.md) row 8 |

Spread: 2 High (R-03, R-05), 5 Medium, 4 Low.

**After deployment.** The assistant uses one version of the law (27/07/2026), so its answers no longer match the law in force when an in-scope article changes (R-02). This is concept drift: the question stays the same, but the correct answer changes. EUR-Lex is checked for a new version at the start of each sprint. If an in-scope article has changed, the new text is loaded, recorded in the manifest and tested again.

"When / where" gives the sprint(s) and whether the risk arises during development or after deployment. "Linked to" gives the IDs of the assumption (A-xx) or constraint (C-xx) in [Assumptions & Constraints](03-assumptions-and-constraints.md), or the row number in [Dependencies](06-dependencies.md), that the risk comes from.

## Risk details

Copy this block for each risk.

### Risk R-01: Source text differs from the Official Journal

| Field | Content |
|---|---|
| **Risk (event)** | The EUR-Lex text differs from the Official Journal in an in-scope article. |
| **Linked to** | A-01; C-01; [Dependencies](06-dependencies.md) row 3 |
| **Cause** | The consolidated text is a documentation tool made by the EU Publications Office; only the Official Journal text is legally authentic. |
| **When / where** | Sprint 2; development |
| **Mitigation** | Annex III point 3, Article 6 and Article 113 are compared with the Official Journal by 18/11/2026 ([Major Activities](04-major-activities.md) row 4). Every answer states that only the Official Journal text is authentic. |
| **Probability (basis)** | 1: EUR-Lex builds this text from the Official Journal |
| **Impact (basis)** | 4: answers would quote a text that is not the official wording (O2) |
| **Score** | 4 (Low) |
| **Trigger** | At least 1 difference found in the comparison with the Official Journal on 18/11/2026 |
| **Contingency plan (B plan)** | For the affected article, the Official Journal wording replaces the consolidated text in the index, and the change is recorded in the source manifest (D3). |
| **Owner** | Yeşim (Product Owner) |
| **Schedule effect** | Under 1 week |

### Risk R-02: The law or its official reading changes (concept drift)

| Field | Content |
|---|---|
| **Risk (event)** | An in-scope article is amended, or the European Commission adopts its final guidelines on high-risk classification (Article 6), before 30/12/2026, so some answers describe outdated rules or miss the official reading. |
| **Linked to** | A-02; C-01; [Major Activities](04-major-activities.md) rows 18, 32 |
| **Cause** | The regulation is changed by amending acts, and the Commission explains it in guidelines; the knowledge base holds only the 27/07/2026 regulation text (C-01). |
| **When / where** | Sprints 2–4; development and after deployment |
| **Mitigation** | EUR-Lex and the Commission's AI Act page are checked at the start of every sprint ([Major Activities](04-major-activities.md) row 32). Every answer shows the version date and states that it is based only on the regulation text. |
| **Probability (basis)** | 3: the Commission published draft Article 6 guidelines on 19/05/2026 and has said the final version will be adopted by the end of 2026; the last amendment (Regulation (EU) 2026/1744) is already in the 27/07/2026 version |
| **Impact (basis)** | 3: answers on the changed article or on Article 6 become partly wrong for users, so a technical requirement is partly unmet |
| **Score** | 9 (Medium) |
| **Trigger** | A newer consolidated version changes an in-scope article, or the final Article 6 guidelines are published, at a sprint-start check (04/11, 25/11 or 16/12/2026) |
| **Contingency plan (B plan)** | Before 09/12/2026: a changed article is loaded, re-indexed and the `dev` evaluation is run again. After 09/12/2026: answers about the changed article, or about Article 6, show a notice with the change date and a link to the new text or guidelines. Adding the guidelines as a second source is brought to the next sprint review as a scope change. |
| **Owner** | Yaren (Scrum Master) |
| **Schedule effect** | 1–2 weeks |

### Risk R-03: Too few pilot users

| Field | Content |
|---|---|
| **Risk (event)** | Fewer than 5 people join the pilot (16/12–23/12/2026). |
| **Linked to** | A-04; [Dependencies](06-dependencies.md) row 9 |
| **Cause** | The pilot is at the end of December; users are volunteers from the team's contacts. |
| **When / where** | Sprints 3–4; validation |
| **Mitigation** | Each member names 2 candidates by 04/11/2026. Dates are fixed with 5 people by 18/11/2026. 7 people are invited in case 2 drop out. Sessions last at most 45 minutes, online or in person ([Major Activities](04-major-activities.md) row 26). |
| **Probability (basis)** | 3: holiday period; participation is voluntary and unpaid |
| **Impact (basis)** | 4: O1 and O3 need at least 5 users |
| **Score** | 12 (High) |
| **Trigger** | Fewer than 5 names on 18/11/2026, or fewer than 5 finished sessions on 23/12/2026 |
| **Contingency plan (B plan)** | The pilot is extended to 27/12/2026, and METU graduate students working on software or AI are invited. If there are still fewer than 5 users, O1 and O3 are reported with the actual number, the sample size is reported, and the Project Review Committee is informed. |
| **Owner** | Gözde Nur (Development Team Member; pilot) |
| **Schedule effect** | Up to 4 days |

### Risk R-04: Targets change after review

| Field | Content |
|---|---|
| **Risk (event)** | The Project Review Committee asks for different targets or a different scope at a sprint review. |
| **Linked to** | A-06; [Dependencies](06-dependencies.md) row 5 |
| **Cause** | The target levels were set by the team before the first committee review. |
| **When / where** | Sprints 1–2; planning |
| **Mitigation** | Feedback on the targets is asked at the Sprint 1 review and added to the charter ([Major Activities](04-major-activities.md) row 34). |
| **Probability (basis)** | 2: the targets have not been reviewed yet |
| **Impact (basis)** | 2: questions, tests and charter pages need 2–4 weeks of changes |
| **Score** | 4 (Low) |
| **Trigger** | The committee asks for a change at the Sprint 1 review (28/10/2026) or the Sprint 2 review (18/11/2026) |
| **Contingency plan (B plan)** | Renegotiate the target: the Product Owner agrees with the committee which deliverables change, and the changes go into Charter v2 (D7). If time is needed, features 5–7 are moved out of the beta. |
| **Owner** | Yeşim (Product Owner) |
| **Schedule effect** | 2–4 weeks |

### Risk R-05: Cloud budget runs out

| Field | Content |
|---|---|
| **Risk (event)** | Google Cloud spending reaches $70 before 09/12/2026, so the $100 credit would run out before 30/12/2026. |
| **Linked to** | A-07; C-05; C-06; [Dependencies](06-dependencies.md) row 8 |
| **Cause** | The server is billed for every hour it runs. A server left on, or repeated test runs, increase the cost. |
| **When / where** | Sprints 2–4; development and after deployment |
| **Mitigation** | Billing alerts at $25, $50 and $70. Development runs on Colab and laptops; the server runs only for tests, the beta and the pilot. The bill is checked at the end of Sprints 2 and 3 ([Major Activities](04-major-activities.md) rows 29, 31). |
| **Probability (basis)** | 2: billing alerts are set, and the server is off when not in use |
| **Impact (basis)** | 5: the credit is fixed; if it runs out, the assistant stops before the pilot |
| **Score** | 10 (High) |
| **Trigger** | The bill shows $70 or more on any day before 09/12/2026 |
| **Contingency plan (B plan)** | The server runs only during pilot sessions and the final demo, and all other tests run on Colab or laptops. The Product Owner informs the Project Review Committee if a target is affected. |
| **Owner** | Kaan (Development Team Member; cloud and costs) |
| **Schedule effect** | About 1 week |

### Risk R-06: A team member leaves

| Field | Content |
|---|---|
| **Risk (event)** | A team member leaves the course or cannot work for 2 weeks or more. |
| **Linked to** | A-09; C-07 |
| **Cause** | Course withdrawal, illness or other courses can take a member away for weeks. |
| **When / where** | Sprints 1–4; development |
| **Mitigation** | All work is documented in the repository; at least two members know each area ([Major Activities](04-major-activities.md) rows 37–38). |
| **Probability (basis)** | 2: all four members are enrolled and active |
| **Impact (basis)** | 3: the other three members take over a quarter of the work; later deliverables move by 1–2 months |
| **Score** | 6 (Medium) |
| **Trigger** | A member misses 2 sprint events in a row, or announces leaving the course |
| **Contingency plan (B plan)** | Narrow the scope: the member's open work is reassigned at the next sprint planning, beta features 5–7 are reduced first, and the Project Review Committee is informed. |
| **Owner** | Yaren (Scrum Master) |
| **Schedule effect** | 2–4 weeks |

### Risk R-07: The model or a library changes

| Field | Content |
|---|---|
| **Risk (event)** | The selected model or a library that the assistant uses is changed or removed by its authors during the project. |
| **Linked to** | A-10; C-03; [Dependencies](06-dependencies.md) row 6; [Facilities & Resources](09-facilities-and-resources.md) rows 4–6 |
| **Cause** | Model and library authors publish new versions, change licences or remove files without notice. |
| **When / where** | Sprints 2–4; development |
| **Mitigation** | The model file is downloaded once and stored with its version and hash ([Major Activities](04-major-activities.md) row 16); the version is recorded in every evaluation run. |
| **Probability (basis)** | 2: model files on these sites are updated by their authors without notice; the version used is recorded in each evaluation run |
| **Impact (basis)** | 2: another model or library must be chosen and the evaluation runs repeated; 2–4 weeks |
| **Score** | 4 (Low) |
| **Trigger** | The model file's hash differs from the stored hash at any evaluation run, or the model can no longer be downloaded |
| **Contingency plan (B plan)** | The stored copy of the model stays in use. If the stored copy cannot be used, the next candidate from the model selection spike is chosen, recorded in a new ADR, and the `dev` evaluation is run again. |
| **Owner** | Kaan (Development Team Member) |
| **Schedule effect** | 1–2 weeks |

### Risk R-08: Work falls behind

| Field | Content |
|---|---|
| **Risk (event)** | A sprint ends with planned work not done, so the next release starts at least 1 week late. |
| **Linked to** | C-07; [Release Plan](10-release-plan.md); [Dependencies](06-dependencies.md) rows 2, 4, 7, 10–16 |
| **Cause** | Four part-time students with other courses; every sprint has a fixed end date. |
| **When / where** | Sprints 1–4; development |
| **Mitigation** | Progress is checked in the middle of each sprint; unfinished work is moved to the next sprint and recorded at the review ([Major Activities](04-major-activities.md) row 37). |
| **Probability (basis)** | 3: four part-time students; every sprint has a fixed end date |
| **Impact (basis)** | 2: a delay of 1 week in each sprint adds up to 4 weeks |
| **Score** | 6 (Medium) |
| **Trigger** | A deliverable due in a sprint is not finished at that sprint's review (28/10, 18/11 or 09/12/2026) |
| **Contingency plan (B plan)** | Narrow the scope: the Product Owner removes the lowest-priority story from the next sprint to make room for the late work, and the change is recorded in the sprint report. |
| **Owner** | Yaren (Scrum Master) |
| **Schedule effect** | About 1 week |

### Risk R-09: Answers are used as legal advice

| Field | Content |
|---|---|
| **Risk (event)** | A pilot user says they would make a legal decision based only on the assistant's answer. |
| **Linked to** | C-08; [Major Activities](04-major-activities.md) rows 11, 14 |
| **Cause** | Users want a yes/no answer about their own product. |
| **When / where** | Sprint 4 and after deployment; validation |
| **Mitigation** | A notice is shown on the page and with every answer ([Major Activities](04-major-activities.md) rows 11, 14). The pilot survey asks how users would use the answer. |
| **Probability (basis)** | 2: every answer states that it is information, not legal advice |
| **Impact (basis)** | 4: the O4 goal is not met |
| **Score** | 8 (Medium) |
| **Trigger** | At least 1 pilot user says in the survey (by 23/12/2026) that they would decide only from the answer |
| **Contingency plan (B plan)** | Hand over to a human: for legal-decision questions, the assistant shows only the article text and a notice to contact the company's legal team. The result is reported in D11. |
| **Owner** | Yeşim (Product Owner) |
| **Schedule effect** | Under 1 week |

### Risk R-10: Pilot users do not match the target users

| Field | Content |
|---|---|
| **Risk (event)** | Fewer than 3 of the pilot users have worked on an AI or education software product, so the pilot results do not represent the target users. |
| **Linked to** | A-08; [Dependencies](06-dependencies.md) row 9 |
| **Cause** | Pilot users are volunteers from the team's contacts; the team cannot choose who agrees to take part. |
| **When / where** | Sprints 2–4; validation |
| **Mitigation** | Each candidate is asked about their work background when invited; candidates who work on AI or education products are invited first ([Major Activities](04-major-activities.md) row 26). |
| **Probability (basis)** | 2: the contacts work in software and AI, but few of them work on education products |
| **Impact (basis)** | 3: O1 and O3 are measured, but on users outside the target group |
| **Score** | 6 (Medium) |
| **Trigger** | Fewer than 3 matching users among the confirmed participants on 18/11/2026 |
| **Contingency plan (B plan)** | METU graduate students working on AI in education are invited. The pilot results are reported separately for users with and without this background in D11. |
| **Owner** | Gözde Nur (Development Team Member; pilot) |
| **Schedule effect** | Under 1 week |

### Risk R-11: Cloud credit is late

| Field | Content |
|---|---|
| **Risk (event)** | The Google Cloud credit is not available to the team by the start of the trial deployment (18/11/2026). |
| **Linked to** | C-06; [Dependencies](06-dependencies.md) row 8 |
| **Cause** | The course provides the credit; when it reaches the team is decided outside the team. |
| **When / where** | Sprint 2; deployment |
| **Mitigation** | The team asks the course staff for the credit by the start of Sprint 2 (04/11/2026). |
| **Probability (basis)** | 2: the credit is given through the course, and its date is set outside the team |
| **Impact (basis)** | 2: the beta and the pilot run from a team laptop instead; 2–4 weeks of extra work |
| **Score** | 4 (Low) |
| **Trigger** | No usable credit on 11/11/2026 |
| **Contingency plan (B plan)** | The beta runs on a team laptop and is shared with the pilot users through a temporary link during the sessions; the Project Review Committee is informed. |
| **Owner** | Kaan (Development Team Member) |
| **Schedule effect** | About 1 week |
### Example (illustrative only)

| Field | Content |
|---|---|
| **Risk (event)** | End-to-end latency does not meet the target on the available hardware |
| **Linked to** | A-04: "The allocated GPU quota supports the latency target for 20 concurrent users" |
| **Cause** | The GPU quota comes from shared cloud credits; the final allocation is not known at project start |
| **When / where** | Sprints 2-4; during development and after deployment |
| **Mitigation** | Early capacity test in Sprint 2; batching, caching and quantization trials |
| **Probability (basis)** | 3: the Sprint 2 pilot measured p95 latency at 1.6× the target |
| **Impact (basis)** | 4: latency is an acceptance criterion of the MVP deliverable |
| **Score** | 12 (High) |
| **Trigger** | p95 end-to-end latency > 2× target at the end of Sprint 4 |
| **Contingency plan (B plan)** | Switch to a smaller quantized model; renegotiate the number of concurrent users with the AI customer; move to queue-based asynchronous answers |
| **Owner** | A named team member in the Data Scientist role |
| **Schedule effect** | About 2 weeks |

## Checklist before submitting

- [x] At least 5 risks
- [x] At least one risk from each of the five layers (data / model / infrastructure / integration / people-process)
- [x] Every risk is written as an event, with when and where
- [x] Every assumption in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md) has a risk here, and the IDs match both ways
- [x] Every risk that comes from a constraint names the in-scope activity in [Major Activities](03-project-canvas_v2/04-major-activities.md) that mitigates it
- [x] Probability values are residual (after mitigation), and each has a basis
- [x] Risks that threaten an acceptance criterion or success criterion have an impact of at least 4
- [x] Every risk scoring 10 or more has a mitigation, a numeric trigger with a date or sprint, a contingency plan and a named owner
- [x] Every owner is a named person listed in [Project Organization](03-project-canvas_v2/08-project-organization.md)
- [x] No contingency plan repeats work already planned under [Major Activities](03-project-canvas_v2/04-major-activities.md)
- [x] Scores are spread out (not all low, not all high)
- [x] Risk timings fall inside the project's sprint timeline
