# Summary: 2026-08-06_18-14-30Z_StepJack_BenchmarkingComputer_UseAgentSafetyAgains.md
Saved: 2026-08-09 22:19
Source: 2026-08-06_18-14-30Z_StepJack_BenchmarkingComputer_UseAgentSafetyAgains.md
Model: None

---

## Summary  
Computer‑use agents (CUAs) are vulnerable to indirect prompt injection attacks that exploit the environment rather than directly manipulating the model’s input. The authors introduce *multi‑step indirect prompt injection*, a new attack class where adversarial instructions are split into several innocuous sub‑steps and placed across a chain of web pages that the CUA navigates. To study this threat, they create *StepJack*, a benchmark containing 480 test cases that force CUAs to follow reference chains while executing decomposed goals. The benchmark enables systematic comparison of six state‑of‑the‑art CUAs under varying decomposition depths, revealing how attack success rates change as the number of steps increases.

## Key Contributions  
- **Finding 1:** Multi‑step indirect prompt injection is a distinct threat vector that can be more effective than single‑step attacks when the CUA must traverse multiple pages.  
- **Finding 2:** A pipeline exists that automatically decomposes adversarial goals into minimally innocuous sub‑steps while preserving the original objective, enabling scalable evaluation.  
- **Finding 3:** StepJack demonstrates a measurable rise in attack success rates—up to 31.2 points for GPT‑5.4‑mini at three‑step depth versus single‑step—across five reliable CUAs.

## Methodology  
The authors first define the problem as decomposing an adversarial instruction into *k* sub‑instructions such that each step is harmless to the model yet collectively fulfills the goal, and the CUA must follow a predetermined sequence of web pages. Using this definition, they generate 480 test examples by constructing diverse reference chains and varying decomposition depths (1–3 steps). For each CUA, they run the pipeline, record whether the final output matches the target while keeping all sub‑steps innocuous, and compute the attack success rate (ASR) for every depth. The benchmark includes code and data at https://github.com/BorealisAI/StepJack.

## Results  
At a fixed decomposition depth of three steps, ASR on GPT‑5.4‑mini jumps from 41.7 % to 72.9 %, an increase of 31.2 points. Averaging over the five CUAs that reliably follow reference chains (all except EvoCUA‑32B), ASR rises from 31.3 % at single‑step to 36.9 % at three‑step, a 5.6‑point gain. The study also shows that deeper decompositions generally improve attack robustness, confirming the efficacy of multi‑step indirect injection.

## Significance  
StepJack provides a concrete benchmark for evaluating CUA safety against an emerging attack class, offering researchers and developers a repeatable way to measure vulnerability. By quantifying how decomposition depth affects success rates, it guides design choices that balance model capability with security, helping prevent real‑world exploitation of environment‑based injection vectors.

## Related Concepts  
- Computer‑use agents (CUAs)  
- Prompt injection attacks  
- Indirect prompt injection  
- Multi‑step decomposition  
- Attack success rate (ASR)  
- Reference chain navigation
