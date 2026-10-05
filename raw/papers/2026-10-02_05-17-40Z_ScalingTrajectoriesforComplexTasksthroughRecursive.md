---
title: Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite
published: 2026-10-02T05:17:40Z
authors: Zongxia Li, Yucheng Shi, Zhongzhi Li, Junyao Yang, Ruhan Wang, Chengsong Huang, Fuxiao Liu, Haitao Mi, Jordan Boyd-Graber,  LeoweiLiang
url: http://arxiv.org/abs/2610.02826v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite

## Abstract
Successful trajectories on difficult tasks provide valuable supervision for model improvement, but specialized harnesses introduce interventions that may be unavailable during deployment. We propose Recursive Self-Rewrite (RSR), a framework that uses one base model, Qwen-3.8-27B, to discover successful solutions under diverse harnesses and reconstruct them as training trajectories under a general harness. A planner extracts procedures into runbooks, a critic screens for verifier and solution leakage and guides recursive revision, and an executor follows qualified runbooks in fresh sandboxes. Across approximately 3K self-curated terminal tasks, three harnesses jointly solve 759 tasks, 34.3% more than the strongest individual harness in the recorded pool. RSR expands 2,001 successful source trajectories into 11,094 rewritten trajectories for supervised finetuning. Training on these trajectories outperforms both the base model and direct trajectory SFT. Compared with the base model, pass@3 increases from 57.0% to 74.2% on Terminal-Bench 2, from 1.5% to 9.1% on Terminal-Bench 4, from 39.0% to 63.0% on our self-curated Terminal-Bench Hard, and from 3.0% to 6.0% on our Software Terminal-Bench. Process reward on Long-Horizon Terminal-Bench rises from 0.21 to 0.29. These results show how diverse harness-assisted experiences can be reconstructed into reusable capabilities for a model operating under a general harness.

## Metadata
- **Published**: 2026-10-02T05:17:40Z
- **Authors**: Zongxia Li, Yucheng Shi, Zhongzhi Li, Junyao Yang, Ruhan Wang, Chengsong Huang, Fuxiao Liu, Haitao Mi, Jordan Boyd-Graber,  LeoweiLiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02826v1)