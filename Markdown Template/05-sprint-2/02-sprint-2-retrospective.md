# Sprint 2 Retrospective

**Sprint 2:** 28/10/2026 – 18/11/2026 · **Release:** Alpha 0.1 (baseline) · **Team:** ELIZA (Yeşim, Yaren, Kaan, Gözde Nur)

**Sprint goal:** *Q&A dataset v1 (D2) and the indexed source text (D5) are ready, the baseline retrieval is measured with Recall@5 against the charter target and gives answers with Article/Annex citations and the version date, and Project Charter v2 (D7) is ready for the Sprint 2 review on 18/11/2026.*

| What went well? | What went bad? | Action | Assigned to |
|---|---|---|---|
| The source text was parsed, chunked and indexed early, so the baseline could be run before the end of the sprint. | The 20-chunk check against the source (KAN-94) was done after the index was built. If it had failed, we would have had to rebuild the index. | Check a sample of chunks before anything goes into the index. | Gözde Nur |
| The Q&A dataset v1 has 46 questions written with one shared method; `test` was frozen on 11/11. | The question-writing method came after the lecture on 04/11, so questions written before it had to be checked and relabelled again. | When the course changes how we work, update the DoR/DoD that week and add the rework to Jira as sub-tasks. | Yaren |
| The baseline runs from `README.md` with pinned `requirements.txt`, `config/rag.yaml` and `prompts/`, and every run is logged in W&B. | The experiment card, technical summary, design document and SBOM all waited for the baseline results and were all on one person at the end. | Every document gets an owner and a second writer, and is drafted while the work is being done. | Yaren |
| Story map v2, story requirements for every epic and a test case for every story were finished. | We put the generation and citation tasks (KAN-125 to KAN-129) in the sprint, but did not start them. | Move them to Sprint 3. Add optional work only after the required work is on track. | Yeşim |
| The UI technology was chosen and the mockup was drawn by 11/11, as planned. | Jira was updated later, so the burndown stayed flat and dropped at the end. | Update the status on the day the work changes; check the board at each stand-up. | Kaan |
| Every Sprint 1 review comment has a decision in the Charter v2 response table. | Charter v2 waited for the baseline results and was finished in the last two days. The pilot users (KAN-158) are still not named. | Set a fixed date for updating the charter with results. Send the pilot invitations this week. | Yaren, Gözde Nur |
| The safety questions are written. | The safety story (KAN-83) did not move because the rubric (KAN-50) is not finished. | Finish the rubric in the first week of Sprint 3. | Yeşim, Kaan |

## Hot Air Balloon Retrospective

| ☀️ Sunny Skies | 🔥 Hot Air | ⛈️ Storm Clouds | 🎒 Sandbags |
|---|---|---|---|
| Baseline measured (Alpha 0.1) | Working pipeline from text to index | Pilot users not confirmed (R-03) | Documents left to the end |
| Hybrid retrieval in Sprint 3 | Shared question-writing method | Answer time on CPU (R-12) | Board updated late |
| Sprint 2 review on 18/11 | `test` split frozen early | Heavier Sprint 3 (R-07) | Rework after the DoR changed |

## Commitments check

| Commitment | Promised in | Fulfilled? | Notes |
|---|---|---|---|
| Sprint 2 runs from 28/10 to 18/11/2026, with the upload on 14/11 | [DoR/DoD](../03-definition-of-ready-definition-of-done.md); C-07 | Yes | Follows the course calendar. |
| Four team members, no new members | C-07 | Yes | All four contributed. |
| One source only: the consolidated text of 27/07/2026 | C-01 | Yes | Checked for a newer version (KAN-157). |
| Open-source, quantized answer model | C-03 | Yes | Llama-3.1-8B-Instruct `Q4_K_M` via Ollama. |
| CPU only; C-05 reviewed with the baseline answer times | C-05 | Partly | The CPU answer time still has to be added to the experiment card. |
| $100 Google Cloud credit kept as a reserve | C-06 | Yes | Not used. |
| `test` frozen on 11/11 and never used for tuning | [DoR/DoD](../03-definition-of-ready-definition-of-done.md) | Yes | Frozen on 11/11 (KAN-53). |

## Follow-up on the Sprint 1 actions

| Sprint 1 action | Done? | Comment |
|---|---|---|
| Check that IDs match on all pages and in Jira before each review | Yes | Done for Charter v2. |
| Every story gets an epic and a sprint at planning | Yes | All Sprint 2 stories have an epic. |
| Ask for feedback on an early draft | Partly | Done for the question set, not for the technical documents. |
| Check the sync and template updates at the start of the sprint | Yes | Checked at the start of Sprint 2. |
| Freeze the pages 2 days before a review | Partly | Charter v2 and the technical documents changed until the end. |

## Individual comments

**Yeşim:** 

**Yaren:** I wrote the Sprint 2 Definition of Ready, Definition of Done and sprint goal with the team (KAN-117), and updated them on 08/11 after the instructor's feedback and the lecture on RAG test sets. I wrote the questions for use case (d) exam monitoring (KAN-66), ran the cross-check of all questions against the official text and followed every flag until it was resolved (KAN-52), and checked the story roles against ISO/IEC 5339 (KAN-116). I ran the planning poker session (KAN-115), worked on the Risks page and the O1 and O3 targets for Charter v2 (KAN-110, KAN-108), compared 20 random chunks with the source text and wrote the preprocessing report (KAN-94, KAN-95). At the end of the sprint I prepared the Jira backlog export and led this retrospective (KAN-119, KAN-120). I learned how a RAG test set is built (gold sources, a `val` split for tuning and a frozen `test` split), how the source text becomes chunks with their reference and version date, and what Recall@k measures against the charter target. My main lesson: when a rule changes mid-sprint, the rework must be written in Jira, or nobody sees it.In Sprint 3 I will check every citation against the retrieved chunk IDs and report the citation coverage on `val` (KAN-128, KAN-129), and make sure every document has a second writer at sprint planning.

**Kaan:** 

**Gözde Nur:** 

## Lessons Learned

- **Process:** When a rule changes mid-sprint, make the rework visible in Jira the same week.
- **Planning:** Add optional work only after the required work is on track.
- **Data:** Quality checks come before the next step, not after.
- **Documentation:** Write documents while the work happens; a spike is not done without its note.
