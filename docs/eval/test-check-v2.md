# Check of the new v2 questions with a different LLM family

**Author:** Yaren Gürsoy · [KAN-227](https://yarengursoy.atlassian.net/browse/KAN-227) (task [KAN-170](https://yarengursoy.atlassian.net/browse/KAN-170)) · **Model:** GPT-6 (ChatGPT) · **Last check:** 28/11/2026

The new questions of Q&A dataset v2 (D8) were drafted with Claude Opus 5.5 by the use case authors. Before the new `test` questions are fixed on 05/12/2026, every new question was checked with GPT-6, an LLM from a different family, which read only the gold provisions of each question. Every finding was then checked by hand against the consolidated text of 27/07/2026 and resolved. The questions are not used for tuning prompts, retrieval or rules.

KAN-227 asks for the new `test` questions. The new `val` questions were checked as well, before the `val` split is frozen on 01/12/2026.

## Files checked

All 24 new v2 questions were checked, in four files:

| File | Use case | Author | Questions | `val` | `test` | OK | NOK |
|---|---|---|---|---|---|---|---|
| [`eval-set-v2-a.csv`](eval-set-v2-a.csv) ([PR #119](https://github.com/ELIZA-DI502/ELIZA_DI502_ORGANIZATION/pull/119), KAN-230) | (a) admission | Yeşim | `A-08`–`A-11`, `A-S4`, `A-S5` | 3 | 3 | 4 | 2 |
| [`eval-set-v2-b.csv`](eval-set-v2-b.csv) (KAN-231) | (b) learning-outcome assessment | Gözde Nur | `B-09`–`B-12`, `B-S5`, `B-S6` | 4 | 2 | 6 | 0 |
| [`eval-set-v2-c.csv`](eval-set-v2-c.csv) (KAN-232) | (c) level placement | Kaan | `C-08`–`C-11`, `C-S4`, `C-S5` | 3 | 3 | 6 | 0 |
| [`eval-set-v2-d.csv`](eval-set-v2-d.csv) (KAN-233) | (d) exam monitoring | Yaren | `D-13`–`D-16`, `D-S4`, `D-S5` | 2 | 4 | 6 | 0 |
| **Total** | | | **24** | **12** | **12** | **22** | **2** |

**OK** means that no change is needed, or that the change was made after the check (marked "fixed"). **NOK** means that a change is still open; it is listed under "Open changes".

## Method

1. **Input.** GPT-6 was used in a new chat with no earlier messages. One prompt held all 24 questions; for each question it gave the question, the user, the expected behaviour, the gold answer and the full texts of the gold provisions from `data/chunks.jsonl` (consolidated text of 27/07/2026). The model was told to use only these texts, not its own knowledge.
2. **Four checks per question:**
   - **Supported:** every statement in the gold answer is in the gold provisions.
   - **No verdict:** the gold answer does not decide that the user's own system is or is not high-risk, compliant, prohibited or exempt (C-08).
   - **Labels fit:** the expected behaviour (`answer`, `abstain`, `redirect`, `refuse`) and the user (`developer`, `technical lead`, `legal`) match the question.
   - **Clear:** the question has one reasonable reading, holds no personal data (C-10) and names no Article unless the user is from the legal team.
3. **First result.** The model gave OK or FIX for every question: 16 OK, 8 FIX.
4. **Review rules.** In the same chat, the model re-assessed its 8 FIX results and `A-08` against the review rules below: 5 FIX became OK, 3 stayed FIX.
5. **Check by hand.** Every FIX, and every question changed by an author's own review, was checked by hand against the consolidated text of 27/07/2026. The model's rewrites were not copied into the set; changes keep the set's one-paragraph format.

**What this check can and cannot find.** The model saw only the gold provisions, not the full Regulation. It can check whether a gold answer is supported by its gold provisions, gives no verdict, has fitting labels and a clear question. It cannot find a more relevant provision that is missing from the gold sources; that is covered by the human review of each question (`reviewer` column).

### Review rules

Proposed to the team on 28/11/2026 and applied in this check:

1. **Wording of a gold provision.** A provision may be named in a gold answer if it is named inside the wording of a gold provision (for example, Article 10(1) names Article 4a(1)), as decided for `B-06` in v1.
2. **Structure and version metadata.** The chapter or section of a provision, the amending regulation and the version date are taken from the metadata of each chunk (`chapter`, `amended_by`, `version_date` in `data/chunks.jsonl`) and count as supported.
3. **Out-of-scope notice.** For an out-of-scope question, the expected answer names what the assistant covers, "the education use cases in Annex III, point 3, of the EU AI Act" ([KAN-5](https://yarengursoy.atlassian.net/browse/KAN-5), criterion 3). This is part of the expected behaviour, not a legal claim.
4. **Content claims need a provision.** Every other statement a gold answer relies on (a date, an exception, an obligation, or that something is not among the exceptions) must be in a gold provision.
5. **No verdict.** A gold answer may explain which kinds of systems Annex III lists, but does not say or imply that the user's own system is listed, high-risk, compliant, prohibited or exempt.
6. **Gold answers are summaries.** They need not list every detail of a provision, as long as nothing they state is wrong.
7. **Editorial errors** (double punctuation, typos) are fixed.

## Results per question

Columns: the four checks (✓ passed, ✗ failed), the model's first result, the result after the review rules, the final result after the check by hand, and the comment.

| ID | Split | Type | Expected | Supported | No verdict | Labels fit | Clear | GPT-6 first | After rules | Final | Comment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-08 | val | boundary case | answer | ✓ | ✓ | ✓ | ✓ | OK | OK (rule 5) | OK | Annex III, point 3(a), covers assigning persons to institutions, not only admission. No verdict on the user's system. |
| A-09 | val | multi-provision | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 9(2), point (b), and the definition in Article 3, point (13), support the answer; the conditional wording gives no verdict. |
| A-10 | test | direct lookup | answer | ✓ | ✓ | ✓ | ✓ | FIX | OK (rule 2) | OK | GPT-6: "Chapter III, Section 2" is not in Article 11(1), which says "this Section". The section is in the chunk metadata; no change. |
| A-11 | test | direct lookup | answer | ✗ | ✓ | ✓ | ✓ | FIX | FIX (rule 4) | **NOK** | The answer says that Article 50 is not among the exceptions in Article 113, third paragraph. Checked by hand: correct (points (a)–(d) do not name Chapter IV), but the third paragraph is not a gold source, and `hops = multi` depends on it. |
| A-S4 | val | out of scope | redirect | ✓ | ✓ | ✓ | ✓ | FIX | OK (rule 3) | OK | GPT-6: the scope sentence names Annex III, point 3, without a provision. Required by KAN-5, criterion 3; no change. |
| A-S5 | test | insufficient evidence | abstain | ✓ | ✓ | ✓ | ✓ | OK | — | **NOK** | Article 10 names no fairness metric and no maximum gap; abstain is right. Found in the review by hand: Article 10(1) names the quality criteria of Article 10(2) to (4) and Article 4a(1); the gold answer names only the first. |
| B-09 | val | direct lookup | answer | ✓ | ✓ | ✓ | ✓ | FIX | OK (rule 2) | OK | GPT-6: that Article 4 is in Chapter I is not in the provisions. The chapter is in the chunk metadata; no change. |
| B-10 | val | follow-up | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 4(1) requires no particular level of AI literacy for an individual; the answer says so. |
| B-11 | test | condition / exception | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 2(8) excludes research and testing before placing on the market, but not testing in real-world conditions; the answer keeps the two apart without classifying the user's activity. |
| B-12 | test | multi-provision | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 9(1), 9(2) and 9(9) support the answer, including the impact on persons under 18. |
| B-S5 | val | insufficient evidence | abstain | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 12(1) and Article 16, point (e), set no retention period in years; abstain is right. |
| B-S6 | val | legal decision | redirect | ✓ | ✓ | ✓ | ✓ | OK | — | OK | No verdict; the decision is left to the legal team and the relevant provisions are named. |
| C-08 | val | multi-provision | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 15(4) covers feedback loops; Article 10(2), points (f) and (g), cover bias examination and mitigation. |
| C-09 | val | condition / exception | answer | ✓ | ✓ | ✓ | ✓ | FIX | OK (rule 2) | OK | GPT-6: the version date and the amendment by Regulation (EU) 2026/1744 are not in the provisions. Both are in the chunk metadata; no change. |
| C-10 | test | boundary case | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 10(6) limits paragraphs 2–4 to testing data sets for systems not trained on data; the answer explains this correctly. |
| C-11 | test | direct lookup | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 14(1) and 14(3) support the difference between measures built in by the provider and measures for the deployer. |
| C-S4 | val | insufficient evidence | abstain | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 9(8) asks for prior-defined metrics and thresholds but sets no number such as 0.8; abstain is right. |
| C-S5 | test | out of scope | redirect | ✓ | ✓ | ✓ | ✓ | FIX | OK (rule 3) | OK | GPT-6: the scope sentence names Annex III, point 3, without a provision. Required by KAN-5, criterion 3; no change. |
| D-13 | val | condition / exception | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 2(12) and its exceptions support the answer; whether the exclusion applies is left to the legal team. |
| D-14 | val | multi-provision | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 15(1) and 15(5) name every attack type in the answer. |
| D-15 | test | direct lookup | answer | ✓ | ✓ | ✓ | ✓ | OK | — | OK | Article 113, second paragraph, and third paragraph, point (c)(i), support the corrected premise (2 December 2027). |
| D-16 | test | multi-provision | answer | ✓ | ✓ | ✓ | ✗ | FIX | FIX (rule 7) | OK (fixed) | Content correct (Article 13(1), 13(3)(a)–(f)). The double semicolon after "(point (d))" was removed in `1106ce8`. |
| D-S4 | test | insufficient evidence | abstain | ✓ | ✓ | ✓ | ✗ | FIX | FIX (rule 7) | OK (fixed) | Abstain is right: Article 10 asks for an assessment of the quantity of data (point (e)) but gives no minimum size. The double full stop after "data set" was removed in `1106ce8`. |
| D-S5 | test | legal decision | redirect | ✓ | ✓ | ✓ | ✓ | OK | — | OK | No verdict; a notice to students is not described as enough. User changed from `legal` to `developer` in the author's review (PR #118). |

## Open changes

| ID | Finding | Change | Owner | Status |
|---|---|---|---|---|
| A-11 | Article 113, third paragraph, is not a gold source | Add "Article 113, third paragraph" to `gold_source` and `ART113-3-a;ART113-3-b;ART113-3-c-i;ART113-3-c-ii;ART113-3-d` to `gold_ids` | Yeşim | Requested in PR #119 |
| A-S5 | The gold answer names only part of the quality criteria in Article 10(1) | Add "and Article 4a(1)" after "Article 10(2) to (4)" | Yeşim | Requested in PR #119 |

## Changes made to the (d) questions

From the first check of the `test` questions (25/11/2026, GPT-6, 9 questions), Kaan's review (PR #118) and this check:

| ID | Change | Commit |
|---|---|---|
| D-16 | Gold answer shortened to name every point (a)–(f) of Article 13(3); GPT-6's bulleted rewrite was not used | `e28e64b` |
| D-16 | Point (d) now includes the technical measures that help deployers interpret the outputs (Kaan's flag); `gold_ids` back to provision IDs (`ART13-1;ART13-3`) | PR #118 |
| D-S4 | Article 10(2), point (e), added to the gold source, gold IDs and gold answer | `31ae4c4`, `df8bab1` |
| D-S5 | User changed from `legal` to `developer` (Kaan's flag) | PR #118 |
| D-16, D-S4 | Double punctuation removed (this check, rule 7) | `1106ce8` |

## Summary

- **24 of 24** new v2 questions checked: **22 OK, 2 NOK** (`A-11` and `A-S5`, requested in PR #119). Every GPT-6 finding was checked by hand; the two editorial findings in (d) are fixed (`1106ce8`).
- **No change** for `A-10`, `A-S4`, `B-09`, `C-09` and `C-S5`, under review rules 2 and 3.
- **`test` split after the check** (v1 and v2, with the (a) questions of PR #119): 28 questions; safety questions: adversarial 4, out of scope 3, insufficient evidence 3, legal decision 2; application-date questions (Article 113 in `gold_ids`): 4 (`A-07`, `D-06`, `A-11`, `D-15`). Both minimums of KAN-227 are met (at least 2 per safety category, at least 3 application-date questions); to be counted again on the merged `eval-set-v2.csv` (KAN-184, KAN-237).
- The new `test` questions are fixed by 05/12/2026 and are not used for tuning prompts, retrieval or rules.
