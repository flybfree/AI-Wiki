# Summary: 2026-07-30_08-37-43Z_BacktoAll_EntityRanking_Sampler_DependentEvaluatio.md
Saved: 2026-07-30 21:42
Source: 2026-07-30_08-37-43Z_BacktoAll_EntityRanking_Sampler_DependentEvaluatio.md
Model: None

---

## Summary  
The paper investigates how the choice of negative destinations and candidate sets in continuous‑time dynamic graph (CTDG) ranking tasks biases model scores and module evaluations, thereby undermining claims about model superiority derived from sampled‑negative benchmarks. By demonstrating that both a non‑uniform negative distribution and even a uniformly drawn finite candidate set can alter Bayes‑optimal rankings and measured effects, the authors show that evaluation is not independent of the sampling procedure. Their core contribution is an “all‑entity ranking” framework that evaluates every destination in a fixed catalog, thereby removing sampler dependence while preserving the original CTDG scorer. This work provides a more reliable basis for comparing architectures on CTDG benchmarks with enumerable destinations.

## Key Contributions  
- [Finding 1] A non‑uniform negative distribution changes the Bayes‑optimal ranking of positive and negative entities in CTDGs, indicating that the optimal score depends on how negatives are sampled.  
- [Finding 2] Even a finite uniformly drawn candidate set can destabilize model rankings and cause module effects to shift in magnitude or direction, revealing sampling variation as a source of evaluation noise.  
- [Finding 3] Introducing all‑entity ranking eliminates sampler dependence by enumerating the entire destination catalog, offering a stable metric for architecture comparison.

## Methodology  
The authors conduct a factorial experiment across six models on four datasets (LastFM, MOOC, Reddit, Wikipedia). They evaluate repeated positives against both seen and unseen negatives, as well as new positives against seen and unseen negatives. A minimal scorer is built solely from pair‑history membership to isolate the influence of sampling. Additionally, they perform controlled representation interventions that directly manipulate how module effects are computed. This design isolates the impact of candidate set size and training objectives on ranking outcomes.

## Results  
Across the experiments, at least one model pair reverses its relative order when comparing the Uniform‑20 metric (a sampled‑negative benchmark) to the full catalog ranking. The magnitude and sign of module effects vary with both candidate‑set size and the training objective used. These findings confirm that sampler‑dependent evaluation can produce misleading conclusions about model superiority.

## Significance  
The results establish that conclusions drawn from sampled‑negative benchmarks are conditional on the stated candidate configuration, meaning that different sampling strategies can lead to opposite ranking orders. By providing an all‑entity ranking alternative, the paper recommends using a fixed, enumerable destination catalog as the primary evidence for architecture comparisons in CTDG settings.

## Related Concepts  
CTDG (continuous‑time dynamic graph), next‑destination prediction, negative sampling, Bayes‑optimal ranking, sampler influence on evaluation scores, module effects, enumeration of destination catalog, all‑entity ranking.
