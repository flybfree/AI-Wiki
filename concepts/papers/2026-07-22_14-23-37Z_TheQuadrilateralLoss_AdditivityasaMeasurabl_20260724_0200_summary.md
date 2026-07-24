# Summary: 2026-07-22_14-23-37Z_TheQuadrilateralLoss_AdditivityasaMeasurableBehavi.md
Saved: 2026-07-24 02:00
Source: 2026-07-22_14-23-37Z_TheQuadrilateralLoss_AdditivityasaMeasurableBehavi.md
Model: None

---

## Summary  
The paper proposes the quadrilateral loss, a differentiable penalty that quantifies additivity in dense neural networks by measuring how swapping one coordinate of two training points changes predictions. This mixed‑difference term vanishes exactly when the swapped coordinate is uncorrelated with the others and equals the expected per‑coordinate interaction mass from an interventional Shapley‑GAM model. By treating additivity as a measurable dial, the authors show that moderate regularization can improve both accuracy and additivity on small datasets without imposing structural masks or weight constraints. The loss also reveals that pre‑regularization interaction magnitudes do not reliably predict which interactions survive after penalisation.

## Key Contributions  
- [Finding 1] The quadrilateral loss is a second‑order mixed difference that vanishes iff the coordinate carries no interaction, providing a mathematically precise measure of additivity.  
- [Finding 2] This loss equals in expectation the per‑coordinate interaction mass of the Shapley‑GAM model, linking it to causal interpretability.  
- [Finding 3] A moderate penalty improves accuracy and additivity simultaneously; pre‑regularization interaction magnitudes barely predict what a regularized model retains.

## Methodology  
The authors define the quadrilateral loss as a differentiable gradient of the mixed difference between predictions after swapping one coordinate across training pairs. They evaluate this loss on small datasets, comparing it to alternative exact‑additivity routes such as structural masks, weight decay, backfitting, shared‑section models, and bagged boosted stumps. The experiments are seeded repeatedly to assess stability across data regimes.

## Results  
Moderate application of the quadrilateral penalty yields higher test accuracy while preserving additivity, and per‑feature surrender curves show that interaction magnitude before regularisation does not strongly correlate with retained interactions after penalisation. Across seeds and datasets, pre‑regularization interaction rankings reverse between unpenalised and penalised models. Converging routes to exact additivity—structural masks, behavioural penalties, weight decay, backfitting, shared‑section models, bagged boosted stumps—agree on the underlying shape functions despite differing ranking orders.

## Significance  
The quadrilateral loss offers a practical, differentiable way to enforce additivity without altering network architecture or imposing heavy structural constraints. It provides empirical insight into how dense networks naturally suppress interactions and how regularisation can be tuned to balance accuracy and interpretability, especially on limited data.

## Related Concepts  
Additive models, Shapley‑GAM, quadratic loss, mixed differences, piecewise‑linear networks, weight decay, backfitting, shared‑section model, bagged boosted stumps, structural masks.
