---
title: MCPDisCo: Seesaw-Mitigated Tuning for MCP-Native Agents
url: http://arxiv.org/abs/2610.14956v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_14-29-23Z_MCPDisCo_Seesaw_MitigatedTuningforMCP_NativeAgents.md
generated_at: 2026-10-13 21:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MCPDisCo introduces an ecosystem-scale reinforcement learning framework designed to train agents that natively interact with the Model Context Protocol (MCP) ecosystem across 70 servers and 527 tools spanning six domains. The paper identifies and addresses a critical joint-learning failure mode called the "reasoning-tool seesaw," where improving reasoning quality inadvertently degrades tool-use performance and vice versa, and proposes token-masked reward attribution combined with bidirectional gradient surgery to decouple these competing objectives. The framework achieves higher task success rates while using fewer chain-of-thought tokens, and demonstrates monotone generalization gains on out-of-distribution benchmarks including MCP-Atlas and GAIA.

## Key Takeaways
- The Thought-Markov Decision Process (Thought-MDP) explicitly models internal reasoning as a first-class state alongside routing, execution, and termination decisions, enabling the agent to learn a hierarchy of capabilities from tool-format skills up to cross-server composition rather than treating reasoning as a hidden or auxiliary process.
- The reasoning-tool seesaw is identified as a fundamental interference problem in joint optimization: gradients from the reasoning objective and the tool-action objective conflict in shared model parameters, causing one capability to improve at the expense of the other. MCPDisCo mitigates this through token-masked reward attribution, which assigns supervision signals only to the appropriate reasoning or action token spans, and bidirectional gradient surgery, which surgically removes conflicting gradient components from both objectives before updating shared parameters.
- Training on real-server, long-horizon interactions across 70 MCP servers and 527 tools in six domains, combined with evaluation on the out-of-distribution MCP-Atlas benchmark and the GAIA benchmark, confirms that the learned behavior generalizes beyond the specific training server distribution and transfers to broader agentic tasks, with model weights and implementation made publicly available.

## Context
The Model Context Protocol has emerged as a standardized substrate for the agentic web, enabling heterogeneous services to expose capabilities through a common interface. However, training agents to navigate this ecosystem requires mastering a capability hierarchy that spans individual tool formatting, server-level transfer, and multi-server composition—challenges that existing fine-tuning and RL approaches handle poorly when reasoning and tool-use objectives are jointly optimized. MCPDisCo addresses this gap by providing the first ecosystem-scale RL training pipeline specifically designed for MCP-native agents, bridging the divide between reasoning quality and tool-execution reliability that has plagued prior agentic training methods.

## Implications
For practitioners building agentic systems on the MCP ecosystem, MCPDisCo offers a reproducible training recipe and open model weights that demonstrate agents can achieve higher task success with fewer reasoning tokens, reducing inference cost and latency in production deployments. The identification and mitigation of the reasoning-tool seesaw provides a generalizable insight for any multi-objective agentic training pipeline, suggesting that gradient surgery and token-level reward masking are transferable techniques beyond MCP specifically. For the broader AI research community, the framework validates that long-horizon, multi-server RL training at ecosystem scale is feasible and that learned agent behaviors can generalize to unseen servers and benchmarks, setting a foundation for more capable and efficient autonomous agents in standardized tool-use environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14956v1)
