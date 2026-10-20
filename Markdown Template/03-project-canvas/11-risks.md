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

Risks R-01 to R-09, R-19 and R-21 are the flip sides of assumptions A-01 to A-09, A-10 and A-11 in [Assumptions & Constraints](03-assumptions-and-constraints.md). R-10 to R-18, R-20 and R-22 come from constraints, from the sprint calendar in the [Release Plan](10-release-plan.md), from the data source and from the evaluation design. Risks that come from a dependency name its row in [Dependencies](06-dependencies.md). Thresholds in the triggers are the success criteria in the [Project Executive Summary](01-project-executive-summary.md) and the acceptance criteria in [Deliverables](05-deliverables.md). Owners are the team members named in [Project Organization](08-project-organization.md). Probability is residual, after the mitigation.

| # | Layer | Risk (event) | When / where | Probability | Impact | Score | Owner | Linked to |
|---|---|---|---|---|---|---|---|---|
| R-01 | Data | The EUR-Lex consolidated text (27/07/2026) differs from the Official Journal wording in an in-scope provision | Sprints 1–2; development | 1: consolidated texts are prepared by the Publications Office from the Official Journal acts; errors in them are rare | 2: a secondary result is affected: answers on that provision cite wording that is not authentic until the chunk is corrected from the Official Journal text, re-indexed and the affected `dev` questions are re-evaluated; the correction itself takes under 2 weeks | 2 (Low) | Yeşim (Product Owner) | A-01; C-01 |
| R-02 | Data | A new amending act changes an in-scope provision before 30/12/2026, so answers from the designated version become outdated | Sprints 2–4 and after deployment | 2: Regulation (EU) 2026/1744 was adopted in July 2026; a second amendment of the same provisions within five months would be unusual | 3: re-indexing and re-running the evaluation; dates in answers partly outdated until then | 6 (Medium) | Yaren (Scrum Master) | A-02; C-01 |
| R-03 | Data | More than 5 evaluation questions cannot be mapped to a provision-level gold source, or the two reviewers disagree on them, so a use case has fewer than 3 questions and D2 and M2 (28/10/2026) are at risk | Sprint 1 (D2) and Sprint 3 (D8); development | 2: every question is written from one Annex III point 3 use case, and the disagreement procedure of A-03 applies; conditional questions on Article 6(3) are the hardest | 4: D2 criteria 1–2 (20–30 questions, at least 3 per use case) would not be met | 8 (Medium) | Kaan (Development Team Member) | A-03; [Dependencies](06-dependencies.md) row 2 |
| R-04 | People / process | Fewer than 5 proxy users take part in the pilot between 16/12 and 23/12/2026 | Sprint 4; pilot | 3: the pilot falls in the week before the new-year holidays, and participation is voluntary and unpaid | 4: O1 and O3 need at least 5 pilot users (success criteria; D11 criterion 1) | 12 (High) | Gözde Nur (Development Team Member) | A-04; C-07; [Dependencies](06-dependencies.md) row 9 |
| R-05 | Data | Splitting the text into provisions needs manual correction of more than 5% of the chunks | Sprints 1–2; development | 2: the EUR-Lex HTML marks articles and paragraphs as separate elements; Annex points are less regular; a first test split of the 27/07/2026 text by the team gave 188 provision-level chunks for 19 Articles and Annex III (19/10/2026), to be confirmed in the Sprint 1 parsing spike | 2: extra manual work of under 1 week in Sprint 2 (D5) | 4 (Low) | Yeşim (Product Owner) | A-05; [Dependencies](06-dependencies.md) row 4 |
| R-06 | People / process | The Project Review Committee asks for different O2 or O4 target levels at the Sprint 1 review | Sprint 1 review; recorded in D7 | 2: the levels follow the course's example acceptance criteria | 3: D9 and D12 criteria and the evaluation plan are rewritten in Sprint 2 | 6 (Medium) | Yeşim (Product Owner) | A-06; [Dependencies](06-dependencies.md) row 5 |
| R-07 | Infrastructure | Google Cloud spending exceeds the planned $70 allocation by the end of Sprint 3 (09/12/2026), leaving too little credit for the Sprint 4 pilot, the release-candidate evaluation and the final demonstration | Sprints 2–3; deployment | 2: development runs on Colab and own computers; the cloud instance runs only for tests, the beta and the pilot; billing alerts are set | 4: without enough remaining credit the beta cannot stay up for the pilot and the release candidate cannot be demonstrated on the course cloud account (D11, D12 criterion 6) | 8 (Medium) | Kaan (Development Team Member) | A-07; C-05, C-06; [Dependencies](06-dependencies.md) row 8 |
| R-08 | Data | Fewer than 70% of the realism ratings of the 10 sampled questions are 4 or 5 out of 5 | Sprint 3 (D8); development | 2: the questions come from the Annex III point 3 use cases and are checked by a second team member | 4: D8 criterion 7 (at least 70% rated 4 or 5) would not be met | 8 (Medium) | Yaren (Scrum Master) | A-08 |
| R-09 | People / process | A team member leaves the course or is unavailable for 2 weeks or more | Sprints 1–4 | 2: all four are enrolled; members also have jobs, other courses and theses | 4: one of the four work areas stops; beta features may miss D9 | 8 (Medium) | Yaren (Scrum Master) | A-09; C-07 |
| R-10 | Infrastructure | The quantized open-source model on the CPU-only Google Cloud instance needs more than 30 s per answer (median on the `dev` split) | Sprint 1 spike; Sprints 2–4; development and deployment | 3: no GPU is available; the candidate 3–4B quantized models can still answer slowly on CPU-only hardware, especially with long answers and retrieved context; not measured yet on the planned deployment instance; the Sprint 1 spike gives the first measurement | 4: answers this slow would remove the time saving that O1 measures (30 s is the team's operational early-warning threshold, not an O1 criterion) | 12 (High) | Kaan (Development Team Member) | C-03, C-05; [Dependencies](06-dependencies.md) row 6 |
| R-11 | Data | A user enters personal data in a question, and it is stored in a log or index | Sprints 3–4; pilot and after deployment | 2: questions are about products, not people; pilot users are briefed; questions are not logged | 4: C-10 is breached; storing personal data violates a fixed privacy rule of the system | 8 (Medium) | Gözde Nur (Development Team Member) | C-10 |
| R-12 | Model | O2 is not met on the `dev` split at the end of Sprint 3: the expected provision is cited for fewer than 80%, or answers are fully supported by their cited passages for fewer than 75%, of in-scope questions | Sprints 2–3 (D6, D9); confirmed on `test` in Sprint 4 (D12) | 3: multi-provision and condition/exception questions (Article 6(3)) are hard for small quantized models; first measurement comes with the alpha | 4: O2 success criterion and D9 criterion 2 | 12 (High) | Yeşim (Product Owner) | C-01, C-03 |
| R-13 | Model | A safety question gets a wrong response: the assistant gives a compliance verdict, answers an out-of-scope question, answers without sufficient evidence, or follows a prompt-injection or evasion request | Sprints 2–4; development and pilot | 3: small models often follow injected instructions; no verdict is allowed and the legal-decision target is 100%, so a single wrong answer there fails it | 4: O4 success criterion and D9 criteria 3–4 | 12 (High) | Gözde Nur (Development Team Member) | C-08, C-10 |
| R-14 | People / process | The alpha does not answer every `dev` question end to end by 18/11/2026 (M4) | Sprint 2; development | 3: parsing, retrieval, the model and the web page are joined for the first time within one 2-week sprint | 4: D6 criterion 2; the beta starts late | 12 (High) | Yeşim (Product Owner) | C-07 |
| R-15 | Integration | Pilot users cannot reach the deployed beta on Google Cloud by 09/12/2026 (access, quota or network set-up problems) | Sprint 3; deployment | 2: one standard instance with a public web page; a trial deployment is done before the beta deployment | 4: D9 criterion 1; the pilot cannot start | 8 (Medium) | Gözde Nur (Development Team Member) | C-05; [Dependencies](06-dependencies.md) rows 11 and 13 |
| R-16 | People / process | The D8 `dev` questions are not frozen by 04/12/2026, so the beta cannot be scored on them by 09/12/2026 | Sprint 3; development | 2: D2 already holds 20–30 questions; new questions are collected from 25/11 | 3: D9 results are reported late, within the checkpoint gap | 6 (Medium) | Yaren (Scrum Master) | C-07; [Dependencies](06-dependencies.md) row 12 |
| R-17 | People / process | A fault found in the pilot cannot be fixed and re-evaluated before 30/12/2026 | Sprint 4; between the pilot and the release candidate | 2: no new features are planned in Sprint 4; the pilot ends on 23/12 | 4: D12 criteria would be reported on an unfixed release | 8 (Medium) | Yeşim (Product Owner) | C-07; A-04; [Dependencies](06-dependencies.md) row 15 |
| R-18 | Integration | The EUR-Lex page of the consolidated text is unavailable or changes its format before the source file is stored | Sprint 1; data collection | 1: the file is downloaded once in Sprint 1 and stored with its hash (D3) | 1: a download delay of a few days | 1 (Low) | Yeşim (Product Owner) | C-01; [Dependencies](06-dependencies.md) row 3 |
| R-19 | Integration | The licence of the selected open-source language model or embedding model does not permit its use in the project or the publication of its answers | Sprint 1; model selection | 2: licences differ between candidate models (Apache 2.0, MIT, community licences with extra terms); each licence is read before the ADR | 2: another candidate model is chosen in under 2 weeks | 4 (Low) | Kaan (Development Team Member) | A-10; C-03; [Dependencies](06-dependencies.md) row 6 |
| R-20 | Model | An answer cites an Article or Annex point that is not among the retrieved chunks | Sprints 2–4; development and pilot | 2: small models can invent references; the citation-ID check blocks citations that do not match a retrieved chunk | 4: D6 criterion 4 (100% of citations match retrieved chunk IDs) and O2 (b) | 8 (Medium) | Kaan (Development Team Member) | C-03 |
| R-21 | Data | More than 3 of the questions taken or adapted from the AI Act Evaluation Benchmark (Davvetas et al., 2026) have a gold answer or source that does not match the 27/07/2026 text, or the benchmark cannot be reused, so D2 has fewer than 5 questions from published work | Sprint 1 (D2) and Sprint 3 (D8); development | 2: a first check by the team (19/10/2026) found 1 of the 32 in-scope question–answer pairs citing the wrong Article and 1 doubtful; the repository README states CC BY 4.0 for the data; every adapted question is checked against the official text (A-03) | 4: D2 criterion 13 would not be met | 8 (Medium) | Kaan (Development Team Member) | A-11; [Dependencies](06-dependencies.md) row 1 |
| R-22 | Model | The held-out `test` questions are used while tuning prompts, retrieval or rules, so the D12 results overstate the real quality | Sprints 2–4; development | 2: the `test` split is fixed in Sprint 1 (D2) and for new questions on 09/12/2026 (D8), and stored apart from the `dev` questions; tuning runs read only the `dev` split | 4: D12 criteria 1–2 could not be claimed as held-out results | 8 (Medium) | Yaren (Scrum Master) | [Major Activities](04-major-activities.md) rows 23, 25, 27; [Dependencies](06-dependencies.md) row 16 |

Spread: 5 High (R-04, R-10, R-12, R-13, R-14), 13 Medium, 4 Low; no Critical risk.

**Mitigations for medium and low risks**

| # | Mitigation (before the risk happens) |
|---|---|
| R-01 | Word-for-word check of Annex III point 3, Article 6 and Article 113 against the Official Journal by 18/11/2026 (A-01; [Major Activities](04-major-activities.md) row 4); every answer states that only the Official Journal text is authentic (C-08; row 10). |
| R-02 | EUR-Lex check for a newer consolidated version at the start of each sprint (A-02; [Major Activities](04-major-activities.md) row 32); the version date is shown with every answer (C-09). After deployment, a new consolidated version that changes an in-scope provision is the trigger for maintenance: new manifest row, re-index and re-run of the evaluation, approved by the Product Owner and recorded as an ADR. |
| R-03 | Every question is written from one use case and checked by a second team member; disagreements are logged (A-03, D2 criterion 7). |
| R-05 | Sprint 1 spike on the HTML structure before any chunking code is written (A-05). |
| R-06 | Ask for feedback on the target levels at the Sprint 1 review and record it in Charter v2 (A-06, D7 criterion 4). |
| R-07 | Billing alerts at $25, $50 and $70; the instance is stopped outside test, beta and pilot windows; development on Colab (C-05); billing check at the end of Sprints 2 and 3 (A-07; [Major Activities](04-major-activities.md) rows 29, 31). |
| R-08 | Proxy users contribute questions to D8; realism rating of 10 questions (A-08, D8 criterion 7). |
| R-09 | Each work area is documented in the repository (README, ADRs, spike notes); two members know each area (Yeşim and Yaren: data and evaluation; Kaan and Gözde Nur: model and application); availability checked at sprint planning ([Major Activities](04-major-activities.md) rows 37–38). |
| R-11 | No logging of user questions; personal-data reminder on the page and a rule-based input check (C-10; [Major Activities](04-major-activities.md) row 13: personal-data reminder and input check). |
| R-15 | Trial cloud deployment with a smoke test from outside the team's network in Sprint 2, or at the latest at the start of Sprint 3, before the beta deployment ([Major Activities](04-major-activities.md) rows 28–29). |
| R-16 | New D8 questions are collected and reviewed from 25/11; the D8 `dev` freeze date (04/12) is in the [Release Plan](10-release-plan.md) ([Major Activities](04-major-activities.md) row 25). |
| R-17 | Pilot problems are logged as they occur while Beta 0.5 stays unchanged for all participants (16/12–23/12/2026); fixes may be prepared separately but are applied only to the release candidate; no new features are added in Sprint 4 ([Major Activities](04-major-activities.md) row 30; [Release Plan](10-release-plan.md)). |
| R-18 | The source file is stored in the repository with its SHA-256 hash in Sprint 1 (D3; [Major Activities](04-major-activities.md) row 4). |
| R-19 | Each candidate model's licence is read in the model selection spike before its ADR is accepted and recorded in `ai-bom.yaml` (A-10; [Major Activities](04-major-activities.md) rows 6 and 16). |
| R-20 | Citation-ID check: every cited Article or Annex point must match a retrieved chunk, otherwise the citation is not shown; checked on all `dev` answers (D6 criterion 4; [Major Activities](04-major-activities.md) rows 10 and 23). |
| R-21 | The benchmark licence is re-checked by 23/10/2026 ([Dependencies](06-dependencies.md) row 1); each adapted question is checked against the official text and cross-checked by a second member like any other question (A-03, A-11; D2 criteria 7 and 13); if fewer than 5 benchmark questions remain usable, questions are taken or adapted from other published work on the EU AI Act. |
| R-22 | The `test` file is kept apart from the `dev` file; evaluation scripts for tuning read only the `dev` split; any use of a `test` question outside the final evaluation is logged and the question is excluded from held-out claims (D8 criterion 4; [Major Activities](04-major-activities.md) rows 25 and 27). |

"When / where" gives the sprint(s) and whether the risk arises during development or after deployment. "Linked to" gives the IDs of the assumption (A-xx) or constraint (C-xx) in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md), or the row number in [Dependencies](03-project-canvas_v2/06-dependencies.md), that the risk comes from.

## Risk details

Copy this block for each risk.

### Risk R-04: Too few pilot users

| Field | Content |
|---|---|
| **Risk (event)** | Fewer than 5 proxy users take part in the pilot between 16/12 and 23/12/2026 |
| **Linked to** | A-04; C-07; [Dependencies](06-dependencies.md) row 9 |
| **Cause** | The pilot is in the last two weeks of December; participants are volunteers from the team's professional contacts |
| **When / where** | Sprint 4; pilot |
| **Mitigation** | Each team member names 2 candidates by 04/11/2026; name 5 participants and fix their dates by 18/11/2026 (A-04; [Major Activities](04-major-activities.md) row 26); recruit 7 so that 2 can drop out; sessions of at most 45 minutes, online or in person |
| **Probability (basis)** | 3: holiday period; voluntary and unpaid participation |
| **Impact (basis)** | 4: O1 and O3 success criteria and D11 criterion 1 require at least 5 users |
| **Score** | 12 (High) |
| **Trigger** | Fewer than 5 named participants on 18/11/2026, or fewer than 5 completed sessions on 23/12/2026 |
| **Contingency plan (B plan)** | Extend the pilot to 27/12/2026 (accepted schedule risk: this leaves 3 days before 30/12/2026) and invite METU graduate students working on software or AI from outside DI 502; if fewer than 5 users still take part, report O1 and O3 with the number reached, mark them "not measured at the planned sample size" in Charter v4 (D13) and inform the Project Review Committee |
| **Owner** | Gözde Nur (Development Team Member; pilot protocol and pilot users) |
| **Schedule effect** | Up to 4 days, taken from the fix window before 30/12 |

### Risk R-10: Answers too slow on the available compute

| Field | Content |
|---|---|
| **Risk (event)** | The quantized open-source model on the CPU-only Google Cloud instance needs more than 30 s per answer (median on the `dev` split) |
| **Linked to** | C-03, C-05; [Dependencies](06-dependencies.md) row 6 |
| **Cause** | No GPU is available (C-05); answer time grows with model size and answer length |
| **When / where** | Sprint 1 spike; Sprints 2–4; development and deployment |
| **Mitigation** | Sprint 1 spike that measures answer time of at least two model sizes on CPU only, in a Colab CPU runtime or on a short-lived Google Cloud instance of the planned deployment type, not on a GPU runtime ([Major Activities](04-major-activities.md) row 6: model selection spike); answer length capped; only the top retrieved provisions are sent to the model |
| **Probability (basis)** | 3: the candidate 3–4B quantized models (Qwen3-4B, Phi-3.5-mini-instruct, Llama-3.2-3B-Instruct, see [Facilities & Resources](09-facilities-and-resources.md) row 4) can still answer slowly on CPU-only hardware, especially with long answers and retrieved context; not yet measured on our questions or on the deployment instance; the Sprint 1 spike gives the first measurement |
| **Impact (basis)** | 4: slow answers remove the time saving measured by O1. The 30 s threshold is the team's operational early-warning level, not an O1 success criterion |
| **Score** | 12 (High) |
| **Trigger** | Median answer time above 30 s on CPU in the spike note on 28/10/2026; or on the `dev` split on the CPU environment available to the team (Colab CPU runtime or own computer) at the end of Sprint 2 (18/11/2026); or on the planned Google Cloud instance type in the trial deployment, before the beta is deployed (row 28) |
| **Contingency plan (B plan)** | Switch to a smaller quantized model than the chosen one (for example 1–2B parameters), recorded in a new ADR; if the median is still above 30 s, show the retrieved provisions with their wording first and the generated explanation after it, so that users can find the provision without waiting for the full answer |
| **Owner** | Kaan (Development Team Member; retrieval and answer generation) |
| **Schedule effect** | About 1 week |

### Risk R-12: O2 Grounded not met

| Field | Content |
|---|---|
| **Risk (event)** | On the `dev` split at the end of Sprint 3, the expected provision is cited for fewer than 80%, or answers are fully supported by their cited passages for fewer than 75%, of in-scope questions |
| **Linked to** | C-01, C-03 |
| **Cause** | Multi-provision questions and conditions and exceptions (Article 6(3)) are hard to retrieve and summarise for small quantized models |
| **When / where** | Sprints 2–3 (D6, D9); confirmed on `test` in Sprint 4 (D12) |
| **Mitigation** | Chunks follow Article and paragraph boundaries (D5); citation-ID check (D6); answers are based only on retrieved provisions; results per question type are tracked from the alpha onward ([Major Activities](04-major-activities.md) rows 9 and 23: retrieval pipeline, evaluation runs) |
| **Probability (basis)** | 3: no measurement yet; the alpha gives the first one on 18/11/2026 |
| **Impact (basis)** | 4: O2 success criterion and D9 criterion 2 |
| **Score** | 12 (High) |
| **Trigger** | Early warning: expected provision cited in fewer than 60% of in-scope `dev` questions on 18/11/2026 (alpha). Main trigger: O2 (a) below 80% or (b) below 75% on the `dev` split on 09/12/2026 |
| **Contingency plan (B plan)** | If O2 (a) is below 80%, check for each failing question type whether the failure comes from retrieval or from citation selection. Where the expected provision is not retrieved, the assistant returns an insufficient-evidence notice instead of answering from the wrong provisions; where it is retrieved but not cited correctly, the answer cites only verified retrieved references. If (a) is met but (b) is below 75%, the assistant shows the wording of the retrieved provision with a short fixed-format explanation instead of a freely generated answer. In all cases, results are reported per question type in D9 and D12, the decision is recorded in Charter v3 (D10), and the Project Review Committee is informed |
| **Owner** | Yeşim (Product Owner) |
| **Schedule effect** | About 1 week |

### Risk R-13: Safety response fails

| Field | Content |
|---|---|
| **Risk (event)** | A safety question in any of the four O4 categories (out-of-scope, insufficient-evidence, legal-decision, adversarial) gets a wrong response: the assistant gives a compliance verdict, answers an out-of-scope question, answers without sufficient evidence, or follows a prompt-injection or evasion request |
| **Linked to** | C-08, C-10 |
| **Cause** | Small models follow instructions in the user's text; no verdict is allowed and the legal-decision target is 100%, so one failure there misses it; the other three categories need at least 80% |
| **When / where** | Sprints 2–4; development and pilot |
| **Mitigation** | Rule-based checks before and after the model call (input check, decision-phrase and verdict check) and a fixed system prompt ([Major Activities](04-major-activities.md) rows 11–12: out-of-scope and legal-decision notices, input and output safety checks); every safety category is in the `dev` split (D2, D8) |
| **Probability (basis)** | 3: prompt injection succeeds often on small models; not measured yet |
| **Impact (basis)** | 4: O4 success criterion and D9 criteria 3–4 |
| **Score** | 12 (High) |
| **Trigger** | Early warning: at least one compliance verdict, or wrong responses to more than half of the `dev` safety questions of any category, with the alpha on 18/11/2026. Main trigger on 09/12/2026 (D9): at least one answer with a classification or compliance verdict, a wrong response to any legal-decision question, or fewer than 80% expected responses in any of the other three categories |
| **Contingency plan (B plan)** | For the failing category, replace the generated answer with a fixed notice for that category: a refusal or out-of-scope or insufficient-evidence notice with a one-sentence reason, plus a pointer to the relevant provision only where one exists; no provision is cited for prompt-injection or fully out-of-scope questions. Report the O4 result per category in D9 and D12 |
| **Owner** | Gözde Nur (Development Team Member; safety checks) |
| **Schedule effect** | Under 1 week |

### Risk R-14: Alpha not working end to end

| Field | Content |
|---|---|
| **Risk (event)** | The alpha does not answer every `dev` question end to end by 18/11/2026 (M4) |
| **Linked to** | C-07 |
| **Cause** | No production code in Sprint 1 (C-07); parsing, retrieval, the model and the web page are joined for the first time in Sprint 2 |
| **When / where** | Sprint 2; development |
| **Mitigation** | Sprint 1 spikes on parsing and on running the model ([Major Activities](04-major-activities.md) rows 6–7); one question answered end to end by the middle of Sprint 2 before any part is extended |
| **Probability (basis)** | 3: first integration of four parts within one 2-week sprint |
| **Impact (basis)** | 4: D6 criterion 2; the beta starts late |
| **Score** | 12 (High) |
| **Trigger** | No question answered end to end on 11/11/2026, or fewer than 100% of `dev` questions answered without error on 18/11/2026 |
| **Contingency plan (B plan)** | Reduce the alpha to the minimum flow (question, retrieval, answer with citation and version date) running from `README.md` on one machine. At M6 (20/11/2026) the Product Owner decides the beta scope based on whether this minimum flow works on the `dev` questions: if it does not, features 5–7 are deferred and Sprint 3 starts with completing the alpha; the decision is recorded in the M6 checkpoint notes and in D9 (criterion 5). The gap 19/11–24/11 is used only as an optional fix buffer, not as planned development time |
| **Owner** | Yeşim (Product Owner) |
| **Schedule effect** | About 1 week, taken from the beta features |

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
