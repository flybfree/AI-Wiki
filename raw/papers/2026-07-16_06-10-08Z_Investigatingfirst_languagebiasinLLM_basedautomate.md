---
title: Investigating first-language bias in LLM-based automated essay scoring: A cross-prompt evaluation of an open-weight AI-model on TOEFL essays
published: 2026-07-16T06:10:08Z
authors: John Maurice Gayed
url: http://arxiv.org/abs/2607.14605v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Investigating first-language bias in LLM-based automated essay scoring: A cross-prompt evaluation of an open-weight AI-model on TOEFL essays

## Abstract
This study examines the cross-prompt generalization and first-language (L1) scoring effects of a LoRA-adapted open-weight large language model (Gemma-3-27B-it) applied to automated essay scoring. Using the identical model and inference configuration reported in "AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models" (Gayed, 2026), which was fine-tuned on 480 argumentative essays from two prompts, we evaluate scoring accuracy on the full TOEFL11 corpus: 12,100 essays written by test-takers from 11 first-language backgrounds across eight prompts, none of which were seen during training. The model's raw scores (0.5-5.0) are mapped to the same three proficiency bands (low, medium, high) used by ETS, enabling direct comparison. The model achieved an overall band agreement of 77.79% and a quadratic weighted kappa of 0.702, with adjacent-band agreement of 99.98%. Accuracy was stable across all eight unseen prompts, with no advantage for prompts thematically related to the training data, indicating robust cross-prompt generalization. However, the model exhibited a systematic, L1-linked scoring offset. Within every proficiency band, essays from European-language backgrounds received consistently higher scores than essays from East-Asian-language backgrounds, a pattern not attributable to the composition of the fine-tuning data. This is the first large-scale L1 fairness analysis of a fine-tuned open-weight LLM for automated essay scoring.

## Metadata
- **Published**: 2026-07-16T06:10:08Z
- **Authors**: John Maurice Gayed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.14605v1)