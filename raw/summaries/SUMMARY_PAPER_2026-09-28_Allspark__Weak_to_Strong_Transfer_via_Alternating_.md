---
title: Allspark: Weak to Strong Transfer via Alternating Chain of Thought
url: http://arxiv.org/abs/2609.32913v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_20-05-21Z_Allspark_WeaktoStrongTransferviaAlternatingChainof.md
generated_at: 2026-09-28 21:57
model: qwen3.6-35b-a3b
---

## Summary
Allspark introduces a weak-to-strong transfer framework that enables reasoning improvements learned by a small model to benefit larger models without requiring expensive rollouts from the strong model during training. By using alternating chains of thought where a weak teacher communicates with a frozen partner, the method allows text-based steering across different model families and tokenizers at inference time. Experiments demonstrate accuracy gains in math and reasoning tasks, including successful transfer to external models like Kimi and Nemotron, highlighting a viable path for efficient knowledge distillation via chain-of-thought interaction.

## Key Takeaways
- Allspark addresses the high cost of large-model reinforcement learning by training a weak teacher alongside a frozen copy of itself; the two alternate reasoning segments while the frozen model generates the final answer, effectively eliminating the need for costly strong-model rollouts during the training phase.
- The framework relies on text-based communication between models, which allows a trained weak teacher to steer stronger students from different model families and with distinct tokenizers at inference time without requiring parameter updates or architectural modifications to either model.
- Empirical evaluations across Qwen for math/reasoning and Inkling for ARC-AGI-2 reveal accuracy improvements in both within-family and cross-family settings, including transfers to Kimi and Nemotron, while emphasizing the need to analyze the tradeoff between accuracy gains and inference token consumption.

## Context
As frontier language models become increasingly capable, reinforcement learning has emerged as a key method for enhancing reasoning, yet the computational expense of generating rollouts

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32913v1)
