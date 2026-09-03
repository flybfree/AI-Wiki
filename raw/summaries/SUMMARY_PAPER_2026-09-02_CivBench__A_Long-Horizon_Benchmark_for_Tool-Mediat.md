---
title: CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in Civilization VI
url: http://arxiv.org/abs/2609.02459v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_11-31-39Z_CivBench_ALong_HorizonBenchmarkforTool_MediatedAge.md
generated_at: 2026-09-02 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary  
CivBench is an open‑source benchmark that evaluates language model agents in a long‑horizon, tool‑mediated version of Civilization VI using the Model Context Protocol. The study shows that despite full tool access and explicit guidance, agents often under‑monitor strategically relevant state and fail to follow near‑term commitments from their own planning reflections.

## Key Takeaways  
- Agents query victory progress only every 30–75 turns instead of the recommended every 20 turns, leading to missed warning windows in seven out of twenty detectable defeats.  
- The RAG@10 metric varies between 48.2 % and 65.8 %, indicating that many agents do not execute commitments made within ten subsequent turns.  
- Both patterns persist under a shared playbook protocol, suggesting they are deviations from instruction rather than lack of capability.

## Context  
The paper contributes to the growing body of work on long‑horizon AI planning by exposing real‑world tool usage in a realistic game setting. It highlights that even advanced language models struggle with sustained strategic monitoring and execution when only textual feedback is provided, which is relevant for any system relying on iterative reasoning.

## Implications  
For practitioners developing autonomous agents, CivBench underscores the need for explicit mechanisms to enforce timely state queries and commitment follow‑through. The findings suggest that current model architectures may require architectural or training adjustments to better align with long‑term planning goals in tool‑mediated environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02459v1)
