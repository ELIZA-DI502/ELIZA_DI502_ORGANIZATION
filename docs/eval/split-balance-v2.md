# Balance of the question categories in each split (v2)

**Author:** Yaren Gürsoy · [KAN-184](https://yarengursoy.atlassian.net/browse/KAN-184) (task [KAN-170](https://yarengursoy.atlassian.net/browse/KAN-170), D8 criterion 2) · **Counted on:** 28/11/2026

This page checks that each split of Q&A dataset v2 (D8) holds the categories that D8 criterion 2 asks for, before the `val` split is frozen on 01/12/2026 (KAN-185).

## What was counted

- **Questions:** all 70 questions of v2: the 46 questions of [`eval-set-v1.csv`](eval-set-v1.csv) and the 24 new questions of [`eval-set-v2-a.csv`](eval-set-v2-a.csv) ([PR #119](https://github.com/ELIZA-DI502/ELIZA_DI502_ORGANIZATION/pull/119), not yet merged), [`eval-set-v2-b.csv`](eval-set-v2-b.csv), [`eval-set-v2-c.csv`](eval-set-v2-c.csv) and [`eval-set-v2-d.csv`](eval-set-v2-d.csv). Every ID is unique.
- **Split:** the `split` column.
- **Safety category:** the `type` of every question with `category` = `safety`.
- **Application-date question:** a question with an Article 113 provision in `gold_ids` (`ART113-…`).
- **Follow-up pair:** a question with `follows <ID>` in `context`, and the question it follows.

## Result

| Criterion (KAN-184) | Target | `val` | `test` | Met |
|---|---|---|---|---|
| Application-date questions per split | at least 3 | 6 | 4 | ✓ |
| Adversarial questions per split | at least 2 | 2 | 4 | ✓ |
| Out-of-scope questions per split | at least 2 | 2 | 3 | ✓ |
| Insufficient-evidence questions per split | at least 2 | 3 | 3 | ✓ |
| Legal-decision questions per split | at least 2 | 2 | 2 | ✓ |
| Safety questions in total | at least 16 | 9 | 12 | ✓ (21) |
| The four use cases in each split | (a), (b), (c), (d) | 7 / 14 / 9 / 12 | 9 / 3 / 7 / 9 | ✓ |
| Follow-up pairs in the same split | all | 5 of 5 | none in `test` | ✓ |

All criteria of KAN-184 are met.

## Questions per split

| | `val` | `test` | Total |
|---|---|---|---|
| Questions | 42 (v1 30, v2 12) | 28 (v1 16, v2 12) | 70 |
| Share | 60% | 40% | |

**Application-date questions:** `val`: `B-06`, `C-04`, `C-05`, `D-04`, `D-08`, `B-09` · `test`: `A-07`, `D-06`, `A-11`, `D-15`.

**Follow-up pairs (`val`):** `A-02` → `A-05`, `B-03` → `B-01`, `C-03` → `C-02`, `D-10` → `D-09`, `B-10` → `B-09`.

## Other axes (for the data card)

Not required by KAN-184; counted for the comparison with the target mix of the [question-writing method](question-writing-method.md) (Step 6, check 3).

| Axis | `val` | `test` |
|---|---|---|
| Question type (scenario questions) | direct lookup 9 · multi-provision 9 · boundary case 5 · condition / exception 5 · follow-up 5 | direct lookup 9 · boundary case 3 · condition / exception 2 · multi-provision 2 |
| User | developer 21 · technical lead 15 · legal 6 | developer 14 · technical lead 9 · legal 5 |
| Premise | own product 32 · general 10 | own product 23 · general 5 |
| Hops | single 28 · multi 6 · none 8 | single 13 · multi 4 · none 11 |
| False premise | 3 (`B-07`, `C-04`, `C-05`) | 2 (`A-04`, `D-15`) |
| Time-sensitive | 6 | 3 |

Notes:

- **Premise:** own product is 79% of all questions (target about 60%), because all 24 new v2 questions describe the user's own product. Every split still has more than 3 general questions.
- **Labels:** `C-09` is labelled `time-sensitive` but has no Article 113 provision in `gold_ids`; `D-06` has `ART113-3-a` but is not labelled `time-sensitive`. The counts above use `gold_ids`.

## Next step

The counts are to be run again on the merged `eval-set-v2.csv` (KAN-237), after PR #119 is merged. A change to `A-11` (PR #119) does not change the counts: its `gold_ids` keep an Article 113 provision in both options.
