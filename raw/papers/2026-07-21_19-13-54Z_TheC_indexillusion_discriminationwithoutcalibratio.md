---
title: The C-index illusion: discrimination without calibration in published survival models
published: 2026-07-21T19:13:54Z
authors: Rafael da Silva, Danilo Alvares
url: http://arxiv.org/abs/2607.19526v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# The C-index illusion: discrimination without calibration in published survival models

## Abstract
Recent work has argued normatively, on synthetic data, that evaluating survival models by discrimination alone (concordance index) yields systematically misleading model comparisons, because the metric ignores calibration and time-dependent accuracy. Whether this matters for real, published, non-clinical models has not been tested. We reproduce three published survival-ML models across three structurally distinct domains -- hard-drive failure prediction, peer-to-peer credit default, and user disengagement on digital platforms -- validate our instrument against the anchor paper's own synthetic experiment, and test five pre-registered hypotheses under a Holm-corrected family-wise error rate. Three of five reject (though one pre-registered threshold clears by a narrow margin). A model reproducing the published literature's discrimination almost exactly (C = 0.9595 vs. 0.958 reported) fails a formal calibration test at p < 0.001; a broad feature-ablation search finds no single attribute responsible for its discrimination, so the calibration failure is not a trivial shortcut artifact. A lender's estimated default risk is biased upward by roughly two percentage points, growing to nearly four in the riskiest segment, when loan prepayment is treated as non-informative censoring rather than a competing risk. A platform's churn model shows probability estimates that degrade with the horizon even as global discrimination stays within the pre-registered C-index band. A direct test of whether metric choice inverts model preference does not reject, though with limited power given two to three models per domain; the failure mode we document is better characterized as misplaced confidence in a chosen model than as choosing the wrong one. We release a pre-registered evaluation harness with full code and an annotated notebook, so these results can be verified independently and the audit extended.

## Metadata
- **Published**: 2026-07-21T19:13:54Z
- **Authors**: Rafael da Silva, Danilo Alvares
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19526v2)