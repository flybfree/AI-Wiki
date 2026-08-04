# Summary: 2026-08-03_16-10-29Z_WassersteinmixingtimeoftheunadjustedLangevinalgori.md
Saved: 2026-08-04 00:44
Source: 2026-08-03_16-10-29Z_WassersteinmixingtimeoftheunadjustedLangevinalgori.md
Model: None

---

## Summary  
The paper investigates the asymptotic bias of the unadjusted Langevin algorithm (ULA) in a classical setting where the target distribution is log‑smooth and strongly log‑concave. By establishing new Wasserstein distance estimates for this bias, the authors derive a mixing time that scales as \(κ\sqrt{d}/\varepsilon\), where \(κ\) is the condition number of the underlying density, \(d\) its dimension, and \(\varepsilon\) the desired precision. This result improves upon the previous state‑of‑the‑art bound by a factor of \(\sqrt{d}/\varepsilon\). The contribution lies in providing a theoretically grounded, fast‑mixing guarantee for ULA that is directly applicable to many high‑dimensional optimization problems.

## Key Contributions  
- [Finding 1] A new Wasserstein mixing time estimate \(κ\sqrt{d}/\varepsilon\) for the asymptotic bias of ULA.  
- [Finding 2] An improvement over prior results by a factor \(\sqrt{d}/\varepsilon\), yielding faster convergence in high dimensions.  
- [Finding 3] The bound is valid specifically for log‑smooth strongly log‑concave measures, expanding its applicability.

## Methodology  
The authors employ a probabilistic coupling argument combined with moment‑based analysis to bound the Wasserstein distance between the empirical distribution of ULA samples and the target measure. They condition on the algorithm’s step size \(\varepsilon\) and use properties of the underlying density (log‑smoothness and strong log‑concavity) to control the bias term, ultimately translating this into a mixing time estimate.

## Results  
The main theoretical result is that the Wasserstein distance between ULA trajectories and the target distribution decays at a rate \(O(κ\sqrt{d}/\varepsilon)\), implying a mixing time of order \(κ\sqrt{d}/\varepsilon\). This bound is tighter than earlier works, which gave a mixing time proportional to \(d/\varepsilon\) or larger constants.

## Significance  
Faster mixing reduces computational cost and improves the reliability of ULA for large‑scale problems where exact sampling is infeasible. The improvement by \(\sqrt{d}\) is especially valuable in high‑dimensional machine learning and Bayesian inference, where dimension can be prohibitive.

## Related Concepts  
- Wasserstein distance  
- Mixing time  
- Langevin dynamics (unadjusted)  
- Log‑smooth measures  
- Strongly log‑concave distributions  
- Condition number \(κ\)  
- Dimension \(d\)  
- Target precision \(\varepsilon\)
