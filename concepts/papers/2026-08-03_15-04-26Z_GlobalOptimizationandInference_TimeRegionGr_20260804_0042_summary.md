# Summary: 2026-08-03_15-04-26Z_GlobalOptimizationandInference_TimeRegionGraftingf.md
Saved: 2026-08-04 00:42
Source: 2026-08-03_15-04-26Z_GlobalOptimizationandInference_TimeRegionGraftingf.md
Model: None

---

## Summary  
The paper introduces GRAFT, a method for agentic workflow optimization that allows inference‑time adaptation without re‑optimizing the entire workflow. It replaces only selected regions using label‑free execution‑quality signals while preserving the globally optimized structure of the workflow. This enables instance‑wise improvement across diverse tasks such as mathematical reasoning and code generation. By keeping the global optimizer intact, GRAFT avoids the computational cost of full re‑optimization.

## Key Contributions  
- [Finding 1] GRAFT enables inference‑time adaptation by locally replacing regions based on label‑free quality signals.  
- [Finding 2] It preserves a globally optimized workflow while only swapping subregions that improve local performance.  
- [Finding 3] The approach yields higher average scores than the prior MaAS method, with further gains from stronger executors.

## Methodology  
The authors model each agentic workflow as composed of a global optimizer and an executor. Offline generation creates alternative region candidates; at inference time they evaluate these alternatives using execution‑quality metrics without ground‑truth labels. Replacements are selected per instance to improve local quality while maintaining consistency, leaving the rest of the workflow unchanged.

## Results  
Experiments across mathematical reasoning, code generation, and multi‑hop knowledge questions show GRAFT improves average scores by 3.85 points over MaAS under matched optimizer and executor settings. Replacing only the executor with a stronger model yields additional gains without re‑optimizing the global workflow.

## Significance  
This work demonstrates that optimized workflows can be dynamic policies adaptable to feedback, reducing reliance on costly offline search and enabling real‑time personalization across diverse tasks.

## Related Concepts  
- Agentic workflow optimization  
- Region grafting  
- Label‑free evaluation  
- Inference‑time adaptation  
- Globally optimal policy  
- Local replacement  
- Execution‑quality signals
