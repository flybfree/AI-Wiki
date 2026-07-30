---
title: OptimismBench: Forecasting Bias and the Alignment Effect in Language Model Judgment
published: 2026-07-29T14:38:55Z
authors: Seonglae Cho, Adriano Koshiyama
url: http://arxiv.org/abs/2607.26981v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OptimismBench: Forecasting Bias and the Alignment Effect in Language Model Judgment

## Abstract
Large language models are increasingly used as decision aids whose probability judgments shape downstream choices. Whether those judgments carry a systematic directional tilt has been hard to detect: calibration metrics aggregate unsigned errors, and naturalistic uncertainty offers no ground-truth probability. When an LLM rates a startup's success at 70% but its failure at 15%, the missing 15 points expose a distortion no aggregate score flags. We introduce OptimismBench, which detects directional bias with inverted pairs: each scenario elicits both P(success) and P(failure), and asymmetry between the two framings yields a signed bias score without ground truth. Across 16 models from 8 providers, fourteen are optimistic; pessimism appears only in Anthropic's frontier tier. Eleven matched base-versus-chat pairs across four families show post-training sets the sign of the bias, with opposite shifts in different families. The pattern survives prompt, temperature, perspective, and self-debiasing ablations. A seventeen-model six-language comparison further shows model identity dominates language, with inter-model variance at 4.7x inter-language variance. We release 3,870 items across 10 languages for per-model directional-bias auditing. When alignment makes a model more helpful, it also tilts its probabilities; downstream pipelines inherit the tilt by default.

## Metadata
- **Published**: 2026-07-29T14:38:55Z
- **Authors**: Seonglae Cho, Adriano Koshiyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26981v1)