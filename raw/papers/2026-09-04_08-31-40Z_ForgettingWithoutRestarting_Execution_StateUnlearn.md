---
title: Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents
published: 2026-09-04T08:31:40Z
authors: Chao Yao, Yangbo Wei, Zhen Huang, Junhong Qian, Chenle Chen, Shaoqiang Lu, Chen Wu, Lei He
url: http://arxiv.org/abs/2609.04875v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents

## Abstract
Long-running LLM agents are stateful: beyond the transcript they accrete compressed summaries, plaintext memory, pending tool plans, and, under every serving API, a KV cache. Yet today's "forget" operations delete a plaintext memory record and stop, leaving every artifact derived from the revoked information intact. We formalize execution-state unlearning: after a forget request, the agent must behave as if it had never observed the target. Modeling the runtime as a deterministic transition system, we prove that the pre-target trajectory prefix is shared with this counterfactual world for free, that the post-target suffix is irreducibly tainted without token-level attribution, and that exact unlearning requires at least $T-τ+1$ recomputed transitions, where $τ$ is the target's injection step. Provenance-Guided Selective Replay attains this bound as a cross-layer contract spanning prompt, compressed memory, and cache: a provenance graph locates the injection point, checkpoint restoration reduces to cropping the KV cache, and sanitized replay regenerates the counterfactual suffix. Audited with elicitation, stochastic, and string-free behavioral tests across three agent suites, nine baselines, and three model families, memory deletion leaves leakage unchanged, instruction-based forgetting collapses under elicitation (Leak@probes = 1.00), and source redaction still acts on a revoked preference in 80% of episodes, while selective replay is indistinguishable from a full reset at up to 9x fewer recomputed tokens.

## Metadata
- **Published**: 2026-09-04T08:31:40Z
- **Authors**: Chao Yao, Yangbo Wei, Zhen Huang, Junhong Qian, Chenle Chen, Shaoqiang Lu, Chen Wu, Lei He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04875v1)