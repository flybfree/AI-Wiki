---
title: Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models
published: 2026-07-30T15:59:51Z
authors: Sara Candussio, Daniel Scalena, Luca Bortolussi, Elisabetta Fersini, Malvina Nissim, Gabriele Sarti
url: http://arxiv.org/abs/2607.28707v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models

## Abstract
Entropy-based pruning has been proposed as an effective method for compressing Chain-of-Thought (CoT) reasoning with negligible accuracy loss. We test the robustness of low- and high-entropy CoT step selection methods across various models and reasoning tasks, showing that entropy offers no advantage over random pruning in any evaluated setting. Moving from sentences to tokens, we then show that retaining low-entropy tokens seems effective only on mathematical benchmarks. We find this is due to the inherently low-entropy nature of numeric tokens, which also convey semantic content in such problems. Finally, we demonstrate that patching a subset of a few CoT tokens with their original activations recovers near-perfect full-trace performance, providing causal evidence that task information is not concentrated in a small set of CoT tokens identifiable by heuristics, but rather distributed across the full reasoning chain.

## Metadata
- **Published**: 2026-07-30T15:59:51Z
- **Authors**: Sara Candussio, Daniel Scalena, Luca Bortolussi, Elisabetta Fersini, Malvina Nissim, Gabriele Sarti
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28707v1)