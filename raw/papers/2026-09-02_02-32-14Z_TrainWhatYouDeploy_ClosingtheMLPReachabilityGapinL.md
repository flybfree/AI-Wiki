---
title: Train What You Deploy: Closing the MLP Reachability Gap in Low-Rank Clone Distillation
published: 2026-09-02T02:32:14Z
authors: Wenhui Chen, Zhifeng Li, Jie Zhou, Navan Preet Singh, Madalina Ciobanu, Chenghua Wang, Qingqing Mao, Ritankar Das
url: http://arxiv.org/abs/2609.02006v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Train What You Deploy: Closing the MLP Reachability Gap in Low-Rank Clone Distillation

## Abstract
A compressed student has two shapes that need not agree: the weight it deploys at inference and the weight family its training can reach. We show that a state-of-the-art weight-inheritance distiller, Low-Rank Clone (LRC), deploys a full-width student MLP but ties training to a teacher-induced slice, leaving 62.5-81.4% of each deployed matrix's independent linear degrees of freedom unreachable-paid for at inference, never trainable. Our principle is one line: train what you deploy. From the identical LRC warm start, we make the training object the entire deployed matrix, with no change in deployed shape, deployed parameter count, or inference FLOPs, via two mergeable realizations (Dense-LRC and CORE-LRC) that both collapse to one deployed weight. This recovers stranded capacity: taking the stronger realization per teacher, +2.36/+2.71/+10.45 Avg9 over matched-budget plain-LRC baselines across three teachers (Llama3.2-3B, Llama3.1-8B, Qwen2.5-3B), with the largest gain on the widest teacher (Qwen), where it reaches the original recipe's approx. 20B-token accuracy at 10B tokens (2x token efficiency); there the strictly same-lineage arm still recovers +6.39, the fully controlled figure. Controls strongly support attributing the gain to the enlarged reachable set, rather than to added parameters or the recipe. From approx. 10B distillation tokens plus a short SFT, a half-parameter 1.5B student matches its approx. 9T-token teacher's 9-task macro-average, within evaluation noise and with a residual MMLU deficit, and a 2.7B student beats Meta's own official compression of Llama3.1-8B at ~900x fewer compression tokens (a token count under unmatched recipes, not a compute claim). All results are from single-seed runs on the LRC backbone.

## Metadata
- **Published**: 2026-09-02T02:32:14Z
- **Authors**: Wenhui Chen, Zhifeng Li, Jie Zhou, Navan Preet Singh, Madalina Ciobanu, Chenghua Wang, Qingqing Mao, Ritankar Das
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02006v1)