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

Probability is residual (after mitigation). Sprint dates: Sprint 1 14/10–28/10, Sprint 2 04/11–18/11, Sprint 3 25/11–09/12, Sprint 4 16/12–30/12/2026. Rows with a score of 10 or more have a detail block below.

| # | Layer | Risk (event) | When / where | Probability | Impact | Score | Owner | Linked to |
|---|---|---|---|---|---|---|---|---|
| R-01 | Data | The consolidated text differs from the Official Journal wording in at least one in-scope provision. | Sprint 2; development | 1 (basis: the consolidated text is produced by the EU Publications Office from the Official Journal acts) | 4 (a wrong provision text breaks the O2 Grounded acceptance criteria) | 4 (Low) | Yeşim | A-01, C-01 |
| R-02 | Data | A new amending act changes an in-scope provision before 30/12/2026, or after the release, so answers become outdated. | Sprints 2–4; development and after deployment | 2 (basis: the last amendment, Reg. (EU) 2026/1744, was adopted on 08/07/2026; amending acts take months from proposal to adoption) | 3 (re-indexing and re-checking the evaluation set takes 1–2 weeks) | 6 (Medium) | Yaren | A-02, C-01 |
| R-03 | Data | For more than 3 evaluation questions, the expected provision cannot be fixed at paragraph or point level. | Sprints 1–2; development | 2 (basis: in our check of the public benchmark (Davvetas et al., 2026), 1 of the 32 in-scope question–answer pairs cited the wrong Article and 1 was doubtful) | 4 (gold sources are needed for the O2 Grounded measurement in D6 and D12) | 8 (Medium) | Kaan | A-03 |
| R-04 | People / process | Fewer than 5 pilot users take part in the D11 pilot evaluation. | Sprints 3–4; validation | 3 (basis: 0 of 5 participants confirmed on 18/10/2026) | 4 (O1 Faster and O3 Clear cannot be measured as planned in D11) | 12 (High) | Gözde Nur | A-04 |
| R-05 | Model | The assistant gives a substantive answer to out-of-scope questions instead of an out-of-scope notice. | Sprints 2–4; development and after deployment | 3 (basis: not yet measured; first measured on the D2 out-of-scope questions with the alpha, Sprint 2) | 4 (the O4 Safe criterion in D9 and D12 is not met) | 12 (High) | Yeşim | C-04; Major Activities: out-of-scope notice |
| R-06 | Integration | The licence of the selected open-source LLM or embedding model does not permit its use in the project. | Sprint 1; development | 2 (basis: licences differ between candidate models: Apache 2.0, MIT and community licences with extra terms) | 2 (another candidate model is chosen; under 2 weeks) | 4 (Low) | Gözde Nur | A-06, C-03 |
| R-07 | Data | Splitting the EUR-Lex text into provision-level chunks needs manual correction for more than 10 provisions. | Sprints 1–2; development | 2 (basis: a test split of the 27/07/2026 text gave 188 provision-level chunks for 19 Articles and Annex III) | 2 (1–2 weeks of manual work) | 4 (Low) | Yeşim | A-05 |
| R-08 | People / process | Cloud spending passes $70 before the end of Sprint 3. | Sprints 2–4; development | 2 (basis: the instance is billed per running hour and is stopped when not in use; mitigation: budget alerts at $50 and $70) | 4 (no money left for the pilot and the final demo; >20% of the budget) | 8 (Medium) | Kaan | A-07, C-06 |
| R-09 | Data | Pilot users rate the evaluation questions as unrealistic (fewer than 4 of 5 rate them 4 or 5 out of 5). | Sprint 4; validation | 2 (basis: the questions are adapted from the education scenarios of a published benchmark (Davvetas et al., 2026)) | 2 (a secondary check; the question set is revised for D13) | 4 (Low) | Yaren | A-08 |
| R-10 | Infrastructure | Without a GPU, the median response time is longer than the median time of a manual search, so O1 Faster is not met. | Sprints 2–4; development and after deployment | 3 (basis: CPU-only generation is slower than GPU generation; to be measured in the Sprint 1 spike on running a quantized LLM) | 4 (O1 Faster is a success criterion) | 12 (High) | Gözde Nur | C-05 |
| R-11 | People / process | A team member cannot work on the project for more than 2 weeks. | Sprints 1–4; development | 2 (basis: all four members have worked on the charter and Jira in Sprint 1) | 3 (deliverables move by 2–4 weeks) | 6 (Medium) | Yaren | C-07 |
| R-12 | Data | A user types personal data into a question and it is stored in a log. | Sprints 2–4; development and after deployment | 3 (basis: questions are free text, and D2 includes personal-data inputs on purpose) | 3 (C-10 is broken; logs must be cleaned) | 9 (Medium) | Kaan | C-10; Major Activities: logging without user identity |
| R-13 | Model | An answer contains a compliance verdict ("your system is high-risk") or cites a provision that was not retrieved. | Sprints 2–4; development and after deployment | 3 (basis: not yet measured; first measured on the D2 legal-decision questions with the alpha, Sprint 2) | 4 (D9 and D12 require 0 verdicts and correct citations) | 12 (High) | Yeşim | C-08; Major Activities: no-verdict and citation checks |

## Risk details

### Risk R-04: Not enough pilot users

| Field | Content |
|---|---|
| **Risk (event)** | Fewer than 5 pilot users take part in the D11 pilot evaluation. |
| **Linked to** | A-04 |
| **Cause** | Pilot users are volunteers from the team's professional contacts; December is a busy month. |
| **When / where** | Sprints 3–4; validation |
| **Mitigation** | Each member names 2 candidates by 04/11/2026; the pilot is planned as one 30-minute online session per user. |
| **Probability (basis)** | 3: 0 of 5 participants confirmed on 18/10/2026 |
| **Impact (basis)** | 4: O1 Faster and O3 Clear are measured only in D11 |
| **Score** | 12 (High) |
| **Trigger** | Fewer than 5 confirmed participants on 18/11/2026 (end of Sprint 2) |
| **Contingency plan (B plan)** | Run the pilot with the confirmed users plus METU students from other DI 502 teams as proxy users, and report the smaller sample as a limitation in D11. |
| **Owner** | Gözde Nur |
| **Schedule effect** | About 1 week |

### Risk R-05: Out-of-scope questions are answered

| Field | Content |
|---|---|
| **Risk (event)** | The assistant gives a substantive answer to out-of-scope questions instead of an out-of-scope notice. |
| **Linked to** | C-04 |
| **Cause** | Small open-source LLMs tend to answer from their general knowledge when the retrieved text does not cover the question. |
| **When / where** | Sprints 2–4; development and after deployment |
| **Mitigation** | In-scope activity "out-of-scope notice" in Major Activities: an input check before retrieval and a "no evidence, no answer" rule in the prompt. |
| **Probability (basis)** | 3: not yet measured; first measured with the alpha on the D2 out-of-scope questions, Sprint 2 |
| **Impact (basis)** | 4: the O4 Safe criterion in D9 and D12 is not met |
| **Score** | 12 (High) |
| **Trigger** | Fewer than 8 of 10 out-of-scope `dev` questions receive the notice at the end of Sprint 2 (18/11/2026) |
| **Contingency plan (B plan)** | Degrade gracefully: when the input check marks a question as uncertain, show only the retrieved provisions and the out-of-scope notice, without a generated answer. |
| **Owner** | Yeşim |
| **Schedule effect** | About 1 week |

### Risk R-10: Answers are too slow without a GPU

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

### Risk R-13: Compliance verdict or wrong citation in an answer

| Field | Content |
|---|---|
| **Risk (event)** | An answer contains a compliance verdict ("your system is high-risk") or cites a provision that was not retrieved. |
| **Linked to** | C-08 |
| **Cause** | Users ask for yes/no decisions; small LLMs do not always follow "do not decide" instructions and can invent references. |
| **When / where** | Sprints 2–4; development and after deployment |
| **Mitigation** | In-scope activities "no-verdict check" and "citation-ID check" in Major Activities: every cited ID must match a retrieved chunk, and verdict phrases are blocked before the answer is shown. |
| **Probability (basis)** | 3: not yet measured; first measured with the alpha on the D2 legal-decision questions, Sprint 2 |
| **Impact (basis)** | 4: D9 and D12 require 0 verdicts and correct citations |
| **Score** | 12 (High) |
| **Trigger** | At least 1 verdict or 1 citation that does not match a retrieved chunk on the `dev` split at the end of Sprint 3 (09/12/2026) |
| **Contingency plan (B plan)** | Hand over to a human: for legal-decision questions, show only the relevant provisions and a fixed notice that refers the decision to the legal team, without a generated text. |
| **Owner** | Yeşim |
| **Schedule effect** | About 1 week |

## Checklist before submitting

- [ ] At least 5 risks
- [ ] At least one risk from each of the five layers (data / model / infrastructure / integration / people-process)
- [ ] Every risk is written as an event, with when and where
- [ ] Every assumption in [Assumptions & Constraints](03-project-canvas_v2/03-assumptions-and-constraints.md) has a risk here, and the IDs match both ways
- [ ] Every risk that comes from a constraint names the in-scope activity in [Major Activities](03-project-canvas_v2/04-major-activities.md) that mitigates it
- [ ] Probability values are residual (after mitigation), and each has a basis
- [ ] Risks that threaten an acceptance criterion or success criterion have an impact of at least 4
- [ ] Every risk scoring 10 or more has a mitigation, a numeric trigger with a date or sprint, a contingency plan and a named owner
- [ ] Every owner is a named person listed in [Project Organization](03-project-canvas_v2/08-project-organization.md)
- [ ] No contingency plan repeats work already planned under [Major Activities](03-project-canvas_v2/04-major-activities.md)
- [ ] Scores are spread out (not all low, not all high)
- [ ] Risk timings fall inside the project's sprint timeline
