---
title: MCPO: Modality-Contrastive Preference Optimization for Multimodal Chain-of-Thought Compression
published: 2026-09-04T09:54:53Z
authors: Guangheng Yang, Zhenliang Ni, Zhenkai Wu, Han Shu, Juan Feng, Wenming Yang, Jie Hu
url: http://arxiv.org/abs/2609.04947v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MCPO: Modality-Contrastive Preference Optimization for Multimodal Chain-of-Thought Compression

## Abstract
Recently, multimodal large-scale reasoning models have demonstrated remarkable capabilities in solving complex tasks through long Chains-of-Thought (M-CoT). However, excessively long reasoning trajectories incur substantial computational costs and significant KV-cache pressure. Existing CoT compression and alignment paradigms mainly rely on static rules or single-dimensional preferences, lacking fine-grained cross-modal constraints; as a result, they are prone to inducing visual laziness and hallucinatory reasoning. To address these issues, we propose Modality-Contrastive Preference Optimization (MCPO), a highly sample-efficient two-stage length-compression method that requires fewer than 900 training samples. In the compression stage, we introduce a step-level Normalized Cross-Modal Mutual Information (NCMI) pruning algorithm, which automatically identifies and removes visual-independent reasoning steps by comparing the reasoning discrepancies between with-image and no-image contexts. This significantly reduces redundancy and hallucinatory content in the reasoning chains. In the alignment stage, the model first undergoes supervised fine-tuning to achieve domain-adaptive initialization, followed by optimization using an asymmetric multimodal length-controlled preference loss. This objective adopts a highly nonlinear odds-ratio formulation that provides steep gradients in the with-image context to reinforce length constraints for preferred trajectories, while applying a scaled, flat-gradient linear difference in the no-image context to maintain modality consistency, thereby achieving stable cross-modal preference alignment. Extensive experiments on mainstream base models such as Qwen3-VL-Thinking show that our method can reduce CoT length by up to 69.5% and achieve up to 3.34x end-to-end inference speedup while preserving original accuracy.

## Metadata
- **Published**: 2026-09-04T09:54:53Z
- **Authors**: Guangheng Yang, Zhenliang Ni, Zhenkai Wu, Han Shu, Juan Feng, Wenming Yang, Jie Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04947v1)