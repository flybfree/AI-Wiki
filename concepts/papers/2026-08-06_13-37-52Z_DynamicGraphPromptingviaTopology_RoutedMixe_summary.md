# Summary: 2026-08-06_13-37-52Z_DynamicGraphPromptingviaTopology_RoutedMixed_Curva.md
Saved: 2026-08-06 20:45
Source: 2026-08-06_13-37-52Z_DynamicGraphPromptingviaTopology_RoutedMixed_Curva.md
Model: None

---

## Summary  
Dynamic graph prompting typically freezes a pre‑trained temporal backbone and adds lightweight prompts for downstream tasks, but it assumes the underlying embedding space remains static while local topology can change over time. This work identifies that such changes cause a “geometry under‑adaptation” where the optimal representation geometry does not match the evolving edge curvature spectrum of the graph. To remedy this mismatch, the authors introduce CurvPrompt—a topology‑routed mixed‑curvature prompting framework that maintains a bank of curvature‑diverse Riemannian experts and routes each node‑time instance to a sparse subset of these experts. The approach enables dynamic adaptation without retraining the backbone.

## Key Contributions  
- [Finding 1] Temporal shifts in local clustering and degree heterogeneity actively reorganize the edge curvature spectrum, revealing geometry under‑adaptation as an unaddressed problem.  
- [Finding 2] A mixed‑curvature representation built from a bank of Riemannian experts can capture this evolving topology while preserving parameter efficiency.  
- [Finding 3] Soft routing during pre‑training builds a continuous topology–geometry mapping, which transitions to hard Top‑K uniform weighting for downstream adaptation.

## Methodology  
CurvPrompt retains multiple curvature‑diverse experts, each paired with a learnable prompt. A topology‑aware gate inspects the local clustering and degree heterogeneity of each node‑time instance and selects only a sparse subset of experts. During pre‑training, soft routing gradually aligns the graph’s curvature spectrum with the expert space, creating a smooth mapping. For downstream tasks, the system switches to hard Top‑K routing with uniform weights, ensuring that only the most relevant experts contribute while keeping the prompt lightweight.

## Results  
Experiments on four benchmark datasets demonstrate that CurvPrompt markedly improves few‑shot link prediction accuracy and maintains strong performance on node classification. Compared with state‑of‑the‑art dynamic graph prompting baselines, CurvPrompt achieves up to 12 % higher recall in low‑label regimes and consistently outperforms them in zero‑shot settings.

## Significance  
The study proves that geometry‑adaptive prompting is essential for handling the inherent dynamism of temporal graphs. By decoupling representation geometry from static embeddings, CurvPrompt offers a scalable solution to label‑scarce few‑shot tasks, reducing reliance on large labeled datasets and enabling continual adaptation as graph topology evolves.

## Related Concepts  
Dynamic graph prompting, Riemannian geometry, mixed‑curvature representation, topology routing, soft vs. hard routing, curvature spectrum, under‑adaptation, few‑shot learning, parameter‑efficient fine‑tuning.
