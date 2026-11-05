# Prompts: Annex III 3(b) questions

The questions are in [`eval-set-v1.csv`](eval-set-v1.csv) (`B-01`–`B-06`, `B-S1`–`B-S3`). The Sprint 1 file `eval-set-v1-3b.csv` was merged into it on 05/11/2026 and removed; its last version is [here](https://github.com/ELIZA-DI502/ELIZA_DI502_ORGANIZATION/blob/69932de4f1db4a593356de976219de3e74d644e4/docs/eval/eval-set-v1-3b.csv).

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

Model: Claude Opus 5.5 (`claude-opus-5-5`). Questions `B-02`, `B-04` and `B-05` were reworded and `B-06` was added so that the 3(b) questions are not all of one kind: different users (developer, compliance officer, product manager), wording that uses or avoids the terms of the legal text, a legal-decision request and a "when" question. The situation and the gold source stay the same; the Sprint 1 wording is kept in the [Sprint 1 file](https://github.com/ELIZA-DI502/ELIZA_DI502_ORGANIZATION/blob/69932de4f1db4a593356de976219de3e74d644e4/docs/eval/eval-set-v1-3b.csv) (commit `69932de`).

```text
Rewrite this question (for B-06: write a new question about the given provisions) for the EU AI Act test set so that it matches these labels:
user = {user}, phrasing = natural question, wording = {same terms as the legal text | everyday words},
question type = {type}.
Keep the same situation and the same provisions, so the gold answer still holds. Do not add facts that are not in the original question.
```

| ID | Labels asked for |
|---|---|
| B-02 | developer, natural, everyday words, legal-decision request ("yes or no") |
| B-04 | compliance officer, natural, same terms as the legal text |
| B-05 | product manager, natural, same terms as the legal text |
| B-06 (new) | product manager, natural, everyday words, "when" question on the application date of Annex III point 3(b) |

Search-query phrasing was not used: the course asks for natural-language questions, not keyword matches. The author checked the new wording and all gold sources against the PDF of the consolidated text on 05/11/2026. Two errors found in this check were also fixed: `B-01` now lists Article 6(3), first subparagraph (the "no significant risk of harm" condition its answer uses), and `B-04` no longer names Article 5(1)(f) in the question, so the question does not give away its gold source.
