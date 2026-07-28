---
title: A Few Words Go a Long Way: Language Guided Robot Policy Synthesis
published: 2026-07-26T18:00:02Z
authors: Daphne Chen, Archit Ritesh Jain, Eric Goossen, Emma Romig, Michael Murray, Nick Walker, Maya Cakmak
url: http://arxiv.org/abs/2607.23784v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Few Words Go a Long Way: Language Guided Robot Policy Synthesis

## Abstract
While vision-language-action models have demonstrated impressive zero-shot manipulation capabilities, they remain fundamentally black box policies that are difficult to interpret, adapt, or correct when they inevitably fail. In this work, we propose ARCHITECT, a framework that treats robot policy acquisition as an interactive program synthesis task. ARCHITECT leverages the reasoning capabilities of LLM coding agents to synthesize modular robot programs that utilize a suite of perception and control tools. Unlike end-to-end models where distribution shift leads to unpredictable, cascading failures, our modular architecture allows users to isolate failures and localize feedback at the level of abstraction required. We introduce an iterative process where a human supervisor provides natural language corrections to steer the policy. These corrections are grounded in the policy code by program execution traces and distilled into a persistent skill library, a form of long-term in-context learning which enables the agent to accumulate a repertoire of reusable, interpretable behaviors. In a benchmark evaluation on a Franka Panda robot, ARCHITECT outperforms state-of-the-art VLA models and program synthesis baselines on complex, long-horizon tasks, including articulated object manipulation and cloth folding. Our results demonstrate that the synthesized skill library enables the system to transfer to novel tasks with decreasing human intervention, providing a steerable and data-efficient alternative to black-box robot learning. Website: https://robo-architect.github.io/

## Metadata
- **Published**: 2026-07-26T18:00:02Z
- **Authors**: Daphne Chen, Archit Ritesh Jain, Eric Goossen, Emma Romig, Michael Murray, Nick Walker, Maya Cakmak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23784v1)