# Summary: 2026-08-05_21-29-12Z_CanOpen_WeightLLMsProduceKernel_VerifiedCoqProofs_.md
Saved: 2026-08-06 20:30
Source: 2026-08-05_21-29-12Z_CanOpen_WeightLLMsProduceKernel_VerifiedCoqProofs_.md
Model: None

---

## Summary  
The paper investigates whether open‑weight large language models (LLMs) can generate Coq proofs that are accepted by the Coq kernel, a task that requires both syntactic correctness and logical soundness. By running each of six open‑weight LLMs on 100 theorems from the CoqStoq benchmark with temperature set to zero, the authors measured how many generated proofs passed the formal verification step. The study reports a modest overall success rate of 3.5 % (21 verified proofs out of 600 attempts) and highlights that only three models achieved any successful verifications.  

## Key Contributions  
- Finding 1: Open‑weight LLMs can occasionally produce kernel‑verified Coq proofs, with the best performers achieving up to 3.5 % success across 600 attempts.  
- Finding 2: The top models—Gemma 4 (12/100), Llama 3.3 (8/100) and DeepSeek Coder V2 Lite (1/100)—outperformed the others, while Qwen 3.5, Mistral Small 3.1 and GPT‑OSS produced none.  
- Finding 3: All verified proofs correspond to short or medium‑length human reference proofs; no model succeeded on a long reference proof, suggesting that proof length may be a contributing factor (though the analysis is exploratory).  

## Methodology  
The authors conducted a pilot study in which each LLM produced one attempt per theorem from CoqStoq. All attempts were generated with temperature 0 to ensure deterministic output, and the resulting proofs were fed into the original Coq project environment where the kernel evaluated their validity. The experiment recorded the number of successful verifications, the total token count and time required for each generation, and aggregated GPU hours. No statistical hypothesis testing was performed; only descriptive comparisons among models are reported.  

## Results  
Out of 600 attempts across six models, 21 proofs were accepted by Coq, yielding a 3.5 % success rate. The three successful models generated between 741 and 36,193 output tokens per verified proof, taking 14.9 to 178.0 seconds and consuming 0.0167 to 0.2000 aggregate GPU hours. The verified theorems covered 15 distinct statements, 11 of which were not solved by a baseline of standard Coq tactics. No statistical test was conducted to determine if one model systematically outperformed another; the results remain descriptive.  

## Significance  
This pilot study demonstrates that open‑weight LLMs can contribute to formal proof generation and verification, albeit at a low frequency. It provides empirical evidence on token cost and runtime for successful proofs, offering a baseline for future research into scaling verification with model size and training data. The findings also underscore the importance of short reference proofs in guiding LLM output, which may inform prompt engineering and benchmark design.  

## Related Concepts  
Open‑weight LLMs, Coq kernel, Calculus of Inductive Constructions, Kernel‑verified proofs, CoqStoq benchmark, temperature 0 sampling, token cost analysis, success rate, proof length bias, formal verification, baseline tactics.
