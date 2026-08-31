---
title: A Probabilistic Interpretation of KV Cache Eviction
published: 2026-08-28T12:57:07Z
authors: Renato Geh, Alex Chen, Daniel Israel, Aditya Grover, Guy Van den Broeck
url: http://arxiv.org/abs/2608.28293v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Probabilistic Interpretation of KV Cache Eviction

## Abstract
The premise and promise of KV (cache) eviction is simple: higher throughput can be achieved by evicting some entries from the KV cache, at a negligible cost to quality. This holds empirically for many existing methods, though most rely on creative heuristics for selecting which entries to drop. Despite recent advances, the problem of KV eviction has remained informal in the literature. This paper aims to properly formalize this problem through the lens of probabilistic reasoning and reveal what can be learned from this perspective. Concretely, we (1) formalize the problem of KV eviction and, unfortunately, prove that it is computationally hard, (2) show that by framing it probabilistically, KV eviction reduces to the problem of expectation estimation, which can be approximated through sampling, (3) show that through this probabilistic interpretation, correcting for evicted entries during decoding---a previously ignored problem---becomes feasible, and (4) reveal that existing methods in the literature are zero-variance biased estimators that can be easily adapted in order to enable decode time correction. In practice, we show that this probabilistic version of KV eviction coupled with decode time correction is more robust to different tasks compared to existing eviction methods and achieves competitive performance at the same compression budget.

## Metadata
- **Published**: 2026-08-28T12:57:07Z
- **Authors**: Renato Geh, Alex Chen, Daniel Israel, Aditya Grover, Guy Van den Broeck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28293v1)