---
title: GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI
published: 2026-08-22T11:40:27Z
authors: Zhesheng Zhang, Jiahao Lu, Wei Liu, Cong Pan, Jianhua Yang, Yixiang Chen, Hongyuan Yu, Mengqi Zhang, Kailin Lyu, Zhumin Chen, Keji He
url: http://arxiv.org/abs/2608.21928v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI

## Abstract
In embodied AI, safety risk can be latent: a benign instruction and a safe scene become hazardous only when composed. Prior work has advanced embodied safety by varying visual contexts or evaluating execution-time dynamics, but the complementary axis of fixing the scene and varying only the instruction remains underexplored. We introduce GuardianBench, an instruction-contrastive benchmark grounded in international safety standards that isolates this latent contextual risk through 3,024 instruction-scene examples organized as same-scene Safe/Unsafe contrastive pairs across various hazard categories. Benchmarking state-of-the-art vision-language models (VLMs) reveals instruction-insensitive verdicts: models disproportionately approve both instructions under a given scene; across the primary models, average pair accuracy is only 24.1%. Our systematic rationale audit localizes the dominant failure: models fail to bind the instruction-relevant cues that differentiate safe from unsafe compositions. As a post-training case study, Verdict Log-Odds Supervision (VLOS), a lightweight verdict-level objective, substantially improves performance on open-weight backbones. Together, our latent contextual risk task formulation, standards-grounded contrastive benchmark construction, pair-level and rationale-level failure diagnosis, and benchmark-enabled verdict calibration establish GuardianBench as a controlled evaluation suite for exposing and improving safety reasoning over instruction-scene compositions under latent contextual risk.

## Metadata
- **Published**: 2026-08-22T11:40:27Z
- **Authors**: Zhesheng Zhang, Jiahao Lu, Wei Liu, Cong Pan, Jianhua Yang, Yixiang Chen, Hongyuan Yu, Mengqi Zhang, Kailin Lyu, Zhumin Chen, Keji He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21928v1)