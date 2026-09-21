---
title: CoLearn: An Agentic Tutor that Learns its Learner in a Human--AI Co-Learning Loop
published: 2026-09-17T23:48:10Z
authors: Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
url: http://arxiv.org/abs/2609.21154v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoLearn: An Agentic Tutor that Learns its Learner in a Human--AI Co-Learning Loop

## Abstract
Good tutoring adapts to the individual: it tracks what a learner knows, notices why they go wrong, and asks the next question that will help most. Most deployed tutoring tools instead serve fixed item banks and treat a wrong answer as a single bit of signal. We present CoLearn, an interactive, agentic tutor that supports an iterative tutoring loop: the learner practises, and the system builds an evidence-grounded memory of the learner's mastery and misconceptions. This memory is updated as evidence accumulates and is used to generate the next personalised question. CoLearn has three components: (i) a persistent learner-state memory that updates per-topic mastery with a soft-evidence variant of Bayesian Knowledge Tracing, where a large language model acts as a continuous observation function; (ii) adaptive question generation that targets the learner's weakest topic and recurring misconceptions; and (iii) an evidence view that makes personalisation visible and testable through live progress visualisation and blind A/B comparison. In blind A/B evaluation, questions conditioned on this memory are preferred over non-personalised ones 68-69% of the time, and in persona simulations with hidden ground-truth mastery the agent's belief converges toward the learner's true mastery.

## Metadata
- **Published**: 2026-09-17T23:48:10Z
- **Authors**: Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21154v1)