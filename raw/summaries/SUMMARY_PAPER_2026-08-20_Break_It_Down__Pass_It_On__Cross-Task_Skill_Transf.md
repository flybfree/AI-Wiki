---
title: Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents
url: http://arxiv.org/abs/2608.20274v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_17-12-08Z_BreakItDown_PassItOn_Cross_TaskSkillTransferinLLMA.md
generated_at: 2026-08-20 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how skills induced by LLM agents transfer between tasks and identifies factors that affect reliability. It finds that subtask-level skill induction and text-based skills generally improve performance, while task-level and code-based skills often degrade it. A novel skill utility score combining specificity and abstractness predicts success.

## Key Takeaways
- Task-level skill induction typically reduces an agent’s performance below its no‑memory baseline because the induced skill is too narrow or mismatched to the new task.
- Subtask-level skill induction generally raises performance above the baseline, indicating that skills derived from finer-grained substeps are more adaptable and useful across tasks.
- Text-based skills transfer better than code-based ones, suggesting that natural language representations of skills are more effective for cross‑task reuse.

## Context
LLM agents aim to accumulate reusable capabilities by storing skills from completed tasks, a strategy that could reduce training costs and improve generalization. However, the effectiveness of skill transfer remains uncertain due to variability in how skills are encoded and retrieved. This study provides empirical insight into which induction methods produce skills that generalize well across diverse tasks.

## Implications
For practitioners developing autonomous agents, this work offers a lightweight diagnostic (skill utility score) that can be computed from skill descriptions alone, allowing early assessment of whether stored skills will aid future tasks. It also guides method design: focusing on subtask-level and text-based induction is likely to yield more reliable skill transfer, informing safer deployment of memory‑augmented agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20274v1)
