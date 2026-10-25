# Spike: choosing the answer model

**Sprint:** 1 · **Author:** Gözde Nur · **Date:** 25/10/2026 · **Jira:** KAN-30, KAN-24

## 1. What question does this spike answer?

ELIZA needs a language model that writes the answer. The course requires an open-source, quantized model (C-03). We have no dedicated GPU (C-05).

This spike answers two questions:

1. Which model gives the best answers to our questions?
2. Can simple rules stop the model from giving legal verdicts or helping users avoid the law (C-08)?

## 2. How did we test?

- **Questions.** We used our 8 questions on Annex III point 3(b) ([`eval-set-v1-3b.csv`](../eval/eval-set-v1-3b.csv)). Five are normal questions. Three are safety questions: one asks how to avoid the rules, one asks about fines, and one asks for a number that the law does not give.
- **Text given to the model.** Retrieval is not built yet. So we gave each question the correct provisions by hand, plus one or two unrelated provisions. This tests only the model, not the search.
- **Same conditions for every model.** The same prompt, the same questions and the same settings.
- **Settings.** We used the 4-bit version of each model (`Q4_K_M`) and temperature 0, so the model gives the same answer every time. The answer limit was 300 tokens (`max_tokens`), and the context window was 4,096 tokens (`n_ctx`).
- **Two rule-based checks** ([`checks.py`](model-selection/checks.py)):
  - The **input check** runs before the model. If the user asks how to avoid the rules, or asks about fines or the GDPR, the system gives a fixed reply. The model is not called.
  - The **output check** runs after the model. If the answer says something like "your system is not high-risk", that sentence is deleted and a short note is added.
- **When does an answer pass?** It cites the correct article and point, gives no verdict, and does not refuse without a reason. A script scored each answer. Then I read every answer myself.

## 3. Which models did we test, and why?

We chose well-known open-source instruction models with clear licences.

| Model | Size | Licence | Why we tested it |
|---|---|---|---|
| Llama-3.2-3B-Instruct | 3B | Llama 3.2 Community License | Small and fast; runs on CPU |
| Qwen3-4B | 4B | Apache-2.0 | Small and strong for its size |
| Phi-4-mini-instruct | 3.8B | MIT | Small; the simplest licence |
| Llama-3.1-8B-Instruct | 8B | Llama 3.1 Community License | Larger; we wanted to see if a larger model gives better answers |
| Qwen3-8B | 8B | Apache-2.0 | Larger; for the same reason |

We started with small models (3–4B) because they are fast on a CPU. Their answers often picked the wrong point of an article, so we also tried two 8B models.

## 4. What happened in each run?

We ran the test 5 times. After each run we fixed one problem.

| Run | Models | What we changed | Passed (of 8) |
|---|---|---|---|
| 1 | Llama-3.2-3B, Qwen3-4B, Phi-4-mini | First test | 5, 4, 2 |
| 2 | Same three | Shorter prompt. Added the input check and the output check, because in run 1 Qwen3-4B helped a user avoid the rules and two models gave verdicts. | 5, 5, 5 |
| 3 | Phi-4-mini | Fixed the output check, which also deleted normal "if …" sentences. Split Article 6(3) into its points (a)–(d). | 5 |
| 4 | Llama-3.1-8B, Qwen3-8B, Phi-4-mini | Tried the larger models. Turned off Qwen3's "thinking" mode with `/no_think`. | 7, 2*, 5 |
| 5 | Llama-3.1-8B, Qwen3-8B | Tried a second way to turn off Qwen3's "thinking" mode (an empty thinking block). | 7, 2 |

\* The script first counted 7 for Qwen3-8B in run 4. When I read the answers, I saw that its 5 normal answers were only thinking text, with no answer. The script had found the article numbers inside the thinking text. The correct count is 2 (the two safety questions answered by the input check).

## 5. What did we find?

**Llama-3.1-8B-Instruct gave the best answers.**

- It passed 7 of 8 questions in both run 4 and run 5.
- It cited the correct articles and usually named the correct point.
- It gave a real answer, not long "thinking" text.
- It failed one question (B-02): it did not name Article 6(3)(b).
- When I read the answers, I found two mistakes the script missed:
  - In B-03 it said Article 49(2) does not apply, but it does.
  - In B-04 one sentence contradicts itself.

**Qwen3-8B is not a good fit for us.**

- Qwen3-8B is a "thinking" model: it writes a long reasoning text before the answer. In our test, this reasoning used the whole answer limit (300 tokens), and it was the slowest model. We need short, fast answers on a CPU, so we chose models that answer directly.

**Phi-4-mini-instruct is our fallback.**

- It passed 5 of 8 questions, so its answers are weaker than Llama's.
- It is 2–3 times faster than the 8B models, and its licence (MIT) is the simplest.

**The rule-based checks worked.**

- The input check answered the two safety questions (avoiding the rules, fines) in every run after run 1.
- The output check deleted every verdict sentence, for example "it is not considered high-risk".

## 6. How long did one answer take?

These are average times for one normal question.

| Model | Seconds |
|---|---|
| Small models (run 1, CPU) | 38–54 |
| Phi-4-mini (run 4) | 93 |
| Llama-3.1-8B (runs 4 and 5) | 206–232 |
| Qwen3-8B (runs 4 and 5) | 329–348 |

These times are too long for users. Runs 4 and 5 used a Colab GPU, but the times show that the model probably did not use it. We must measure the time again on the CPU machine that we will use for deployment.

## 7. Recommendation

1. Use **Llama-3.1-8B-Instruct** (`Q4_K_M`, temperature 0). This is decision [D9 in the design document](../../Markdown%20Template/11-system-architecture-design-document.md).
2. Keep **Phi-4-mini-instruct** as the fallback. Switch to it if Llama is too slow on our CPU machine (R-16).
3. Keep the input check and the output check in the product.
4. Measure the answer time of Llama-3.1-8B on the deployment CPU in Sprint 2, before deliverable D6.

The notebooks and result files of all runs are in [`model-selection/`](model-selection/).
