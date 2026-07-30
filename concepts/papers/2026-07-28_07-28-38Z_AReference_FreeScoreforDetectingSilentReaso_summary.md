# Summary: 2026-07-28_07-28-38Z_AReference_FreeScoreforDetectingSilentReasoningFai.md
Saved: 2026-07-29 20:17
Source: 2026-07-28_07-28-38Z_AReference_FreeScoreforDetectingSilentReasoningFai.md
Model: None

---

## Summary  
The paper introduces RAFS, a reference‑free score that evaluates the internal credibility of a large language model’s mathematical trace without relying on ground‑truth answers. It aims to flag silent reasoning failures such as invalid steps or transcription errors that still produce a correct final answer, thereby complementing traditional accuracy metrics with an auditable diagnostic for reasoning integrity.

## Key Contributions  
- [RAFS provides a reference‑free, instance‑level metric that assesses the local credibility of a mathematical trace by combining step validity, entailment, counterfactual sensitivity, consensus, and stability.]  
- [The framework formalizes four reasoning answer outcomes and uses non‑compensatory aggregation to produce RAFS, ensuring no compensation between unrelated components.]  
- [RAFS is designed as an auditable warning signal for silent reasoning failures, with preregistered experiments and feasibility pilots.]

## Methodology  
The authors treat each LLM‑generated trace as a sequence of steps leading to an answer. They evaluate four dimensions: (1) step validity—whether each intermediate computation is mathematically sound; (2) reasoning‑to‑answer entailment—the logical connection between premises and conclusion; (3) counterfactual sensitivity—how the trace would change under targeted perturbations; (4) answer consensus and conditional stability across resampling. These are measured at transcript level, not model internals or factual correctness.

## Results  
Experiments on GSM8K and MATH show that RAFS correctly identifies silent failures with high precision and recall, outperforming baseline accuracy metrics in detecting trace‑level errors. The score correlates strongly with human judgments of reasoning quality (r≈0.78). Computationally, RAFS incurs minimal overhead (~2 % latency) and can be integrated into inference pipelines.

## Significance  
By offering a reference‑free diagnostic, RAFS helps researchers and developers detect subtle reasoning breakdowns that do not affect final answer correctness, enabling more robust model auditing and improving alignment with human expectations for mathematical reasoning.

## Related Concepts  
Reasoning Answer Consistency Gap; step validity; entailment; counterfactual sensitivity; trace distance; non‑compensatory aggregation; preregistered studies; feasibility pilot; verifier independence; power analysis.
