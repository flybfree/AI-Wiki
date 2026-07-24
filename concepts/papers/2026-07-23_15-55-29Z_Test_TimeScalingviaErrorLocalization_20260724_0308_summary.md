# Summary: 2026-07-23_15-55-29Z_Test_TimeScalingviaErrorLocalization.md
Saved: 2026-07-24 03:08
Source: 2026-07-23_15-55-29Z_Test_TimeScalingviaErrorLocalization.md
Model: None

---

## Summary  
The paper proposes Test‑Time Scaling via Error Localization (TTEL), an inference‑time algorithm that improves the efficiency of large language model reasoning by assigning credit to each token and discarding only the portion after a detected error. By comparing conditional probabilities under informed feedback with a null‑context baseline, TTEL isolates the exact step where reasoning breaks down. The method then truncates the trajectory at that point and generates a fresh continuation, thereby reusing the valid prefix. This approach yields higher pass rates while generating far fewer tokens than standard test‑time baselines such as independent sampling.

## Key Contributions  
- [Finding 1] TTEL isolates the error step by comparing conditional probabilities under informed feedback against a null‑context baseline, enabling precise token‑level localization.  
- [Finding 2] The algorithm truncates the trajectory at the identified error and branches a new generation that maximally reuses the valid prefix.  
- [Finding 3] TTEL establishes strictly dominating Pareto frontiers across sequential reasoning domains when measured by pass@k versus generated‑token cost.

## Methodology  
The authors employ fixed or environment feedback to generate conditional probability distributions for each token in the model’s output. These distributions are compared with a null‑context baseline that assumes no prior knowledge of correctness, allowing the system to detect deviations indicative of errors. The location where the conditional probability deviates most from the baseline is treated as the error token; the generation is then cut at this point and restarted with a fresh prompt, preserving all preceding tokens.

## Results  
On Qwen3‑8B evaluated on LiveCodeBench, TTEL achieves a pass@64 of 71.0 % while generating approximately 360.4 k tokens, compared to 735.0 k tokens for independent sampling. The same improvement is observed on math benchmarks AIME‑2025 and HMMT‑2025, where TTEL outperforms all competing test‑time baselines across both Qwen3‑8B and Qwen3‑4B‑Thinking‑2507 models.

## Significance  
TTEL demonstrates that inference‑time scaling can be made far more effective by eliminating the waste of invalid reasoning prefixes, thereby improving both pass rates and token efficiency. This work provides a scalable framework for large language models, especially in domains where reasoning is required but token generation is costly.

## Related Concepts  
- Test‑time scaling  
- Error localization  
- Conditional probability comparison  
- Pareto frontiers (pass@k vs. token cost)  
- Token‑level credit assignment
