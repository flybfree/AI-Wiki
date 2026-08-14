---
title: SPADE: Speculative Decoding for Precise and Low Cost Distributed Edge Cloud Inference
published: 2026-08-13T10:43:57Z
authors: Divya Jyoti Bajpai, Kishan Kumar Upadhyay, Manjesh Kumar Hanawal
url: http://arxiv.org/abs/2608.13076v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPADE: Speculative Decoding for Precise and Low Cost Distributed Edge Cloud Inference

## Abstract
Large Language Models (LLMs) have achieved remarkable success in natural language understanding and generation, but their deployment is constrained by high computational demands. Deploying smaller LLMs directly on the edge can circumvent this, but with degraded accuracy. Deploying smaller cloud-based big LLMs preserves performance, but at the cost of expensive per-token computation. We present a distributed inference framework, \our{}, that integrates speculative decoding (SD) across edge and cloud. A compact draft model deployed on the edge generates candidate tokens rapidly, and a large verifier model on the cloud validates these tokens in parallel. Accepted tokens are retained, while only rejections trigger verifier correction, substantially reducing the number of cloud queries. Our plug-and-play design shifts the bulk of computation to the edge, significantly lowers inference time and cloud cost, and preserves the accuracy of the big model without any retraining requirement. Our approach demonstrates a practical path toward scalable, cost-efficient, and accurate deployment of LLMs in real-world environments. Experimental results across multiple Natural Language Processing tasks using SpecBench and CNN/Dailymail datasets demonstrate that \our{} reduces the cloud model calls by $76\%$ with zero loss in accuracy as compared to the full model.

## Metadata
- **Published**: 2026-08-13T10:43:57Z
- **Authors**: Divya Jyoti Bajpai, Kishan Kumar Upadhyay, Manjesh Kumar Hanawal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13076v1)