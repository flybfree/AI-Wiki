---
title: PASTABench: Proactive Assessment of Sequential Trajectories for Agent Safety
published: 2026-09-23T14:34:45Z
authors: Jiapeng Sun, Yujin Zhou, Han Zhu, Pengcheng Wen, Jiayi Zhou, Sirui Han, Yike Guo
url: http://arxiv.org/abs/2609.28197v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PASTABench: Proactive Assessment of Sequential Trajectories for Agent Safety

## Abstract
As Large Language Models (LLMs) evolve into autonomous agents that alter real-world states, ensuring operational safety across multi-step workflows has become a critical challenge. While recent work has moved beyond single-turn evaluation toward multi-turn paradigms, key limitations persist: step-level methods treat actions in isolation, missing how risks accumulate, while trajectory-level evaluations operate post-hoc, offering no opportunity for timely intervention. To address these limitations, we formalize Decoupled Proactive Safety Monitoring along three dimensions: whether to intervene, when to intervene, and what the risk is. We introduce PASTABench, a benchmark of 1,139 multi-turn trajectories spanning 5 risk categories and 13 subcategories. We further propose the Optimal Intervention Window (OIW), anchored by annotated Earliest-Signal and Trigger turns, to quantify intervention timeliness. Evaluation of 16 LLMs reveals that proactive intervention remains largely unsolved, with the best model achieving only 40.74% optimal-timing interventions. Fine-grained diagnosis further uncovers pervasive lexical overfitting: competitive safety scores of smaller models mask keyword hypersensitivity rather than genuine risk comprehension, as their proactive capability largely collapses once hazard vocabulary is neutralized.

## Metadata
- **Published**: 2026-09-23T14:34:45Z
- **Authors**: Jiapeng Sun, Yujin Zhou, Han Zhu, Pengcheng Wen, Jiayi Zhou, Sirui Han, Yike Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28197v1)