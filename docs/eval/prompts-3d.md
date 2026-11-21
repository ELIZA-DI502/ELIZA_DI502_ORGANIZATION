# How the D questions were written

**Author:** Yaren Gürsoy (questions `D-01`–`D-10`, `D-S1`–`D-S3`, use case (d) exam monitoring, and this record) · [KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65)


> **Note on the prompts.** I drafted the questions in an interactive chat with Claude Sonnet 5.5 between 04/11 and 08/11/2026, and the chat was not archived. The prompts below were reconstructed on 21/11/2026, following the questions and the way the other use cases were written [`question-writing-method.md`](question-writing-method.md)). They give the instructions I used; the exact wording in the original chat may differ.

## How I wrote the questions, step by step

1. I picked the use case: AI that monitors and detects prohibited behaviour of students during tests (Annex III, point 3(d)).
2. I chose the provisions a developer of such a tool needs: Annex III 3(d) (and 3(b) for comparison), Article 2(1)(a), 3(3), 5(1)(f), 6(2)–(4), 8–16, 49(2) and 113. All of them are in `data/provision-list.csv`.
3. I asked Claude Sonnet 5.5 for candidate questions with gold sources (first prompt below).
4. I kept 13 questions: 10 scenario questions with every question type, and 3 safety questions (2 adversarial, 1 out of scope). I did not keep two questions about the same situation.
5. I rewrote them in simple words, the way a developer, technical lead or legal team member would ask (second prompt).
6. I drafted the gold answers with the LLM only from the texts of the gold provisions (third prompt), and the expected behaviour of the safety questions (fourth prompt).
7. I checked every answer and source against the PDF of the consolidated text of 27/07/2026. A second member reviewed all 13 questions on 10/11/2026; `D-04`, `D-06`, `D-S1` and `D-S2` were corrected on 14/11/2026.
8. After the [question-writing method](question-writing-method.md) (KAN-85) was adopted, I labelled all my questions with its columns (`user`, `premise`, `hops`, `challenge`, `gold_ids`).

## Which methods from the course slides I used

| Method (slides) | What I did | Example |
|---|---|---|
| **A · Generate, then filter** | The LLM wrote candidate questions with gold sources; I kept the clear ones and checked every answer and source against the text of the law. | 13 questions kept (steps 3, 4, 7) |
| **B · Category-controlled** | I chose the question types and the users first. | `D-02` legal team, `D-07` condition / exception, `D-10` follow-up |
| **C · Multi-hop** | The answer of one provision is needed for the next. | `D-04`: Annex III 3(d) → Article 113, third paragraph, point (c)(i) |
| **E · Hard cases on purpose** | Questions the assistant must refuse or redirect, and a time-sensitive one. | `D-S1`, `D-S2` adversarial; `D-S3` GDPR (out of scope); `D-04` application date |


## Prompts

Model: Claude Sonnet 5.5 (`claude-sonnet-5-5`), 04/11–08/11/2026, interactive chat on claude.ai.

**Generating candidates**

```text
Write candidate questions for Annex III point 3(d) of Regulation (EU) 2024/1689 (AI systems that monitor and detect prohibited behaviour of students during tests in education).
- Scenario questions that a developer, a technical lead or a legal team member at an EdTech company might ask: direct lookup, condition/exception, multi-provision, follow-up and boundary case.
- Cover these situations: where the tool is classified, schools vs universities, a provider outside the EU, the application date, the difference from a grading tool (point 3(b)), a feature that reads students' emotions, a tool that only does a narrow task while a human decides, the provider's obligations, and human oversight.
- Safety questions: two adversarial questions and one out-of-scope question.
For each question give the gold source (Article, paragraph, point). Use only the consolidated text of 27/07/2026. Never state that a system is or is not compliant or high-risk.
```

**Simplifying the selected questions**

```text
Rewrite these questions in simple, everyday language, as the given user would ask them (developer, technical lead or legal team). Do not use article numbers in the question. Keep the same situation, so the gold source still holds.
```

**Gold answers**

```text
Here are the texts of the gold provisions from the consolidated text of 27/07/2026. Write a short gold answer for this question using only these texts. Do not add anything that is not in them, and do not say whether the user's product is high-risk or compliant.
```

**Expected behaviour for the safety questions**

```text
For each of these safety questions, write the expected behaviour of the assistant: refuse (with a one-sentence reason) or redirect (out of scope). If a relevant provision exists, name it.
```

## The questions I kept

| ID | Labels | Gold provisions |
|---|---|---|
| D-01 | direct lookup; developer, general | Annex III, point 3(d); Article 6(2) |
| D-02 | direct lookup; legal team, general | Annex III, point 3(d) |
| D-03 | direct lookup; legal team, own product | Article 2(1), point (a); Article 3(3) |
| D-04 | direct lookup, multi-hop, time-sensitive; technical lead, general | Article 113, third paragraph, points (a) and (c)(i); Annex III, point 3(d); Article 6(2) |
| D-05 | multi-provision; technical lead, general | Annex III, points 3(b) and 3(d); Article 6(2); Articles 8–15 |
| D-06 | boundary case; developer, own product | Article 5(1)(f); Annex III, point 3(d); Article 113, third paragraph, point (a) |
| D-07 | condition / exception; technical lead, own product | Article 6(3); Article 6(4); Article 49(2) |
| D-08 | multi-provision; developer, own product | Annex III, point 3(d); Article 6(2)–(3); Articles 8–16; Article 5(1)(f); Article 113 |
| D-09 | multi-provision; technical lead, own product | Article 8(1); Articles 9–15; Article 16 |
| D-10 | follow-up; technical lead, own product | Article 14(1) and (4); Article 13(1); Article 12(1) |
| D-S1 | adversarial (refuse); developer | Article 6(3) |
| D-S2 | adversarial (refuse); technical lead | Article 5(1)(f) |
| D-S3 | out of scope (redirect); legal team | — (GDPR, C-04) |
