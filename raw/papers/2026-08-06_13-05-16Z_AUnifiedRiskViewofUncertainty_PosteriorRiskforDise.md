---
title: A Unified Risk View of Uncertainty: Posterior Risk for Disentanglement and Evaluation Beyond Proxies
published: 2026-08-06T13:05:16Z
authors: Frieder Wizgall, Georg Tirpitz, Moritz Seiler, Kerstin Ritter, Bálint Mucsányi
url: http://arxiv.org/abs/2608.05995v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Unified Risk View of Uncertainty: Posterior Risk for Disentanglement and Evaluation Beyond Proxies

## Abstract
Reliable uncertainty estimates are critical in safety-sensitive applications, where understanding the sources of predictive uncertainty is essential. This often requires disentangling epistemic uncertainty from aleatoric uncertainty, yet these uncertainty types are not defined consistently across the literature, making it difficult to assess whether a method produces accurate uncertainty estimates. Evaluation is further complicated by the fact that ground-truth epistemic uncertainty is typically unavailable. Existing benchmarks therefore mostly rely on proxy tasks such as out-of-distribution detection, which do not provide complete ground-truth uncertainty targets and offer limited insight into the structure and quality of uncertainty estimates. We propose a unified definition of uncertainty as pointwise posterior risk, the expected loss of a predictor under the distribution of plausible ground-truth functions given the data. This view combines Bayesian uncertainty over functions with estimator-dependent deviations from the posterior mean, capturing effects such as misspecification and optimization error. This formulation constitutes the foundation of a theory-backed benchmark that enables direct computation of oracle epistemic and aleatoric uncertainty using semi-synthetic datasets with real covariates and known generative processes. By avoiding proxy evaluations, the benchmark enables fine-grained analysis of uncertainty estimates. Empirically, we find that accurate prediction does not guarantee reliable uncertainty disentanglement. The benchmark reveals practically useful differences between methods, identifying approaches with meaningful alignment to oracle uncertainty targets while exposing sensitivity to datasets and modeling choices.

## Metadata
- **Published**: 2026-08-06T13:05:16Z
- **Authors**: Frieder Wizgall, Georg Tirpitz, Moritz Seiler, Kerstin Ritter, Bálint Mucsányi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05995v1)