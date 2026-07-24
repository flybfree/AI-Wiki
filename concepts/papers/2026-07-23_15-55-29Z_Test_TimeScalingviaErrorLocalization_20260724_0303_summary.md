# Summary: 2026-07-23_15-55-29Z_Test_TimeScalingviaErrorLocalization.md
Saved: 2026-07-24 03:03
Source: 2026-07-23_15-55-29Z_Test_TimeScalingviaErrorLocalization.md
Model: None

---

## Summary  
The paper proposes Test‑Time Scaling via Error Localization (TTEL), an inference‑time algorithm that improves large language model performance by locally identifying where errors occur and reusing valid reasoning prefixes, thereby scaling efficiently without discarding correct tokens. It achieves this by comparing conditional probabilities under feedback to a null‑context baseline, isolating the step at which an error happened. This approach avoids the inefficiency of independent sampling and sequential multi‑turn refinement.

## Key Contributions  
- [Finding 1] TTEL establishes strictly dominating Pareto frontiers across sequential reasoning domains, measured by pass@k versus generated‑token cost.  
- [Finding 2] The algorithm achieves a pass@64 of 71.0 % on LiveCodeBench with Qwen3‑8B while generating roughly half the tokens compared to independent sampling (360.4 k vs. 735.0 k).  
- [Finding 3] TTEL cleanly outperforms competing test‑time baselines on both Qwen3‑8B and Qwen3‑4B‑Thinking‑2507 across math benchmarks AIME‑2025 and HMMT‑2025.  

## Methodology  
The authors introduced an inference‑time algorithm that uses fixed or environment feedback to perform token‑level error localization. By comparing conditional probabilities under informed feedback against a null‑context baseline, TTEL isolates the step where an error occurred. The trajectory is then truncated and a new generation is branched from the valid prefix, maximizing reuse of correct reasoning.

## Results  
Extensive evaluations demonstrate that TTEL establishes strictly dominating Pareto frontiers across sequential reasoning domains, measured by pass@k versus generated‑token cost. On LiveCodeBench with Qwen3‑8B, TTEL attains a pass@64 of 71.0 % while generating approximately half as many tokens (360.4 k) compared to independent sampling (735.0 k). The method also cleanly outperforms competing test‑time baselines on AIME‑2025 and HMMT‑2025 across both Qwen3‑8B and Qwen3‑4B‑Thinking‑2507.

## Significance  
This work matters because it provides a principled, scalable way to improve LLM performance on complex tasks without sacrificing token efficiency. By localizing errors and reusing valid prefixes, TTEL reduces computational waste, enabling higher pass rates with fewer tokens—a crucial advantage for resource‑constrained deployment.

## Related Concepts  
test‑time scaling, error localization, conditional probability comparison, Pareto frontiers, independent sampling, sequential multi‑turn refinement, token‑level credit assignment, inference‑time algorithms, large language model reasoning.
