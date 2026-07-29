---
title: A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain
url: http://arxiv.org/abs/2607.25415v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_08-10-25Z_AControlSystem_aDataset_andaRecipeforMakingFrozenL.md
generated_at: 2026-07-28 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a framework that treats the components of an LLM agent harness as a small action space and learns an online policy using reinforcement learning to optimize them. Experiments compare this learned control system with static baselines across tool-use, code generation, and retrieval tasks on two model providers. The approach yields more adaptable agents while maintaining verifiability.

## Key Takeaways
- The authors treat the harness as a fixed human‑legible action space and learn a policy over it using ε‑greedy contextual bandits and REINFORCE, scoring actions with a multi‑objective reward that includes task success, verifier score, compliance, cost, latency, and unsupported‑claim penalties. This enables sample‑efficient online optimization without code search.
- They use DSPy as both the context assembler and baseline, evaluating across three verifiable domains (tool‑use workflows, HumanEval, HotpotQA) on local Ollama and AWS Bedrock models, showing that learned policies outperform static prompts in adaptability and compliance.
- The release includes harness‑control‑system code, a cross‑domain task suite, full training logs with reward decomposition, and a deployment recipe for applying the system to any organization’s domain and verification setup.

## Context
Recent advances in large language model agents have focused on building complex workflows that combine prompting, tool use, memory, and planning. However, these systems often rely on opaque self‑modifying code or costly search loops, making them hard to audit and deploy. This paper introduces a more transparent, sample‑efficient reinforcement learning approach that learns the harness directly.

## Implications
For practitioners, this method provides an auditable way to improve LLM agents without exposing proprietary model APIs, supporting responsible AI deployment. For industry, it lowers the barrier to domain‑specific agent customization while preserving verification and cost constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25415v1)
