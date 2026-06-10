---
title: 'Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models'
published: 2026-06-03T17:57:51Z
authors: Yichen Gao, Yiqun Zhang, Zijing Wang, Yujia Li, Heng Guo, Xi Wu, Xiaocui Yang, Shi Feng, Yifei Zhang, Daling Wang
url: http://arxiv.org/abs/2606.05161v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models

## Abstract
Audio-language models (ALMs) often follow text that conflicts with audio, even when the audio evidence is clear. This raises a basic question: is the audio-supported answer unavailable, or is it represented but overridden by the conflicting text? We examine this question using a same-audio counterfactual that keeps the audio fixed, removes only the conflicting text, and measures the resulting shift in model preference. Across five ALMs and four conflict tasks, 64.1% of conflict samples show a sign flip: the same-audio branch prefers the audio-supported answer, whereas the joint branch prefers the text-supported answer. This pattern suggests that the relevant audio evidence is encoded but loses in arbitration. Activation patching further localizes the reversal to answer-position computation, and patching effects closely track output candidate-score differences (Spearman rho=0.93). Using this diagnostic, we propose Gated Audio Counterfactual Logit Correction (GACL), a training-free decoding rule that interpolates between joint and same-audio scores. Under a strict 5 pp faithfulness-drop budget, GACL improves nAUC by 17.8 points over the best contrastive baseline and transfers without retuning to vision-text arbitration (up to +40.5 pp).

## Metadata
- **Published**: 2026-06-03T17:57:51Z
- **Authors**: Yichen Gao, Yiqun Zhang, Zijing Wang, Yujia Li, Heng Guo, Xi Wu, Xiaocui Yang, Shi Feng, Yifei Zhang, Daling Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.05161v1)