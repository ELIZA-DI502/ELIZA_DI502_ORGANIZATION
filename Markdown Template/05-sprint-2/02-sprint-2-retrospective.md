# Sprint 2 Retrospective

**Sprint 2:** 28/10/2026 – 18/11/2026 · **Release:** Alpha 0.1 (baseline) · **Team:** ELIZA (Yeşim, Yaren, Kaan, Gözde Nur)

**Sprint goal:** *Q&A dataset v1 (D2) and the indexed source text (D5) are ready, the baseline retrieval is measured with Recall@5 against the charter target and gives answers with Article/Annex citations and the version date, and Project Charter v2 (D7) is ready for the Sprint 2 review on 18/11/2026.*

| What went well? | What went bad? | Action | Assigned to |
|---|---|---|---|
| The source text was parsed, chunked and indexed early, so the baseline could be run before the end of the sprint. | The 20-chunk check against the source (KAN-94) was done after the index was built. If it had failed, we would have had to rebuild the index. | Check a sample of chunks before anything goes into the index. | Gözde Nur |
| The Q&A dataset v1 has 46 questions written with one shared method; `val`/`test` membership was fixed on 09/11. | The question-writing method came after the lecture on 04/11, so questions written before it had to be checked and relabelled again. | When the course changes how we work, update the DoR/DoD that week and add the rework to Jira as sub-tasks. | Yaren |
| The baseline runs from `README.md` with pinned `requirements.txt`, `config/rag.yaml` and `prompts/`, and every run is logged in W&B. | The experiment card, technical summary, design document and SBOM all waited for the baseline results and were all on one person at the end. | Every document gets an owner and a second writer, and is drafted while the work is being done. | Yaren |
| Story map v2, story requirements for every epic and a test case for every story were finished. | We left too little time for generation and citation work at the end of Sprint 2. Gözde completed KAN-125 on 12 November. On 14 November, Yaren completed KAN-128 and KAN-129, and Yeşim completed the Sprint 2 scope of KAN-126. We agreed to carry KAN-127 into Sprint 3 and opened KAN-222 there to improve citation specificity and show the sources line in the interface. | Start work that other tasks depend on in the first week. At the sprint midpoint, check that each dependency has an owner and that enough time remains to integrate and verify the required work. Add optional work once the required work is on track. | Yeşim |
| The UI technology was chosen and the mockup was drawn by 11/11, as planned. | Jira was updated later, so the burndown stayed flat and dropped at the end. | Update the status on the day the work changes; check the board at each stand-up. | Kaan |
| Every Sprint 1 review comment has a decision in the Charter v2 response table. | Charter v2 waited for the baseline results and was finished in the last two days. The pilot users (KAN-158) are still not named. | Set a fixed date for updating the charter with results. Send the pilot invitations this week. | Yaren, Gözde Nur |
| The safety questions are written. | The safety story (KAN-83) did not move because the rubric (KAN-50) is not finished. | Finish the rubric in the first week of Sprint 3. | Yeşim, Kaan |

## Hot Air Balloon Retrospective

| ☀️ Sunny Skies | 🔥 Hot Air | ⛈️ Storm Clouds | 🎒 Sandbags |
|---|---|---|---|
| Baseline measured (Alpha 0.1) | Working pipeline from text to index | Pilot users not confirmed (R-03) | Documents left to the end |
| Beta in Sprint 3: paragraph-level citations and relations between provisions | Shared question-writing method | Answer time on CPU (R-12) | Board updated late |
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
| `test` frozen on 11/11 and never used for tuning | [DoR/DoD](../03-definition-of-ready-definition-of-done.md) | Yes | `val`/`test` membership fixed on 09/11 (KAN-53, commit `842c692`); since then `test` has not been run or used for tuning. The gold content is frozen at submission (Q-32). |

## Follow-up on the Sprint 1 actions

| Sprint 1 action | Done? | Comment |
|---|---|---|
| Check that IDs match on all pages and in Jira before each review | Yes | Done for Charter v2. |
| Every story gets an epic and a sprint at planning | Yes | All Sprint 2 stories have an epic. |
| Ask for feedback on an early draft | Partly | Done for the question set, not for the technical documents. |
| Check the sync and template updates at the start of the sprint | Yes | Checked at the start of Sprint 2. |
| Freeze the pages 2 days before a review | Partly | Charter v2 and the technical documents changed until the end. |

## Individual comments

**Yeşim:** As Product Owner, I prepared the question-writing method and the D2 data card with its decision log (KAN-85), wrote the admission questions (KAN-45), and selected and adapted seven benchmark questions (KAN-48). I reviewed the use case (b) questions (KAN-52) and ran the structural check of the gold sources, which identified items for the authors and reviewers to follow up on (KAN-51). After the Sprint 1 review, I reorganised the Jira backlog (project work became tasks, and KAN-24 and KAN-25 were merged into KAN-2) and updated Story Map v2, the story requirements for every epic and the story test cases to match it (KAN-90, KAN-112–114). I also documented our responses to the Sprint 1 review (KAN-106) and added the Charter v2 change notes (KAN-111). I checked EUR-Lex for a newer consolidated version (KAN-157), completed the corpus datasheet (KAN-96), and added the sources line with version dates to the saved validation answers (KAN-126). This sprint taught me to record which dataset version was used for each result and to distinguish fixed split membership from the final review of gold answers. In Sprint 3, I will work on more specific citations and their display in the interface (KAN-222), how answers explain relationships between provisions (KAN-127), and question set v2.

**Yaren:** I wrote the Sprint 2 Definition of Ready, Definition of Done and sprint goal with the team (KAN-117), and updated them on 08/11 after the instructor's feedback and the lecture on RAG test sets. I wrote the questions for use case (d) exam monitoring (KAN-66), ran the cross-check of all questions against the official text and followed every flag until it was resolved (KAN-52), and checked the story roles against ISO/IEC 5339 (KAN-116). I ran the planning poker session (KAN-115), worked on the Risks page and the O1 and O3 targets for Charter v2 (KAN-110, KAN-108), compared 20 random chunks with the source text and wrote the preprocessing report (KAN-94, KAN-95). At the end of the sprint I prepared the Jira backlog export and led this retrospective (KAN-119, KAN-120). I learned how a RAG test set is built (gold sources, a `val` split for tuning and a frozen `test` split), how the source text becomes chunks with their reference and version date, and what Recall@k measures against the charter target. My main lesson: when a rule changes mid-sprint, the rework must be written in Jira, or nobody sees it. I've checked citation against the retrieved chunk IDs and report the citation coverage on `val` (KAN-128, KAN-129), and make sure every document has a second writer at sprint planning.

**Kaan:** I worked on the architecture and the technical documents of Sprint 2. I accepted React + Node.js as the user interface technology (D1, KAN-103), drew the interface mockup with its waiting and error states (KAN-104), kept the design document in line with the system and answered the Sprint 1 review comments on it (D15, comments 6–8, KAN-102), and wrote the SBOM (KAN-105), the E1 baseline card (KAN-100) and the technical summary (KAN-101). On the evaluation side I wrote the evaluation rubric (KAN-50) and the level placement (c) questions (KAN-47), mapped the provision list to the D2 questions (KAN-84), and recorded the committee's feedback on the O2 and O4 levels in Charter v2 (KAN-109). I also started the web interface and backend for the demo (KAN-122). I learned that a baseline score becomes useful only when the failures are broken down by cause: a gold provision was among the 8 chunks for 24 of the 27 questions, so the next gain is in the answer step, not in the search. Next sprint I will update the experiment card and the technical summary right after each run, not at the end of the sprint.

**Gözde Nur:** I built the RAG pipeline of the baseline as notebooks that rerun from the start: chunking (the consolidated text of 27/07/2026 split into 105 provision chunks with their reference and version date), split (the questions split into `val` and a frozen `test`, KAN-53, frozen on 09/11 with its SHA-256) and embedding (KAN-97). In the settings run (KAN-99) I compared five embedding models and dense against hybrid search, and labelled the frequent words with an LLM jury to test word removal for BM25 (KAN-221); the chosen setup, bge-m3 with BM25 and weighted RRF (0.8/0.2), reached Recall@8 0.59 on `val`, logged in W&B. I then generated the answers with Llama 3.1 8B (KAN-125) and compared them with a full-text baseline (Claude Haiku 5.5): the expected provision was cited for 70% of the questions against 81%. I also wrote the use case (b) questions (KAN-46), reviewed the use case (c) questions (KAN-52), and kept the README, config, prompts and the design document (D9, D11) in line with the code (KAN-98). I learned that good retrieval is not enough: a gold provision was among the 8 chunks for 24 of the 27 questions, yet many answers said the text does not answer or cited another provision, so the gap is in the answer step. I also learned that a frozen file must only change through its own notebook; review notes once changed the `test` hash.

## Lessons Learned

- **Process:** When a rule changes mid-sprint, make the rework visible in Jira the same week.
- **Planning:** Add optional work only after the required work is on track.
- **Data:** Quality checks come before the next step, not after.
- **Documentation:** Write documents while the work happens; a spike is not done without its note.
