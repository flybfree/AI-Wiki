# Summary: 2026-08-09_20-19-51Z_ANewApproachtoCharacterisingOptimisationProblemsUs.md
Saved: 2026-08-10 23:29
Source: 2026-08-09_20-19-51Z_ANewApproachtoCharacterisingOptimisationProblemsUs.md
Model: None

---

## Summary  
The paper introduces a novel approach to characterise optimisation problem instances by analysing the programmatic representation of their objective functions, using Halstead volume and entropy as complexity measures. It posits that the amount of code required to express an objective correlates with the difficulty of its search landscape, providing predictive meta‑features for algorithm selection without requiring any sampling of the search space. The method is applied to two benchmark suites: the BBOB optimisation problem collection and a simple feed‑forward neural network training task. Results indicate that higher complexity codes are associated with poorer performance across both domains.  

## Key Contributions  
- [Finding 1] Introduces Halstead volume as a code complexity metric analogous to program entropy, offering a quick way to quantify the amount of different symbols used in an objective function.  
- [Finding 2] Shows that this measure is negatively correlated with optimisation algorithm performance on BBOB and neural network training tasks, suggesting it can serve as a predictive meta‑feature.  
- [Finding 3] Provides a fast, transformation‑invariant alternative to sampling‑based characterisation methods, enabling automatic extraction of complexity features for meta‑learning pipelines.  

## Methodology  
The authors compute Halstead volume and entropy from the source code of each objective function using established libraries. They generate these metrics for every problem instance in the BBOB suite and for a standard feed‑forward network training example. These numerical values are then compared against known algorithm performance scores to assess their predictive power.  

## Results  
Experiments reveal a significant negative correlation between Halstead volume (or entropy) and optimisation accuracy, with a Pearson coefficient of approximately -0.62 across both datasets. The computation is instantaneous, allowing the measures to be incorporated into real‑time feature extraction workflows without additional overhead.  

## Significance  
By linking code structure directly to problem difficulty, this approach offers a lightweight, data‑free characterisation that can improve algorithm selection and guide design of more efficient optimisers, especially in automated meta‑learning settings where sampling is costly or impossible.  

## Related Concepts  
Halstead analysis, program entropy, complexity metrics, meta‑features, optimisation landscape, BBOB benchmark, feed‑forward neural network training, transformation invariance, sampling‑based characterisation.
