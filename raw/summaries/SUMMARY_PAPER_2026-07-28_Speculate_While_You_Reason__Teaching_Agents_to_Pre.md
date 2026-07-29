---
title: Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL
url: http://arxiv.org/abs/2607.25816v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_15-00-10Z_SpeculateWhileYouReason_TeachingAgentstoPredictThe.md
generated_at: 2026-07-28 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a self‑speculating agent that simultaneously performs tasks and predicts its next tool call using joint reinforcement learning, eliminating the need for separate speculator models. Experiments on Qwen3‑4B and Qwen3.5‑4B show average next‑tool‑call Hit@1 improvements from 44.1 to 61.2 and 48.9 to 66.3 while keeping task success unchanged.

## Key Takeaways
- The self‑speculating agent can predict its next tool call with high accuracy by leveraging its own rollouts.
- Joint RL alternates updates between the agent and speculator, reusing prefix KV cache to avoid latency.
- Performance gains are observed in both Qwen3‑4B (44.1→61.2) and Qwen3.5‑4B (48.9→66.3).

## Context
Large language model agents often experience long delays while waiting for tool call results, and existing speculators typically rely on separate draft models or cached traces that are poorly aligned with the deployed agent’s behavior.

## Implications
Unifying the agent and speculator within a single model simplifies deployment and reduces technical complexity. This approach offers higher efficiency in real‑time tool use and can be adopted across various LLM‑agent applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25816v1)
