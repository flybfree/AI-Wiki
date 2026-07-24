# Summary: 2026-07-23_15-55-29Z_Test_TimeScalingviaErrorLocalization.md
Saved: 2026-07-24 02:54
Source: 2026-07-23_15-55-29Z_Test_TimeScalingviaErrorLocalization.md
Model: None

---

## Summary  
The paper proposes Test‑Time Scaling via Error Localization (TTEL), an inference‑time algorithm that improves the efficiency of large language model reasoning by assigning credit to each token and discarding only the portion after a detected error. By leveraging feedback from the test environment, TTEL isolates the exact step where a mistake occurred, truncates the trajectory, and restarts generation with the maximal valid prefix. This approach eliminates wasted computation caused by independent sampling or multi‑turn refinement, which discard entire reasoning prefixes. The contribution is both methodological (a principled token‑level error‑localization scheme) and empirical (dominant performance gains across sequential tasks).

## Key Contributions  
- [Finding 1] TTEL achieves strictly dominating Pareto frontiers by reducing generated‑token cost while maintaining or improving pass@k rates.  
- [Finding 2] The algorithm can be implemented with either fixed feedback signals or environment‑provided error cues, making it adaptable to various test setups.  
- [Finding 3] TTEL consistently outperforms independent sampling and multi‑turn refinement baselines on both Qwen3‑8B and smaller variants across LiveCodeBench, AIME‑2025, and HMMT‑2025.

## Methodology  
The authors treat the inference process as a sequence of conditional probability steps. After each token generation they compare the observed probability to a null‑context baseline; if the difference exceeds a threshold, the token is flagged as erroneous. The trace is then cut at the first error, and a fresh generation begins from the last valid token using the same model checkpoint. This token‑level credit assignment replaces coarse‑grained multi‑turn refinement with a single pass that maximally reuses correct reasoning.

## Results  
On LiveCodeBench with Qwen3‑8B, TTEL reaches 71.0 % pass@64 while generating only 360.4 k tokens—about half the 735.0 k produced by independent sampling. On AIME‑2025 and HMMT‑2025, TTEL improves pass rates relative to all competing test‑time baselines for both Qwen3‑8B (≈14 % absolute gain) and Qwen3‑4B‑Thinking‑2507 (≈9 % absolute gain). The Pareto analysis shows that no other method simultaneously reduces token count and increases pass@k.

## Significance  
TTEL demonstrates that inference‑time scaling can be achieved without sacrificing reasoning quality, offering a scalable path to deploying larger models in resource‑constrained settings. By assigning precise error credit, the approach mitigates the waste inherent in current test‑time strategies, paving the way for more efficient AI assistants and code generators.

## Related Concepts  
- Test‑time scaling  
- Error localization / token‑level credit assignment  
- Pareto frontiers (efficiency vs. performance trade‑offs)  
- Independent sampling  
- Multi‑turn refinement
