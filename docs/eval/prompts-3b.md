# How Gözde Nur wrote her evaluation questions with an LLM

**Author:** Gözde Nur Özdemir (questions `B-01`–`B-07`, `B-S1`–`B-S3`, use case (b) learning-outcome assessment, and this record) · [KAN-46](https://yarengursoy.atlassian.net/browse/KAN-46)

The questions are in [`eval-set-v1.csv`](eval-set-v1.csv) (`B-01`–`B-07`, `B-S1`–`B-S3`). This page records how I drafted them with an LLM, the prompts and the model, as the course asks (*"If a model generated them, name the exact model"*).

## How I wrote the questions, step by step

1. I picked the use case: AI that grades or evaluates students (Annex III, point 3(b)).
2. I chose the articles a developer of such a tool needs: Annex III 3(b), Article 6(2)–(4), 49(2), 5(1)(f), Articles 8–15 and 113. All of them are in `data/provision-list.csv`.
3. I asked Claude Opus 5.5 for candidate questions with answers (prompt below). It gave 22. Some were based on real examples from the EU AI Act Service Desk.
4. In Sprint 1 I kept 8 of the 22. I wanted at least one question of each type and no two questions about the same situation.
5. I rewrote them in simple words, the way a developer would ask, without article numbers.
6. On 05/11/2026 I changed three questions and added a ninth one (`B-06`), so that different people ask in different ways (see the last section).
7. On 07/11/2026 I added `B-07`, a false-premise question, with the prompt of the team's [question-writing method](question-writing-method.md) (KAN-85), and labelled all my questions with its new columns (`user`, `premise`, `hops`, `challenge`, `gold_ids`). The set now has **10 questions**.
8. I checked every answer and source against the PDF and fixed two mistakes.
9. For each question, `eval-set-v1.csv` says who wrote it, which model and prompt were used, and where it came from.

## Which methods from the course slides I used

The course slides *Building test datasets for RAG* list five method families. My 3(b) questions use four of them; I applied them by hand with one LLM prompt, not with the RAGAS or DeepEval tools.

| Method (slides) | What I did | Example |
|---|---|---|
| **A · Generate, then filter** | The LLM wrote 22 questions with answers; I kept the clear ones and checked every answer and source against the text of the law. | 22 candidates → 8 kept (steps 3, 4, 7 above) |
| **B · Category-controlled** | I chose the question types first, one of each, and different people asking (developer, product manager). | `B-01` condition / exception, `B-04` boundary case, `B-05` asked by a product manager |
| **C · Multi-hop** | Some answers need two provisions together. | `B-03`: Article 6(4) **and** Article 49(2); `B-06`: the date in Article 113 **and** the use case in Annex III 3(b) |
| **E · Hard cases on purpose** | Questions the assistant must refuse, redirect, or say it cannot answer. | `B-S1` asks how to get around the law; `B-S2` asks about fines (out of scope); `B-S3` asks for an accuracy number the law does not give |

I did not use **D · Schema-based generation**: the slides suggest it when real documents are few or private, and our document, the AI Act, is public.

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

In Sprint 1 I selected 8 of the 22 candidates (`B-01`–`B-05`, `B-S1`–`B-S3`) and checked every gold answer against the PDF of the consolidated text. The ninth question, `B-06`, was added on 05/11/2026 (next section).

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
