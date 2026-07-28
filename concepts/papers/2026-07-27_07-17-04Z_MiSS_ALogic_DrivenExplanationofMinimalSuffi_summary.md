# Summary: 2026-07-27_07-17-04Z_MiSS_ALogic_DrivenExplanationofMinimalSufficientCo.md
Saved: 2026-07-28 00:09
Source: 2026-07-27_07-17-04Z_MiSS_ALogic_DrivenExplanationofMinimalSufficientCo.md
Model: None

---

## Summary  
MiSS (Minimal Sufficient Coalition) is a logic-driven, black-box framework designed to explain the predictions of 3D point cloud classifiers by identifying minimal sufficient coalitions of geometric regions that can certify the original output under perturbation-relative sufficiency reasoning. Unlike traditional explainers requiring white-box logical encodings or Boolean feature spaces, MiSS leverages a superpoint partition as an interpretable abstraction layer to generate candidate coalitions and verify their sufficiency through blackbox statistical queries. The system combines heuristic search with exact certification to produce statistically verified attributions with guaranteed minimum cardinality when successful.

## Key Contributions  
- [Finding 1] MiSS introduces a query-based, logic-driven approach that separates the proposal of candidate coalitions from their verification using a MaxSAT-based optimization framework, enabling scalable and interpretable explanations without requiring access to the classifier’s internal logic.  
- [Finding 2] The method guarantees minimum cardinality in certified sufficient coalitions through an adaptive heuristic floor and exact-size fallback, ensuring that explanations are both minimal and statistically valid under perturbation testing.  
- [Finding 3] MiSS achieves higher precision and coverage than rule-based baselines on benchmark datasets like ModelNet40 and ShapeNet with PointNet and PointMLP classifiers, while reducing explanation time compared to exhaustive search methods.

## Methodology  
MiSS operates by treating the input point cloud as a superpoint partition—an abstraction that groups points into geometric regions. The framework then formulates the problem of certification as a logical satisfiability question: can a subset (coalition) of these regions, when perturbed within a specified distribution, still produce the same classifier prediction? A MaxSAT procedure proposes coalitions using an adaptive cardinality floor to limit complexity, while blocking clauses and a surrogate acquisition heuristic prune suboptimal candidates. Exact-size fallback ensures that only feasible-sized coalitions are considered, and a safely tightened upper bound bounds the search space. The blackbox statistical oracle evaluates sufficiency by querying whether perturbations within each region preserve the original prediction, providing a binary attribution of validity.

## Results  
Experiments on ModelNet40 and ShapeNet with PointNet and PointMLP classifiers demonstrate that MiSS outperforms rule-based explainers in both precision (the proportion of correct attributions) and coverage (the fraction of predictions explained by sufficient coalitions). The system consistently achieves higher performance than baselines such as rule-based or exhaustive search methods, which often fail to produce minimal or statistically valid explanations. Notably, MiSS reduces explanation time significantly compared to exhaustive search approaches, making it computationally efficient while maintaining high accuracy.

## Significance  
MiSS advances the field of explainable AI for 3D point cloud classifiers by introducing a principled, logic-driven framework that balances interpretability, efficiency, and statistical rigor. By decoupling proposal from verification and guaranteeing minimum cardinality in certified explanations, MiSS addresses key limitations of existing methods that either require white-box access or produce non-minimal or unverifiable attributions. This work opens new possibilities for trustworthy AI systems where explanations must be both meaningful to humans and robust under real-world perturbations.

## Related Concepts  
- Superpoint partition: A geometric abstraction layer grouping points into regions for interpretability.  
- Perturbation-relative sufficiency reasoning: The idea that a prediction remains valid if small, localized perturbations do not change it.  
- MaxSAT procedure: A heuristic optimization method used to propose candidate coalitions.  
- Blackbox statistical oracle: A query-based system that evaluates sufficiency without access to model internals.  
- Minimal sufficient coalition: The smallest set of geometric regions whose sufficiency can certify the original prediction.
