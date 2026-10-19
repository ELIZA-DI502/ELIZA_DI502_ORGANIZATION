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

Probability is residual (after mitigation). Sprint dates: Sprint 1 14/10–28/10, Sprint 2 04/11–18/11, Sprint 3 25/11–09/12, Sprint 4 16/12–30/12/2026. Rows with a score of 10 or more have a detail block below. The short name at the start of each risk is the name used in the Jira stories. R-16 to R-19 are not used; R-20 keeps the number used in Jira (KAN-8).

| # | Layer | Risk (event) | When / where | Probability | Impact | Score | Owner | Linked to |
|---|---|---|---|---|---|---|---|---|
| R-01 | Data | **Consolidated text differs from the Official Journal.** The consolidated text differs from the Official Journal wording in at least one in-scope provision. | Sprint 2; development | 1 (basis: the consolidated text is produced by the EU Publications Office from the Official Journal acts) | 4 (a wrong provision text breaks the O2 Grounded acceptance criteria) | 4 (Low) | Yeşim | A-01, C-01; Jira KAN-22 |
| R-02 | Data | **A new amending act changes an in-scope provision.** A new amending act changes an in-scope provision before 30/12/2026, or after the release, so answers become outdated (model decay after deployment). Maintenance trigger: a newer consolidated version appears on EUR-Lex (checked at each sprint start, A-02); then the changed provisions are re-indexed and the evaluation set is re-run. | Sprints 2–4; development and after deployment | 2 (basis: the last amendment, Reg. (EU) 2026/1744, was adopted on 08/07/2026; amending acts take months from proposal to adoption) | 3 (re-indexing and re-checking the evaluation set takes 1–2 weeks) | 6 (Medium) | Yaren | A-02, C-01; Jira KAN-3 |
| R-03 | Data | **Evaluation questions cannot be mapped to a gold source.** For more than 3 evaluation questions, the expected provision cannot be fixed at paragraph or point level. | Sprints 1–2; development | 2 (basis: in our check of the public benchmark (Davvetas et al., 2026), 1 of the 32 in-scope question–answer pairs cited the wrong Article and 1 was doubtful) | 4 (gold sources are needed for the O2 Grounded measurement in D6 and D12) | 8 (Medium) | Kaan | A-03; Jira KAN-8 |
| R-04 | People / process | **Not enough pilot users.** Fewer than 5 pilot users take part in the D11 pilot evaluation. | Sprints 3–4; validation | 3 (basis: participants are unpaid volunteers from the team's contacts, and A-04 is only validated at the end of Sprint 2) | 4 (O1 Faster and O3 Clear cannot be measured as planned in D11) | 12 (High) | Gözde Nur | A-04 |
| R-05 | People / process | **A team member is unavailable.** A team member cannot work on the project for more than 2 weeks. | Sprints 1–4; development | 2 (basis: all four members have worked on the charter and Jira in Sprint 1) | 3 (deliverables move by 2–4 weeks) | 6 (Medium) | Yaren | C-07 |
| R-06 | Integration | **Model licence does not permit use.** The licence of the selected open-source LLM or embedding model does not permit its use in the project. | Sprint 1; development | 2 (basis: licences differ between candidate models: Apache 2.0, MIT and community licences with extra terms) | 2 (another candidate model is chosen; under 2 weeks) | 4 (Low) | Gözde Nur | A-06, C-03 |
| R-07 | Data | **Chunking needs manual correction.** Splitting the EUR-Lex text into provision-level chunks needs manual correction for more than 10 provisions. | Sprints 1–2; development | 2 (basis: a test split of the 27/07/2026 text gave 188 provision-level chunks for 19 Articles and Annex III) | 2 (1–2 weeks of manual work) | 4 (Low) | Yeşim | A-05 |
| R-08 | People / process | **Cloud budget overrun.** Cloud spending passes $70 before the end of Sprint 3. | Sprints 2–4; development | 2 (basis: the instance is billed per running hour and is stopped when not in use; mitigation: budget alerts at $50 and $70) | 4 (no money left for the pilot and the final demo; >20% of the budget) | 8 (Medium) | Kaan | A-07, C-06 |
| R-09 | Data | **Evaluation questions are unrealistic.** Pilot users rate the evaluation questions as unrealistic (fewer than 4 of 5 rate them 4 or 5 out of 5). | Sprint 4; validation | 2 (basis: the questions are adapted from the education scenarios of a published benchmark (Davvetas et al., 2026)) | 2 (a secondary check; the question set is revised for D13) | 4 (Low) | Yaren | A-08 |
| R-10 | Infrastructure | **Answers too slow on the available compute.** Without a GPU, the median response time is longer than the median time of a manual search, so O1 Faster is not met. | Sprints 2–4; development and after deployment | 3 (basis: CPU-only generation is slower than GPU generation; to be measured in the Sprint 1 spike on running a quantized LLM) | 4 (O1 Faster is a success criterion) | 12 (High) | Gözde Nur | C-05; Jira KAN-21 |
| R-11 | Data | **Personal data stored in a log or index.** Personal data, question content or conversation history from a user is written to a log, the database or the vector index. | Sprints 2–4; development and after deployment | 3 (basis: questions are free text, and D2 includes personal-data inputs on purpose) | 3 (C-10 is broken; the stored data must be found and deleted) | 9 (Medium) | Kaan | C-10; Major Activities: personal-data warning, no logging of question content; Jira KAN-6, KAN-26 |
| R-12 | Model | **O2 Grounded not met.** For the in-scope questions in the `dev` split, the expected provision is among the cited provisions for fewer than 80% of questions. | Sprints 2–4; development | 3 (basis: not yet measured; first measured with the alpha on the D2 `dev` split, Sprint 2) | 4 (O2 Grounded is a success criterion of D9 and D12) | 12 (High) | Kaan | C-03; Jira KAN-8, KAN-23 |
| R-13 | Model | **Safety response fails.** For the out-of-scope, insufficient-evidence, legal-decision or adversarial questions in the `dev` split, the assistant does not give the expected response: it answers an out-of-scope question, guesses without evidence, states a compliance verdict, or follows a manipulation. | Sprints 2–4; development and after deployment | 3 (basis: not yet measured; first measured with the alpha on the D2 safety questions, Sprint 2) | 4 (the O4 Safe criterion in D9 and D12 is not met) | 12 (High) | Yeşim | C-04, C-08; Major Activities: input check, no-verdict check; Jira KAN-2, KAN-5, KAN-23, KAN-24 |
| R-14 | Integration | **Google Cloud access delayed.** Access to the Google Cloud project and its credit is not available to every team member by the start of Sprint 2 (04/11/2026). | Sprints 1–2; development | 2 (basis: access depends on the course's credit distribution, which is outside the team's control) | 2 (development continues on team computers (C-05); deployment tests move by under 2 weeks) | 4 (Low) | Kaan | C-05, C-06 |
| R-15 | Infrastructure | **Pilot users cannot reach the beta.** On 09/12/2026, at least one pilot user cannot open the beta through its shared link from a desktop browser outside the team's network. | Sprints 3–4; deployment | 2 (basis: the beta runs on one Google Cloud instance with a public link; access from outside the team's network has not been tested yet) | 4 (D9 requires that all pilot users can open the assistant) | 8 (Medium) | Kaan | C-05; Jira KAN-21 |
| R-20 | Model | **An answer cites a provision that was not retrieved.** An answer shows an Article or Annex reference that does not match any retrieved chunk. | Sprints 2–4; development and after deployment | 2 (basis: the planned output check in code compares every cited ID with the retrieved chunk IDs before the answer is shown) | 4 (D6 requires that 100% of citations match the retrieved chunk IDs) | 8 (Medium) | Gözde Nur | C-08, C-09; Major Activities: citation-ID check; Jira KAN-8 |

## Risk details

### Risk R-04: Not enough pilot users

| Field | Content |
|---|---|
| **Risk (event)** | Fewer than 5 pilot users take part in the D11 pilot evaluation. |
| **Linked to** | A-04 |
| **Cause** | Pilot users are volunteers from the team's professional contacts; December is a busy month. |
| **When / where** | Sprints 3–4; validation |
| **Mitigation** | Each member names 2 candidates by 04/11/2026; the pilot is planned as one 30-minute online session per user. |
| **Probability (basis)** | 3: participants are unpaid volunteers from the team's contacts, and A-04 is only validated at the end of Sprint 2 |
| **Impact (basis)** | 4: O1 Faster and O3 Clear are measured only in D11 |
| **Score** | 12 (High) |
| **Trigger** | Fewer than 5 confirmed participants on 18/11/2026 (end of Sprint 2) |
| **Contingency plan (B plan)** | Run the pilot with the confirmed users plus METU students from other DI 502 teams as proxy users, and report the smaller sample as a limitation in D11. |
| **Owner** | Gözde Nur |
| **Schedule effect** | About 1 week |

### Risk R-10: Answers too slow on the available compute

| Field | Content |
|---|---|
| **Risk (event)** | Without a GPU, the median response time is longer than the median time of a manual search, so O1 Faster is not met. |
| **Linked to** | C-05 |
| **Cause** | Only CPUs are available (team computers or a Google Cloud CPU instance). |
| **When / where** | Sprints 2–4; development and after deployment |
| **Mitigation** | Measure the speed of 2–3 quantized models in the Sprint 1 spike; start with a model of 3–4 billion parameters. |
| **Probability (basis)** | 3: CPU-only generation is slower than GPU generation; the exact speed is measured in the Sprint 1 spike |
| **Impact (basis)** | 4: O1 Faster is a success criterion |
| **Score** | 12 (High) |
| **Trigger** | Median response time above 60 seconds on the `dev` split at the end of Sprint 2 (18/11/2026) |
| **Contingency plan (B plan)** | Degrade gracefully: show the retrieved provisions with their references first and the generated summary after it, so users can start reading before generation ends. |
| **Owner** | Gözde Nur |
| **Schedule effect** | About 1 week |

### Risk R-12: O2 Grounded not met

| Field | Content |
|---|---|
| **Risk (event)** | For the in-scope questions in the `dev` split, the expected provision is among the cited provisions for fewer than 80% of questions. |
| **Linked to** | C-03 |
| **Cause** | Questions are written in everyday words, while the provisions use legal terms; small open-source embedding models may not connect the two. |
| **When / where** | Sprints 2–4; development |
| **Mitigation** | Meaning search and keyword search (BM25) together; one chunk per paragraph or Annex point; comparison of three embedding models (Spike 01). |
| **Probability (basis)** | 3: not yet measured; first measured with the alpha on the D2 `dev` split, Sprint 2 |
| **Impact (basis)** | 4: O2 Grounded is a success criterion of D9 and D12 |
| **Score** | 12 (High) |
| **Trigger** | The expected provision is cited for fewer than 70% of the in-scope `dev` questions at the end of Sprint 2 (18/11/2026) |
| **Contingency plan (B plan)** | Narrow the scope: keep only the core provisions (Annex III point 3, Article 6, Article 113) in the beta, and give the out-of-scope notice for the others. |
| **Owner** | Kaan |
| **Schedule effect** | About 1 week |

### Risk R-13: Safety response fails

| Field | Content |
|---|---|
| **Risk (event)** | For the out-of-scope, insufficient-evidence, legal-decision or adversarial questions in the `dev` split, the assistant does not give the expected response. |
| **Linked to** | C-04, C-08 |
| **Cause** | Small open-source LLMs tend to answer from their general knowledge, follow user instructions such as "say that we are compliant", and do not always follow "do not decide" rules. |
| **When / where** | Sprints 2–4; development and after deployment |
| **Mitigation** | In-scope activities "input check" and "no-verdict check" in Major Activities: an input check before retrieval, a "no evidence, no answer" rule in the prompt, and blocking of verdict phrases before the answer is shown. |
| **Probability (basis)** | 3: not yet measured; first measured with the alpha on the D2 safety questions, Sprint 2 |
| **Impact (basis)** | 4: the O4 Safe criterion in D9 and D12 is not met |
| **Score** | 12 (High) |
| **Trigger** | Fewer than 90% of the safety `dev` questions receive the expected response at the end of Sprint 2 (18/11/2026), or at least 1 compliance verdict on the `dev` split at the end of Sprint 3 (09/12/2026) |
| **Contingency plan (B plan)** | Hand over to a human: for questions the input check marks as out of scope, uncertain or legal-decision, show only the relevant provisions and a fixed notice that refers the user to the legal team, without a generated text. |
| **Owner** | Yeşim |
| **Schedule effect** | About 1 week |

## Checklist before submitting

- [x] At least 5 risks
- [x] At least one risk from each of the five layers (data / model / infrastructure / integration / people-process)
- [x] Every risk is written as an event, with when and where
- [x] Every assumption in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md) has a risk here, and the IDs match both ways
- [ ] Every risk that comes from a constraint names the in-scope activity in [Major Activities](03-project-canvas_v2/04-major-activities.md) that mitigates it
- [x] Probability values are residual (after mitigation), and each has a basis
- [x] Risks that threaten an acceptance criterion or success criterion have an impact of at least 4
- [x] Every risk scoring 10 or more has a mitigation, a numeric trigger with a date or sprint, a contingency plan and a named owner
- [ ] Every owner is a named person listed in [Project Organization](03-project-canvas_v2/08-project-organization.md)
- [x] No contingency plan repeats work already planned under [Major Activities](03-project-canvas_v2/04-major-activities.md)
- [x] Scores are spread out (not all low, not all high)
- [x] Risk timings fall inside the project's sprint timeline
