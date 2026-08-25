---
title: CONTRAMEM: Learning Self-Evolving Procedural Memory from Contrasting Multi-Model Trajectories
published: 2026-08-23T18:11:26Z
authors: Zheyuan Deng, Binghang Lu, Hanqi Feng, Shirley Huang, Dianzhuo Wang, Yuanda Xu, Zhiwei Zhang, Yige Sun, Changhong Mou, Runyu Zhang, Yuexing Hao, Barnabas Poczos, Xiaomin Li
url: http://arxiv.org/abs/2608.22533v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CONTRAMEM: Learning Self-Evolving Procedural Memory from Contrasting Multi-Model Trajectories

## Abstract
Autonomous computer-use agents are increasingly applied to long-horizon tasks requiring coordinated application calls, persistent state tracking, and verifier-sensitive writes, yet they remain prone to procedural failures: misreading application state, tool semantics, or task progress. Procedural memory promises more consistent decisions and less redundant exploration, but constructing high-quality memory without model training remains challenging. We introduce CONTRAMEM, a source-flexible, training-free framework for self-evolving procedural memory that treats same-task outcome variation as supervision: differences in correctness, efficiency, recovery, and failure modes expose outcome-relevant procedural distinctions, distilled into a compact bank of app-level Function Cards and task-level Skill Cards that evolves through localized curation rather than append-only accumulation or whole-bank rewriting. On held-out GAIA2/ARE computer-use tasks, CONTRAMEM more than doubles the success rate across the three source-model targets (26.2% to 55.3%), with consistent per-model gains (GPT-5.5: 27.5 to 61.0; Claude Sonnet 4.6: 28.0 to 52.5; DeepSeek V4 Pro: 23.0 to 52.5). The same bank transfers unchanged to the unseen Qwen3.7 Plus (18.5 to 35.5), indicating transferable procedural knowledge rather than model-specific behavior. The same construction carries over unchanged to AppWorld, beating both no memory and its own single-source self-memory variant for all three mid-tier agents on both public test splits. Under a matched trajectory budget, heterogeneous multi-model trajectories yield stronger memory than self- or same-model multi-rollout memory: the margin comes from contrastive behavioral diversity, not stronger source agents or more sampling.

## Metadata
- **Published**: 2026-08-23T18:11:26Z
- **Authors**: Zheyuan Deng, Binghang Lu, Hanqi Feng, Shirley Huang, Dianzhuo Wang, Yuanda Xu, Zhiwei Zhang, Yige Sun, Changhong Mou, Runyu Zhang, Yuexing Hao, Barnabas Poczos, Xiaomin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22533v1)