---
title: DANGERLENS: Probing Dangerous Representations Hidden by Safety Alignment
published: 2026-10-14T01:10:09Z
authors: Tianzhuo Yang, Shaoheng Yan, Lin Lu, Jiawei Chen, Kaile Wang, Fanyu Meng, Minglu Liu, Yaodong Yang
url: http://arxiv.org/abs/2610.19365v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DANGERLENS: Probing Dangerous Representations Hidden by Safety Alignment

## Abstract
Safety alignment teaches language models to refuse harmful requests, yet the internal accessibility of hazardous concepts can retain traces of earlier training. Can checkpoints with equally safe behavior differ in what remains accessible behind their refusals? In this work, we investigate this question through paired training histories and a direct audit of intermediate representations. We introduce DANGERLENS, a probe that maps hidden states into vocabulary space and uses blinded semantic judgments to distinguish harmful goals and operational means from hazard recognition and safety control. Experiments on three Qwen1.5 scales show that checkpoints with prior harmful exposure generally retain greater hazardous concept accessibility after the same safety alignment, with the strongest separation in intermediate and later layers. The same harmful update also produces different behavioral trajectories from closely matched starting points. Human relevance validation and readout ablations reinforce the measured accessibility contrast. Our findings show that training history remains visible inside behaviorally matched models and motivate internal accessibility audits alongside output safety evaluations.

## Metadata
- **Published**: 2026-10-14T01:10:09Z
- **Authors**: Tianzhuo Yang, Shaoheng Yan, Lin Lu, Jiawei Chen, Kaile Wang, Fanyu Meng, Minglu Liu, Yaodong Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19365v1)