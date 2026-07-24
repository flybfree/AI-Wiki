---
title: The Mechanism Matters: When Knowledge Graphs Help Reinforcement Learning
published: 2026-07-21T22:43:16Z
authors: Mohammed Sameer Syed
url: http://arxiv.org/abs/2607.19616v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Mechanism Matters: When Knowledge Graphs Help Reinforcement Learning

## Abstract
Knowledge graphs (KGs) are widely used to inject prior knowledge into reinforcement learning (RL), yet the literature is dominated by single-domain, positive-result method papers, so we lack a systematic account of when KG structure helps an agent, when it is neutral, and when it hurts. We conduct a controlled study that independently varies the RL task, the injection mechanism (state features, action masking, or potential-based reward shaping), and KG quality. Using a synthetic, fully controllable KG over MiniGrid environments, we report three findings. First, on compositional sparse-reward tasks structured KG guidance improves sample efficiency and solve reliability (70% to 97% of seeds), and a shuffle control that permutes the KG's edges while preserving their count collapses the benefit toward baseline (masking p=0.0001; shaping p=0.006), so the gain is structural rather than generic regularization. Second, KG value scales with the amount of task-relevant knowledge the graph contains. Third, and most consequential, safety depends on the mechanism: soft, optimality-preserving injection benefits from correct knowledge and harmlessly ignores incorrect knowledge, whereas hard masking is brittle, forbidding essential actions when the KG is incomplete or corrupted and making a wrong KG worse than none. A UMLS-derived clinical case study on sepsis management under offline RL is a careful null, underscoring that benefits require task structure the chosen mechanism can exploit. Our results give practitioners concrete guidance on how, and how much, to trust a KG when using it to guide RL.

## Metadata
- **Published**: 2026-07-21T22:43:16Z
- **Authors**: Mohammed Sameer Syed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19616v1)