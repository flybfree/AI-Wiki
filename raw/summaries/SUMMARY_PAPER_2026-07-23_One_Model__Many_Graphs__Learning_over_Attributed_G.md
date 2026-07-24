---
title: One Model, Many Graphs: Learning over Attributed Graphs across Heterogeneous Modalities with Vision-Language Models
url: http://arxiv.org/abs/2607.19128v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_14-18-25Z_OneModel_ManyGraphs_LearningoverAttributedGraphsac.md
generated_at: 2026-07-23 23:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces OMG‑VLM, a unified framework that leverages a pretrained vision‑language model as a shared backbone to learn over attributed graphs with heterogeneous modality schemas. The authors demonstrate that the approach outperforms existing GNN and LLM baselines on node classification and link prediction tasks while generalizing across unseen graph structures.

## Key Takeaways
- OMG‑VLM uses a single pretrained VLM as a common embedding space, eliminating the need for separate models when graphs contain only textual nodes, visual nodes, or both.  
- The framework introduces structure‑aware adapters that incorporate neighborhood information without leaving the VLM’s native representation, enabling effective integration of modality‑specific data.  
- Experiments across multiple domains show consistent improvements over state‑of‑the‑art GNN and LLM methods, highlighting strong cross‑graph generalization.

## Context
The rise of multimodal AI systems has created a need for models that can handle diverse input types simultaneously. Graph learning remains fragmented because most algorithms assume uniform data modalities, limiting their applicability to real‑world datasets where attributes span text and images. This paper addresses that gap by proposing a modality‑agnostic backbone.

## Implications
OMG‑VLM offers practitioners a scalable solution for integrating graph data into multimodal models without sacrificing performance. By unifying training across heterogeneous graphs, it can be deployed in applications such as social network analysis, medical imaging triage, and recommendation systems where both textual and visual cues are present.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19128v1)
