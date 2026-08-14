---
title: Perturbation-based Regional Interpretability through Subtraction Mapping (PRISM): naming-error dissociations in language models and post-stroke aphasia
url: http://arxiv.org/abs/2608.12717v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_02-02-05Z_Perturbation_basedRegionalInterpretabilitythroughS.md
generated_at: 2026-08-13 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PRISM, a method that uses subtraction analysis to map how layer perturbations in large language models correspond to clinical naming test categories and lesion patterns of post‑stroke aphasia. By aligning error profiles across 213 patients with transformer layers, the authors demonstrate a robust phonemic‑favoring dissociation and a frontal‑perisylvian cortical cluster that replicate both in the model.

## Key Takeaways
- PRISM applies subtraction analysis to transformer layers, treating each layer as a subject and comparing error proportions across clinical naming categories. 
- The method yields a deep layer cluster and a frontal‑perisylvian cortical cluster that correspond to phonemic‑favoring errors in both patients and models. 
- Semantic‑favoring trends are consistently signed but not statistically significant, indicating the dissociation is specific.

## Context
Mechanistic interpretability of large language models has long relied on global error analysis, which cannot pinpoint spatial or functional specializations. This work bridges that gap by using a neuroimaging‑inspired subtraction framework to test regionally specific functions in AI components, offering a falsifiable test of specialization claims.

## Implications
For researchers, PRISM provides a concrete protocol to evaluate whether transformer layers correspond to cognitive operations, guiding future interpretability studies. For industry, it suggests that fine‑grained layer behavior may be leveraged for specialized applications such as clinical language assistance, though causal claims remain speculative until Stage 3 interventions are tested.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12717v1)
