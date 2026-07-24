# Summary: 2026-07-21_18-57-22Z_DoSheafNeuralNetworksUseHolonomy_AMeasure__Interve.md
Saved: 2026-07-24 01:10
Source: 2026-07-21_18-57-22Z_DoSheafNeuralNetworksUseHolonomy_AMeasure__Interve.md
Model: None

---

## Summary  
The paper investigates whether the geometric mechanisms—rotations, area changes, or orientation shifts—that underlie sheaf neural networks (SNNs) actually drive their predictions, rather than merely serving as a by‑product of task learning. By training SNNs on a high‑homophily GraphUniverse dataset and measuring triangle‑loop products, the authors obtain a basis‑independent metric that separates rotation from stalk‑space area and orientation. Their measure‑intervene‑control study shows that interventions such as replacing learned SO(2) transports with identities dramatically affect performance, revealing post‑training sensitivity to the full connection structure. The work therefore provides a principled way to evaluate geometric contributions in neural architectures.

## Key Contributions  
- [Finding 1] Neural Sheaf Propagation (NSP) raises the triangle‑weighted mean two‑dimensional SO(2) loop rotation from 0.010 to 0.388 radians for triangle counting, indicating a strong geometric effect.  
- [Finding 2] Replacing all learned SO(2) transports with identities sharply increases test error, establishing that the network is post‑training sensitive to its complete connection structure.  
- [Finding 3] A graph‑summary ridge predictor outperforms NSP; diagonal maps improve accuracy, and fixed‑degree graphs develop increasing rotation but do not surpass the training‑mean predictor.

## Methodology  
The authors construct a custom high‑homophily GraphUniverse regime where SNNs propagate information through triangle loops. They compute trained triangle‑loop products and extract three basis‑independent quantities: the average SO(2) rotation, the area of stalk‑space, and the orientation of each loop. By varying the training set size and performing controlled interventions—such as swapping learned rotations with identity maps—they isolate whether geometric changes or connection sensitivity drive performance differences.

## Results  
The primary experimental results are: (1) NSP’s triangle‑counting rotation jumps from 0.010 to 0.388 rad, a tenfold increase; (2) after the intervention, test error rises sharply, confirming that the network relies on its learned SO(2) transports; (3) a ridge predictor based on graph summaries achieves higher accuracy than NSP, while diagonal maps further improve performance; (4) fixed‑degree graphs exhibit growing rotation but do not outperform the training‑mean predictor.

## Significance  
This study separates geometric change from connection sensitivity in sheaf neural networks, offering a basis‑independent measure that can be applied to any graph‑based architecture. By demonstrating post‑training sensitivity through interventions, it clarifies whether learned rotations are essential for task success or merely artifacts of the training process.

## Related Concepts  
Sheaf Neural Networks (SNN), holonomy, SO(2) loop rotation, triangle‑loop products, high‑homophily GraphUniverse regime, measurement‑intervene‑control study, graph‑summary ridge predictor, diagonal maps, fixed‑degree graphs.
