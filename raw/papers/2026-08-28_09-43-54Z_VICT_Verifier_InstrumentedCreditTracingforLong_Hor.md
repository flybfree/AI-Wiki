---
title: VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning
published: 2026-08-28T09:43:54Z
authors: Pengcheng Li, Zhengyang Zhang, Dongxu Zhang, Sui Huang, Shaohua Ma
url: http://arxiv.org/abs/2608.28128v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning

## Abstract
Fine-grained credit assignment is a central challenge in reinforcement learning for long horizon LLM agents. Standard objectives often train from programmatically verifiable terminal rewards by broadcasting each sparse outcome to every action in a trajectory. Existing methods typically seek finer credit from the rollout side, constructing auxiliary trajectory signals or additional comparisons to estimate action importance. Although useful, these approaches still treat the verifier that judged success as a scalar reward, discarding its internal task structure. Our key insight is that many verifiable tasks already encode the relevant checks inside their terminal verifier. We propose VICT (VerifierInstrumented Credit Tracing), a training-time interface that exposes executable or evidence backed atoms and traces them back to actions through dependency-valid proof edges. VICT redistributes group-relative advantage only along those edges, shifting credit assignment from rollout-side inference to verifierside tracing. It preserves the original terminal reward, abstains when evidence is incomplete or ambiguous, and changes only the training-time advantage tensor, requiring no learned critic, process labels, branch rollouts, or inference-time verifier access. On ALFWorld and WebShop, VICT improves substantially over outcome-only training and achieves strong performance alongside recent fine-grained credit methods; ablations rule out dense atom rewards, final-commit credit, temporal proximity, and sparsity as sufficient explanations.

## Metadata
- **Published**: 2026-08-28T09:43:54Z
- **Authors**: Pengcheng Li, Zhengyang Zhang, Dongxu Zhang, Sui Huang, Shaohua Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28128v1)