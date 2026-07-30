---
title: WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models
published: 2026-07-29T08:48:35Z
authors: Hao Jiang, Peiru Du, Pengfei Yao, Mengting Li, Siyuan Lou, Kuo Cai, Sheng Yu, Qiang Luo, Jian Liang, Ruiming Tang, Fei Pan, Peng Jiang, Wenwu Ou
url: http://arxiv.org/abs/2607.26621v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models

## Abstract
Large language models (LLMs) have demonstrated strong reasoning capabilities, motivating their adoption as backbones for foundation recommendation models (FRMs). Existing approaches typically enhance recommendation with explicit Chain-of-Thought (CoT) under the Think-then-Answer paradigm. However, generating lengthy rationales introduces substantial inference overhead, while fixed CoT templates struggle to model diverse, dynamic, and context-dependent user interests. We propose WhisperRec, an efficient latent reasoning framework for FRMs. WhisperRec compresses teacher-generated CoT into learnable latent reasoning tokens, enabling a Latent-Reason-then-Answer paradigm that performs reasoning in latent space without producing verbose rationales. This design retains decision-relevant reasoning information while avoiding the latency bottleneck of autoregressive rationale generation. Specifically, it first introduces Multi-View Adaptive CoT (MV-ACoT) to construct diverse, high-quality supervision from complementary perspectives on user interests. MV-ACoT also adapts reasoning complexity to each instance, applying lightweight analysis to clear cases and targeted multi-factor reasoning to challenging ones. Building on a pre-trained FRM, WhisperRec then employs a three-stage Latent Reasoning Alignment procedure to progressively internalize teacher CoT into latent representations. Finally, curriculum-based post-training activates latent-token reasoning for downstream recommendation while preserving standard recommendation capability. Experiments on an industrial-scale Kuaishou dataset and the public Kuaishou LLM-Rec benchmark show that WhisperRec consistently outperforms explicit-CoT methods and conventional baselines. Compared with explicit CoT Think and No-Think variants, WhisperRec improves SID@64 by 17.44% and 9.33%, respectively, and achieves over 10x higher online inference throughput.

## Metadata
- **Published**: 2026-07-29T08:48:35Z
- **Authors**: Hao Jiang, Peiru Du, Pengfei Yao, Mengting Li, Siyuan Lou, Kuo Cai, Sheng Yu, Qiang Luo, Jian Liang, Ruiming Tang, Fei Pan, Peng Jiang, Wenwu Ou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26621v1)