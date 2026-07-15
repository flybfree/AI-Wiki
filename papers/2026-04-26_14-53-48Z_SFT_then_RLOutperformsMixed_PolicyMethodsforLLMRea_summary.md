---
title: "Summary: 2026-04-26_14-53-48Z_SFT_then_RLOutperformsMixed_PolicyMethodsforLLMRea.md"
date: 2026-04-26
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-04-26_14-53-48Z_SFT_then_RLOutperformsMixed_PolicyMethodsforLLMRea.md


**Source**: [Original Paper](http://arxiv.org/abs/2604.23747v1)
Saved: 2026-05-07 22:29
Source: 2026-04-26_14-53-48Z_SFT_then_RLOutperformsMixed_PolicyMethodsforLLMRea.md
Model: None

---

## Summary
Recent mixed-policy optimization methods for LLM reasoning that interleave or blend supervised and reinforcement learning signals report improvements over the standard SFT-then-RL pipeline. We show that numerous recently published research papers rely on a faulty baseline caused by two distinct bugs: a CPU-offloaded optimizer bug in DeepSpeed that silently drops intermediate micro-batches during gradient accumulation (affecting multiple downstream frameworks including TRL, OpenRLHF and Llama-Factory), and a loss aggregation bug in OpenRLHF that incorrectly weights per-mini-batch losses. Together they suppress SFT performance, with the optimizer bug accounting for most of the gap and the loss aggregation bug contributing a smaller additional effect.

## Key Takeaways
- Recent mixed-policy optimization methods for LLM reasoning that interleave or blend supervised and reinforcement learning signals report improvements over the standard SFT-then-RL pipeline.
- We show that numerous recently published research papers rely on a faulty baseline caused by two distinct bugs: a CPU-offloaded optimizer bug in DeepSpeed that silently drops intermediate micro-batches during gradient accumulation (affecting multiple downstream frameworks including TRL, OpenRLHF and Llama-Factory), and a loss aggregation bug in OpenRLHF that incorrectly weights per-mini-batch losses.
- Together they suppress SFT performance, with the optimizer bug accounting for most of the gap and the loss aggregation bug contributing a smaller additional effect.

## Context
Recent mixed-policy optimization methods for LLM reasoning that interleave or blend supervised and reinforcement learning signals report improvements over the standard SFT-then-RL pipeline.

## Implications
Even a truncated variant with just 50 RL steps outperforms mixed-policy methods on math benchmarks while using fewer FLOPs.

## Original Reference
- Title: SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning
- Authors: Alexis Limozin, Eduard Durech, Torsten Hoefler, Imanol Schlag, Valentina Pyatkin
- Published: 2026-04-26T14:53:48Z
- URL: http://arxiv.org/abs/2604.23747v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-04-26_14-53-48Z_SFT_then_RLOutperformsMixed_PolicyMethodsforLLMRea.md

[[SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning]]