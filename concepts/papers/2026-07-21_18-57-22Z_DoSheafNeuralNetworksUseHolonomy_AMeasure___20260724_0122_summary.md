# Summary: 2026-07-21_18-57-22Z_DoSheafNeuralNetworksUseHolonomy_AMeasure__Interve.md
Saved: 2026-07-24 01:22
Source: 2026-07-21_18-57-22Z_DoSheafNeuralNetworksUseHolonomy_AMeasure__Interve.md
Model: None

---

## Summary  
The paper investigates whether the geometric intuition behind sheaf neural networks (SNNs) is reflected in their learned behavior by performing a measure‑intervene‑control study on triangle‑loop products. By measuring the rotation of two‑dimensional SO(2) loops, separating it from other geometric components such as area and orientation, the authors isolate the effect of holonomy while controlling for alternative explanations. Their experiments show that trained SNNs exhibit measurable rotations that are sensitive to graph structure, yet these changes do not always translate into improved task performance. The study thus provides a basis‑independent metric for evaluating whether geometric mechanisms drive neural computation.

## Key Contributions  
- [Finding 1] Trained sheaf networks produce a triangle‑weighted mean two‑dimensional SO(2) loop rotation that rises from 0.010 to 0.388 rad in the GraphUniverse regime, indicating a genuine learned holonomy effect.  
- [Finding 2] Replacing all learned SO(2) transports with identity matrices sharply increases test error, demonstrating post‑training sensitivity of predictions to the complete connection structure.  
- [Finding 3] A graph‑summary ridge predictor and diagonal maps improve accuracy over the triangle‑counting baseline, suggesting that global geometric summaries can be more effective than local holonomy alone.

## Methodology  
The authors construct synthetic high‑homophily GraphUniverse graphs where each node is a point in ℝ². They train Neural Sheaf Propagation (NSP) to compute triangle‑loop products and extract the SO(2) component of the resulting rotation matrix. Using a measure‑intervene‑control framework, they compare the learned rotation against alternative geometric quantities (area, orientation), replace the learned transport with identity to intervene, and evaluate whether the intervention degrades performance. The control experiment replaces all rotations with fixed values to isolate sensitivity to the full connection.

## Results  
Across varying training set sizes, the measured rotation increases monotonically with graph size, reaching 0.388 rad for the largest dataset. Intervening by forcing identity transports reduces accuracy dramatically, confirming that predictions rely on learned holonomy. However, a ridge predictor based on global graph statistics outperforms the triangle‑counting model, and diagonal maps (projecting rotations onto a single axis) also improve performance while remaining below the training‑mean bound.

## Significance  
This work establishes a rigorous, basis‑independent way to quantify whether geometric mechanisms such as holonomy are actually employed by neural architectures. By separating rotation from other geometric attributes and controlling for interventions, it clarifies the causal role of geometry in SNN behavior, informing future research on interpretable deep learning models.

## Related Concepts  
- Sheaf Neural Networks (SNN)  
- Holonomy / SO(2) rotations  
- Triangle‑loop products  
- GraphUniverse regime  
- Measure‑intervene‑control methodology  
- Ridge regression and diagonal maps
