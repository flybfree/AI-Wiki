---
title: LAVE: Latent Visual Evidence-Enhanced Planning for Video Tool-use Agents
published: 2026-08-05T10:25:47Z
authors: Zijian Wang, Junnan Zhu, Rongzhen Li, Xiao Liu, Guohui Xiang, Quan Lu, Lijia Liu, Yining Wang, Jiang Zhong, Kaiwen Wei
url: http://arxiv.org/abs/2608.07585v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LAVE: Latent Visual Evidence-Enhanced Planning for Video Tool-use Agents

## Abstract
Long-video understanding requires models to efficiently acquire and reuse sparse visual evidence from long and redundant video streams. Recent video tool-use agents address this challenge by iteratively invoking visual Tools at different temporal scales, but their Tool-Planner communication typically relies on textual observations. Such text-only interfaces provide lossy summaries of Tool computations, causing previously computed visual evidence not verbalized to be discarded and unavailable for subsequent planning. We identify this limitation as the Tool observation bottleneck and propose Latent Visual Evidence-Enhanced Planning (LAVE), a training-free framework for reusing latent visual evidence from completed Tool calls. LAVE introduces a dual-channel observation interface: the visible channel preserves the original textual trajectory, while the latent channel stores pre-verbal visual updates with their Tool roles, source-frame timestamps, and visual locations. During planning, LAVE retrieves evidence relevant to the current Planner state but not covered by textual observations, and integrates it through bounded timestamp-aligned latent updates with entropy-constrained frame-time routing. This enables video agents to reuse existing visual computation without additional training, frame replay, or modifications to the original orchestration. Extensive experiments on Video-MME, LongVideoBench, and CG-Bench show that LAVE consistently improves video tool-use agents across backbones. Under a comparable frame budget, LAVE improves the Video-MME overall score by 3.76 points over the strongest baseline, demonstrating the effectiveness of latent visual evidence reuse for multi-step video-agent planning.

## Metadata
- **Published**: 2026-08-05T10:25:47Z
- **Authors**: Zijian Wang, Junnan Zhu, Rongzhen Li, Xiao Liu, Guohui Xiang, Quan Lu, Lijia Liu, Yining Wang, Jiang Zhong, Kaiwen Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07585v1)