---
title: Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models
url: http://arxiv.org/abs/2607.26922v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_13-53-02Z_TwoCallsBeatFiveAgents_EvaluatingMulti_AgentPipeli.md
generated_at: 2026-07-29 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates a five-role multi‑agent pipeline called Parishad running on the local Qwen2.5‑7B‑Instruct model across GSM8K and HumanEval. It finds that using JSON format reduces GSM8K accuracy to 45% due to error accumulation, while plaintext restores it to 82%. A two‑call self‑refinement V1 improves GSM8K accuracy to 86.2% with less token usage but harms HumanEval performance.

## Key Takeaways
- The JSON data format causes a significant drop in GSM8K accuracy from 75% to 45%, highlighting how communication structure impacts multi‑agent pipelines.
- Two‑call self‑refinement V1 boosts GSM8K accuracy to 86.2% while using only 7.4 times fewer tokens, showing efficiency gains possible with simple strategies.
- Task‑specific redesign V2 restores HumanEval performance at 95.1%, proving that generic multi‑agent approaches can degrade task‑specific benchmarks.

## Context
Multi‑agent LLM pipelines are often assumed to be universally beneficial, yet this study reveals that local models suffer from format‑induced errors and overfitting to complex tasks. The findings challenge the assumption that more agents always improve output quality on smaller architectures.

## Implications
For practitioners deploying 7B models locally, simpler approaches like two‑call refinement or task‑aware gating may outperform elaborate multi‑agent setups. This suggests a need for format‑aware design and evaluation tailored to specific benchmarks in the field.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26922v1)
