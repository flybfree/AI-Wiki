---
title: Sixteen models, fewer than two voices: measuring ensemble dispersion where no answer is uniquely correct
url: http://arxiv.org/abs/2608.00285v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_20-42-53Z_Sixteenmodels_fewerthantwovoices_measuringensemble.md
generated_at: 2026-08-03 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how sixteen language models from ten families generate distinct formulations of a psychotherapeutic case, comparing ensemble outputs to single-model baselines. It finds that ensembles increase semantic diversity to an average Vendi Score of 1.69 versus 1.43 for one model, yet the source of this dispersion is examined through per‑model dissent contributions and variance explained by model identity.

## Key Takeaways
- The Vendi Score quantifies distinct formulations as exp(entropy) yielding 1.69 on average, showing ensembles produce more varied readings than a single model.
- Per‑model dissent, defined as the complement of each model’s mean similarity to its ensemble peers, identifies the most divergent voice within an ensemble rather than decomposing overall diversity.
- Model identity explains only part of the variance in dissent; the observed outliers reflect ensemble composition changes, not individual model quirks.

## Context
The study addresses a longstanding challenge in AI research: measuring how diverse and uncertain multiple models are when generating human‑relevant outputs. By applying formal entropy metrics to language generation tasks, it bridges theoretical diversity theory with practical model ensembles, offering a quantitative baseline for evaluating interpretability and reliability.

## Implications
For practitioners, the findings suggest that ensemble performance should be evaluated not only by aggregate accuracy but also by the internal disagreement captured in dissent scores. This can guide decisions on model selection, risk mitigation, and trustworthiness in high‑stakes applications such as mental health support systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00285v1)
