---
title: EvoIn: Bridging Evolution and Internalization for Agent Fine-Tuning
url: http://arxiv.org/abs/2609.35290v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_14-36-01Z_EvoIn_BridgingEvolutionandInternalizationforAgentF.md
generated_at: 2026-09-29 01:49
model: qwen3.6-35b-a3b
---

## Summary
EvoIn is a fine-tuning framework that bridges evolution and internalization to enhance agent decision-making without relying on evolved harnesses at inference time. By analyzing execution traces, evolving new procedures in the harness for validation, rewriting them into self-contained reasoning traces, and fine-tuning the model, EvoIn enables agents to internalize improved logic. Evaluations show significant gains of 10.9 points in-domain and 9.2 points out-of-domain, with generalization to unseen tasks and other model families.

## Key Takeaways
- EvoIn evolves decision-making procedures by temporarily instantiating them in the harness to validate effectiveness, then guides the agent to generate reasoning traces that reflect these improved decisions before rewriting and fine-tuning the model on self-contained versions that remove explicit harness references.
- The framework consistently improves pass rates by 10.9 points in-domain and 9.2 points out-of-domain across diverse benchmarks, demonstrating that internalized decision procedures generalize well to unseen tasks and apply broadly

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35290v1)
