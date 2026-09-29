---
title: Jailbreaks for Black-Box Uncertainty Quantification in Large Reasoning Models
published: 2026-09-28T15:02:03Z
authors: Lucas Biechy, Cédric Eichler, Adrien Boiret, Nicolas Anciaux
url: http://arxiv.org/abs/2609.35350v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Jailbreaks for Black-Box Uncertainty Quantification in Large Reasoning Models

## Abstract
While Large Reasoning Models (LRMs) excel at complex reasoning, alignment through reinforcement learning often induces systemic overconfidence. In production environments, where logits may be unavailable, robust black-box uncertainty quantification (UQ) is essential for trustworthiness and safety. Focusing on question-answering for LRMs, we show that existing black-box methods, such as paraphrase-based self-consistency and confidence verbalization, offer little to no improvement over simple repeated sampling, suggesting that alignment suppresses useful output variability. We introduce prompt-level relaxation operators that broaden the model's effective output distribution by approximating the effect of an optimal policy obtained with a stronger KL-regularization parameter, hence closer to the reference model. Theoretically, we demonstrate that relaxation improves calibration. We propose Jailbreak for Uncertainty (J4U), a jailbreak-derived technique for UQ that empirically reproduces the behavioral signatures predicted by our relaxation theory. Across 3 datasets and 4 LRMs, including a closed-source production model, J4U's improvement over repeated sampling achieves statistical significance in up to 6 times more LRM-dataset-metric settings than the strongest black-box UQ state-of-the-art baseline we evaluate, with average ECE reductions up to 5 times larger. These results provide a practical tool for UQ in black-box LRM deployment.

## Metadata
- **Published**: 2026-09-28T15:02:03Z
- **Authors**: Lucas Biechy, Cédric Eichler, Adrien Boiret, Nicolas Anciaux
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35350v1)