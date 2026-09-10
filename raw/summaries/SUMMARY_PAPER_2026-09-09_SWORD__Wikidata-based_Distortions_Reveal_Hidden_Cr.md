---
title: SWORD: Wikidata-based Distortions Reveal Hidden Cross-Lingual Inconsistencies in LLM Factual Error Rejection
url: http://arxiv.org/abs/2609.09349v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-08_18-39-01Z_SWORD_Wikidata_basedDistortionsRevealHiddenCross_L.md
generated_at: 2026-09-09 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SWORD, a multilingual benchmark that tests large language models’ ability to reject factually incorrect statements by perturbing Wikidata triples. The study shows that models often perform better on plausible distortions than on random substitutions and that Asian languages suffer larger performance drops compared with other languages.

## Key Takeaways
- Models achieve higher accuracy on semantically plausible distortions than on nonsensical random substitutions, indicating reliance on distributional familiarity rather than true factual verification.
- Cross‑lingual performance gaps can reach up to 28 percentage points (a 49% relative reduction) for some models when evaluating statements in East Asian languages versus other language groups.
- The benchmark reveals that multilingual factual reasoning exhibits asymmetric capabilities, meaning accuracy metrics do not capture these hidden inconsistencies.

## Context
LLMs are evaluated on benchmarks that primarily reward correct answer selection, which can mask deeper issues with factual understanding. This paper argues that standard evaluation methods overlook how models handle language‑specific distortions and how performance varies across linguistic groups.

## Implications
For researchers, SWORD provides a tool to uncover hidden biases in multilingual AI systems, guiding more balanced model development. For industry practitioners, the findings suggest that fairness testing across languages is essential before deploying LLMs in global applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09349v1)
