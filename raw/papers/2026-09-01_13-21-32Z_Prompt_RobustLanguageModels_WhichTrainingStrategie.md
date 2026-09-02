---
title: Prompt-Robust Language Models: Which Training Strategies Work?
published: 2026-09-01T13:21:32Z
authors: Frederic Sadrieh, Michal Štefánik
url: http://arxiv.org/abs/2609.01217v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prompt-Robust Language Models: Which Training Strategies Work?

## Abstract
Despite their strong performance, large language models remain highly sensitive to prompt formulation. Prior work addresses this through refined data construction or through dedicated robustness objectives. We reproduce and compare these strategies under controlled conditions, and measure how effective they are in addressing models' prompt sensitivity. We find the current robustness fine-tuning methods improve over standard fine-tuning and in-context learning, but the best-to-worst prompt gap remains as high as 40-57% of performance. Moreover, the recent robustness-enhancing methods we test - CoIN for contrastive alignment and PPCL for consistency regularization - often fail to outperform the simplest data construction strategy: training on one template per batch. Our diagnostics explain these results. The auxiliary objectives move the quantity they penalize, but do not generalize beyond it. Additionally, data construction strategies differ due to the conflicting signs of per-template gradients on 57-64% of parameters. Thus, batches that mix formulations force the optimizer to reconcile competing updates instead of finding a shared, prompt-agnostic one.

## Metadata
- **Published**: 2026-09-01T13:21:32Z
- **Authors**: Frederic Sadrieh, Michal Štefánik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01217v1)