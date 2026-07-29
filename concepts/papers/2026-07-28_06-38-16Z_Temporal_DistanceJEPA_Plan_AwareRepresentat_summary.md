# Summary: 2026-07-28_06-38-16Z_Temporal_DistanceJEPA_Plan_AwareRepresentationLear.md
Saved: 2026-07-28 22:32
Source: 2026-07-28_06-38-16Z_Temporal_DistanceJEPA_Plan_AwareRepresentationLear.md
Model: None

---

## Summary  
Joint‑Embedding Predictive Architectures (JEPAs) enable latent world model predictive control by learning to predict in a compressed representation space rather than reconstructing raw pixels, thereby allowing planning from offline demonstration logs without explicit rewards. The paper’s core contribution is the introduction of Temporal‑Distance JEPA (TD‑JEPA), which extracts a directed temporal cost directly from reward‑free trajectories and uses it both as a planner cost and as a representation signal that improves Euclidean distance when contact geometry dominates. By mining same‑trajectory step order as positive targets, cross‑trajectory pairs as negative heuristics, and enforcing rollout consistency with the planning horizon, TD‑JEPA co‑designs a progress‑aware cost function that aligns with topological plan ordering while preserving the benefits of Euclidean embedding. Empirically, this approach lifts Two‑Room success to 100 % under locked evaluation, improves OGB‑Cube by 14.2 points over baseline LeWM planning, and matches or exceeds both LeWM and a concurrent RC‑aux baseline across all evaluated environments.

## Key Contributions  
- [Finding 1] A directed temporal cost function is derived from offline trajectories using same‑trajectory step order as positive targets, cross‑trajectory pairs as negative heuristics, and rollout consistency to match the planner horizon.  
- [Finding 2] The mined cost serves dual roles: it becomes the deployment cost for planning when progress is topological, and it improves Euclidean distance in representation space when contact geometry dominates.  
- [Finding 3] Ablations demonstrate that each component—directed head, cross‑trajectory negatives, and rollout consistency—significantly contributes to performance gains.

## Methodology  
TD‑JEPA retains the LeWM encoder–predictor backbone of standard JEPAs but augments it with a custom loss that incorporates the temporal cost. The encoder processes a trajectory to produce latent embeddings; the predictor learns short‑horizon predictions in this space. During training, the model is optimized to minimize prediction error while simultaneously encouraging alignment between successive steps (positive targets) and misalignment across trajectories (negative heuristics). A rollout consistency term ensures that the planner horizon matches the length of the rollout used for supervision. The resulting cost function is directly injected into the planning algorithm, allowing it to rank imagined futures by their temporal distance from the current state.

## Results  
Under locked evaluation—where the model and plan are trained on the same offline log—TD‑JEPA achieves 100 % success in Two‑Room, a 2.6‑point improvement over LeWM’s 97.4 %. On OGB‑Cube, TD‑JEPA raises performance by 14.2 points relative to LeWM planning and outperforms the concurrent RC‑aux baseline. Across all tested environments (Two‑Room, OGB‑Cube, Push‑T), TD‑JEPA matches or exceeds both LeWM and RC‑aux baselines, indicating that the temporal cost improves both representation learning and plan quality.

## Significance  
By mining a directed temporal structure from reward‑free logs, TD‑JEPA bridges the gap between representation learning and planning without requiring explicit rewards, enabling more robust offline‑learning pipelines. The dual role of the mined cost—both as a planner metric and as a representation signal—offers flexibility across environments where progress is topological versus geometric. This work demonstrates that co‑designing cost functions with plan time can significantly boost performance in latent world model predictive control.

## Related Concepts  
- Joint‑Embedding Predictive Architectures (JEPAs)  
- Latent World Model Predictive Control  
- Euclidean distance as a progress proxy  
- Temporal consistency term  
- Cross‑trajectory negative sampling  
- Rollout‑consistency alignment
