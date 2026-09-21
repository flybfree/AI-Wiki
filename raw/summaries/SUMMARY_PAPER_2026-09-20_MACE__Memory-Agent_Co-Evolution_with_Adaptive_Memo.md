---
title: MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems
url: http://arxiv.org/abs/2609.21533v1
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-18_09-25-06Z_MACE_Memory_AgentCo_EvolutionwithAdaptiveMemoryGra.md
generated_at: 2026-09-20 20:11
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces MACE, a memory-agent co-evolution framework designed to enhance the reliability and efficiency of multi-agent systems by dynamically adapting how agents store and retrieve collaborative experiences. By organizing dependencies into functional units and using feedback from task outcomes to refine these memories, MACE significantly outperforms existing baselines across multiple benchmarks.

## Key Takeaways
- Grouping dependencies into functional memory units improves the retention of action prerequisites and required outputs compared to unstructured data storage methods.
- Connecting these units into a graph structure facilitates the retrieval of complex, joint requirements necessary for multi-step tasks by preserving the relationships between different components.
- The research identifies that agent preferences for specific information formats (such as instructions versus checklists) vary depending on the task type, necessitating an adaptive approach rather than static scoring systems.
- MACE utilizes a "MemGoG" structure to represent relationships like support, conflict, and repair, allowing agents to navigate complex dependencies more effectively within a set memory budget.
- The system employs a feedback loop that updates memory scores based on actual task outcomes, enabling the model to learn which information combinations are most effective for specific goals over time.

## Context
As multi-agent systems become increasingly complex, one of the primary hurdles is ensuring agents can effectively reuse past experiences without being overwhelmed by irrelevant data or losing critical context. This research addresses a fundamental challenge in long-term memory management and knowledge transfer within collaborative AI environments, moving toward more autonomous and self-correcting systems.

## Implications
For practitioners and researchers, MACE suggests that building better multi-agent systems requires more than just larger context windows; it requires sophisticated, feedback-driven mechanisms for organizing and retrieving information dynamically. This work paves the way for more robust AI applications capable of refining their own internal knowledge bases based on real-world performance and success metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.21533v1)
