---
title: From Training to Deployment: Post-Hoc Causal Feature Identification via Sensitivity Ratios
published: 2026-07-28T10:26:09Z
authors: Athanasios Vlontzos, Giorgos Papanastasiou, Bernhard Kainz, Sotirios Tsaftaris
url: http://arxiv.org/abs/2607.25546v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Training to Deployment: Post-Hoc Causal Feature Identification via Sensitivity Ratios

## Abstract
Given a model that is already trained, which features does it rely on causally versus spuriously? Existing methods require access to the training procedure and cannot answer this post-hoc. We introduce the \textbf{Normalised Sensitivity Ratio~(NSR)}, a post-hoc, model-agnostic diagnostic for this question under a structured-shift regime: environments differ primarily in the mean of spurious features while the causal mechanism and causal marginals remain stable, as in multi-site clinical data or multi-batch genomics. Within this regime, causal features induce constant model sensitivity across environments while spurious features track shift. NSR formalises this as the squared coefficient of variation of per-environment sensitivity. Under a linear structural causal model (SCM) with $K\ge3$ non-degenerate environments, NSR achieves exact identification (Theorem~1). We fully characterise failure: weak shifts ($O(\varepsilon^4)$ collapse), degenerate geometry, and proxy attenuation ($O((1-α)^4)$), giving practitioners quantitative criteria for assessing whether the regime holds. Finite-sample rates are $O_p(n^{-1})$ under the null and $O_p(n^{-1/2})$ under the alternative. Experiments confirm all theoretical predictions on synthetic data (area under the ROC curve [AUROC] $= 1.000$ under conditions satisfying the regime), show consistent rankings across five model families (Kendall $τ\ge0.529$), and recover six of eight causal features on bike-sharing data (Precision@7 $= 0.75$) without modifying any trained model.

## Metadata
- **Published**: 2026-07-28T10:26:09Z
- **Authors**: Athanasios Vlontzos, Giorgos Papanastasiou, Bernhard Kainz, Sotirios Tsaftaris
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25546v1)