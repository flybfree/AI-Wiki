# Summary: 2026-08-03_15-04-26Z_GlobalOptimizationandInference_TimeRegionGraftingf.md
Saved: 2026-08-04 00:57
Source: 2026-08-03_15-04-26Z_GlobalOptimizationandInference_TimeRegionGraftingf.md
Model: None

---

## Summary  
The paper tackles the limitation of current agentic workflow optimization, which fixes a complete workflow before execution and cannot adapt to local quality signals observed at runtime. To overcome this, GRAFT (Global Optimization and Inference‑Time Region Grafting) introduces a mechanism that preserves a globally optimized workflow while locally swapping only selected regions based on label‑free execution‑quality feedback. This allows instance‑wise adaptation without costly whole‑workflow re‑optimization. The approach works across diverse tasks such as mathematical reasoning, code generation, and multi‑hop knowledge questions.

## Key Contributions  
- GRAFT enables inference‑time region adaptation by evaluating local alternatives using label‑free quality signals while preserving the overall workflow structure.  
- On average, GRAFT improves over the strongest prior method MaAS by 3.85 points across a range of tasks.  
- Replacing only the executor with a stronger model yields additional gains, demonstrating that an optimized workflow can evolve as a flexible execution policy.

## Methodology  
GRAFT retains a globally optimized workflow and then, at inference time, selects region‑level alternatives using label‑free quality metrics derived from execution results. The system evaluates each candidate replacement only if it improves local performance without breaking global consistency. No model training is required; the process is purely heuristic and works with any existing optimizer and executor configuration.

## Results  
Experimental evaluations across mathematical reasoning, code generation, and multi‑hop knowledge questions show that GRAFT consistently outperforms MaAS by 3.85 points on average. Moreover, swapping only the executor for a stronger model provides further improvements, confirming that the workflow can be refined incrementally. The method requires no modification to the underlying optimizer or executor.

## Significance  
GRAFT reveals that an optimized workflow is not merely a static artifact but an adaptable policy that can respond to real‑time feedback and leverage stronger executors. This reduces computational overhead compared with full re‑optimization, enabling more efficient agentic systems that can continuously improve without sacrificing global performance.

## Related Concepts  
global optimization, inference‑time region grafting, label‑free quality signals, task‑specific workflow search, MaAS (prior method), agentic workflows, execution policy adaptation.
