---
title: Agentic Router: An Execution-Grounded Continual Learning Approach With Memory
published: 2026-08-10T06:53:24Z
authors: Yuxuan Chen, Rongpeng Li, Zhifeng Zhao, Yuntao Liu, Xing Xu, Honggang Zhang
url: http://arxiv.org/abs/2608.09184v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Router: An Execution-Grounded Continual Learning Approach With Memory

## Abstract
Large language model (LLM) agents provide a promising interface for command-line-based network operations, but a plausible command may still fail or introduce operational risk after execution. Existing approaches mainly focus on command generation or final configuration correctness, and do not use execution-grounded experience to jointly improve candidate coverage and action selection. We propose an execution-grounded dual-path consequence-aware agent for CLI-based SONiC operations, which generates multiple complete actions, predicts their execution consequences, and selects the final action through utility- and risk-aware reranking. The proposal-side path abstracts reusable operational lessons into retrievable guidance to improve feasible-action coverage without modifying the proposal LLM, while the selection-side path adapts the consequence predictor through session-level LoRA updates using real SSH feedback to improve conditional selection quality. Experiments over multi-turn SONiC operation sessions with different Qwen3 proposal models show that the framework improves feasible-action coverage and top-1 execution success, and that the two adaptation paths provide complementary gains over interaction.

## Metadata
- **Published**: 2026-08-10T06:53:24Z
- **Authors**: Yuxuan Chen, Rongpeng Li, Zhifeng Zhao, Yuntao Liu, Xing Xu, Honggang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09184v1)