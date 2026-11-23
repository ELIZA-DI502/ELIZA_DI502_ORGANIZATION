# How the new C questions for v2 were written

**Author:** Kaan Kocatürk (questions `C-08`–`C-11`, `C-S4`, `C-S5`, use case (c) level placement, and this record) · [KAN-232](https://yarengursoy.atlassian.net/browse/KAN-232)

The questions are in [`eval-set-v2-c.csv`](eval-set-v2-c.csv), in the column format of [`eval-set-v2-b.csv`](eval-set-v2-b.csv). This page records the prompt and the model, as for the other v2 questions ([`prompts-3b-v2.md`](prompts-3b-v2.md), [`prompts-3d-v2.md`](prompts-3d-v2.md)). `eval-set-v1.csv` is not changed.

## How I wrote the questions, step by step

1. The task (KAN-232) asks for 6 new questions for use case (c): 2 `val` scenario questions, 2 `test` scenario questions and 2 safety questions, one of them an insufficient-evidence question.
2. I asked Claude Opus 5.5 in an interactive chat that had the repository open (prompt below). It read the [question-writing method](question-writing-method.md), the 46 v1 questions, the v2 questions of use cases (b) and (d), the E1 baseline card, `data/provision-list.csv` and `data/chunks.jsonl`.
3. It chose topics and gold provisions that no v1 or v2 question uses as its main provision, so that no new question is the same as or close to an earlier one: feedback loops (Article 15(4), third subparagraph), bias detection with special categories of personal data (Article 4a(1), from Regulation (EU) 2026/1744), systems without trained models (Article 10(6)), the split of oversight measures between provider and deployer (Article 14(3)) and testing thresholds (Article 9(8)). Each question is derived from a baseline finding (column `origin`).
4. The scenario questions cover the four question types that are not follow-ups (direct lookup, condition / exception, multi-provision, boundary case), and come from all three users. The safety questions are the categories use case (c) needed: an insufficient-evidence question, as the task asks, and an out-of-scope question, which use case (c) did not have in v1 and no v2 question has.
5. The questions contain no personal data (C-10); `C-09` names special categories of personal data only as a legal term. No gold answer gives a verdict on the user's product (C-08).
6. The gold answers were drafted only from the texts of the gold provisions in `data/chunks.jsonl`, and every `gold_ids` value is a `provision_id` in `data/provision-list.csv`. Every quoted phrase was checked against the consolidated text of 27/07/2026 (`data/CELEX_02024R1689-20260727_EN.html`). The independent review by another team member is still to be done (column `reviewer`).
7. Splits: `C-08`, `C-09` and `C-S4` are in `val`; `C-10`, `C-11` and `C-S5` are in `test`, so each split gets one of the two safety questions.

## Prompt

Model: Claude Opus 5.5 (`claude-opus-5-5`), 23/11/2026, interactive chat with the repository open. The prompt is given in English, translated from the original (Turkish) prompt, which gave the "Done when" text of KAN-232.

```text
KAN-232: Use case (c): write the v2 questions. 6 new level placement questions go to docs/eval/eval-set-v2-c.csv: 2 val scenario questions, 2 test scenario questions and 2 safety questions, one of them an insufficient-evidence question. The prompts go to prompts-3c-v2.md. The gold answers are checked against the consolidated text of 27/07/2026 and reviewed by another team member. eval-set-v1.csv is not changed. Do this.
```

## The questions

| ID | Split | Labels | Gold provisions | Baseline finding |
|---|---|---|---|---|
| C-08 | val | multi-provision; technical lead, own product | Article 15(4), third subparagraph; Article 10(2), points (f) and (g) | `C-06`: another point cited |
| C-09 | val | condition / exception, time-sensitive; legal team, general | Article 4a(1) | `C-05`: the search did not bring the gold provisions |
| C-10 | test | boundary case; developer, own product; multi-hop | Article 10(1), (6), (2), (3) and (4) | `D-03`: fixed "does not answer" sentence |
| C-11 | test | direct lookup; developer, own product | Article 14(1) and (3) | `D-10`: the search did not bring the gold provisions of Articles 12–14 |
| C-S4 | val | insufficient evidence (abstain); developer, own product | Article 9(8) | fixed sentence for 10 of 30 baseline answers |
| C-S5 | test | out of scope (redirect); technical lead, own product | — | no out-of-scope question for use case (c) in v1 |
