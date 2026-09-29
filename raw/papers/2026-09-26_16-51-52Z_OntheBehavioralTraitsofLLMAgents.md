---
title: On the Behavioral Traits of LLM Agents
published: 2026-09-26T16:51:52Z
authors: Haokai Zhao, Jie Gao, Yunze Xiao, Xintao Wang, Weihao Xuan, Aditya Joshi, Mark Dredze, Jen-tse Huang
url: http://arxiv.org/abs/2609.32776v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Behavioral Traits of LLM Agents

## Abstract
Users increasingly describe different AI agents as distinct colleagues to work with. AI personality research aims to quantify such impressions by attributing human-like "traits" to agents. However, existing measures fall short: models' self-reports (S-data) diverge from their actual behavior, while informant ratings from LLM judges (I-data) are costly to scale and cover few everyday scenarios. In this paper, we propose A-B-D to infer traits bottom-up from behavioral data (B-data), namely how agents act on their environment and communicate with users, as recorded in existing trajectories. From 345,667 real-world trajectories spanning 80 models, 12 tasks, and 50 harnesses, we extract 318 candidate features that capture both the actions an agent takes at each step (functional) and the language accompanying them (linguistic). We retain only features that show instance-level stability, cross-task consistency, and model discriminability. Factor analysis of the remaining 79 features uncovers six stable, model-attributable factors, two functional and four linguistic. For example, Kimi-K3 exhibits the most planfulness, whereas GPT-5.5 and GPT-5.6 are the least energetic. Moreover, we quantify the "knowledge-action gap" in the wild: these factors correlate only weakly with self-reported Big Five scores, even for conceptually matched pairs such as extroversion and energetic (r = 0.07, p = 0.58). Our work offers a new lens for understanding AI personality, with implications for users, developers, and researchers from both computer science and social science.

## Metadata
- **Published**: 2026-09-26T16:51:52Z
- **Authors**: Haokai Zhao, Jie Gao, Yunze Xiao, Xintao Wang, Weihao Xuan, Aditya Joshi, Mark Dredze, Jen-tse Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32776v1)