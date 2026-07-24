---
title: Offline RL with Hierarchical Action Chunking
url: http://arxiv.org/abs/2607.20834v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_01-48-46Z_OfflineRLwithHierarchicalActionChunking.md
generated_at: 2026-07-23 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Hierarchical Implicit Q‑Chunking (HiQC), an offline goal‑conditioned reinforcement learning method that tackles the curse of horizon by combining latent high‑level planning with low‑level action chunking. The authors show that conditioning the low‑level critic on extended action sequences yields unbiased k‑step value backups, compressing the effective horizon at both planning and execution levels. Empirically HiQC outperforms standard hierarchy and flat chunking on the OGBench suite, especially on long‑horizon navigation tasks.

## Key Takeaways
- The low‑level critic is conditioned on temporally extended action sequences, which provides unbiased k‑step value backups that reduce horizon error.  
- HiQC’s dual decomposition compresses the effective horizon at both planning and execution levels, leading to a tighter theoretical bound than flat chunking or standard hierarchy alone.  
- Empirical results demonstrate HiQC achieves the highest aggregate performance on OGBench, with notable gains on long‑horizon tasks such as humanoid‑giant navigation.

## Context
Offline goal‑conditioned RL seeks to learn policies from static datasets without online interaction, a promising approach for large‑scale deployment. However, long‑horizon tasks suffer from error accumulation that limits performance. Hierarchical methods attempt to mitigate this by breaking tasks into subgoals, but often introduce myopic low‑level controllers that exacerbate the problem.

## Implications
HiQC offers a practical framework for scaling offline RL to long‑horizon problems without sacrificing value stability, which is crucial for robotics and autonomous systems. Practitioners can adopt this chunking strategy to design more reliable policies from limited data, reducing the need for costly online training.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20834v1)
