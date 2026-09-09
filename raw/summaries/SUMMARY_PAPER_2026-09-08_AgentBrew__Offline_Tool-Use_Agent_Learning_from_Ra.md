---
title: AgentBrew: Offline Tool-Use Agent Learning from Raw Real-World Trajectories
url: http://arxiv.org/abs/2609.05837v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-05_03-04-23Z_AgentBrew_OfflineTool_UseAgentLearningfromRawReal_.md
generated_at: 2026-09-08 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces AgentBrew, an offline framework that learns tool‑use policies directly from a single batch of raw interaction trajectories without needing task verifiers or iterative rollouts. The method reconstructs aligned instructions retroactively and uses PMI‑based credit assignment to weight policy updates, achieving strong performance gains over existing approaches.

## Key Takeaways
- AgentBrew extracts training signals from noisy real‑world trajectories by inferring the underlying instruction for each trajectory and assigning per‑action credits via pointwise mutual information.  
- The framework improves Qwen3‑32B by +8.7 Accuracy and +9.7 Score on average across three MCP applications, outperforming both larger models and rejection sampling.  
- Offline learning can recover useful supervision that filtering‑based methods discard, demonstrating the value of fine‑grained credit weighting.

## Context
Training large language models for real‑world tool use typically relies on costly simulator interactions or explicit task definitions, which are often unavailable in production settings. AgentBrew’s ability to work with a single batch of raw data reduces reliance on expensive simulation infrastructure and simplifies deployment pipelines.

## Implications
The results suggest that fine‑grained offline learning can deliver competitive performance without sacrificing scalability, encouraging industry adoption where real‑world interaction budgets are limited. Practitioners may integrate AgentBrew into existing LLM tool‑use systems to enhance efficiency while minimizing additional compute costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05837v1)
