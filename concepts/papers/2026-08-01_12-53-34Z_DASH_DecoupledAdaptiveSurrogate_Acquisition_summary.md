# Summary: 2026-08-01_12-53-34Z_DASH_DecoupledAdaptiveSurrogate_AcquisitionHarness.md
Saved: 2026-08-03 20:29
Source: 2026-08-01_12-53-34Z_DASH_DecoupledAdaptiveSurrogate_AcquisitionHarness.md
Model: None

---

## Summary  
The paper introduces DASH (Decoupled Adaptive Surrogate‑Acquisition Harness) to improve automated Bayesian optimization by treating the surrogate model and acquisition function as independent, adaptively tuned components. Instead of jointly optimizing a single combined criterion, DASH selects surrogates based on predictive reliability, uncertainty calibration, and ranking consistency while letting an acquisition controller reallocate quotas across different acquisition functions. A two‑stage pipeline builds a BO shortlist that is then handed off to a large‑language model for final decision making. The integrated harness supplies domain knowledge through a knowledge‑guided warm start and structured memory, grounding the optimization in external expertise.

## Key Contributions  
- [Finding 1] DASH decouples surrogate selection from acquisition adaptation, allowing each component to be tuned according to its intrinsic role—surrogate reliability versus campaign context.  
- [Finding 2] The two‑stage acquisition controller periodically reallocates acquisition function quotas and constructs a shortlist that is subsequently evaluated by an LLM for the optimal final choice.  
- [Finding 3] An integrated harness combines knowledge‑guided warm starts with structured memory, providing domain expertise and accumulated feedback to guide both surrogate construction and acquisition decisions.

## Methodology  
The authors address the mismatch between surrogate selection (which depends on model reliability) and acquisition adaptation (which reacts to task dynamics). DASH implements a two‑stage acquisition controller that allocates a fixed quota of evaluations among several acquisition functions, builds a candidate set, and then delegates the final selection to an LLM. Surrogate models are chosen using predictive reliability scores, calibrated uncertainty estimates, and consistency checks across rankings. The knowledge harness supplies initial data points (warm start) and stores structured observations, enabling the system to leverage external domain knowledge throughout optimization.

## Results  
Across four chemical‑optimization tasks, DASH improves trajectory‑level Acceleration Factor by 12.51 % and endpoint Enhancement Factor by 5.00 % relative to the best AutoBO baseline. Performance remains robust across different LLM backbones, as confirmed by ablation studies that isolate each component’s contribution. Full‑table analysis and behavioral contamination checks reveal no evidence of benchmark memorization or source‑cell leakage, indicating genuine gains.

## Significance  
DASH demonstrates that separating surrogate and acquisition adaptation can yield substantial efficiency gains in large‑scale optimization problems, especially when augmented with language models. By respecting the distinct roles of each component and grounding decisions in domain knowledge, DASH reduces wasted evaluations and accelerates convergence without sacrificing solution quality.

## Related Concepts  
Bayesian Optimization, surrogate model, acquisition function, AutoBO, predictive reliability, uncertainty calibration, ranking consistency, two‑stage acquisition controller, knowledge‑guided warm start, structured memory, LLM, Acceleration Factor, Enhancement Factor.
