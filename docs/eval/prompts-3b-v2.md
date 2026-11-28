# How the new B questions for v2 were written

**Author:** Gözde Nur Özdemir (questions `B-09`–`B-12`, `B-S5`, `B-S6`, use case (b) learning-outcome assessment, and this record)

The questions are in [`eval-set-v2-b.csv`](eval-set-v2-b.csv). This page records how I drafted them with an LLM, the prompts and the model, as for the v1 questions in [`prompts-3b.md`](prompts-3b.md).

## How I wrote the questions, step by step

1. I wanted 6 new questions for use case (b): 1 application-date question, 1 follow-up, 2 safety questions, written in the same way as the v1 questions.
2. I asked Claude Opus 5.5 for about 12 candidates (first prompt below). It gave 12, each with its question type, challenge, user, gold provisions and the baseline error it came from.
3. I asked it to compare them with the old questions so that none is the same as, or very close to, a v1 question (second prompt). It checked all 46 v1 questions by shared words and shared gold provisions and replaced 6 candidates.
4. I chose 5 questions. Three of them were still close to v1 questions, so I asked for different ones that are still correct (third prompt): the follow-up had the same answer as `B-06`, the condition question was about Article 6(3) like `B-01`, `D-07` and `C-01`, and the "ignore your rules" question was like `D-S1`.
5. I had 3 safety questions, but I wanted 2, so I removed the out-of-scope one and added a multi-provision question. Its first version was close to `B-S3` (accuracy) and `A-02` (human oversight), so I replaced it with a question on risk management for students under 18 (Article 9(9)).
6. The gold answers were drafted only from the texts of the gold provisions in `data/chunks.jsonl`. I checked every sentence against the consolidated text of 27/07/2026.
7. KAN-231 asks for 2 `val` and 2 `test` scenario questions, so I moved `B-11` and `B-12` to `test` (21/11/2026). `B-09` and `B-10` stay in `val`, because a follow-up stays in the same split as the question it follows.
8. After Yeşim's review (KAN-231, PR #117, 26/11/2026) I fixed the three flags with the same model (fourth prompt) and checked every change against the consolidated text of 27/07/2026: `B-09` no longer says that everyone has to get training (Article 4(1) asks for measures that support AI literacy); `B-11` was replaced, because the first version (Article 2(8), testing before the market) overlapped with the example in `prompts/answer.yaml` and needed a conditional answer: the new question is on the exclusion for personal non-professional use (Article 2(10), Article 3, point (4)); `B-S6` now gives the conditions of Article 6(3) (points (a) to (d) of the second subparagraph and the profiling rule of the third subparagraph). I also added the two optional notes to the gold answers of `B-10` and `B-12`. The new `B-11` is a `test` question, so it still needs the check with a different LLM family ([`test-check-v2.md`](test-check-v2.md)).

## Prompts

Model: Claude Opus 5.5 (`claude-opus-5-5`), 20/11/2026.

**Candidates**

```text
Propose about 12 new evaluation questions for use case (b) in the same way as our v1 questions (docs/eval/question-writing-method.md), one of them a follow-up. I will choose from them.
```

**Not the same as the old questions**

```text
We have old B questions and other v1 questions. The new questions must not be the same as them or very similar.
```

**Different but correct**

```text
Remove these, and give different ones, but they must also be correct.
```

**Review flags (26/11/2026)**

```text
Fix the review flags of Yeşim on B-09, B-11 and B-S6 (PR #117), and add her optional notes on B-10 and B-12.
```

## The questions I kept

| ID | Split | Labels | Gold provisions |
|---|---|---|---|
| B-09 | `val` | direct lookup, time-sensitive; technical lead, own product | Article 4(1); Article 113, third paragraph, point (a) |
| B-10 | `val` | follow-up (follows `B-09`); technical lead, own product | Article 4(1) |
| B-11 | `test` | condition / exception; developer, own product | Article 2(10); Article 3, point (4) |
| B-12 | `test` | multi-provision; technical lead, own product | Article 9(1), (2) and (9) |
| B-S5 | `val` | insufficient evidence; developer, own product | Article 12(1); Article 16, point (e) |
| B-S6 | `val` | legal decision; developer, own product | Annex III, point 3(b); Article 6(2); Article 6(3), first to third subparagraph; Article 14(4) |
