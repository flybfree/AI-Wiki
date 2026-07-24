# Summary: 2026-07-22_13-23-08Z_DirectionalKernelMeanDifference_AFastSignedStatist.md
Saved: 2026-07-24 01:51
Source: 2026-07-22_13-23-08Z_DirectionalKernelMeanDifference_AFastSignedStatist.md
Model: None

---

## Summary  
The paper introduces Directional Kernel Mean Difference (DKMD), a signed statistic for univariate distribution comparison that explicitly preserves the direction of distributional shifts, unlike the squared Maximum Mean Discrepancy (MMD) which discards directional information by squaring the kernel‑based distance. DKMD integrates the difference of kernel mean embeddings against a fixed odd weighting function, yielding a new testable measure with strong theoretical properties.

## Key Contributions  
- Finding 1: DKMD is antisymmetric, immune to symmetric distributional differences, and monotonic under stochastic dominance, providing a signed metric that respects order.  
- Finding 2: The authors derive a data‑driven Riemann estimator that ensures asymptotic consistency with the continuous formulation of RKHS distance, thereby preserving theoretical guarantees on empirical evaluations.  
- Finding 3: They propose an O(N log N) prefix‑suffix scanning algorithm that computes DKMD efficiently by leveraging sorting and two‑pointer traversal, requiring only linear memory.

## Methodology  
The construction begins by forming kernel mean embeddings for each sample using a chosen bandwidth, then computing their difference weighted by an odd function to maintain sign. To approximate the theoretical signed distance on finite data, they employ a Riemannian estimator that maps empirical moments to the continuous space while preserving consistency. The computational scheme first sorts the data and computes prefix sums of the kernel contributions; a second pass scans suffixes, combining them in O(N log N) time. This approach eliminates the quadratic cost of pairwise kernel evaluation.

## Results  
Empirical experiments on synthetic benchmarks demonstrate that DKMD correctly isolates directional shifts from symmetric perturbations, remains robust to heavy‑tailed outliers that could otherwise flip the sign of the mean difference, and scales to millions of samples within seconds. Theoretical analysis confirms asymptotic consistency with the continuous RKHS formulation, confirming that the data‑driven estimator retains the signed nature of the statistic.

## Significance  
DKMD offers a fast, theoretically sound alternative to MMD for tasks where preserving shift direction is essential, such as anomaly detection, A/B testing, and causal inference. By maintaining antisymmetry and monotonicity under stochastic dominance, it provides interpretable results that are not compromised by symmetric noise, enabling reliable decision making in high‑dimensional pipelines.

## Related Concepts  
- Signed statistics (e.g., signed MMD)  
- Riemannian geometry  
- Kernel mean embedding  
- Stochastic dominance  
- Prefix‑suffix scanning algorithm
