# Summary: 2026-08-07_03-52-01Z_FasterQuery_KeyLearningSharpensAttentioninSelf_Att.md
Saved: 2026-08-09 22:40
Source: 2026-08-07_03-52-01Z_FasterQuery_KeyLearningSharpensAttentioninSelf_Att.md
Model: None

---

## Summary  
The paper investigates how different parameterizations of the self‑attention circuit affect both training dynamics and the resulting attention patterns in single‑layer models trained for next‑token prediction. By collapsing or factorizing the query‑key and output‑value circuits, the authors show that the two sub‑circuits can learn at distinct effective learning rates, which drives qualitatively different attention concentrations. Faster query‑key learning relative to slower output‑value learning leads to sharper attention on task‑relevant tokens while preserving comparable predictive performance.

## Key Contributions  
- [Finding 1] Factorized parameterizations induce an implicit rescaling of the two circuits’ learning rates, meaning that one circuit’s updates are proportionally larger than the other’s.  
- [Finding 2] Gradient‑flow analysis reveals that output‑value and query‑key parameters move along a single line in parameter space, with their relative speeds dictated by those effective learning rates.  
- [Finding 3] When query‑key learning is faster than output‑value learning, the model compensates by increasing attention mass on relevant tokens, producing sharper attention patterns that improve interpretability proxies.

## Methodology  
The authors perform a gradient‑flow analysis on single‑layer self‑attention models trained for next‑token prediction. They compare two parameterizations: (i) collapsed where query‑key and output‑value share a single weight matrix, and (ii) factorized where they are separate matrices with independent scaling factors. By computing the differential equations governing each circuit’s parameters from the loss gradient, they derive closed‑form dynamics that describe how the two sets of weights evolve over training.

## Results  
Theoretical analysis shows that if the effective learning rate for query‑key is larger than that for output‑value, the model compensates by allocating more attention mass to tokens whose representations are close to the current query. This yields sharper attention maps (larger gradient magnitudes) while keeping next‑token loss comparable across parameterizations. Experiments confirm that tuning the relative learning rates changes attention concentration without sacrificing predictive accuracy.

## Significance  
Understanding how circuit factorization influences training trajectories provides new interpretability tools for self‑attention models and may guide design choices such as weight sharing or scaling factors to achieve more focused attention.

## Related Concepts  
Self‑attention, query‑key output‑value circuits, gradient flow, collapsed vs. factorized parameterization, learning rate scaling, attention concentration, next‑token prediction.
