---
title: Training Language Models to Cooperate with Inference-Time Controllers
published: 2026-07-26T17:44:33Z
authors: Moumita Choudhury, Vanshaj Khattar, Jing Liu, Toshiaki Koike-Akino, Ankush Chakrabarty, Shlomo Zilberstein, Ye Wang
url: http://arxiv.org/abs/2607.23771v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Language Models to Cooperate with Inference-Time Controllers

## Abstract
Large language model (LLM) performance increasingly depends not only on the base model, but also on the inference-time controller used to organize reasoning. Existing post-training methods, however, typically optimize for a single fixed interaction pattern, despite real deployments relying on diverse controllers such as Chain-of-Thought, self-consistency, debate, planning, and verification pipelines. This creates a training--deployment mismatch and limits transfer to new workflows. We introduce CALM (Controller-Aware Language Models), a post-training framework that explicitly places controllers in the training loop. We formulate controller-aware post-training as multi-task reinforcement learning over controller-induced interaction protocols, where controllers are compositions of reusable local reasoning modules. This structure also induces a module-level decomposition of mixed-controller training under a turn-level GRPO objective, enabling a systematic study of controller and module-aware training strategies. We evaluate CALM on held-out controller compositions and broader controller shifts, showing that controller-aware post-training improves generalization across inference-time workflows beyond single-controller optimization.

## Metadata
- **Published**: 2026-07-26T17:44:33Z
- **Authors**: Moumita Choudhury, Vanshaj Khattar, Jing Liu, Toshiaki Koike-Akino, Ankush Chakrabarty, Shlomo Zilberstein, Ye Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23771v1)