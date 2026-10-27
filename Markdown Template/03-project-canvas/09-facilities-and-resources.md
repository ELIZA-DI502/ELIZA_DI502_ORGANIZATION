# Facilities & Resources

This page lists the infrastructure, tools and resources the team needs to support development, who obtains each one, and where it stands.

"Cloud service from the university" is a weak entry. It does not say what is needed, who requests it, or whether it is ready. A strong entry answers all three: "GPU runtime for experiments, one shared allocation under the university cloud credit. Responsible: the Data Scientist who handles infrastructure. Status: access granted on <date>." (illustrative only)

## Resource categories

Cover each category that applies:

| Category | Examples from the template | AI-specific points from the ISO standards |
|---|---|---|
| **Compute & hosting** | GPU access, cloud credits, vector database hosting, deployment environment | Training can need substantial computing power and waiting time [1]. AI systems can consume considerable compute and memory, and GPUs add cost [1]. The runtime environment can differ from the development environment [1]. |
| **APIs & third-party services** | An LLM provider, an embedding service, and any usage/rate limits to plan around | A project can depend on other organizations for infrastructure or capability [1]. |
| **Software & licenses** | Development tools, orchestration frameworks, monitoring/eval tools | — |
| **Data access** | Storage for the corpus, access permissions, special environments for sensitive data | Datasets can be large and are often stored apart from code [1]. Data stores holding sensitive data enlarge the attack surface and need protection [1]. |
| **Physical/logistical needs** | Lab space, shared workstations | — |

Say also *where* each resource runs: on-premise, as a cloud service, or through a third party [2]. A cloud service is a capability offered through cloud computing and used through a defined interface [2].

## Fields

| Field | What it means | Question it answers | Source |
|---|---|---|---|
| **Resource** | The item, named precisely (type, size, provider) | What exactly do we need? | |
| **Description** | What it is used for, where it runs, and any usage or rate limit | Why do we need it, and what limits apply? | [2] |
| **Responsible Person/Team** | Who obtains or provisions it (e.g., requests API credits, sets up cloud accounts, configures shared repositories) | Who makes it happen? | |
| **Status** | Where the item stands now, with a date | Is it ready? | |

Write Status as a short dated fact, such as "requested on <date>" or "access granted on <date>".

## Rules

1. Every category in the table above is either covered or marked as not needed.
2. Every row names a Responsible Person/Team.
3. Every API or third-party service row states its usage or rate limits.
4. Every compute row says what hardware is used and where it runs [2].
5. The deployment environment has its own row.
6. Every data-access row names the storage and the access permissions, and says whether sensitive data needs a special environment [1].
7. Every row has a dated Status.
8. A fixed limit on a resource is also written as a constraint in [Assumptions & Constraints](03-assumptions-and-constraints.md).
9. The chance that a resource fluctuates or fails is a risk in [Risks](11-risks.md).
10. When work waits for someone else to deliver a resource, that wait is also a row in [Dependencies](06-dependencies.md).

## Test to apply to your draft

Could a new team member start work using only this table: knowing what to use, where it runs, whom to ask, and whether it is ready?

## Not this / this

Each row below shows a resource problem that this page would have caught.

| Not this | Rule broken | This (illustrative only) |
|---|---|---|
| The charter names "the cloud service provided by the university" as the project's resource, while the experiment cards report runs on a team member's laptop GPU. | The resource used is not the resource listed (rule 4) | Two compute rows: "Laptop GPU (12 GB VRAM), member-owned, for development runs" and "Cloud GPU under the university credit, for staging and load tests", each with its Responsible person and dated Status. |
| A retrospective notes that API rate limits and latency spikes disrupted response-time tests, and that limited GPU resources forced a mid-sprint move to a paid notebook tier. | Limits not planned in advance (rules 3, 4) | "External data API, free tier: 60 calls per minute; test scripts cache responses." "Notebook GPU, free tier: session limit per day; fine-tuning runs scheduled within it." Plus a constraint for each limit in [Assumptions & Constraints](03-assumptions-and-constraints.md). |

Two good practices to copy:

- Recording access as a precondition: "Team members were granted access permissions for the documentation, task-tracking and repository tools."
- Confirming compute before the work that needs it: "GPU or notebook runtime confirmed for fine-tuning."

## Patterns to use if you are stuck

One row each for:

- **Development compute:** hardware, owner, where it runs.
- **Training or experiment compute:** GPU type and allocation; credit or quota.
- **LLM and embedding access:** hosted locally or through an API; rate limits.
- **Vector database:** where it is hosted.
- **Data storage:** location of raw and processed data; who has access.
- **Shared repository and experiment tracking:** who configures them.
- **Deployment environment:** where the MVP runs.

## What doesn't belong here

- **Costs and person-hours** go in [Cost & Funding](07-cost-and-funding.md).
- **Fixed limits** (a credit amount, a quota) are constraints in [Assumptions & Constraints](03-assumptions-and-constraints.md).
- **A resource failing or fluctuating** is a risk in [Risks](11-risks.md).
- **Waiting for an outside party** is a dependency in [Dependencies](06-dependencies.md).
- **Every third-party library, tool and model with its version and license** goes in [Software Bill of Materials](../10-software-bill-of-materials.md). List here only what the team needs access to.
- **Documentation of the datasets themselves** goes in the [Datasheets](../11-datasheets/README.md) pages. List here only storage and access.

## Resources

Categories: **Compute & hosting** rows 1–3 and 13; **APIs & third-party services** rows 4–5 (no hosted LLM or embedding API is used, so no rate limits apply; the EUR-Lex text is downloaded once, not queried through an API); **Software & licenses** rows 4–6 and 9–12; **Data access** rows 7–8; **Physical/logistical needs**: not needed (row 14).

| # | Resource | Description | Responsible Person/Team | Status |
|---|---|---|---|---|
| 1 | Team members' own computers (4, CPU only; RAM and CPU of each are recorded in the Sprint 1 spike notes by 27/10/2026). Gözde Nur: MacBook Pro 14-inch (2024), Apple M4 (10-core CPU), 16 GB RAM, macOS Sequoia 15.1 ([learning spike](../../docs/spikes/learning-gozde-nur.md)) | Development compute: running the pipeline, the Sprint 1 spikes (source parsing, quantized LLM) and the D6 alpha. On-premise, member-owned. No dedicated GPU (C-05). | Each member for their own computer; Kaan measures the LLM answer time on them in the model selection spike | In use since the start of Sprint 1 (14/10/2026) |
| 2 | Google Colab, free tier | Optional notebook runtime for spikes that do not fit on a team computer. Cloud service (Google). Free-tier session and GPU limits are not guaranteed, so no deliverable depends on it; not used for deployment. | The member who runs the spike | Optional; not used yet (checked on 20/10/2026) |
| 3 | Google Cloud project with the course credit (reserve) | Not used in the plan: the system runs on a team computer (C-05, row 13). The $100 credit (C-06) is kept as a reserve and is used only if the language model cannot meet the answer-time limit on the team computers (A-07; R-13 contingency); in that case billing alerts are set first and a CPU instance runs only during the pilot sessions and the final demo. Cloud service. | Kaan | Not used; kept as a reserve (decided on 25/10/2026) |
| 4 | Open-source quantized LLM, 4-bit, run locally: Llama-3.1-8B-Instruct `Q4_K_M` (Llama 3.1 Community License), fallback Phi-4-mini-instruct `Q4_K_M` (MIT), served by Ollama (D4, design decision D9) | Answer generation. Runs locally on the team computers, including the computer used for the pilot and the final demo (row 13). No hosted API, so no rate limit; the limits are CPU speed and memory (A-07, R-13). Downloaded from Hugging Face; its licence must permit academic use and publication of answers (A-10, R-07). Listed with version and licence in the SBOM (`10-software-bill-of-materials.md`). | Kaan | Chosen in D4 (design decision D9), to be confirmed at M3 (28/10/2026); licence checked (A-10); answer time on one team computer 15 s (model selection spike) |
| 5 | Open-source embedding model: bge-base-en-v1.5 (MIT), via `sentence-transformers` (D4, design decision D10) | Embeds the provision chunks and the questions. Runs locally in the same environments as row 4. No rate limit. Downloaded from Hugging Face; licence as in A-10 (R-07). Listed in the SBOM (`10-software-bill-of-materials.md`). | Kaan | Chosen in D4 (design decision D10), to be confirmed at M3 (28/10/2026); licence checked (A-10) |
| 6 | Vector store and keyword index: Chroma, saved on disk, cosine distance (design decision D11); BM25 keyword index with `rank_bm25`, in memory, used from E2 (design decision D12) | Index of the provision-level chunks (the number of chunks is estimated in the Sprint 1 parsing spike and reported in D5). Runs on the same machine as the application, with no separate hosting service (confirmed in D4). | Kaan | Chosen in D4 (design decisions D11, D12), to be confirmed at M3 (28/10/2026) |
| 7 | Source corpus: consolidated text of Regulation (EU) 2024/1689, version 27/07/2026 (CELEX 02024R1689-20260727), from EUR-Lex | Downloaded once as HTML and stored in the team repository (`data/`), with `data/manifest.csv` (D3). Public legal text with no personal data, so no special environment is needed. Reused with source acknowledgement (C-09). Access: all team members through the repository. | Yeşim (A-01, A-05) | Stored file and manifest due with D3 (27/10/2026) ([Dependencies](06-dependencies.md) row 3; R-01) |
| 8 | Evaluation set and pilot results | `docs/eval/eval-set-v1.csv` (D2), later `eval-set-v2.csv` (D8), and the pilot results (D10), stored in the team repository. Access: team members. Questions taken or adapted from published work keep their source and attribution. Pilot participants are not identified in the files (P1, P2, …). Questions typed into the assistant are not stored (C-10); the evaluation questions contain no personal data. | Yaren (evaluation set and results); Gözde Nur (pilot results, A-04) | Evaluation set due with D2 (11/11/2026); pilot in Sprint 4 (16/12–23/12/2026) |
| 9 | GitHub organisation ELIZA-DI502, repository ELIZA_DI502_ORGANIZATION | Code, charter pages and pull requests. Course template updates are merged in by the `hoca-sync` workflow. Access: the four members and the course reviewers. | Gözde Nur (configured the sync workflow) | In use since 12/10/2026; `hoca-sync` added on 14/10/2026 |
| 10 | Jira project KAN (yarengursoy.atlassian.net), Jira–GitHub sync workflow | Backlog, sprints and story tracking; issues linked to GitHub through Jira keys. The course requires two reviewer accounts on Jira and Confluence: the general reviewer (Reviewer 1) and the team's reviewer (Reviewer 3). | Yaren | In use since 13/10/2026. Reviewer 3 access confirmed; Reviewer 1 invitation pending as of 20/10/2026: Yaren sends the invitations for Jira and Confluence and verifies access before the Sprint 1 review (28/10/2026) |
| 11 | Confluence space "Eliza / DI502" (yarengursoy.atlassian.net) and Confluence sync workflow | Course documentation space; pages synced from the repository on every push to `main`. | Yaren (space); Gözde Nur (sync workflow) | Space created on 04/10/2026; synced from the repository since 18/10/2026 |
| 12 | Experiment tracker (Weights & Biases, free tier, as required by the course) | Cloud-based experiment tracking for the Sprint 2–4 evaluation runs (D6 criterion 5, D9, D11). The free tier is planned; account access, the applicable usage limits and the project visibility settings are checked before the first experiment. No user questions or conversation content are logged (C-10). | Yaren | Planned as of 20/10/2026; account access and free-tier limits to be verified before the first D6 experiment (by 11/11/2026) |
| 13 | Deployment environment: the web application run locally from `README.md` on a team computer; interface technology chosen in D4 | Runs the baseline (D6), the beta (D9) and the release candidate (D11). The pilot (16/12–23/12/2026) and the final demo (30/12/2026) are held in person on this computer, so no shared link or hosted server is needed. Before the pilot, the system is installed on it from the README and its answer time is measured ([Major Activities](04-major-activities.md) row 29; R-10, R-13). No user accounts; no personal data is requested; question content is not logged; the conversation of a session is kept in the session database (PostgreSQL, design decision D4) only until the session ends and is then deleted (C-10). On-premise, member-owned. | Gözde Nur (application); Kaan (pilot computer set-up and answer time) | Planned: baseline by 14/11/2026, whole pipeline by 05/12/2026, pilot computer set up and measured by 09/12/2026 |
| 14 | Physical or logistical resources | Not needed: the team works on its own computers and meets online. | Yaren (Scrum Master) | Not needed, confirmed on 20/10/2026 |

## Example (illustrative only)

Scenario: a legal research assistant. Names, limits and dates are illustrative.

| # | Resource | Description | Responsible Person/Team | Status |
|---|---|---|---|---|
| 1 | Cloud GPU (1 × 24 GB) under the university credit | Experiments and staging deployment; cloud service; limited to the allocated credit (C-02) | Member 1 (Data Scientist, infrastructure) | Requested on 14/10/2026; granted on 17/10/2026 |
| 2 | Hosted LLM API | Answer generation in staging; 500 calls per day on the academic tier (C-05) | Member 2 | API key issued on 20 Oct |
| 3 | Embedding model, run locally | Document and query embeddings; on the cloud GPU | Member 2 | Downloaded and tested on 22/10/2026 |
| 4 | Vector database | Index of the document set; hosted on the cloud project | Member 3 | Planned for 28/11/2026 |
| 5 | Shared storage for raw and processed documents | Encrypted bucket; access for team members only; no PII stored (C-03) | Member 3 (Business Analyst; contact with the data provider) | Created on 15/10/2026 |
| 6 | Shared code repository and experiment tracker | Version control and run logs | Member 4 | Configured on 10/10/2026 |
| 7 | Staging environment for the MVP | Web app on the cloud project; used by pilot AI users | Member 4 (Data Scientist, staging deployment) | Planned for 02/12/2026 ([Dependencies](06-dependencies.md) row 4) |

## Checklist before submitting

- [x] Every category is covered or marked as not needed (rule 1)
- [x] Every row names a Responsible Person/Team (rule 2)
- [x] Every API or third-party service row states its usage or rate limits (rule 3)
- [ ] Every compute row says what hardware is used and where it runs (rule 4)
- [x] The deployment environment has its own row (rule 5)
- [x] Every data-access row names storage, permissions and any sensitive-data needs (rule 6)
- [x] Every row has a dated Status (rule 7)
- [x] Every fixed limit also appears as a constraint in [Assumptions & Constraints](03-assumptions-and-constraints.md) (rule 8)
- [x] Every resource that could fail has a risk in [Risks](11-risks.md) (rule 9)
- [x] Every wait on an outside party is a row in [Dependencies](06-dependencies.md) (rule 10)

---

## References

[1] ISO/IEC JTC 1/SC 42, *ISO/IEC 5338:2023 Information technology — Artificial intelligence — AI system life cycle processes*, 1st ed. Geneva, Switzerland: International Organization for Standardization and International Electrotechnical Commission, Dec. 2023. UK implementation: BS ISO/IEC 5338:2023, London, UK: BSI Standards Limited, 2024.

[2] ISO/IEC JTC 1/SC 42, *ISO/IEC 5339:2024 Information technology — Artificial intelligence — Guidance for AI applications*, 1st ed. Geneva, Switzerland: International Organization for Standardization and International Electrotechnical Commission, Jan. 2024. UK implementation: BS ISO/IEC 5339:2024, London, UK: BSI Standards Limited, 2024.
