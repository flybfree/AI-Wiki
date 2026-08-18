---
title: Prompting is not enough: supervised baselines and leakage control for measuring shared decision-making with LLMs in pediatric encounters
published: 2026-08-14T18:02:08Z
authors: Bernardo Modenesi, Jody Lin, Kimberly Kaphingst, Angela Zhu, Maya Wheeler, Peilu Zhang, Angela Fagerlin
url: http://arxiv.org/abs/2608.14792v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prompting is not enough: supervised baselines and leakage control for measuring shared decision-making with LLMs in pediatric encounters

## Abstract
Objectives: To determine whether zero-shot prompting of a large language model (LLM) is sufficient to detect shared decision-making (SDM) behaviors in real clinical encounters, and whether supervised learning adds value under patient-grouped, nested evaluation.   Methods: We analyzed 21 audio-recorded outpatient surgical decision encounters (19 unique patients; 7,566 utterance segments; ~6.1 hours) between families of children with multiple long-term conditions and their surgical providers. Trained coders labeled segments for 12 SDM behaviors (human-human macro Cohen's kappa = 0.695). We compared a zero-shot local LLM (Qwen 2.5 32B), a supervised classifier over frozen sentence embeddings, and their logistic stack, under patient-grouped outer folds with inner cross-fitted thresholds and patient-resampled confidence intervals.   Results: The zero-shot LLM reached macro kappa = 0.139 (95% CI 0.111-0.164). The supervised classifier reached kappa = 0.227 (0.186-0.262), a paired improvement of 0.088 (0.051-0.119). A logistic stack of the two reached kappa = 0.242 (0.198-0.284). We identified multiple corpus-specific leakage paths, including grouping sibling recordings separately and allowing labels from an outer held-out patient to enter few-shot exemplars used while fitting downstream models.   Conclusion: Zero-shot prompting alone is not sufficient to measure SDM behavior as reliably as a small supervised model, and patient-level grouping alone does not prevent leakage when labeled prompt exemplars are precomputed outside the outer evaluation loop. Reported performance is sensitive to the unit of data splitting and to where labeled exemplars enter the pipeline. External validation is needed before these findings generalize beyond this population, model, prompt, and codebook.

## Metadata
- **Published**: 2026-08-14T18:02:08Z
- **Authors**: Bernardo Modenesi, Jody Lin, Kimberly Kaphingst, Angela Zhu, Maya Wheeler, Peilu Zhang, Angela Fagerlin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14792v1)