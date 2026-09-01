---
title: CineForge: Self-Improving Agents for Long-Horizon Video Generation
published: 2026-08-30T07:29:46Z
authors: Junxiang Liu, Lin Wang, Haiyu Shi, Hongxu Ma, Xiaoyu Yang, Chunjie Chen, Xiaoxiao Xu, Kaiqiao Zhan, Boao Wang, Shuizhou Shi, Tianyun Zhu, Jie Li, Jiangtong Li
url: http://arxiv.org/abs/2608.29621v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CineForge: Self-Improving Agents for Long-Horizon Video Generation

## Abstract
Long-horizon story-driven video generation requires a production agent to coordinate narrative decomposition, state tracking, shot design, prompt construction, rendering, and revision across interdependent scenes. Existing adaptive video systems primarily refine requests or reusable skills, leaving recurring production failures disconnected from persistent, stage-targeted improvements across stories. We introduce CineForge, a self-evolving video-production agent framework that couples CineForge-Produce for video generation with CineForge-Evolve for cross-story policy evolution. CineForge-Produce organizes each source story into typed narrative, character, spatial, and cinematic states, uses them to coordinate asset and clip generation, and records the process as a canonical production trajectory. CineForge-Evolve applies Case-to-Pattern-to-Policy Evolution (CPPE) to review trajectory evidence, consolidate recurrent findings into bounded stage-local patches, and deploy validated updates through structural replay and confidence-controlled paired evaluation. To measure complete story realization, we introduce CineScope, which combines a 100-script CineScope-Data suite with a human-aligned, multiscale CineScope-Metric spanning causal state, directorial orchestration, pacing and resource allocation, and character arc. Across CineScope-Data and two public benchmarks, the evolved CineForge policy improves CineScope-Metric from 4.024 to 4.380, outperforms three long-video baselines with consistent gains under ScriptAgent, and reduces review LLM calls by 37.0% on new stories. These results establish production trajectories as actionable experience for video agents that improve cumulatively across long-form storytelling tasks.

## Metadata
- **Published**: 2026-08-30T07:29:46Z
- **Authors**: Junxiang Liu, Lin Wang, Haiyu Shi, Hongxu Ma, Xiaoyu Yang, Chunjie Chen, Xiaoxiao Xu, Kaiqiao Zhan, Boao Wang, Shuizhou Shi, Tianyun Zhu, Jie Li, Jiangtong Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29621v1)