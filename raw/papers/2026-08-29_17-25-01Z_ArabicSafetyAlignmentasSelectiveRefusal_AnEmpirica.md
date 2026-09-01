---
title: Arabic Safety Alignment as Selective Refusal: An Empirical Study of SFT, DPO, and Guard Calibration
published: 2026-08-29T17:25:01Z
authors: Mohamad Zbib, Ammar Mohanna
url: http://arxiv.org/abs/2608.29378v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Arabic Safety Alignment as Selective Refusal: An Empirical Study of SFT, DPO, and Guard Calibration

## Abstract
Arabic large language models must refuse harmful prompts without over-refusing benign or sensitive prompts, yet a single refusal rate hides this trade-off. We evaluate it using benign refusal B and harmful-prompt refusal H, where H measures refusal rather than harmful compliance. Across five Arabic-capable models and 130 runs on the full human-written AraSafe set, refusal-only supervised fine-tuning (SFT) collapses toward blanket refusal, whereas selected mixed-SFT configurations reach H = 90% to 93% at B = 14% to 23%; four selected configurations exceed the H = 90% target in all three runs, while Fanar does so in two of three. Direct Preference Optimization (DPO) and inference guards change B and H differently across models rather than acting as uniform upgrades. In a blinded 300-response audit, annotator binary-refusal agreement is 89.0% (kappa = 0.78); Qwen3Guard and Aya Expanse 32B reach 88.7% and 91.0% accuracy, respectively, with no conclusive paired difference. Selected SFT raises H on Arabizi for all five models, but none reaches 90%, showing only partial transfer from Modern Standard Arabic. Overall, the results support model-specific operating-point selection: set a deployment target and retain only interventions that improve it.

## Metadata
- **Published**: 2026-08-29T17:25:01Z
- **Authors**: Mohamad Zbib, Ammar Mohanna
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29378v1)