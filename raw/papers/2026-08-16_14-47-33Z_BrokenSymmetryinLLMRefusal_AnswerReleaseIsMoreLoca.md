---
title: Broken Symmetry in LLM Refusal: Answer Release Is More Local Than Refusal Restoration
published: 2026-08-16T14:47:33Z
authors: Yiqi Liu, Yang Wang, Songxin Wang, Chenghao Xiao, Chenghua Lin
url: http://arxiv.org/abs/2608.15772v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Broken Symmetry in LLM Refusal: Answer Release Is More Local Than Refusal Restoration

## Abstract
When a language model refuses to answer a prompt, it is unclear whether the correct answer is erased from its internal representations, or merely suppressed at the output layer. We investigate this mechanism using a controlled withhold setting, which yields perfectly matched answering and refusal trajectories for bidirectional activation patching. We uncover a causal asymmetry in intervention locality under matched causal interventions, which we term broken symmetry. Even when a model generates a clean refusal, the correct answer remains linearly recoverable from its hidden states. Furthermore, releasing this withheld answer is a highly local operation, requiring only a single-position patch. Conversely, the reverse operation is not equally local: reimposing suppression requires broader interventions across multiple positions, and assembling a coherent refusal sequence is more difficult still. We further demonstrate that while an average answer-to-refusal displacement vector marks the geometric difference between these states, it fails to act as a reliable, reversible linear control toggle between behaviours. Taken together, our findings show that refusal does not function as a simple symmetric switch. For safety and auditing, this implies that probe recoverability can overestimate true behavioural control, and locating refusal-relevant directions does not reliably grant the ability to steer a model from answering to coherent refusal.

## Metadata
- **Published**: 2026-08-16T14:47:33Z
- **Authors**: Yiqi Liu, Yang Wang, Songxin Wang, Chenghao Xiao, Chenghua Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15772v1)