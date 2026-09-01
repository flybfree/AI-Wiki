---
title: Emergent Misalignment Is Not Magical
published: 2026-08-29T08:00:32Z
authors: Mingxuan Li, Qirun Dai, Heran Wang, Chenhao Tan
url: http://arxiv.org/abs/2608.29118v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Emergent Misalignment Is Not Magical

## Abstract
Fine-tuning large language models (LLMs) on narrowly harmful datasets can lead to misalignment broadly, a phenomenon known as emergent misalignment (EM). EM poses a challenge for AI safety and our understanding of LLMs. Prior work often frames EM as an unexpected behavior, and explains it by appealing to general misalignment directions or anthropomorphizing it as acquiring an evil persona. However, the mechanisms behind these framings remain obscure. In this work, we show that EM is a predictable and data-dependent generalization phenomenon. By examining the base model's representation of EM training data and evaluation prompts, we find that evilness after EM training is highly predictable from representational distance: the closer an evaluation prompt is to training data centroid, the more evilness it elicits from EM models after training (with an average Spearman correlation of -0.73 across 12 model-dataset settings). Building upon this analysis, we further demystify EM by showing that (1) its effectiveness changes significantly based on training data format; (2) there is not a general misalignment direction that transfers across different EM models; (3) the effect of EM is fundamentally different from persona changes. Furthermore, we extend the EM generalization metric from a scalar distance to a dataset-specific generalization direction, which robustly predicts EM models' evilness under semantics-preserving prompt perturbations including appending random tokens and paraphrasing, where other methods do not reliably generalize.

## Metadata
- **Published**: 2026-08-29T08:00:32Z
- **Authors**: Mingxuan Li, Qirun Dai, Heran Wang, Chenhao Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29118v1)