# Prompts: Annex III 3(b) questions

**Author:** Gözde Nur Özdemir (questions `B-01`–`B-06`, `B-S1`–`B-S3`, and this record) · [KAN-46](https://yarengursoy.atlassian.net/browse/KAN-46)

The questions are in [`eval-set-v1.csv`](eval-set-v1.csv) (`B-01`–`B-06`, `B-S1`–`B-S3`).

## How I made the 3(b) questions

1. I picked the use case: AI that grades or evaluates students (Annex III, point 3(b)).
2. I chose the articles a developer of such a tool needs: Annex III 3(b), Article 6(2)–(4), 49(2), 5(1)(f), Articles 8–15 and 113. All of them are in `data/provision-list.csv`.
3. I asked Claude Opus 5.5 for candidate questions with answers (prompt below). It gave 22. Some were based on real examples from the EU AI Act Service Desk.
4. In Sprint 1 I kept 8 of the 22. I wanted at least one question of each type and no two questions about the same situation.
5. I rewrote them in simple words, the way a developer would ask, without article numbers.
6. On 05/11/2026 I changed three questions and added a ninth one (`B-06`), so that different people ask in different ways (see the last section). The set now has **9 questions**.
7. I checked every answer and source against the PDF and fixed two mistakes.
8. For each question, `eval-set-v1.csv` says who wrote it, which model and prompt were used, and where it came from.

## Prompts

Model: Claude Opus 5.5 (`claude-opus-5-5`), 24/10/2026. Questions `B-01`–`B-05`, `B-S1`–`B-S3`.

**Generating candidates**

```text
Write several candidate questions for Annex III point 3(b) of Regulation (EU) 2024/1689 (AI systems that evaluate learning outcomes).
- Scenario questions that a developer at an EdTech company might ask: direct lookup, condition/exception, multi-provision, follow-up and boundary case.
- Safety questions: legal decision, out of scope, insufficient evidence, adversarial.
- Where possible, adapt examples from the European Commission's AI Act Service Desk and name the source.
For each question give the gold source (Article, paragraph, point) and a short gold answer based only on the consolidated text of 27/07/2026. For safety questions, give the expected behaviour. Never state that a system is or is not compliant or high-risk.
```

**Simplifying the selected questions**

```text
Rewrite these questions in simpler, everyday language, as a developer would ask them. Do not use legal terms or article numbers in the question.
```

The author selected 8 of the candidates and checked every gold answer against the PDF of the consolidated text.

## Rewording for more varied questions (05/11/2026)

Model: Claude Opus 5.5 (`claude-opus-5-5`). I chose the labels below for each question; the model drafted the wording, and I edited and checked it. I reworded `B-02`, `B-04` and `B-05` and added `B-06` so that the 3(b) questions are not all of one kind: different users (developer, compliance officer, product manager), wording that uses or avoids the terms of the legal text, a legal-decision request and a "when" question. The situation and the gold source stay the same.

```text
Rewrite this question (for B-06: write a new question about the given provisions) for the EU AI Act test set so that it matches these labels:
user = {user}, phrasing = natural question, wording = {same terms as the legal text | everyday words},
question type = {type}.
Keep the same situation and the same provisions, so the gold answer still holds. Do not add facts that are not in the original question.
```

| ID | Labels I chose |
|---|---|
| B-02 | developer, natural, everyday words, legal-decision request ("yes or no") |
| B-04 | compliance officer, natural, same terms as the legal text |
| B-05 | product manager, natural, same terms as the legal text |
| B-06 (new) | product manager, natural, everyday words, "when" question on the application date of Annex III point 3(b) |

Search-query phrasing was not used: the course asks for natural-language questions, not keyword matches. I checked the new wording and all gold sources against the PDF of the consolidated text on 05/11/2026. I also fixed two errors I found in this check: `B-01` now lists Article 6(3), first subparagraph (the "no significant risk of harm" condition its answer uses), and `B-04` no longer names Article 5(1)(f) in the question, so the question does not give away its gold source.
