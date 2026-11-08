# Questions selected from the AI Act Evaluation Benchmark

**Jira:** [KAN-48](https://yarengursoy.atlassian.net/browse/KAN-48) · **Selected by:** Yeşim (Product Owner) · **Date:** 04/11/2026 · **For:** D2 Q&A Generation-Dataset v1 (`eval-set-v1.csv`, due 11/11/2026)

D2 criterion 13 asks for at least 5 questions taken or adapted from published work on the EU AI Act, each with its source and attribution, and each checked against the official text like any other question ([Deliverables](../../Markdown%20Template/03-project-canvas/05-deliverables.md); [Dependencies](../../Markdown%20Template/03-project-canvas/06-dependencies.md) row 1). This page records which items were selected from the benchmark, why, and how they were turned into the 7 questions in [`eval-set-v1.csv`](eval-set-v1.csv). The decisions are also in the decision log of the [Q&A data report](../../Markdown%20Template/11-datasheets/03-qa-data-report.md).

## Source

| | |
|---|---|
| Work | A. Davvetas, M. Papademas, X. Ziouvelou, V. Karkaletsis (2026). *AI Act Evaluation Benchmark: An Open, Transparent, and Reproducible Evaluation Dataset for NLP and RAG Systems.* arXiv:2603.09435 ([paper](https://arxiv.org/abs/2603.09435)) |
| Data | [github.com/davidath/ai-act-evaluation-benchmark](https://github.com/davidath/ai-act-evaluation-benchmark), commit `d323167` (26/06/2026): `scenarios.json` (339 scenarios) and `qa_pairs.json` (137 question-answer pairs) |
| Licence | The JSON files are under Creative Commons Attribution 4.0 International (CC BY 4.0); re-checked in the repository README on 04/11/2026. Every adapted question names its source in the `origin` column. |

Item numbers below are the position of the item in the `data` list of each file, counted from 0.

## How the benchmark authors made the items

Checked against the paper (arXiv:2603.09435v1, 10/03/2026) on 08/11/2026. Section numbers are the paper's.

| | What the paper says |
|---|---|
| Scenarios (`scenarios.json`) | Generated with **gpt-oss-120b** (Apache 2.0 licence), run on one GPU with llama.cpp after MXFP4 quantisation, at temperature **0.15** to reduce variance (Section 3.2). The authors first read Article 5 and Article 6 with Annex III by hand and drew flowcharts of the classification steps. They then wrote four prompt templates, one per risk tier (prohibited, high-risk, limited, minimal). Each template gives the model a legal-analyst role and the text of the relevant articles, and asks for a batch of scenarios in JSON, each with the role in the AI value chain (provider or deployer), intended use, system type, input data and domain, with constraints for variety (Sections 3.2, 4.1, Table 1). Result: 339 scenarios (70 prohibited, 86 high-risk, 84 limited, 99 minimal). |
| Risk labels | Risk levels were specified through category-specific generation templates. The authors report a "qualitative human validation of the entries generated" done "to the best of our resources", without its size, but do not document an independent, scenario-by-scenario legal validation of the labels; they state that validation by legal experts is still needed (Sections 4.2, 6). They also note that generating for variety produced edge cases, most often between the prohibited and high-risk tiers. |
| Question-answer pairs (`qa_pairs.json`) | The paper describes their fields (question, answer, relevant article) and gives one example, but does not say how they were made, by which model, or how many there are (Section 4.1). The count of 137 is from the repository file. |
| AI Act text | Cited as Regulation (EU) 2024/1689 (2024), without a version date or a statement that a consolidated text was used (Section 3.1). |
| Licence | The paper states no licence for the dataset; it names only the Apache 2.0 licence of gpt-oss-120b (Section 3.2). The CC BY 4.0 licence of the data files is from the repository README, checked on 04/11/2026. |

These points help explain the two findings below: the benchmark predates Regulation (EU) 2026/1744, and its risk labels were generated through category-specific prompts without documented independent legal validation of every scenario. For this reason, benchmark answers and labels are not used as gold.

## How the items were selected

1. **Education only.** Scenarios in the education domains or about students, exams or admission (31 scenarios), and question-answer pairs whose article is in our provision list ([`data/provision-list.csv`](../../data/provision-list.csv); 26 pairs).
2. **One clear use case.** The item fits one of the four Annex III point 3 use cases, or concerns all of them (application date, the Article 6(3) exception).
3. **Covers what the set needs.** Together the items cover all four use cases and several question types (D2 criteria 2 and 3), including a boundary case and an application-date question.
4. **Not already covered.** Situations already used by the team's own questions are left out (for example emotion detection during lessons, from KAN-10).

Seven items are selected, two more than the minimum, so that the set still has at least 5 if one is removed in the cross-check (KAN-52).

## Two findings that change how the items are used

- **Some benchmark answers are older than our source text.** The benchmark was built before Regulation (EU) 2026/1744 amended the AI Act. For example, pair #88 gives 2 August 2026 as the application date of the high-risk rules for Annex III systems; in the consolidated text of 27/07/2026, which ELIZA uses (C-01), Article 113, third paragraph, point (c)(i) sets 2 December 2027. Answers on other amended provisions (Articles 2, 4, 10 and 113) may also be out of date.
- **Some benchmark risk labels are not consistent.** The risk labels were generated with an LLM. For example, emotion recognition in online lessons is labelled `prohibited` in scenario #45 but `high-risk` in scenarios #109 and #139, although Article 5(1)(f) prohibits emotion recognition in education institutions except for medical or safety reasons.

**Therefore** only the situation or the question is taken from the benchmark. The gold answer and the gold source of every adapted question are written from the consolidated text of 27/07/2026, not from the benchmark's answer, label or article list.

## Selected items

| ID | Benchmark item | Use case | Question type | Gold source (from the consolidated text) | Suggested reviewer (KAN-52) |
|---|---|---|---|---|---|
| BM-01 | `scenarios.json` #73 | (a) admission | direct lookup | Annex III, point 3(a); Article 6(2); Article 6(3), third subparagraph | Kaan |
| BM-02 | `qa_pairs.json` #11 | (a) admission | condition / exception | Article 6(3), first subparagraph; second subparagraph, point (d); third subparagraph | Gözde Nur |
| BM-03 | `scenarios.json` #103 | (b) learning-outcome assessment | direct lookup | Annex III, point 3(b); Article 6(2) | Gözde Nur |
| BM-04 | `scenarios.json` #94 | (c) level placement | direct lookup | Annex III, point 3(c); Article 6(2) | Kaan |
| BM-05 | `scenarios.json` #84 | (d) exam monitoring | direct lookup | Annex III, point 3(d); Article 6(2) | Yaren |
| BM-06 | `scenarios.json` #139 | (d) exam monitoring | boundary case | Article 5(1), first subparagraph, point (f); Annex III, point 3(d) | Yaren |
| BM-07 | `qa_pairs.json` #88 | (a) admission (the date applies to all four) | direct lookup (application date) | Article 113, third paragraph, point (c)(i); Annex III, point 3(a) | Kaan |

### BM-01 · Scenario #73

- **Original:** "AI platform that determines admission to university programmes based on academic records and socio‑economic background" (role: Deployer; system type: Admission decision AI; input data: Academic transcripts, standardized test scores, demographic data; benchmark label: high-risk)
- **Why:** a direct example of use case (a).
- **Question:** "Our platform decides which applicants are admitted to our university programmes, using their transcripts, standardised test scores and socio-economic data. Which AI Act provisions relate to it?"
- **Answer (gold, from the consolidated text of 27/07/2026):** Annex III, point 3(a) lists AI systems intended to be used to determine access or admission or to assign natural persons to educational and vocational training institutions at all levels, and Article 6(2) makes the AI systems referred to in Annex III high-risk. If the system performs profiling of natural persons, the Article 6(3) exception can never apply (Article 6(3), third subparagraph).
- **Gold source:** Annex III, point 3(a); Article 6(2); Article 6(3), third subparagraph

### BM-02 · Question-answer pair #11

- **Original question:** "Can a provider consider an Annex III AI system as not high‑risk?"
- **Original answer:** "Yes, if it meets certain conditions such as performing a narrow procedural task, improving a prior human activity, or detecting decision‑making patterns without replacing human assessment, and documents this assessment." (article: 6)
- **Why:** the Article 6(3) exception is the question developers ask most. The question is turned into a concrete admission situation, using condition (d) (preparatory task), because the team's question B-01 already covers condition (a).
- **Question:** "Our tool does not decide admissions. It only prepares a short summary of each application for the admission committee, which then assesses every applicant itself. Is there an exception under which it is not high-risk, and what are its conditions?"
- **Answer (gold, from the consolidated text of 27/07/2026):** Under Article 6(3), an Annex III system is not considered high-risk where it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making, and one of the conditions in points (a) to (d) is fulfilled. Point (d) covers a system intended to perform a preparatory task to an assessment relevant for the Annex III use cases. The exception never applies if the system performs profiling of natural persons (Article 6(3), third subparagraph).
- **Gold source:** Article 6(3), first subparagraph; Article 6(3), second subparagraph, point (d); Article 6(3), third subparagraph
- **Note:** Article 6(4) (the provider documents its assessment) also concerns this question, but it is not in `data/provision-list.csv`, so it is left out of the gold answer until the open decision Q-12 in the data report is made.

### BM-03 · Scenario #103

- **Original:** "AI that evaluates student learning outcomes and automatically adjusts curriculum pathways" (role: Deployer; system type: Adaptive learning outcome AI; input data: Assessment scores, interaction logs, learning analytics; benchmark label: high-risk)
- **Why:** matches the wording of Annex III, point 3(b), including "to steer the learning process".
- **Question:** "Our app scores students' assessments and then automatically changes the learning path each student follows. Which AI Act provisions relate to it?"
- **Answer (gold, from the consolidated text of 27/07/2026):** Annex III, point 3(b) lists AI systems intended to be used to evaluate learning outcomes, including when those outcomes are used to steer the learning process of natural persons in educational and vocational training institutions at all levels. Under Article 6(2), the AI systems referred to in Annex III are considered high-risk.
- **Gold source:** Annex III, point 3(b); Article 6(2)

### BM-04 · Scenario #94

- **Original:** "AI that determines the appropriate level of education for students based on prior achievement and aptitude tests" (role: Provider; system type: Education placement AI; input data: Test scores, learning analytics, socio‑demographic data; benchmark label: high-risk)
- **Why:** a direct example of use case (c).
- **Question:** "Our tool decides whether new students join beginner, intermediate or advanced classes, based on their earlier grades and an aptitude test. Which AI Act provisions relate to it?"
- **Answer (gold, from the consolidated text of 27/07/2026):** Annex III, point 3(c) lists AI systems intended to be used for assessing the appropriate level of education that an individual will receive or will be able to access, in the context of or within educational and vocational training institutions at all levels. Under Article 6(2), the AI systems referred to in Annex III are considered high-risk.
- **Gold source:** Annex III, point 3(c); Article 6(2)

### BM-05 · Scenario #84

- **Original:** "AI platform that evaluates student exam submissions for plagiarism and cheating in real time" (role: Provider; system type: Exam monitoring AI; input data: Student code submissions, text similarity databases, webcam feeds; benchmark label: high-risk)
- **Why:** a direct example of use case (d).
- **Question:** "During online exams, our platform checks students' code and text for plagiarism and watches their webcam feed to flag cheating in real time. Which AI Act provisions relate to it?"
- **Answer (gold, from the consolidated text of 27/07/2026):** Annex III, point 3(d) lists AI systems intended to be used for monitoring and detecting prohibited behaviour of students during tests in the context of or within educational and vocational training institutions at all levels. Under Article 6(2), the AI systems referred to in Annex III are considered high-risk.
- **Gold source:** Annex III, point 3(d); Article 6(2)

### BM-06 · Scenario #139

- **Original:** "Emotion recognition AI used in online examinations to detect stress and possible cheating behaviour" (role: Deployer; system type: Exam stress detection AI; input data: Webcam video, voice analysis, keystroke dynamics; benchmark label: high-risk)
- **Why:** a boundary case between exam monitoring (Annex III, point 3(d)) and the prohibition in Article 5(1)(f). The benchmark label `high-risk` does not match the text; the gold answer follows Article 5(1)(f).
- **Question:** "We want to detect stress and possible cheating in online exams by analysing students' emotions from their webcam video and voice. Which AI Act provisions relate to this?"
- **Answer (gold, from the consolidated text of 27/07/2026):** Article 5(1)(f) prohibits placing on the market, putting into service for this specific purpose, or using AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons. Monitoring and detecting prohibited behaviour of students during tests is an Annex III use case (point 3(d)), but being listed in Annex III does not lift the prohibition on inferring emotions.
- **Gold source:** Article 5(1), first subparagraph, point (f); Annex III, point 3(d)

### BM-07 · Question-answer pair #88

- **Original question:** "When does the AI Regulation become applicable to high‑risk AI systems listed in Annex III?"
- **Original answer:** "From 2 August 2026, with certain provisions applying earlier for specific sections." (article: 113)
- **Why:** the set needs application-date questions (objective O2 (d)). The benchmark answer is out of date; the gold answer is taken from Article 113 in the consolidated text of 27/07/2026.
- **Question:** "From when do the high-risk rules apply to an AI system that decides student admissions?"
- **Answer (gold, from the consolidated text of 27/07/2026):** Chapter III, Sections 1, 2 and 3 (with the exception of Article 6(5)) apply from 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III, which includes admission systems under Annex III, point 3(a) (Article 113, third paragraph, point (c)(i), as amended by Regulation (EU) 2026/1744). The general application date of 2 August 2026 does not apply to these rules.
- **Gold source:** Article 113, third paragraph, point (c)(i); Annex III, point 3(a); Article 113, second paragraph (added on 08/11/2026, because the last sentence of the answer rests on it)

## How the questions were written

- **Questions:** each benchmark situation was rewritten as a question a developer would ask about their own product, in their own words (decision Q-05). The questions are in [`eval-set-v1.csv`](eval-set-v1.csv) with their gold answers, and repeated above.
- **Gold answers and gold sources:** written from the consolidated text of 27/07/2026 ([`data/CELEX_02024R1689-20260727_EN.pdf`](../../data/CELEX_02024R1689-20260727_EN.pdf)), quoting the provision where possible; gold sources use the names in `data/provision-list.csv` (decision Q-08). The benchmark answers, labels and article lists were not used as gold.
- **LLM use (D2 criterion 6):** the selection, the questions and the gold answers were drafted with claude-opus-5-5 (Claude Opus 5.5) in an interactive chat on 04/11/2026. The prompt asked the model to find education items in the benchmark files, compare them with the provision list, and draft one question per selected item with a gold answer taken only from the consolidated text. Yeşim chose the items, edited the questions and checked every gold answer against the PDF.
- **Origin column:** `Adapted from AI Act Evaluation Benchmark (Davvetas et al., 2026, arXiv:2603.09435), <file> #<item>, CC BY 4.0`.
- **Labels (08/11/2026):** the questions carry the labels of the [question-writing method](question-writing-method.md) (`user`, `premise`, `hops`, `challenge`, `gold_ids`); BM-01, BM-02 and BM-07 were labelled with the other Case A questions.
- **Next:** each question is checked by a team member other than its author (KAN-52), recorded in the `reviewer` column; the suggested reviewer is in the table above. The questions count towards their use case (D2 criterion 2), so each use case owner writes fewer questions of their own. The other questions of each use case are added to the same file by 11/11/2026.

## Items not selected

| Benchmark items | Reason |
|---|---|
| Scenarios #111, #141 (dropout prediction), #117 (vocational apprenticeship), #133, #149 (scholarships) | It is not clear which Annex III point 3 use case they fall under, so a gold answer would be disputable. |
| Scenarios #17, #25, #30 (labelled `prohibited`) | The label cannot be supported by the provisions in our list. |
| Scenarios #45, #109 (emotion recognition in lessons) | Already covered by the team's emotion-detection question (from KAN-10). |
| Scenario #48 (teachers' emotional states) | About staff, not students; outside the four use cases. |
| Limited- and minimal-risk education scenarios (#161–#316) | Not high-risk. They may be used later as out-of-scope questions (D8). |
| Other question-answer pairs on our articles (#1–#10, #12–#15, #17, #19, #20, #41, #42, #74, #82, #90, #100, #135) | General questions not tied to an education use case, or already covered by the team's questions (#41, Article 50(1), from KAN-11). |
