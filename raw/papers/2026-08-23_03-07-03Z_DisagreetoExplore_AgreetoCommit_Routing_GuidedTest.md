---
title: Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents
published: 2026-08-23T03:07:03Z
authors: Kang Chen, Junjie Nian, Yixin Cao, Yugang Jiang
url: http://arxiv.org/abs/2608.22191v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents

## Abstract
Software-engineering agents solve repository-level tasks through long, stochastic tool-use trajectories, and repeated attempts often find fixes missed by one run. Test-time scaling is difficult because patches lack canonical answer forms, while sibling actions from a shared prefix are correlated. We study whether native MoE router traces can guide steering and selection without an external judge or selection-time test execution. Our analysis shows that routing provides a robust behavioral role signal; token-granular readouts and decision-matched comparison sets turn it into effective control. We therefore introduce Risa (Routing-Informed Steering and Arbitration): within trajectories, routing encourages diverse exploration and controlled convergence during patch commitment; across separately sampled trajectories, agreement at informative patch positions selects a final candidate. We evaluate on SWE-bench Verified using open-weight sparse MoE agents across scales and reasoning-effort settings. Risa's routing arbitration raises the macro-average resolved rate from 44.9% under uniform sampling to 48.2% on the gpt-oss family, matching text consensus without answer-string matching, and it transfers to Qwen3.6, where it improves on uniform choice and matches text consensus on the full 500-task benchmark.

## Metadata
- **Published**: 2026-08-23T03:07:03Z
- **Authors**: Kang Chen, Junjie Nian, Yixin Cao, Yugang Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22191v1)