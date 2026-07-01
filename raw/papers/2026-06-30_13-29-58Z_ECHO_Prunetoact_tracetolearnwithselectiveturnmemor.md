---
title: ECHO: Prune to act, trace to learn with selective turn memory in agentic RL
published: 2026-06-30T13:29:58Z
authors: Zijun Xie, Binbin Zheng, Enlei Gong, Jihua Liu, Yuyang You, Lingfeng Liu, Jiayao Tang, Guanqun Zhao, Aoqi Hu, Zeyu Chen
url: http://arxiv.org/abs/2606.31650v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ECHO: Prune to act, trace to learn with selective turn memory in agentic RL

## Abstract
Long-horizon language agents must repeatedly interact with tools, accumulate evidence, and make decisions under bounded context windows. Existing context-management methods make such rollouts feasible by truncating distant history, folding past turns into summaries, or selecting compact memory states. However, these breakthroughs introduce two coupled limitations. First, as the number of turns grows, historical observations are progressively removed or collapsed into compressed states, making it harder for the policy to reuse fine-grained evidence. Second, once the original turns are no longer source-addressable, outcome-based RL loses an explicit path for aligning policy updates with the evidence that supported a successful final answer. To this end, we propose ECHO, a selective turn-memory framework that jointly addresses history collapse and traceable learning through source-indexed reconstruction. Specifically, ECHO compresses each completed environment turn into a compact memory record, reconstructs bounded policy contexts by selecting from these records, and reuses the selected source indices to route positive outcome credit to the evidence and selection actions that support successful answers. On BrowseComp-Plus, ECHO reaches 43.4% held-out accuracy, outperforming GRPO (28.9%) and the rolling-summary baseline SUPO (36.1%), while using fewer turns and lower trajectory volume than SUPO (Figure 1). Additionally, the trained policy improves zero-shot generalization across multi-objective QA, code generation, and deep information-seeking benchmarks on both dense and MoE backbones.

## Metadata
- **Published**: 2026-06-30T13:29:58Z
- **Authors**: Zijun Xie, Binbin Zheng, Enlei Gong, Jihua Liu, Yuyang You, Lingfeng Liu, Jiayao Tang, Guanqun Zhao, Aoqi Hu, Zeyu Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.31650v1)