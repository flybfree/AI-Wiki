---
title: Who Bridges Safety? Identifying and Targeting Cross-Lingual Shared Safety Pathways
published: 2026-08-10T03:48:47Z
authors: Shuyi Miao, Wangjie Qiu, Pengyang Shao, Canran Xiao, Fei Shen, Zhiming Zheng, Tat-Seng Chua
url: http://arxiv.org/abs/2608.09095v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who Bridges Safety? Identifying and Targeting Cross-Lingual Shared Safety Pathways

## Abstract
Uncovering the internal mechanisms underlying the safety capabilities of large language models (LLMs) is crucial for developing trustworthy artificial intelligence. Currently, mechanistic interpretability studies on multilingual safety are largely confined to local components, such as isolated neurons. However, this static and fragmented perspective overlooks the synergy among components and fails to elucidate how safety signals dynamically propagate within the model to drive safety decisions ultimately. In this work, we move beyond isolated neurons to identify and target the cross-layer functional pathways formed during safety signal propagation, thereby uncovering the mechanisms driving the cross-lingual safety gap. Specifically, we first identify monolingual safety pathways and validate their impact on refusing harmful requests. Subsequent cross-lingual analyses reveal a sparse subset of cross-lingual shared safety pathways, confirming that this intersection acts as the internal bridge transferring safety capabilities from high-resource (HR) languages to non-high-resource (NHR) languages. Building on these mechanistic findings, we propose a pathways-targeted alignment method based on the cross-lingual shared safety pathways. Experimental results show that updating only a small fraction of pathway parameters significantly improves safety in NHR languages while largely preserving the model's general capabilities.

## Metadata
- **Published**: 2026-08-10T03:48:47Z
- **Authors**: Shuyi Miao, Wangjie Qiu, Pengyang Shao, Canran Xiao, Fei Shen, Zhiming Zheng, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09095v1)