---
title: Trust Your Guide Only When Certain: Uncertainty-Aware Sparse Alignment at Inference Time
published: 2026-09-01T03:05:49Z
authors: Zeen Zhu, Zhuo Li, Weiyang Guo, Liye Zhao, Haibing Di, Yequan Wang, Jing Li
url: http://arxiv.org/abs/2609.00624v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trust Your Guide Only When Certain: Uncertainty-Aware Sparse Alignment at Inference Time

## Abstract
A prominent paradigm in inference-time alignment employs lightweight supervisors to steer Large Language Models (LLMs). Through empirical analysis, we identify a structural mismatch in this paradigm: weak supervisors exhibit pervasive high entropy across the vast majority of tokens, yet prevailing dense intervention approaches mandate supervision at every decoding step. This leads to frequent low-confidence interventions that can disrupt valid base-model reasoning and incur substantial utility costs. To resolve this, we propose TUSA (Trust-based Uncertainty Sparse Alignment). Moving away from continuous oversight, TUSA reframes alignment as a dynamic arbitration process, introducing an uncertainty-aware arbiter that authorizes intervention only when two conditions are met: the supervisor is confident and the token is semantically salient. This mechanism effectively filters out uncertainty-driven noise and redundant supervision. Extensive experiments across multiple models and benchmarks show that TUSA consistently improves both safety alignment and general helpfulness. By bypassing approximately 50% of alignment steps, it not only enhances safety preference by up to 15.6%, but also boosts general preference rates by up to 12.0% compared to the dense baseline, demonstrating that selective, high-precision alignment can outperform continuous supervision.

## Metadata
- **Published**: 2026-09-01T03:05:49Z
- **Authors**: Zeen Zhu, Zhuo Li, Weiyang Guo, Liye Zhao, Haibing Di, Yequan Wang, Jing Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00624v1)