---
title: Selective Knowledge Edit Reversal via Gated Singular Vector Shrinkage
published: 2026-09-02T04:32:07Z
authors: Weifeng Jiang, Ruirui Chen, Qianren Mao, Junnan Liu, Qili Zhang, Kwok-Yan Lam
url: http://arxiv.org/abs/2609.02091v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Selective Knowledge Edit Reversal via Gated Singular Vector Shrinkage

## Abstract
Knowledge editing provides an efficient way to update factual knowledge in large language models. However, malicious edits may introduce safety risks, making it necessary to reverse undesirable editing effects. Existing reversal methods for parameter-modifying edits mainly focus on global removal, which may also erase beneficial edits that should be preserved. In this paper, we study selective reversal of edited knowledge, where the goal is to reverse targeted edited facts while preserving the remaining edited facts. Based on the hypothesis that each edit is sparsely encoded within the dominant subspace of the edited matrix, we propose a spectral-based reversal framework that locates edit-sensitive components within the dominant singular subspace of edited weights. Experiments across multiple settings demonstrate the effectiveness of our method in reversing selected edits while preserving unrelated edited facts. These results suggest that different edits are sparsely encoded within dominant singular components and can be separable when the number of edits is moderate, making selective spectral reversal a promising direction for locating edit-specific components and repairing edited language models.

## Metadata
- **Published**: 2026-09-02T04:32:07Z
- **Authors**: Weifeng Jiang, Ruirui Chen, Qianren Mao, Junnan Liu, Qili Zhang, Kwok-Yan Lam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02091v1)