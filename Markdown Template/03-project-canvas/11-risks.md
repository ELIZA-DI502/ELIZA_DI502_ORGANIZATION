# Risks

Record here the strategic risks identified at the start of the project. Write each risk as an **event** that could happen, not as a general worry: "Recall@5 on the evaluation set stays below 0.60 at the end of Sprint 3", not "the model fails".

## Risks, assumptions and constraints

A risk is an uncertain event that would hurt the project if it happens. It is connected to two other entries in the charter:

- **Every assumption has a risk on its flip side.** Each assumption in [Assumptions & Constraints](03-assumptions-and-constraints.md) has an ID (A-01, …) and names its linked risk. Register that risk here, give it an ID (R-01, …), and write the assumption's ID in **Linked to**. The IDs must point both ways. Example: the assumption "the dataset covers the in-scope categories" has the risk "the dataset under-represents some categories, leading to poor performance on them".
- **The uncertain part of a constraint is a risk.** A constraint in [Assumptions & Constraints](03-assumptions-and-constraints.md) is a fixed limit, but complying with it can fail. The in-scope activity in [Major Activities](04-major-activities.md) that enforces the constraint is the risk's mitigation. Example: the constraint "no PII is stored" has the risk "users submit PII in free-text queries, and it ends up in logs or the retrieval index"; PII masking is the mitigation.

A risk can also come from a dependency in [Dependencies](06-dependencies.md), for example an external API that changes or becomes unavailable. Write the dependency's row number in **Linked to**.

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
| 5 | Very high (>75%): almost certain. If it is basically going to happen, treat it as a constraint in [Assumptions & Constraints](03-assumptions-and-constraints.md). If some uncertainty remains, keep it as an assumption in [Assumptions & Constraints](03-assumptions-and-constraints.md) and link this risk to it |

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
3. **Who is the owner?** Name the person who decides to narrow the scope, switch the model or renegotiate the target with the AI customer. "The project team" is not an owner. Every member manages the project in some capacity, so an owner is always a named person, together with the role they hold in [Project Organization](08-project-organization.md).

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

Do not write only "the model may not work". Write **at least one risk from each of the five layers**. A table with only technical risks is incomplete. The same five layers are used as the constraint categories in [Assumptions & Constraints](03-assumptions-and-constraints.md).

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
- An **assumption** is logged in [Assumptions & Constraints](03-assumptions-and-constraints.md), not here. Its flip-side risk is registered here, with the assumption's ID in **Linked to**.
- Work the team will not do is an **out-of-scope activity** in [Major Activities](04-major-activities.md).

## Risk register

Add rows as needed. Rows with a score of 10 or more also need a detail block (next section).

This page lists only uncertain events that the team cannot fully control. Design questions, such as how to split the text or which model to use, are not listed here. They are answered in the spikes and recorded in the System Architecture Design Document (D4).

Where the risks come from: R-01 to R-06, R-08, R-10 and R-11 are the other side of an assumption in [Assumptions & Constraints](03-assumptions-and-constraints.md); the assumption is named in **Linked to**. The other three come from constraints: R-07 from C-07 (four students, fixed sprint dates), and R-09 and R-12 from C-05 (CPU only, run on a team computer). R-12 is not a design question: the model was chosen in the spike, but the computer used for the pilot is not fixed yet. Whether the assistant reaches its targets (O2, O4) and handles personal data as C-10 requires are design and test questions, not risks: they are answered in the System Design Document (D4) and checked by the acceptance criteria of D6, D9 and D11 (for example D9 criteria 2–4, 7 and 8).

| # | Layer | Risk (event) | When / where | Probability | Impact | Score | Owner | Linked to |
|---|---|---|---|---|---|---|---|---|
| R-01 | Data | **Source text differs from the Official Journal.** The EUR-Lex text differs from the Official Journal in an in-scope article. | Sprint 2; development | 1: EUR-Lex builds this text from the Official Journal | 4: answers would quote a text that is not the official wording (O2) | 4 (Low) | Yeşim (Product Owner) | A-01; C-01; [Dependencies](06-dependencies.md) row 3 |
| R-02 | Data | **The law or its official reading changes (concept drift).** An in-scope article is amended, or the European Commission adopts its final guidelines on high-risk classification (Article 6), before 30/12/2026, so some answers describe outdated rules or miss the official reading. | Sprints 2–4; development and after deployment | 3: the Commission published draft Article 6 guidelines on 19/05/2026; the consultation closed on 23/07/2026, and the final version had not been adopted when checked on 25/10/2026; the last amendment (Regulation (EU) 2026/1744) is already in the 27/07/2026 version | 3: answers on the changed article or on Article 6 become partly wrong for users, so a technical requirement is partly unmet | 9 (Medium) | Yaren (Scrum Master) | A-02; C-01; [Major Activities](04-major-activities.md) rows 18, 32 |
| R-03 | People / process | **Too few pilot users.** Fewer than 5 people join the pilot (16/12–23/12/2026). | Sprints 3–4; validation | 3: holiday period; participation is voluntary and unpaid | 4: O1 and O3 need at least 5 users | 12 (High) | Gözde Nur (Data Scientist; pilot) | A-04; [Dependencies](06-dependencies.md) row 9 |
| R-04 | People / process | **Targets change after review.** The Project Review Committee asks for different targets or a different scope at a sprint review. | Sprints 1–2; planning | 2: the targets have not been reviewed yet | 2: questions, tests and charter pages need 2–4 weeks of changes | 4 (Low) | Yeşim (Product Owner) | A-06; [Dependencies](06-dependencies.md) row 5 |
| R-05 | People / process | **A team member leaves.** A team member leaves the course or cannot work for 2 weeks or more. | Sprints 1–4; development | 2: all four members are enrolled and active | 3: the other three members take over a quarter of the work; later deliverables move by 1–2 months | 6 (Medium) | Yaren (Scrum Master) | A-08; C-07 |
| R-06 | Model | **The model or a library becomes unavailable.** Access to the selected model or a library is withdrawn by its authors before the team has stored its copy: for example, access to Llama is refused for the team's region, or the files become paid or are removed. | Sprints 1–2; development | 2: the official Llama files on Hugging Face are gated, so Meta approves each download and can refuse it, and the copies on Ollama can be removed by their publishers; Phi-4-mini-instruct and bge-base-en-v1.5 are not gated | 2: another model or library must be chosen and the evaluation runs repeated; 2–4 weeks | 4 (Low) | Kaan (Data Scientist) | A-09; C-03; [Dependencies](06-dependencies.md) row 6; [Facilities & Resources](09-facilities-and-resources.md) rows 4–6 |
| R-07 | People / process | **Work falls behind.** A task that later work depends on ([Dependencies](06-dependencies.md) rows 1, 7, 10–16) is not finished by its date, so the next release starts at least 1 week late. | Sprints 1–4; development | 3: four part-time students; every sprint has a fixed end date | 2: a delay of 1 week in each sprint adds up to 4 weeks | 6 (Medium) | Yaren (Scrum Master) | C-07; [Release Plan](10-release-plan.md); [Dependencies](06-dependencies.md) rows 1, 7, 10–16 |
| R-08 | People / process | **Pilot users do not match the target users.** Fewer than 3 of the pilot users have worked on an AI or education software product, so the pilot results do not represent the target users. | Sprints 2–4; validation | 2: the contacts work in software and AI, but not all of them work on education products | 3: O1 and O3 are measured, but on users outside the target group | 6 (Medium) | Gözde Nur (Data Scientist; pilot) | A-07; [Dependencies](06-dependencies.md) row 9 |
| R-09 | Integration | **The system does not install on the pilot computer.** Installing the system from `README.md` on the computer used for the pilot and the final demo fails, or gives different results than on the developers' computers, because of a different operating system, Python version or package build. | Sprints 3–4; pilot | 2: a team member who did not build the system installs it from the README each sprint, and the pilot computer is set up by 09/12/2026 | 3: the pilot (16/12–23/12/2026) has a fixed window; a late fix shortens it and can reduce the number of O1 and O3 sessions | 6 (Medium) | Kaan (Data Scientist) | C-05; [Major Activities](04-major-activities.md) rows 28, 29; [Dependencies](06-dependencies.md) row 8 |
| R-10 | Data | **The law is unclear for some questions.** For more than 5 evaluation questions, the regulation text does not clearly say which provision applies, because the answer depends on legal interpretation. | Sprints 2–3; development | 3: the exceptions in Article 6(3) depend on interpretation, and the Commission's guidelines on them are still a draft | 2: the question set must be partly rewritten and checked again; 2–4 weeks | 6 (Medium) | Kaan (Data Scientist) | A-03; [Dependencies](06-dependencies.md) row 2 |
| R-11 | Data | **The source format is uneven.** The EUR-Lex HTML does not mark Articles, paragraphs and Annex points in the same way throughout the text, so more than 5% of the provisions lose their numbers. | Sprints 1–2; development | 2: EUR-Lex marks articles, paragraphs and annex points with separate HTML elements, and in the Sprint 1 parsing spike all 22 chunks of Article 6 and Annex III point 3 got their correct identifier from the PDF; the HTML is checked in Sprint 2 (KAN-92) | 2: missing numbers are added by hand; 2–4 weeks | 4 (Low) | Yeşim (Product Owner) | A-05; [Dependencies](06-dependencies.md) row 4 |
| R-12 | Infrastructure | **The answer time does not meet the limit on the pilot computer.** On the team computer used for the pilot and the final demo, the median answer time on the `val` questions is above the answer-time limit recorded in the System Design Document (D4), so the O1 time gain cannot be reached. | Sprints 2–4; development and pilot | 2: on one team computer (CPU only), the selected model answered in 15.4 s, about 38 s in the worst case, below the 60 s limit; measured on one question, outside Docker, and the pilot computer is not fixed yet ([model selection spike](https://github.com/ELIZA-DI502/ELIZA_DI502_ORGANIZATION/blob/main/docs/spikes/model-selection-spike.md)) | 4: the O1 time gain is a success criterion | 8 (Medium) | Kaan (Data Scientist; model and answer time) | C-05; [Major Activities](04-major-activities.md) rows 6, 29; [Dependencies](06-dependencies.md) row 8; [Facilities & Resources](09-facilities-and-resources.md) rows 1, 3, 13 |

Spread of the risks (R-01 to R-12): 1 High (R-03), 7 Medium, 4 Low.

**After deployment.** The assistant uses one version of the law (27/07/2026), so its answers no longer match the law in force when an in-scope article changes (R-02). This is concept drift: the question stays the same, but the correct answer changes. EUR-Lex is checked for a new version at the start of each sprint. If an in-scope article has changed, the new text is loaded, recorded in the manifest and tested again.

"When / where" gives the sprint(s) and whether the risk arises during development or after deployment. "Linked to" gives the IDs of the assumption (A-xx) or constraint (C-xx) in [Assumptions & Constraints](03-assumptions-and-constraints.md), or the row number in [Dependencies](06-dependencies.md), that the risk comes from.

## Risk details

Copy this block for each risk.

**Impact** is the effect if the risk happens; **Schedule effect** is the delay that remains when the contingency plan (B plan) is used.

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
| **Probability (basis)** | 3: the Commission published draft Article 6 guidelines on 19/05/2026; the consultation closed on 23/07/2026, and the final version had not been adopted when checked on 25/10/2026; the last amendment (Regulation (EU) 2026/1744) is already in the 27/07/2026 version |
| **Impact (basis)** | 3: answers on the changed article or on Article 6 become partly wrong for users, so a technical requirement is partly unmet |
| **Score** | 9 (Medium) |
| **Trigger** | A newer consolidated version changes an in-scope article, or the final Article 6 guidelines are published, at a sprint-start check (28/10, 18/11 or 09/12/2026) |
| **Contingency plan (B plan)** | Before 05/12/2026: a changed article is loaded, re-indexed and the `val` evaluation is run again. After 05/12/2026: answers about the changed article, or about Article 6, show a notice with the change date and a link to the new text or guidelines. Adding the guidelines as a second source is brought to the next sprint review as a scope change. |
| **Owner** | Yaren (Scrum Master) |
| **Schedule effect** | 1–2 weeks |

### Risk R-03: Too few pilot users

| Field | Content |
|---|---|
| **Risk (event)** | Fewer than 5 people join the pilot (16/12–23/12/2026). |
| **Linked to** | A-04; [Dependencies](06-dependencies.md) row 9 |
| **Cause** | The pilot is at the end of December; users are volunteers from the team's contacts. |
| **When / where** | Sprints 3–4; validation |
| **Mitigation** | Each member names 2 candidates by 04/11/2026. Dates are fixed with 5 people by 18/11/2026. 7 people are invited in case 2 drop out. Sessions last at most 45 minutes, in person on the pilot computer ([Major Activities](04-major-activities.md) row 26). |
| **Probability (basis)** | 3: holiday period; participation is voluntary and unpaid |
| **Impact (basis)** | 4: O1 and O3 need at least 5 users |
| **Score** | 12 (High) |
| **Trigger** | Fewer than 5 names on 18/11/2026, or fewer than 5 finished sessions on 23/12/2026 |
| **Contingency plan (B plan)** | The pilot is extended to 27/12/2026, and METU graduate students working on software or AI are invited. If there are still fewer than 5 users, O1 and O3 are reported with the actual number, the sample size is reported, and the Project Review Committee is informed. |
| **Owner** | Gözde Nur (Data Scientist; pilot) |
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
| **Contingency plan (B plan)** | Renegotiate the target: the Product Owner agrees with the committee which deliverables change, and the changes go into Charter v2 (D7). If time is needed, Check the source (Feature 6) is deferred first; guided start and follow-up questions (Features 5 and 7) are already planned only if time allows. |
| **Owner** | Yeşim (Product Owner) |
| **Schedule effect** | 2–4 weeks |

### Risk R-05: A team member leaves

| Field | Content |
|---|---|
| **Risk (event)** | A team member leaves the course or cannot work for 2 weeks or more. |
| **Linked to** | A-08; C-07 |
| **Cause** | Course withdrawal, illness or other courses can take a member away for 2 weeks or more. |
| **When / where** | Sprints 1–4; development |
| **Mitigation** | All work is documented in the repository; at least two members know each area ([Major Activities](04-major-activities.md) rows 37–38). |
| **Probability (basis)** | 2: all four members are enrolled and active |
| **Impact (basis)** | 3: the other three members take over a quarter of the work; later deliverables move by 1–2 months |
| **Score** | 6 (Medium) |
| **Trigger** | A member misses 2 sprint events in a row, or announces leaving the course |
| **Contingency plan (B plan)** | Narrow the scope: the member's open work is reassigned at the next sprint planning, Check the source (Feature 6) is deferred first (Features 5 and 7 are already planned only if time allows), and the Project Review Committee is informed. |
| **Owner** | Yaren (Scrum Master) |
| **Schedule effect** | 2–4 weeks |

### Risk R-06: The model or a library becomes unavailable

| Field | Content |
|---|---|
| **Risk (event)** | Access to the selected model or a library is withdrawn by its authors before the team has stored its copy: for example, access to Llama is refused for the team's region, or the files become paid or are removed. |
| **Linked to** | A-09; C-03; [Dependencies](06-dependencies.md) row 6; [Facilities & Resources](09-facilities-and-resources.md) rows 4–6 |
| **Cause** | The authors decide who can download their model and library files; they can refuse access for a country or a user, make the files paid or remove them, without notice. |
| **When / where** | Sprints 1–2; development |
| **Mitigation** | The model files are downloaded as soon as the models are confirmed (M3, 28/10/2026) and stored with their version and hash ([Major Activities](04-major-activities.md) row 16); after that, a change on the authors' side does not affect the stored copy. |
| **Probability (basis)** | 2: the official Llama files on Hugging Face are gated, so Meta approves each download and can refuse it, and the copies on Ollama can be removed by their publishers; Phi-4-mini-instruct and bge-base-en-v1.5 are not gated |
| **Impact (basis)** | 2: another model or library must be chosen and the evaluation runs repeated; 2–4 weeks |
| **Score** | 4 (Low) |
| **Trigger** | A download or access request for a selected model or library is refused or fails before its copy is stored (by 18/11/2026), or the stored copy's hash differs at an evaluation run |
| **Contingency plan (B plan)** | The fallback model Phi-4-mini-instruct (MIT licence, not gated) is used, or for a library the previous pinned version; the change is recorded as a new decision in the System Design Document (D4), and the `val` evaluation is run again. |
| **Owner** | Kaan (Data Scientist) |
| **Schedule effect** | 1–2 weeks |

### Risk R-07: Work falls behind

| Field | Content |
|---|---|
| **Risk (event)** | A task that later work depends on ([Dependencies](06-dependencies.md) rows 1, 7, 10–16) is not finished by its date, so the next release starts at least 1 week late. |
| **Linked to** | C-07; [Release Plan](10-release-plan.md); [Dependencies](06-dependencies.md) rows 1, 7, 10–16 |
| **Cause** | Four part-time students with other courses; every sprint has a fixed end date. |
| **When / where** | Sprints 1–4; development |
| **Mitigation** | Progress is checked in the middle of each sprint; unfinished work is moved to the next sprint and recorded at the review ([Major Activities](04-major-activities.md) row 37). |
| **Probability (basis)** | 3: four part-time students; every sprint has a fixed end date |
| **Impact (basis)** | 2: a delay of 1 week in each sprint adds up to 4 weeks |
| **Score** | 6 (Medium) |
| **Trigger** | A deliverable due in a sprint is not finished on that sprint's upload date (27/10, 14/11 or 05/12/2026) |
| **Contingency plan (B plan)** | Narrow the scope: the Product Owner removes the lowest-priority story from the next sprint to make room for the late work, and the change is recorded on the sprint's welcome page. |
| **Owner** | Yaren (Scrum Master) |
| **Schedule effect** | About 1 week |

### Risk R-08: Pilot users do not match the target users

| Field | Content |
|---|---|
| **Risk (event)** | Fewer than 3 of the pilot users have worked on an AI or education software product, so the pilot results do not represent the target users. |
| **Linked to** | A-07; [Dependencies](06-dependencies.md) row 9 |
| **Cause** | Pilot users are volunteers from the team's contacts; the team cannot choose who agrees to take part. |
| **When / where** | Sprints 2–4; validation |
| **Mitigation** | Each candidate is asked about their work background when invited; candidates who work on AI or education products are invited first ([Major Activities](04-major-activities.md) row 26). |
| **Probability (basis)** | 2: the contacts work in software and AI, but not all of them work on education products |
| **Impact (basis)** | 3: O1 and O3 are measured, but on users outside the target group |
| **Score** | 6 (Medium) |
| **Trigger** | Fewer than 3 matching users among the confirmed participants on 18/11/2026 |
| **Contingency plan (B plan)** | METU graduate students working on AI in education are invited. The pilot results are reported separately for users with and without this background in D10. |
| **Owner** | Gözde Nur (Data Scientist; pilot) |
| **Schedule effect** | Under 1 week |

### Risk R-09: The system does not install on the pilot computer

| Field | Content |
|---|---|
| **Risk (event)** | Installing the system from `README.md` on the computer used for the pilot and the final demo fails, or gives different results than on the developers' computers. |
| **Linked to** | C-05; [Major Activities](04-major-activities.md) rows 28, 29; [Dependencies](06-dependencies.md) row 8 |
| **Cause** | Packages and model runtimes are built by outside authors for specific operating systems and Python versions; the pilot computer may differ from the computers the system was built on. |
| **When / where** | Sprints 3–4; pilot |
| **Mitigation** | `requirements.txt` is fully pinned and the README gives the Python version; each sprint, a team member who did not build the system installs it from the README ([Major Activities](04-major-activities.md) row 28); the pilot computer is set up and its answer time measured by 09/12/2026 (row 29). |
| **Probability (basis)** | 2: a team member who did not build the system installs it from the README each sprint, and the pilot computer is set up by 09/12/2026 |
| **Impact (basis)** | 3: the pilot (16/12–23/12/2026) has a fixed window; a late fix shortens it and can reduce the number of O1 and O3 sessions |
| **Score** | 6 (Medium) |
| **Trigger** | The installation from the README on the pilot computer fails, or its `val` results differ from the beta results, at the set-up check on 09/12/2026 |
| **Contingency plan (B plan)** | The pilot runs on the team member's computer on which the beta was evaluated; the change of computer is recorded in the pilot protocol and in D10. |
| **Owner** | Kaan (Data Scientist) |
| **Schedule effect** | Under 1 week |

### Risk R-10: The law is unclear for some questions

| Field | Content |
|---|---|
| **Risk (event)** | For more than 5 evaluation questions, the regulation text does not clearly say which provision applies, because the answer depends on legal interpretation. |
| **Linked to** | A-03; [Dependencies](06-dependencies.md) row 2 |
| **Cause** | Some education use cases sit on the border of Annex III point 3 and the Article 6(3) exceptions, and the text leaves room for interpretation. |
| **When / where** | Sprints 2–3; development |
| **Mitigation** | Every question is written from one use case and checked by a second member; questions marked "unclear in the text" are recorded ([Major Activities](04-major-activities.md) row 3). |
| **Probability (basis)** | 3: the exceptions in Article 6(3) depend on interpretation, and the Commission's guidelines on them are still a draft |
| **Impact (basis)** | 2: the question set must be partly rewritten and checked again; 2–4 weeks |
| **Score** | 6 (Medium) |
| **Trigger** | More than 5 questions marked "unclear in the text" when D2 is complete (11/11/2026) or the D8 `val` split is frozen (01/12/2026) |
| **Contingency plan (B plan)** | These questions are moved to the legal-decision category: the expected answer shows the relevant provisions without a decision. They are listed in D2 or D8. |
| **Owner** | Kaan (Data Scientist) |
| **Schedule effect** | Under 1 week |

### Risk R-11: The source format is uneven

| Field | Content |
|---|---|
| **Risk (event)** | The EUR-Lex HTML does not mark Articles, paragraphs and Annex points in the same way throughout the text, so more than 5% of the provisions lose their numbers. |
| **Linked to** | A-05; [Dependencies](06-dependencies.md) row 4 |
| **Cause** | The consolidated text is produced by the EU Publications Office; its HTML format is outside the team's control. |
| **When / where** | Sprints 1–2; development |
| **Mitigation** | The Sprint 1 parsing spike checked the identifiers on the PDF; when the HTML is stored (KAN-92), it is compared with the table of contents of the regulation before the splitting code is written ([Major Activities](04-major-activities.md) row 7). |
| **Probability (basis)** | 2: EUR-Lex marks articles, paragraphs and annex points with separate HTML elements, and in the Sprint 1 parsing spike all 22 chunks of Article 6 and Annex III point 3 got their correct identifier from the PDF; the HTML is checked in Sprint 2 (KAN-92) |
| **Impact (basis)** | 2: missing numbers are added by hand; 2–4 weeks |
| **Score** | 4 (Low) |
| **Trigger** | More than 5% of the in-scope provisions without a number when the HTML is checked (KAN-92) or in the D5 check (14/11/2026) |
| **Contingency plan (B plan)** | The missing numbers are added by hand from the Official Journal PDF, and the manual changes are recorded in the preprocessing report (D5). |
| **Owner** | Yeşim (Product Owner) |
| **Schedule effect** | About 1 week |

### Risk R-12: The answer time does not meet the limit on the pilot computer

| Field | Content |
|---|---|
| **Risk (event)** | On the team computer used for the pilot and the final demo, the median answer time on the `val` questions is above the answer-time limit recorded in the System Design Document (D4), so the O1 time gain cannot be reached. |
| **Linked to** | C-05: "The system runs on CPU only, including the pilot and the final demo"; [Major Activities](04-major-activities.md) rows 6, 29; [Dependencies](06-dependencies.md) row 8; [Facilities & Resources](09-facilities-and-resources.md) rows 1, 3, 13 |
| **Cause** | The system runs on CPU only (C-05); a quantized language model generates text more slowly on a CPU, and longer prompts (more retrieved passages) make it slower. The computer used for the pilot is not chosen yet, and the answer time has so far been measured on one computer only. |
| **When / where** | Sprints 2–4; development and pilot |
| **Mitigation** | The model selection spike measured the answer time on CPU ([Major Activities](04-major-activities.md) row 6); the baseline's answer time is recorded in Sprint 2 (18/11/2026); the answer time on the pilot computer is measured on the `val` questions by 09/12/2026 (row 29). |
| **Probability (basis)** | 2: on one team computer (CPU only), the selected model answered in 15.4 s, about 38 s in the worst case, below the 60 s limit; measured on one question, outside Docker, and the pilot computer is not fixed yet ([model selection spike](https://github.com/ELIZA-DI502/ELIZA_DI502_ORGANIZATION/blob/main/docs/spikes/model-selection-spike.md)) |
| **Impact (basis)** | 4: the O1 time gain is a success criterion |
| **Score** | 8 (Medium) |
| **Trigger** | Median answer time above the D4 limit at the baseline evaluation (18/11/2026) or on the pilot computer (09/12/2026) |
| **Contingency plan (B plan)** | First top-k or the answer length is reduced; if the limit is still not met, the smaller fallback model from the model selection spike is used and recorded in the design document; if the limit is still not met, the course's reserve Google Cloud credit (C-06) pays for a CPU instance during the pilot sessions and the final demo only, after billing alerts are set. The Product Owner informs the Project Review Committee if O1 is at risk. |
| **Owner** | Kaan (Data Scientist; model and answer time) |
| **Schedule effect** | 1–2 weeks |

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
- [x] Every assumption in [Assumptions & Constraints](03-assumptions-and-constraints.md) has a risk here, and the IDs match both ways
- [x] Every risk that comes from a constraint names the in-scope activity in [Major Activities](04-major-activities.md) that mitigates it
- [x] Probability values are residual (after mitigation), and each has a basis
- [x] Risks that threaten an acceptance criterion or success criterion have an impact of at least 4
- [x] Every risk scoring 10 or more has a mitigation, a numeric trigger with a date or sprint, a contingency plan and a named owner
- [x] Every owner is a named person listed in [Project Organization](08-project-organization.md)
- [x] No contingency plan repeats work already planned under [Major Activities](04-major-activities.md)
- [x] Scores are spread out (not all low, not all high)
- [x] Risk timings fall inside the project's sprint timeline
