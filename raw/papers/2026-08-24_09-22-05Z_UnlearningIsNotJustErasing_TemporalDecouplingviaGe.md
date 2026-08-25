---
title: Unlearning Is Not Just Erasing: Temporal Decoupling via Generation Inequality
published: 2026-08-24T09:22:05Z
authors: Xunlei Chen, Qirui Ye, Yuang Li, Yi Gong, Zhaokun Wang, Wenyi Li, Shiyao Guo, Jinyu Guo
url: http://arxiv.org/abs/2608.23020v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unlearning Is Not Just Erasing: Temporal Decoupling via Generation Inequality

## Abstract
Large language models (LLMs) require effective unlearning to address privacy regulations and safety concerns. However, achieving precise forgetting without compromising general utility remains challenging. Existing sequence- and token-level methods penalize target outputs without modeling their context-dependent retrieval paths, which can disrupt linguistic structure or suppress benign knowledge. We present ADU, a fine-grained, training-based framework that shifts unlearning from token erasure to contextual attention-pathway decoupling. Exploiting the functional distinction between local and global attention heads, ADU identifies preplan positions that retrieve persistent sensitive anchors and fixes their candidate paths under the original model. It then trains attention-projection adapters to suppress attention mass along these paths while preserving local-attention structure and retain-set language modeling. Post-training activation exchange tests whether the modified attention-output module transmits the learned forgetting effect. ADU achieves the strongest aggregate performance among evaluated baselines on the TOFU and WMDP benchmarks, including a Forget Quality of (0.93) on TOFU. It preserves 87--98% of model utility (92.9% on average versus 81.9% for baselines) while reducing side effects in benign contexts.

## Metadata
- **Published**: 2026-08-24T09:22:05Z
- **Authors**: Xunlei Chen, Qirui Ye, Yuang Li, Yi Gong, Zhaokun Wang, Wenyi Li, Shiyao Guo, Jinyu Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23020v1)