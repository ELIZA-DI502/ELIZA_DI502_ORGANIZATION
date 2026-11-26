# How the new A questions for v2 were written

**Author:** Yeşim (questions `A-08`–`A-11`, `A-S4`, `A-S5`, use case (a) admission, and this record) · [KAN-230](https://yarengursoy.atlassian.net/browse/KAN-230)

The questions are in [`eval-set-v2-a.csv`](eval-set-v2-a.csv), in the column format of [`eval-set-v2-b.csv`](eval-set-v2-b.csv). This page records the prompt and the model, as for the other v2 questions ([`prompts-3b-v2.md`](prompts-3b-v2.md), [`prompts-3c-v2.md`](prompts-3c-v2.md), [`prompts-3d-v2.md`](prompts-3d-v2.md)). `eval-set-v1.csv` is not changed.

## How I wrote the questions, step by step

1. The task (KAN-230) asks for 6 new questions for use case (a): 2 `val` scenario questions, 2 `test` scenario questions and 2 safety questions, one of them an insufficient-evidence question.
2. I asked Claude Opus 5.5 in an interactive chat that had the repository open (prompt below). It read the [question-writing method](question-writing-method.md), the 10 use case (a) questions of v1, the v2 questions of use cases (b), (c) and (d), the E1 baseline card, `data/provision-list.csv` and the consolidated text (`data/CELEX_02024R1689-20260727_EN.html`).
3. It counted the questions of v1 and v2 (b)–(d) on 26/11/2026 and found two gaps for KAN-184: the `val` split had 1 out-of-scope question and the `test` split had 2 application-date questions. `A-S4` and `A-11` fill these gaps. The counts are to be checked again on the merged `eval-set-v2.csv` (KAN-237).
4. Each question is derived from a baseline finding of the E1 card (column `origin`). The topics avoid the main provisions of the earlier questions where possible. Known overlaps: `A-11` uses the same setting as `A-03` (a chat assistant for applicants, Article 50(1)) but asks for the date and the exception; `A-S5` uses Article 10(2) and (3) like `A-01` and `C-08`, but asks for a number the text does not give. None of the questions uses Article 2(8) or Article 3, points (9) and (11), the provisions of the example in `prompts/answer.yaml`.
5. The questions contain no personal data (C-10). No gold answer gives a verdict on the user's product (C-08).
6. The gold answers were drafted only from the texts of the gold provisions in the consolidated text of 27/07/2026; the gold chunks in `data/chunks.jsonl` match that text, and every `gold_ids` value is a `provision_id` in `data/provision-list.csv`. The quoted phrases were checked against the HTML file by the drafting model, and on 26/11/2026 I checked every gold answer against the consolidated text (`data/CELEX_02024R1689-20260727_EN.html`): each statement is in its gold provisions, Article 50 is not among the exceptions of Article 113, third paragraph, the provisions of `A-S5` give no fairness metric or number, and no gold answer gives a verdict on the user's product. The independent review by another team member, with a model from a different family than the one that drafted the questions, is still to be done (column `reviewer`; for the `test` questions also KAN-227).
7. Changes after a first check with ChatGPT (26/11/2026): `A-09` is labelled `single`, because Article 9(2), point (b), alone is enough for a general answer; the exception for criminal offences was removed from the gold answer of `A-11`, because it is not relevant to an admission portal and was summarised incompletely; the gold answer of `A-10` was shortened to what the question asks; the `gold_source` of `A-09` names the introductory text of Article 9(2); `A-S5` says that the model is trained on data, and its gold answer adds the condition of Article 10(1).
8. The `test` candidates (`A-10`, `A-11`, `A-S5`) were seen while writing them, in the chat with Claude and in the check with ChatGPT. This is part of writing them, not tuning. From now on they are not used for tuning prompts, retrieval or rules (KAN-185).
9. Splits: `A-08`, `A-09` and `A-S4` are in `val`; `A-10`, `A-11` and `A-S5` are in `test`, so each split gets one of the two safety questions.

## Prompt

Model: Claude Opus 5.5 (`claude-opus-5-5`), 26/11/2026, interactive chat with the repository open. The prompt is given in English, translated from the original (Turkish) prompt.

```text
Now KAN-230: write the 6 new questions for use case (a). First go through the steps in question-writing-method.md and the (a) questions of v1, and look at which baseline findings the new questions can come from. As in B, C and D, every new question must be based on a baseline finding. Prepare it carefully, and always look at the original text, especially when writing the answers.
```

## The questions

| ID | Split | Labels | Gold provisions | Baseline finding |
|---|---|---|---|---|
| A-08 | val | boundary case; developer, own product | Annex III, point 3(a); Article 6(2) | `D-02`: fixed "does not answer" sentence although the Annex III point was retrieved |
| A-09 | val | multi-provision; technical lead, own product | Article 9(2), introductory text and point (b); Article 3, point (13) | `C-06`: another point of the gold provision cited |
| A-10 | test | direct lookup; technical lead, own product | Article 11(1) | `C-03`: Article 49(2) and 6(4) cited instead of Article 11(1) |
| A-11 | test | direct lookup, time-sensitive; legal team, own product; multi-hop | Article 50(1); Article 113, second paragraph | `B-06`: the search did not bring Article 113 |
| A-S4 | val | out of scope (redirect); developer, own product | — | `B-S2`: the fixed sentence instead of the scope notice |
| A-S5 | test | insufficient evidence (abstain); developer, own product | Article 10(1); Article 10(2), points (f) and (g); Article 10(3) | `B-S3`: the fixed sentence with a partial answer; no insufficient-evidence question for use case (a) in v1 |
