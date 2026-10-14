---
title: The Thinking Leakage in Reinforcement Learning for LLMs
published: 2026-10-09T19:43:51Z
authors: Wenxuan Zhu, Shuming Liu, Bang An, Aznaur Aliev, Bing Li, Yibo Yang, Bernard Ghanem
url: http://arxiv.org/abs/2610.14270v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Thinking Leakage in Reinforcement Learning for LLMs

## Abstract
Hybrid reasoning models such as the Qwen3 series switch between a THINK mode and a NO-THINK mode through a few chat-template tokens. A popular recipe trains such models with reinforcement learning in NO-THINK mode and reports improved reasoning performance. We provide evidence that much of this gain can be explained by thinking leakage: the gain comes largely from partially reactivating the reasoning abilities of the original model's THINK mode instead of learning enhanced reasoning behavior. We train Qwen3-1.7B, 4B, and 8B with GRPO in NO-THINK mode. As accuracy improves, responses become longer and more reflective, are increasingly judged by the original model to resemble its own thinking, and the model's internal activations shift toward its THINK mode. We then investigate at the level of weights, activations, and attention heads: scaling the RL update further elicits THINK-mode behavior and approaches THINK-mode accuracy but does not exceed it; in Qwen3-8B, replacing a low-dimensional THINK-related activation subspace of the RL-trained model with its original-model value removes most of the RL gain, and the reverse exchange transfers a considerable fraction of the gain to the original model; and the RL-induced shift passes through the attention heads that read the empty think block. We further identify a possible mechanism in the GRPO training signal: responses favored by the advantage-weighted update are more THINK-like, and a gradient step computed from this signal moves the model toward its THINK state. Thus, gains in NO-THINK mode can largely reflect reactivation of reasoning abilities already present in the original model.

## Metadata
- **Published**: 2026-10-09T19:43:51Z
- **Authors**: Wenxuan Zhu, Shuming Liu, Bang An, Aznaur Aliev, Bing Li, Yibo Yang, Bernard Ghanem
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14270v1)