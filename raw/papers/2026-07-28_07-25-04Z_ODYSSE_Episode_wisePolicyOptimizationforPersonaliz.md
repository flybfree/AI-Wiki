---
title: ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning
published: 2026-07-28T07:25:04Z
authors: Jiaqi Zhang, Tong Chen, Junliang Yu, Quoc Viet Hung Nguyen, Hongzhi Yin
url: http://arxiv.org/abs/2607.25369v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning

## Abstract
Agentic systems have rapidly advanced in their ability to interact with real-world environments, leverage external tools, and provide services for users. However, unlike natural-world tasks that assume well-defined instructions, human-centered scenarios are characterized by ambiguous requests that lead to large, open-ended solution spaces. Decoding users' personalized preferences is therefore essential for narrowing the candidate solution space. This introduces a new challenge, personalized agentic reasoning, which requires agents to jointly interact with both users and environments to deliver personalized services. In this paper, we present ODYSSE, a Reinforced Fine-Tuning (RFT) framework for personalized agentic reasoning. At its core, ODYSSE proposes Episode-wise GRPO (ESPO), a novel extension of Group Relative Policy Optimization (GRPO) designed to address long action horizons and strong cross-step dependencies in personalized agentic reasoning. Rather than optimizing individual steps independently, ESPO introduces an episode-level reward mechanism together with episodic advantage estimation, enabling upstream evidence to effectively guide downstream personalized decisions and allowing agents to progressively resolve ambiguous user requests across multiple interaction steps. We further propose an episodic batch sampler that groups actions from the same episode into unified training batches, facilitating coherent optimization under ESPO. We evaluate ODYSSE on realistic long-horizon personalized GUI reasoning tasks. Experimental results demonstrate that ODYSSE consistently outperforms both specialist and general-purpose LVLMs, highlighting its effectiveness for personalized agentic reasoning.

## Metadata
- **Published**: 2026-07-28T07:25:04Z
- **Authors**: Jiaqi Zhang, Tong Chen, Junliang Yu, Quoc Viet Hung Nguyen, Hongzhi Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25369v1)