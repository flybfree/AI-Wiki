# Summary: 2026-07-26_04-25-52Z_LocalRegularizationDoesNotCharacterizeMulticlassPA.md
Saved: 2026-07-27 23:52
Source: 2026-07-26_04-25-52Z_LocalRegularizationDoesNotCharacterizeMulticlassPA.md
Model: None

---

## Summary  
The paper investigates whether local regularization—a hypothesis scoring method that selects the minimum‑score test point consistent with the sample—can characterize multiclass PAC learnability. It argues that this principle does not hold for a specific countable class of realizable learning problems. The authors construct an instance family where cyclic triangles cause constant population error despite arbitrarily large training samples, showing that local regularizers fail to capture the true complexity. Their contribution is a negative answer to the characterization question and a new example of a class with low sample complexity but no local regularizer.  

## Semantic links
- [[concepts/papers/2026-08-03_12-10-52Z_MemArbiter_Decision_TimeMemoryArbitrationfo_summary.md|Summary: 2026-08-03_12-10-52Z_MemArbiter_Decision_TimeMemoryArbitrationforLong_H.md]] — 3 title terms overlap; 9 summary/topic terms overlap; semantic match 0.10
- [[concepts/papers/2026-07-25_05-27-52Z_TheEntropicBoundforTransformers_WhyStaticRa_summary.md|Summary: 2026-07-25_05-27-52Z_TheEntropicBoundforTransformers_WhyStaticRankFails.md]] — 3 title terms overlap; 9 summary/topic terms overlap; semantic match 0.08
- [[concepts/papers/2026-06-26_17-24-21Z_PAC_BayesianCertificatesforQuadraticClosed__summary.md|Summary: 2026-06-26_17-24-21Z_PAC_BayesianCertificatesforQuadraticClosed_LoopCon.md]] — 3 title terms overlap; 9 summary/topic terms overlap; semantic match 0.08

## Key Contributions  
- Finding 1: The paper demonstrates that there exists a realizable multiclass learning problem where the sample complexity is O(1/ε log 1/δ), matching typical bounds, yet no local regularizer can learn it.  
- Finding 2: The instance family consists of tournaments derived from complete graphs with cyclic triangles; training removes competitors while test scores rank edges, leading to constant error regardless of sample size.  
- Finding 3: This example shows that the absence of a local regularizer is not due to high intrinsic complexity but rather to the specific structure causing persistent inversions.  

## Methodology  
The authors approach the problem by constructing an explicit instance family and analyzing its PAC learnability. They define hypotheses as edges, instances as tournaments, and describe how training removes vertices while test scores depend on edge rankings. The analysis uses combinatorial reasoning about cyclic triangles to show that any hypothesis consistent with training must incur constant population error.  

## Results  
Theoretical results include: (i) a realizable class with O(1/ε log 1/δ) sample complexity, (ii) no local regularizer can achieve PAC convergence for this class, and (iii) the population error remains constant even as |S| → ∞. The authors also note that standard VC‑dimension arguments are insufficient because the class has dimension at most two.  

## Significance  
This work matters because it challenges a long‑held belief that local regularization is a universal indicator of learnability, especially in multiclass settings. It highlights that sample complexity alone does not guarantee the existence of a simple scoring mechanism, and it provides a concrete counterexample for theoretical studies of regularization methods.  

## Related Concepts  
- Local regularization  
- PAC learnability  
- Sample complexity O(1/ε log 1/δ)  
- VC dimension at most two  
- Tournaments derived from complete graphs  
- Cyclic triangles  
- Population error
