# Summary: 2026-07-23_22-38-04Z_SCALE_Self_SupervisedConstraint_AwareLayoutGEnerat.md
Saved: 2026-07-26 21:31
Source: 2026-07-23_22-38-04Z_SCALE_Self_SupervisedConstraint_AwareLayoutGEnerat.md
Model: None

---

## Summary  
The paper introduces **SCALE**, a framework that tackles the challenge of local place‑and‑route design‑rule violation (DRV) fixing at sub‑2 nm nodes, where complex rule interactions and dense routing geometries limit traditional approaches. By converting multi‑layer layout geometry into structured text and using a self‑supervised language model to reconstruct masked polygons from BEOL context alone, SCALE generates diverse, DRC‑violating layouts without any labeled data. The generated violation pairs are then used to fine‑tune a domain‑adapted deep visual rule classifier (DRC‑VLM), which provides rule‑aware geometric guidance for local repair. This pipeline boosts the solve rates of existing agents by 12–25 % and can reach near‑perfect performance on real sub‑2 nm cases.

## Key Contributions  
- **Self‑supervised layout generation**: A language model reconstructs randomly masked polygons from surrounding BEOL context, eliminating the need for DRC labels.  
- **DRC‑VLM fine‑tuning with generated pairs**: The framework creates synthetic violation‑annotated layouts that train a visual rule classifier to understand advanced node constraints.  
- **Performance boost on real cases**: The method improves solve rates by 12–25 % and achieves up to 97 % accuracy across 100 real sub‑2 nm enclosure, spacing, width, and color‑spacing violations.

## Methodology  
SCALE first serializes the multi‑layer layout into a natural‑language description of polygons, then randomly masks portions of that text. A fine‑tuned language model reconstructs the masked region using only the surrounding BEOL context, producing a new polygon set that is guaranteed to violate DRC rules. The resulting violation pairs are fed back into a convolutional vision transformer (DRC‑VLM) that has been domain‑adapted to the foundry’s specific rule set. During inference, natural‑language rule constraints and high‑temperature sampling guide generation toward diverse, violation‑prone layouts, enabling systematic exploration of repair strategies.

## Results  
Experimental evaluation on 100 real sub‑2 nm test cases shows that SCALE‑augmented agents solve DRC violations at a rate increased by 12–25 % compared to baseline methods, reaching up to 97 % accuracy. The generated violation pairs are consistent with industrial signoff DRC checkers, and the fine‑tuned DRC‑VLM provides rule‑aware guidance that reduces repair effort without sacrificing layout quality.

## Significance  
As semiconductor nodes approach sub‑2 nm, the combinatorial explosion of rule interactions makes manual or heuristic fixing impractical. SCALE’s self‑supervised generation and visual rule learning provide a scalable, data‑efficient solution that integrates directly into existing EDA toolchains, enabling rapid, high‑quality local DRV repair at advanced nodes.

## Related Concepts  
- **Self‑supervised learning** for layout reconstruction  
- **Design‑rule violation (DRV)** fixing in place‑and‑route  
- **Large language model (LLM) guided generation** of geometric structures  
- **Deep visual rule classifier (DRC‑VLM)** for DRC detection and guidance  
- **High‑temperature sampling** to explore diverse layout variants
