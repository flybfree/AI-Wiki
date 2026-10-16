---
title: TRACER: Trajectory-Aware Tool Retrieval for LLM Agents
url: http://arxiv.org/abs/2610.21267v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_05-00-58Z_TRACER_Trajectory_AwareToolRetrievalforLLMAgents.md
generated_at: 2026-10-15 22:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
TRACER is a retrieval front-end system designed to reduce token costs and improve tool-selection accuracy for LLM agents that must choose from large tool registries. By indexing observed tool-call sequences in a trie structure and ranking likely continuations using a learned blend of empirical and contextual priors, TRACER dramatically shrinks the number of tools exposed to the model at each step. The system demonstrates consistent accuracy improvements across multiple environments and models while cutting input token usage by up to 80%.

## Key Takeaways
- TRACER achieves a 4.7-point improvement in GPT-5.4's tool-selection accuracy on a mixed retail-and-telecom τ² environment while reducing input tokens per step by 80%, exposing only 5 out of 128 available tools to the model at any given step. This demonstrates that trajectory-aware retrieval can simultaneously boost accuracy and slash computational overhead.
- In autonomous full-turn execution, TRACER matches GPT-5.4's full-registry task success rate while consuming 61% fewer input tokens per step, showing that the retrieval approach does not sacrifice end-to-end task completion performance despite drastically narrowing the candidate tool set.
- Across six distinct environments and four different language models, TRACER outperforms full-registry selection in 21 of 24 model-environment pairs, with average accuracy gains ranging from 6 to 10 points. The three cases where it trails do so by at most 2.2 points, indicating robust generalizability across diverse agent configurations.

## Context
As LLM-based agents are deployed in increasingly complex enterprise settings involving dozens or hundreds of available tools, the naive strategy of injecting an entire tool registry into the model's prompt becomes prohibitively expensive in token costs and can degrade selection quality as registries grow. TRACER addresses this scalability bottleneck by treating tool selection as a sequential prediction problem, leveraging the structure of past tool-call trajectories to anticipate which tools are most likely needed next. This positions the work at the intersection of retrieval-augmented generation, agent planning, and efficient inference, a rapidly growing area as agentic AI moves from research prototypes to production deployments.

## Implications
For practitioners building agentic systems, TRACER offers a practical path to scaling tool-using agents without proportional increases in inference cost, which is critical for production deployments where token budgets and latency constraints are hard operational limits. The consistent gains across multiple models and environments suggest that trajectory-aware retrieval is a model-agnostic technique that could be integrated into existing agent frameworks. For the broader field, the paper highlights that understanding the sequential structure of tool usage—rather than treating each selection as an independent classification—can unlock both efficiency and accuracy improvements, pointing toward future work on learned priors and failure-mode analysis in agentic tool use.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21267v1)
