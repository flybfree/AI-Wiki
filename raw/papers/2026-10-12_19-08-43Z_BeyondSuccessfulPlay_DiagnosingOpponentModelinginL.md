---
title: Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models
published: 2026-10-12T19:08:43Z
authors: Hanbo Xie, Yue Zhao, Robert C. Wilson
url: http://arxiv.org/abs/2610.17310v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models

## Abstract
Language-model agents are expected to adapt to others whose behavior changes through interaction. Yet adaptation may rely on learned behavioral patterns rather than theory of mind (ToM): the ability to infer others' mental states, including beliefs and intentions. We introduce a benchmark and diagnostic framework for repeated hide-and-seek against algorithmic opponents with explicitly defined recursive belief updates. Their ground-truth beliefs and action probabilities let us distinguish adaptive play, action prediction, and belief tracking through live interaction, fixed-history evaluation, and controlled information interventions. With structured elicitation and behavioral supervised fine-tuning (SFT), we find improved play in several tested settings, but diagnostics reveal limitations in opponent prediction and belief tracking. We test whether supervising opponent action probabilities can address this predictive deficit in Qwen2.5-7B-Instruct. Predictions improve when the model is told the opponent's type and parameter settings, but become less accurate when it must infer the opponent from history without this information. Training on examples that also omit these details reduces the gap, although improvements vary across opponents. Is this limitation specific to smaller open-weight models, or does it also appear in a frontier model? GPT-5.4 also benefits from correct opponent beliefs: supplying them improves its predictions and choices, whereas deeper explicit belief reports and self-generated memory do not consistently improve forecasting from interaction history. This contrast suggests that using useful belief information is easier than inferring it autonomously, even for a frontier model. Together, our findings distinguish improved play and action prediction from reliable belief tracking, providing a framework for evaluating mentalizing and testing targeted improvements.

## Metadata
- **Published**: 2026-10-12T19:08:43Z
- **Authors**: Hanbo Xie, Yue Zhao, Robert C. Wilson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17310v1)