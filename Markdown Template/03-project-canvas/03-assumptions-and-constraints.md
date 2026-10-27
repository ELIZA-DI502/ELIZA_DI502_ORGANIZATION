# Assumptions & Constraints

This page records what your plan rests on. It has two parts:

- An **assumption** is something you treat as true for planning, but have not proven yet. It is a documented bet that you commit to checking.
- A **constraint** is a fixed limit you must work within. It is not uncertain. It bounds the project, especially its scope.

"The dataset will be sufficient" is a weak assumption. "Sufficient" is not defined, nobody can test it, and nobody is responsible for checking it. A strong version says what the bet is based on, how it will be checked, by whom and by when: "The supplied dataset of about 12,000 labelled queries covers the 8 intents in scope, with at least 300 examples each. The Data Scientist preparing the data checks this with an exploratory analysis by the end of Sprint 1." (numbers illustrative only)

The project uses RAG as its basic solution; this is a constraint set by the Project Review Committee, so it should be reflected here.

## Assumption, constraint, risk or out of scope?

Each statement belongs in exactly one place. Use this table to decide where.

| Entry | What it is | Question it answers | Where it goes |
|---|---|---|---|
| **Assumption** | An uncertain belief you plan around, not yet proven | What are we betting on, and how will we check it? | Table 1 on this page |
| **Constraint** | A fixed limit, not uncertain; a rule that limits how the in-scope work is done | What can we not change? | Table 2 on this page |
| **Risk** | An uncertain event that would hurt the project if it happens | What could go wrong, and what will we do about it? | [Risks](11-risks.md) |
| **Out-of-scope activity** | Work the team will not do at all | What are we not building? | [Major Activities](04-major-activities.md), Status = Out of Scope |

## How the entries connect

**Every assumption has a risk on its flip side.** If you assume the dataset covers the in-scope categories, the matching risk is that some categories are under-represented and perform poorly. Log the assumption here and register the matching risk in [Risks](11-risks.md). Cross-reference them by ID, for example A-03 ↔ R-07. An assumption that might not hold must always appear in Risks with a response plan.

**A constraint often creates or removes work.** Write such a decision as three statements, one per place, each pointing to the others:

1. The constraint (this page): the rule the system must obey.
2. An in-scope activity ([Major Activities](04-major-activities.md)): the work you do because of the rule.
3. An out-of-scope activity ([Major Activities](04-major-activities.md)): the features you give up because of it.

The uncertain part of a constraint becomes a risk, and the in-scope activity is its mitigation.

**Scope protects your assumptions.** Define the intended operating domain (users, inputs, languages, categories) and list what is out of scope. Your assumptions then only have to hold inside that boundary. A failure outside the boundary is a documented limitation, not a broken assumption.

**One concern can produce several entries.** For example:

| Entry | Example |
|---|---|
| Constraint | The project will be developed by four students. No additional recruitment is possible. |
| Risk | A member of the team may leave the team or cannot dedicate the required time. |
| Assumption | All defined team members will remain enrolled in the course and continue participation for the full duration of the project. |

To make that assumption checkable, give it an owner and a validation date, for example "checked at each sprint start by the named member" (illustrative only).

## Fields

### Table 1: Assumptions

| Field | What it means | Question it answers |
|---|---|---|
| **#** | ID in the form A-01, A-02, … | Which risk refers to this assumption? |
| **Assumption** | The belief, stated with numbers or a named condition | What exactly are we betting on? |
| **Basis** | The evidence the belief rests on | Based on what? |
| **Validation** | How the belief will be checked, and the date or sprint | How and by when will we know? |
| **Owner** | The named person who does the check | Who is responsible for checking? |
| **Linked risk** | ID of the matching risk in [Risks](11-risks.md) | What happens if the bet is wrong? |

### Table 2: Constraints

| Field | What it means | Question it answers |
|---|---|---|
| **#** | ID in the form C-01, C-02, … | Which activities and risks refer to this constraint? |
| **Category** | One of the five layers used in [Risks](11-risks.md): Data, Model, Infrastructure, Integration, People / process | What kind of limit is this? |
| **Constraints** | The fixed limit, stated as a fact | What can we not change? |
| **Linked activities / risks** | IDs or row numbers in [Major Activities](04-major-activities.md) and [Risks](11-risks.md) | What work does it create or remove, and what is uncertain about it? |

Legal, budget and schedule limits all go under People / process. Technical limits go under Data, Model, Infrastructure or Integration, so that you can describe the technical side in more detail.

## Rules

Assumptions:

1. An assumption could turn out false, and being wrong would visibly change the plan. If it couldn't be wrong, or being wrong wouldn't matter, delete it.
2. An assumption is specific. It uses no undefined words such as "sufficient", "enough" or "stable" without a number.
3. An assumption states its basis.
4. An assumption has a validation method, a date or sprint, and a named owner.
5. An assumption has a linked risk in [Risks](11-risks.md).
6. An assumption concerns a matter outside the project's control. A commitment the team makes about its own work is a plan, not an assumption.
7. These are not assumptions:
   - The performance of the selected LLM, embedding model or API ("the API will work seamlessly"). Handle these as risks.
   - Expected user behaviour ("users will ask contextually related questions"). Define the input boundary as a constraint instead.
   - Having enough resources, such as cloud credits. This is a constraint.
   - "Milestones will be achieved on time". This is a goal.
   - "The system will not have downtimes". This is a desired outcome; restate it as a risk.

Constraints:

8. A constraint is stated as a fact, not as a hope. Write "Compute is limited to the allocated credit", not "The credit will be enough".
9. A constraint gives the number or names the rule; it uses no adjectives such as "limited" or "relatively short".
10. Every constraint has a category, and constraints are grouped by category.
11. A limit the system operates within is a constraint, for example a user-input boundary or English-only text. Work you will not do goes to [Major Activities](04-major-activities.md) as Out of Scope.
12. A constraint that creates or removes work has its matching in-scope and out-of-scope rows in [Major Activities](04-major-activities.md), and each statement points to the others.
13. "Limited computational resources" is a constraint. The assigned resources fluctuating or failing is a risk.

Both:

14. The same statement does not appear as both an assumption and a constraint. Duplicates are an internal inconsistency in the review error types.

## Tests to apply to your draft

**For each assumption, answer four questions.** If you cannot answer one, fix the row.

1. **Based on what?** Name the evidence.
2. **Could it be wrong, and would that change the plan?** If not, delete it.
3. **Who checks it, how, and by when?**
4. **Is it outside our control?** If not, it is a task or a plan, not an assumption.

**For each constraint, answer three questions.**

1. **Is it fixed?** If it is uncertain, it is an assumption or a risk.
2. **Is there a number or a named rule?**
3. **Does it create or remove work?** If yes, the matching rows exist in [Major Activities](04-major-activities.md).

## Not this / this

The left column shows weak entries. Each row names the rule it breaks. The corrected version fixes only that defect. Numbers on the right are illustrative only.

| Not this | Rule broken | This |
|---|---|---|
| "The dataset has enough entries to sufficiently answer questions." | Vague and untestable, with no owner or date (rules 2–4) | "The supplied dataset has at least 200 entries for each of the 6 in-scope topics. Basis: row counts on the dataset's public page. The Data Scientist preparing the data checks this with a per-topic count by the end of Sprint 1. Linked risk: R-02." |
| "Users will ask contextually related questions about the indexed content." | Expected user behaviour is not an assumption (rule 7) | Constraint (Model): "The system handles single-turn, fact-seeking questions about the indexed content only." Plus risk: "Users ask out-of-scope questions and receive confident wrong answers." |
| "The system will not perform complex actions, and will focus on simple questions and answers." | A scope limit written as an assumption (rule 11) | Constraint (Model): "The system answers questions only; it performs no actions on the user's behalf." Plus an out-of-scope row in [Major Activities](04-major-activities.md): "Transactions or account actions for the user." |
| "The project team will have consistent access to the necessary computational resources." | Available resources are a constraint, not an assumption (rule 7) | Constraint (Infrastructure): "Compute is limited to one shared GPU allocation from the university." Plus risk: "The assigned GPU allocation fluctuates or becomes unavailable." |
| "The external data APIs will remain accessible and stable during the project period." | API behaviour is not an assumption (rule 7) | A row in [Dependencies](06-dependencies.md) for the API, and a risk in [Risks](11-risks.md): "The external data API changes its endpoints or is unavailable for more than 1 day." |
| "The free-tier access limits of these APIs will be sufficient for development and testing." | "Sufficient" is vague, and the limit itself is a constraint (rules 2, 7) | Constraint (Integration): "The API free tier allows 500 calls per day." Assumption: "The test plan needs at most 300 calls per day. Basis: planned test-set size × runs per day. Checked by the owner of the evaluation scripts by the end of Sprint 2. Linked risk: R-05." |
| "The project team will maintain continuous internal coordination and follow sprint planning practices." | Within the team's control, so not an assumption (rule 6) | Remove it. Coordination is planned work; put it in [Major Activities](04-major-activities.md) (project management). |
| "The cloud credit provided will be enough to complete the project." | A constraint stated as a hope (rule 8) | Constraint (People / process): "Compute spending is limited to the cloud credit allocated by the university." Assumption: "Planned experiments use at most 70% of that credit. Basis: cost of the Sprint 1 pilot run. Checked by the Data Scientist running experiments by the end of Sprint 2. Linked risk: R-04." |
| "Team members have relatively limited time to work on the project." | Adjective instead of a number (rule 9) | Constraint (People / process): "Each team member works on the project at most 5 hours per week." |
| "The system relies on third-party APIs, so any downtime or API change may affect performance." | Describes an uncertain event, so not a fixed limit (rule 8) | A row in [Dependencies](06-dependencies.md) for the reliance, and a risk in [Risks](11-risks.md) for the downtime. |
| "English" listed both as Assumption 1 and as a constraint. | Duplicate entry (rule 14) | Keep only the constraint (Data): "The system is developed and evaluated on English-language text only." |

A good entry to copy: "The dataset is not a data stream, so some information may not be up to date." It is a fixed, specific limit. It could be sharpened with the date range of the data.

## Patterns to use if you are stuck

Assumption patterns. Each one is concrete, could be false, and would change the plan if it were:

- **Representativeness:** the historical data is representative of the data the system will see after deployment.
- **Label quality:** labels have an error rate below about 5%, checked by manually reviewing a random sample of 200 records.
- **Expert time:** domain experts are available at least 2 hours per week for labelling questions and result review.
- **Environment access:** access to the production or staging environment is provided by week 4.
- **Permission to use data:** using the data for training is permitted under the data agreement and privacy rules, confirmed with the data owner before training begins.
- **Agreed target:** stakeholders agree that a stated metric value on the held-out test set is acceptable for the first release.

Constraint patterns:

- **User-input boundary:** "The system's functional scope is limited to single-turn, contextually related, fact-seeking queries about the indexed content."
- **Language:** "Working with English text only."
- **Team size:** "Four students; no additional recruitment is possible."
- **Compute limit:** a fixed allocation or quota.
- **Privacy rule**, written with its activities:
  - Constraint: "The system shall not persist personally identifiable information (e.g., names, email addresses, national ID numbers) in any database, log or vector index."
  - In scope ([Major Activities](04-major-activities.md)): "Implement PII detection and masking on user inputs before logging." "Configure logs to keep only anonymized interaction data."
  - Out of scope ([Major Activities](04-major-activities.md)): "User accounts, personal profiles, and saved conversation history linked to an identity."
  - Risk ([Risks](11-risks.md)): "Users submit PII in free-text queries, and it ends up in logs or the retrieval index." The masking activity is the mitigation; a review of the logs is the check.

## What doesn't belong here

- **Risk plans** (mitigation, trigger, contingency, owner) go in [Risks](11-risks.md). This page keeps only the ID of the linked risk.
- **Features you will not build** go in [Major Activities](04-major-activities.md) as Out of Scope.
- **Who must deliver what, by when** goes in [Dependencies](06-dependencies.md).
- **The list of tools, compute and data access** goes in [Facilities & Resources](09-facilities-and-resources.md). A fixed limit on one of them stays here as a constraint.
- **Effort and cost figures** go in [Cost & Funding](07-cost-and-funding.md).
- **Goals and targets** go in the objectives of [Project Executive Summary](01-project-executive-summary.md).
- **Milestone dates** go in [Milestones](02-milestones.md). A mandated deadline stays here as a constraint.

CONFLICT: the template says the budget constraint is defined in the Project Executive Summary, but it also lists a set budget as a constraint on this page. Until this is resolved, make the two statements identical.

## 1. Assumptions

Add rows as needed.

| # | Assumption | Basis | Validation (how, by when) | Owner | Linked risk |
|---|---|---|---|---|---|
| A-01 | The EUR-Lex consolidated text of 27/07/2026, which the assistant uses, has the same wording as the official text in the Official Journal for every in-scope provision. (The consolidated text puts the original Act and its later changes into one document; only the Official Journal text is legally valid.) | EUR-Lex makes the consolidated text from the Official Journal texts, but says that it is only a working copy. | By 18/11/2026, compare the provisions changed by the 2026 amendment, Annex III point 3, Article 6 and Article 113 word by word with the Official Journal. For the other in-scope provisions, check that no paragraph or point is missing. Write down every difference. | Yeşim (Product Owner; source corpus) | R-01 |
| A-02 | No new law changes the wording or the start date of an in-scope provision before the project ends (30/12/2026), so the 27/07/2026 text stays up to date. | The last change, Regulation (EU) 2026/1744, is already in the 27/07/2026 text. | At the start of every sprint from Sprint 2, check EUR-Lex for a newer version. If an in-scope provision has changed, record what it affects; the Product Owner decides whether to switch to the new text, and the decision is recorded in section 6 of the [System Design Document](../11-system-architecture-design-document.md). | Yaren (Scrum Master) | R-02 |
| A-03 | For every evaluation question (20–30 in v1, at least 40 in v2), a team member without legal training can find the provision that answers it (the Article, paragraph or Annex point). | The regulation is split into numbered Articles, paragraphs and points, and each question is written about one education use case from the regulation. | By 11/11/2026 (D2), link every v1 question to its provisions and check them in the official text. A question that needs a legal opinion, or on which the writer and the second reviewer disagree, is rewritten or removed, and the change is logged. | Kaan (Data Scientist; evaluation questions) | R-11 |
| A-04 | At least 5 people who work in software or AI can take part in the pilot (a timed search task and a survey) between 16/12 and 23/12/2026. | The team members know such people through work; the team has no access to a real EdTech team. | By 18/11/2026, get 5 names with confirmed pilot dates. | Gözde Nur (Data Scientist; pilot) | R-03 |
| A-05 | The official text marks its Articles, paragraphs and Annex points in a way that lets a script cut it into chunks with the right number on each chunk; at most 5% of the chunks need to be fixed by hand. | In the EUR-Lex HTML, Articles, paragraphs and Annex points are separate elements. | First check in the Sprint 1 [parsing spike](../../docs/spikes/parsing-spike.md), on the PDF (25/10/2026): all 22 chunks of Article 6 and Annex III point 3 got the right number. The HTML is checked when it is stored in Sprint 2 (KAN-92). Full check in D5 (14/11/2026): the chunks are compared with the table of contents, and 20 random chunks are compared word by word with the text. A chunk counts as fixed by hand if its number, its start or end, or its text had to be changed. | Yeşim (Product Owner; source corpus) | R-12 |
| A-06 | The Project Review Committee agrees with our target levels in the Project Executive Summary: for evidence (O2), the expected provision is cited for at least 80% of the in-scope questions, and at least 75% of the in-scope answers are fully supported by the text they cite; for safety (O4), no answer gives a legal verdict, 100% of the legal-decision questions get the expected response, and at least 80% of the questions in each of the other three safety categories (out of scope, missing evidence, adversarial) get it. | The levels follow the example acceptance criteria given in the course. | Ask the committee at the Sprint 1 review (28/10/2026) and write the answer into Project Charter v2 (14/11/2026). | Yeşim (Product Owner) | R-04 |
| A-07 | At least 3 of the 5 pilot users have worked on an AI or education software product, so they are similar to our real users (technical teams building AI systems for education). | The candidates work in software and AI, but not all of them work on education products. | Ask each candidate about their work when inviting them; check when the 5 users are confirmed, by 18/11/2026. | Gözde Nur (Data Scientist; pilot) | R-09 |
| A-08 | All four team members stay in the course and keep working on the project until 30/12/2026. | All four are registered for the autumn term and agreed to the team plan at the start. | The Scrum Master checks at the start of every sprint. | Yaren (Scrum Master) | R-06 |
| A-09 | The licences of the chosen language model and embedding model allow us to use them in this university project and to publish the answers they produce. | Open-source models state their licence on their model page (for example Apache 2.0, MIT, or a community licence with extra rules). | Read the licence of every candidate model before its decision in the System Design Document is accepted, by 27/10/2026, and record it in the SBOM (`10-software-bill-of-materials.md`, D6). | Kaan (Data Scientist; model licences) | R-07 |

## 2. Constraints

Group constraints by category. Add rows as needed.

| # | Category | Constraints | Linked activities / risks |
|---|---|---|---|
| C-01 | Data | The knowledge base contains one source only: the consolidated text of Regulation (EU) 2024/1689, version of 27/07/2026 (151 pages), from EUR-Lex, limited to the in-scope provisions listed in the [Project Executive Summary](01-project-executive-summary.md). | [Major Activities](04-major-activities.md) rows 4, 8 (in scope: source manifest, parsing and chunking), row 18 (out of scope: GDPR, national law, other laws and Commission guidelines); [Risks](11-risks.md) R-01, R-02 |
| C-02 | Data | The system is developed and evaluated on English-language text only, for both questions and the source text. | [Major Activities](04-major-activities.md) row 19 (out of scope: answers in Turkish or other languages) |
| C-03 | Model | The solution is a RAG chatbot with an open-source, quantized language model (DI 502 minimum project requirements: a chatbot application, a RAG system and quantized language models; course tool list: open-source quantized language models). | [Major Activities](04-major-activities.md) rows 6, 9, 10 (in scope: model selection spike, retrieval pipeline, answer generation), row 17 (out of scope: model training or fine-tuning); [Risks](11-risks.md) R-07 (model or library changes) |
| C-04 | Model | The system answers questions about the in-scope provisions for the four education use cases in Annex III point 3 (admission, assessment, level placement, exam monitoring) and their boundary cases only. If follow-up questions are built (Feature 7, not committed), they are supported within one session only; nothing is kept between sessions. Questions outside this boundary receive an out-of-scope notice that names what the assistant covers (Jira KAN-5). | [Major Activities](04-major-activities.md) rows 11, 15 (in scope: out-of-scope notices; follow-ups within one session if built), rows 20, 21 (out of scope: non-education domains, deployer obligations, GPAI model provider obligations, enforcement and penalties, conversation history across sessions) |
| C-05 | Infrastructure | The system runs on CPU only, including the pilot and the final demo, which run locally from `README.md` on a team computer. A GPU (Google Colab, or one team member's computer) may be used to speed up offline experiments; the answer time and the final evaluation are measured on CPU. | [Major Activities](04-major-activities.md) rows 6, 28, 29 (in scope: CPU-only model spike, local run from the README, pilot and demo computer), rows 17, 31 (out of scope: model training, hosted cloud deployment); [Facilities & Resources](09-facilities-and-resources.md); [Risks](11-risks.md) R-10 (installation on the pilot computer), R-13 (answer time on the pilot computer) |
| C-06 | People / process | Budget: $100 of Google Cloud credits from the course. The plan does not depend on it; it is kept as a reserve in case the model cannot run on the team's computers within the answer-time limit (R-13). | [Project Executive Summary](01-project-executive-summary.md); [Facilities & Resources](09-facilities-and-resources.md) row 3; [Major Activities](04-major-activities.md) row 31 (out of scope: hosted cloud deployment and cost tracking); [Risks](11-risks.md) R-13 |
| C-07 | People / process | Four students; no additional recruitment is possible. Duration: 4 sprints, 14/10/2026 – 30/12/2026. No production code is written in Sprint 1 (course rule). | [Release Plan](10-release-plan.md); [Major Activities](04-major-activities.md) rows 6, 7 (in scope: spikes), row 39 (out of scope: production code in Sprint 1); A-08; [Risks](11-risks.md) R-06, R-08 |
| C-08 | People / process | The system provides information, not legal advice: it gives no compliance decision or high-risk classification. EUR-Lex consolidated texts are documentation tools; the legally authentic texts are those published in the Official Journal. | [Major Activities](04-major-activities.md) rows 10, 11, 12, 14 (in scope: authenticity note, out-of-scope and legal-decision notices, safety checks, "not legal advice" notice), row 22 (out of scope: legal advice and compliance decisions); checked by the O4 safety evaluation ([Deliverables](05-deliverables.md) D9 criteria 3–4, D11 criteria 2–3); Jira KAN-2 |
| C-09 | People / process | EUR-Lex content is reused with source acknowledgement, as required by Commission Decision 2011/833/EU. | [Major Activities](04-major-activities.md) rows 4, 10 (in scope: reuse basis in the manifest; source and version date shown with every answer) |
| C-10 | People / process | The system does not request personal data. User questions and conversation history are not written to any log or to the vector index. The question-answer pairs of the active session are kept in the session database only while the session lasts and are deleted when the session ends (System Design Document, design decision D4); no earlier session is kept. Users are reminded not to enter personal data. | [Major Activities](04-major-activities.md) rows 12, 13, 15, 30 (in scope: safety checks, personal-data reminder and input check, conversation kept only for the session and deleted at its end, no question logging), row 21 (out of scope: user accounts and saved conversation history); checked by the privacy check ([Deliverables](05-deliverables.md) D9 criterion 8) |

## Example (illustrative only)

Scenario: a legal research assistant, a RAG chatbot over legal documents. All names, numbers and dates are illustrative.

| # | Assumption | Basis | Validation (how, by when) | Owner | Linked risk |
|---|---|---|---|---|---|
| A-01 | The document set (statutes and case summaries, 2015 onward) covers the 5 practice areas in scope, with at least 150 documents each. | Index listing published by the data provider | Per-area document count, end of Sprint 1 | Data Scientist (named member) | R-01 |
| A-02 | A legal expert is available at least 2 hours per week to review answers. | Verbal agreement at kick-off | Confirm in writing; check attendance at each sprint review | Business Analyst (named member) | R-06 |
| A-03 | Using the documents for retrieval is permitted under their licence. | Licence text on the provider's site | Confirm with the data owner before indexing, Sprint 1 | Business Analyst (named member) | R-07 |
| A-04 | The allocated GPU quota supports the latency target for 20 concurrent users. | Vendor benchmark for the chosen model size | Capacity test, end of Sprint 2 | Data Scientist, infrastructure (named member) | R-04 (the latency example in [Risks](11-risks.md)) |

| # | Category | Constraints | Linked activities / risks |
|---|---|---|---|
| C-01 | People / process | Four students; no additional recruitment; at most 5 hours per member per week. | [Risks](11-risks.md) R-08 |
| C-02 | Infrastructure | Compute is limited to the cloud credit allocated by the university. | [Facilities & Resources](09-facilities-and-resources.md) row 1; [Risks](11-risks.md) R-04 |
| C-03 | People / process | The system shall not persist PII in any database, log or vector index. | [Major Activities](04-major-activities.md) rows 7 (in scope: masking) and 12 (out of scope: user accounts); [Risks](11-risks.md) R-03 |
| C-04 | Model | Single-turn, fact-seeking questions about the indexed documents only; English text only. | [Major Activities](04-major-activities.md) row 13 (out of scope: multi-turn memory) |
| C-05 | Integration | The hosted LLM API allows 500 calls per day on the academic tier. | [Facilities & Resources](09-facilities-and-resources.md) row 2; [Risks](11-risks.md) R-05 |

## Checklist before submitting

- [x] Every assumption could turn out false, and being wrong would change the plan (rule 1)
- [x] No assumption uses an undefined word such as "sufficient", "enough" or "stable" (rule 2)
- [x] Every assumption has a Basis (rule 3)
- [x] Every assumption has a validation method, a date or sprint, and a named owner (rule 4)
- [x] Every assumption has a Linked risk, and that risk exists in [Risks](11-risks.md) with the same ID (rule 5)
- [x] No assumption is about the team's own work, model or API performance, user behaviour, available resources, goals or desired outcomes (rules 6–7)
- [x] Every constraint is stated as a fact, with a number or a named rule and no adjectives (rules 8–9)
- [x] Every constraint has one of the five categories, and constraints are grouped by category (rule 10)
- [x] Every constraint that creates or removes work has its rows in [Major Activities](04-major-activities.md), and the IDs point both ways (rules 11–12)
- [x] No statement appears as both an assumption and a constraint (rule 14)
- [x] The budget statement here matches the one in [Project Executive Summary](01-project-executive-summary.md)
