# Summary: 2026-06-24_14-25-39Z_AnAnalysisofPosteriorCollapse_ParameterizationandI.md
Saved: 2026-06-24 21:01
Source: 2026-06-24_14-25-39Z_AnAnalysisofPosteriorCollapse_ParameterizationandI.md
Model: None

---


## Summary  
This paper investigates why variational deep Gaussian processes (DGPs) often suffer from posterior collapse—a phenomenon in which the variational posterior collapses to the prior and explains all data as noise—by linking it to the DSVI algorithm and the linear prior mean function used across most layers. The authors show that the observed benefits of a linear prior mean stem not from eliminating non‑injective pathology but from better conditioning at initialization, which enables successful training without imposing optimization‑driven constraints on the prior. They introduce an alternative zero‑prior‑mean DGP initialization that mimics a linear prior mean at the start, allowing priors to be chosen based on modeling assumptions rather than algorithmic convenience. Experiments across three common DGPs demonstrate that this approach prevents collapse, improves stability, and can yield performance comparable to or better than standard DGPs with linear priors.

## Key Contributions  
- [Finding 1] Posterior collapse in variational DGPs is tied to the DSVI algorithm and the use of a linear prior mean function across all but the final layer.  
- [Finding 2] The advantage of the linear prior mean derives from improved conditioning at initialization rather than from avoiding non‑injective issues in very deep networks.  
- [Finding 3] A zero‑prior‑mean DGP initialized to mimic a linear prior mean enables training without optimization‑driven constraints, permitting flexible priors.

## Methodology  
The authors systematically analyze three widely used DGPs parameterizations: (i) the standard concatenated GP with a linear prior mean, (ii) a whitened version of the same model, and (iii) an alternative zero‑prior‑mean formulation. They compare these setups under the DSVI algorithm, which is known to be sensitive to initialization. By varying initializations—including the proposed “mimic” initialization—they assess how conditioning affects convergence and posterior collapse. Experiments include training on synthetic and real datasets, measuring both loss reduction and predictive performance.

## Results  
The results confirm that the mimic initialization prevents posterior collapse entirely, while standard linear‑prior‑mean DGPs still experience collapse under poor initializations. The whitened parameterization shows marginally better stability but does not eliminate collapse. Performance metrics (e.g., mean squared error) are on par with or exceed those of conventional DGPs using linear priors, especially when the mimic initialization is employed.

## Significance  
This work matters because it decouples prior choice from algorithmic constraints, allowing researchers to select priors that reflect domain knowledge rather than being forced by optimization heuristics. By providing a principled initialization strategy, the paper addresses a longstanding practical problem in variational DGPs and opens avenues for more flexible Bayesian deep learning models.

## Related Concepts  
Posterior collapse, variational inference, deep Gaussian processes (DGPs), linear prior mean function, DSVI algorithm, non‑injective pathology, whitened parameterization, zero‑prior‑mean initialization.
