---
title: AutoCompact: Learning When to Compact Context in Long-Horizon Coding Agents
url: http://arxiv.org/abs/2610.02163v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_17-54-34Z_AutoCompact_LearningWhentoCompactContextinLong_Hor.md
generated_at: 2026-10-01 23:02
model: qwen3.6-35b-a3b
---

## Summary
AutoCompact introduces a reinforcement learning framework that enables coding agents to autonomously determine when and how to compact their context during long-horizon software engineering tasks, ensuring efficient state management without context overflow. By training the agent via supervised fine-tuning on corrected trajectories followed by joint optimization of coding and compaction policies, the method significantly enhances performance across diverse evaluation benchmarks. Experimental results demonstrate absolute improvements of 9.2% on SWE-bench Verified and 5.0% on SWE-PolyBench Verified, maintaining robustness across varying inference budgets and context window constraints.

## Key Takeaways
- The training pipeline employs a judge-based data collection mechanism where the base agent's compaction decisions, summaries, and post-compaction actions are reviewed; flawed outputs are replaced with corrected versions to ensure trajectories continue effectively, providing high-quality data for supervised fine-tuning before reinforcement learning optimization.
- AutoCompact achieves substantial performance gains over the base model, yielding absolute pass rate improvements of 9.2% on SWE-bench Verified and 5.0% on SWE-PolyBench Verified, with these benefits consistently observed across all evaluated inference budgets regardless of computational constraints.
- The approach demonstrates exceptional adaptability to context window limitations, functioning seamlessly within a 256K context window that never overflows while also effectively managing a constrained

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02163v1)
