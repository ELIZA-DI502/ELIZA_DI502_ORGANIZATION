# How the new D questions for v2 were written

**Author:** Yaren Gürsoy (questions `D-13`–`D-16`, `D-S4`, `D-S5`, use case (d) exam monitoring, and this record) · [KAN-233](https://yarengursoy.atlassian.net/browse/KAN-233)

The questions are in [`eval-set-v2-b.csv`](eval-set-v2-b.csv), after the v2 questions of use case (b). This page records the prompts and the model, as for the other v2 questions ([`prompts-3b-v2.md`](prompts-3b-v2.md)).

## How I wrote the questions, step by step

1. The task (KAN-233) asks for 6 new questions for use case (d): 2 `val` scenario questions, 2 `test` scenario questions and 2 safety questions.
2. I asked Claude Opus 5.5 in an interactive chat that had the repository open (first prompt below). It read the v1 questions, the B v2 questions, the E1 baseline card and `data/chunks.jsonl`, and drafted 6 questions that are not the same as or close to an earlier question, each derived from a baseline finding.
3. I asked it to revise the questions so that they contain no sensitive or personal data and do not repeat the problems flagged in the v1 review (second prompt). It checked the questions against constraints C-02, C-04, C-08 and C-10 and the reviewer notes of v1, and:
   - removed the webcam, photo and recorded-session wording (personal data, C-10);
   - turned two closing sentences into conditions with no verdict (C-08; flags on `A-03`, `B-04`, `D-06`);
   - added Article 10(1), the training condition of Article 10, to `D-S4` (flag on `B-05`);
   - kept only provisions that are gold sources in each gold answer (flag on `C-04`), and named Annex III, point 3(d), and Article 6(2) in the legal-decision question (flag on `B-S4`).
4. The gold answers were drafted only from the texts of the gold provisions in `data/chunks.jsonl`; every `gold_ids` value was checked against the chunk IDs. I check every sentence against the consolidated text of 27/07/2026 before the questions are reviewed (KAN-233).
5. The two safety questions are an insufficient-evidence and a legal-decision question, the two categories that use case (d) did not have in v1. They are in `test`, where these categories were short (KAN-184).

## Prompts

Model: Claude Opus 5.5 (`claude-opus-5-5`), 21/11/2026, interactive chat with the repository open. The prompts are given in English, translated from the original prompts.

```text
Write 6 new evaluation questions for use case (d), exam monitoring: 2 scenario questions for the `val` split, 2 scenario questions for the `test` split and 2 safety questions. Return them as CSV rows in the column format of `docs/eval/eval-set-v2-b.csv`, so that they can be added to that file.
```

```text
Revise the question set so that no question contains sensitive or personal data, and no question repeats an issue that was flagged in the review of v1. Check the questions against the project criteria and constraints before revising them.
```



## The questions

| ID | Split | Labels | Gold provisions | Baseline finding |
|---|---|---|---|---|
| D-13 | val | condition / exception; developer, own product; multi-hop | Article 2(12); Annex III, point 3(d); Article 6(2) | `D-03`: fixed "does not answer" sentence |
| D-14 | val | multi-provision; technical lead, own product | Article 15(1) and (5) | `C-03`, `C-06`: another provision or point cited |
| D-15 | test | direct lookup, false premise, time-sensitive; technical lead, own product; multi-hop | Article 113, second paragraph, and third paragraph, point (c)(i); Annex III, point 3(d); Article 6(2) | `B-07`: false premise accepted |
| D-16 | test | multi-provision; technical lead, own product | Article 13(1) and (3) | `D-10`: the search did not bring the gold provisions |
| D-S4 | test | insufficient evidence (abstain); developer, own product | Article 10(1) and (3) | fixed sentence for 10 of 30 baseline answers |
| D-S5 | test | legal decision (redirect); legal team, own product | Article 50(1); Annex III, point 3(d); Article 6(2); Article 8(1) | `B-S4`: no provision shown |
