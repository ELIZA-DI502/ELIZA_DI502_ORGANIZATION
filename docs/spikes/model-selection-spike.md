# Spike: choosing the answer model

**Sprint:** 1 · **Date:** 25/10/2026 · **Jira:** KAN-57 · **Results:** [`model-selection-results.csv`](model-selection-results.csv)

## Question

Which open-source, quantized model gives the best answers (C-03), and can simple rules stop it from giving legal verdicts (C-08)?

## How we tested

- **No training.** The models are used as published. We only **tested** them: every model answered the same 8 questions on Annex III point 3(b) (AI systems that evaluate learning outcomes, for example grading students' work) ([`eval-set-v1-3b.csv`](../eval/eval-set-v1-3b.csv)). The questions were not split into train, validation and test sets.
- Retrieval is not built yet, so each question got its correct provisions by hand.
- Same prompt and settings for every model: 4-bit (`Q4_K_M`), temperature 0, at most 300 answer tokens. The models ran with `llama-cpp-python` on Google Colab; the answer time on the team computer below was measured with Ollama, which the system will use (D9).
- An answer **passes** if it cites the correct Article and point, gives no verdict, and does not refuse without a reason.

The prompt (the same for every model): a system message with the rules, one example question and answer (not from the test questions), then the provisions and the question.

```text
You explain the EU AI Act (Regulation (EU) 2024/1689, consolidated text of 27 July 2026) to software developers.
- Use only the PROVISIONS. Cite every provision you use, for example Article 6(3)(a). Do not cite provisions that are not relevant to the question.
- When a provision has points (a), (b), ..., name the point whose wording matches the user's description.
- Explain what the provisions say. Never state that the user's system is or is not high-risk, compliant, prohibited or allowed: the user makes that assessment.
- If the provisions answer only part of the question, say what they say and what they do not say.
- If no provision is relevant, reply only: "The provided text does not answer this question."
- At most 120 words.
```

Example given to the model before each question:

- *Question:* "Our app ranks applicants for a university programme. Is that the kind of system the AI Act lists as high-risk?" (with Annex III point 3(a) and Article 6(2) as provisions)
- *Answer:* "Annex III, point 3(a) lists AI systems intended to determine access or admission to educational institutions, and Article 6(2) says that the systems listed in Annex III are considered high-risk. Whether your app falls under this point depends on its intended purpose, so assess it against these provisions."

Each test question is sent as `PROVISIONS: [Article …] text … QUESTION: …`; for a follow-up question, the earlier question is added before it.

The test logic:

```python
for model in models:
    for q in questions:
        if input_check(q):                  # rule: avoiding the rules, fines, GDPR
            answer = fixed_reply(q)         # the model is not called
        else:
            answer = model.chat(prompt(q))  # provisions + question
            answer = remove_verdicts(answer)  # rule: delete "your system is (not) high-risk"
        passed = cites_gold_source(answer, q) and not has_verdict(answer)
```

What each step does:

| Step | What it does |
|---|---|
| `input_check(q)` | Looks for keywords in the question before the model is called. Words such as "avoid", "bypass", "hide" or "loophole" together with "rules" or "AI Act" mean a request to avoid the rules; "fine", "penalty" or "GDPR" mean an out-of-scope topic. |
| `fixed_reply(q)` | Returns a fixed sentence instead of a model answer: a refusal ("I can't help with avoiding or hiding from the AI Act's rules …") or an out-of-scope notice. |
| `prompt(q)` | Builds the message for the model: the rules and the example (above), then the question's provisions and the question. |
| `model.chat(...)` | Sends the message to the model and returns its answer (4-bit model, temperature 0, at most 300 tokens). |
| `remove_verdicts(answer)` | Finds sentences that decide for the user, such as "your system is not high-risk" or "this does not violate the AI Act", deletes them and adds the notice "this is not a legal decision". Sentences that only state a condition ("If your system is high-risk, it must …") are kept. |
| `has_verdict(answer)` | Checks with the same patterns whether a verdict sentence is still in the answer. |
| `cites_gold_source(answer, q)` | Checks that the answer names the question's gold source from [`eval-set-v1-3b.csv`](../eval/eval-set-v1-3b.csv), for example Article 6(3)(a) for B-01. |

## Results

We ran the test 5 times and fixed one problem after each run (details in the CSV).

| Model | Passed (of 8) | Seconds per answer |
|---|---|---|
| **Llama-3.1-8B-Instruct** | **7** | 206–232 (Colab T4) |
| Phi-4-mini-instruct | 5 | 36–100 (Colab CPU; 93 on Colab T4) |
| Llama-3.2-3B-Instruct | 5 | 38–90 (Colab CPU) |
| Qwen3-4B | 5 | 54–117 (Colab CPU); also a "thinking" model, but here thinking was turned off and it answered directly, so its answers could be scored |
| Qwen3-8B | 2 | 329–348 (Colab T4); a "thinking" model, it wrote only reasoning text and no answer. Its 2 passes are the two safety questions answered by the input check, not by the model |

- The input check answered the two safety questions (avoiding the rules, fines) without the model.
- The output check removed every verdict sentence.

### Answer time on one team computer

One of the team members' computers is a Mac with an Apple M3 Pro chip (12 cores: 6 performance and 6 efficiency cores) and 36 GB RAM. It is a candidate for the pilot computer (Major Activities row 29). We measured both selected models on it on 25/10/2026.

How we measured:

- **Settings**: Ollama on macOS, `Q4_K_M`, temperature 0, context window 4,096 tokens, answer limit 300 tokens.
- **CPU only** (`num_gpu` 0), as in C-05.
- **One question**: B-02, the longest prompt of the spike (the same prompt as in run 5).
- **Two runs per model.** The first run includes loading the model; the answer time below is the first run without the loading time. In the second run the prompt came from the cache, so it is not used for the answer time.

| Model | Prompt tokens | Answer tokens | Reading speed | Writing speed | Answer time |
|---|---|---|---|---|---|
| Llama-3.1-8B-Instruct | 894 | 103 | 83 tokens/s | 22 tokens/s | 15.4 s |
| Phi-4-mini-instruct | 877 | 203 | 176 tokens/s | 39 tokens/s | 10.2 s |

Loading the model took 6 s (Llama) and 9 s (Phi-4-mini), once at start.

**Worst case**, calculated from the measured speeds: a prompt of about 2,000 tokens (more retrieved chunks and the session history) and an answer of the full 300 tokens.

| Model | Worst case |
|---|---|
| Llama-3.1-8B-Instruct | about 38 s |
| Phi-4-mini-instruct | about 19 s |

This is one question and one run per model. Ollama ran directly on macOS, not in the Docker container of decision D6 in the design document, which may be slower. The time is measured again at the baseline (18/11/2026) and on the pilot computer by 09/12/2026 (R-13).

## Decision

Use **Llama-3.1-8B-Instruct** and keep **Phi-4-mini-instruct** as the fallback (decision D9 in the [design document](../../Markdown%20Template/11-system-architecture-design-document.md)). The Colab times above are slow; on a team computer's CPU, Llama answered in 15.4 s (see above). The time is measured again at the baseline in Sprint 2.
