# Summary: 2026-07-27_14-55-04Z_DecoupleMix_DecoupledRatioSearchandConvexAllocatio.md
Saved: 2026-07-27 23:01
Source: 2026-07-27_14-55-04Z_DecoupleMix_DecoupledRatioSearchandConvexAllocatio.md
Model: None

---

## Summary  
The paper proposes DecoupleMix, a systematic framework for constructing data recipes for Vision Language Models that separates ratio allocation across capabilities from intra‑class composition within categories. It decouples inter‑class ratios using single‑variable iterative search and intra‑class ratios via convex optimization with diversity scoring. This separation enables scalable, reproducible VLM pretraining without heuristic intuition. Experiments demonstrate superior performance over baseline heuristics and robust transfer of optimal ratios to larger datasets.

## Key Contributions  
- [Finding 1] The formulation of data construction as a mixture‑optimization problem that separates inter‑class and intra‑class ratio optimization.  
- [Finding 2] A single‑variable iterative search for inter‑class allocation across capabilities, and a multidimensional convex optimization with diversity objective for intra‑class composition.  
- [Finding 3] Empirical evidence that optimal ratios discovered on small proxies transfer seamlessly to larger multimodal budgets without retuning.

## Methodology  
The authors treat dataset selection as an optimization problem where the mixture is split into two orthogonal sub‑problems. For inter‑class allocation, they propose a simple iterative algorithm that adjusts ratios based on capability performance metrics. Intra‑class composition is evaluated using Quality and Difficulty scores per dataset, forming a vector that is optimized under convex constraints to maximize diversity while respecting quality thresholds.

## Results  
Experiments show DecoupleMix consistently outperforms heuristic baselines in VLM pretraining. Using 80B additional multimodal tokens, the model matches strong open‑source models trained with larger budgets. The framework also enables controlled validation of dataset contributions as an experiment.

## Significance  
This work transforms data curation from intuition to a reproducible engineering discipline, providing a principled basis for scalable VLM training and reducing wasteful data collection.

## Related Concepts  
- Data recipes  
- Mixture optimization  
- Convex allocation  
- Diversity objective  
- Inter‑class vs intra‑class ratios
