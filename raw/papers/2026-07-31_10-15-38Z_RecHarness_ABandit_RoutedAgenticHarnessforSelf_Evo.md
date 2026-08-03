---
title: RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Recommender Systems
published: 2026-07-31T10:15:38Z
authors: Haoran Ling, Yuecheng Li, Zeyu Song, Jing Yao, Shuwen Kang, Chi Lu, Wenjin Wu, Peng Jiang
url: http://arxiv.org/abs/2607.29241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Recommender Systems

## Abstract
Optimizing modern recommender models still depends heavily on engineers manually iterating over architectural, objective, and training-strategy changes. While LLM-based agents can automate this trial-and-error process, allowing the LLM to both select modification directions and generate concrete hypotheses often leads to unstable search under limited experiment budgets. Inspired by the above challenge, we propose RecHarness, a Bandit-Routed Agentic Harness for automated recommender model optimization. RecHarness separates the optimization process into two steps: a bandit router selects the next modification direction according to historical validation feedback, while the LLM generates a concrete optimization hypothesis and executable code edit within the selected direction. To sustain long-horizon exploration, RecHarness uses a jump-basin mechanism to activate a structural-jump arm when local edits stagnate. Across multiple recommendation tasks, datasets, and model backbones, RecHarness achieves more stable performance improvements and uses limited trial budgets more effectively than LLM-reasoning search. During a 7-day online A/B test on a large-scale short-video advertising platform, the selected candidate improves ADVV by 2.084%, Revenue by 0.534%, and Exposure by 0.559%. Code is available at https://github.com/6lyc/RecHarness.

## Metadata
- **Published**: 2026-07-31T10:15:38Z
- **Authors**: Haoran Ling, Yuecheng Li, Zeyu Song, Jing Yao, Shuwen Kang, Chi Lu, Wenjin Wu, Peng Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29241v1)