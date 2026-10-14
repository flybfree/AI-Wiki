---
title: APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation
published: 2026-10-13T10:14:23Z
authors: Sirui Zhang, Fangyun Wei, Dong Chen, Jinjing Zhao, Yitong Wang, Yunuo Chen, Baining Guo, Zheng-Jun Zha
url: http://arxiv.org/abs/2610.18097v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation

## Abstract
Post-training is crucial for improving text-to-image models, yet existing pipelines typically rely on manually curated training data and fixed training distributions. We introduce APT (Agentic Post-Training), a fully automated framework that adaptively post-trains a base model according to its evolving capability profile. APT coordinates three agents to construct evaluation sets from user requirements, diagnose model-specific strengths and failure modes, and generate reinforcement learning data with an adaptive prompt distribution that emphasizes underperforming capabilities. By repeatedly evaluating, diagnosing, and updating the generator, APT lets the current model's behavior shape its next training tasks, forming a feedback loop inspired by recursive self-improvement. For general-purpose settings without user-specified evaluation scenarios, we further develop an evaluation harness that enables broad and diverse evaluation set generation. Experiments across multiple base models, benchmarks, and generation architectures demonstrate that APT is model-agnostic, benchmark-agnostic, architecture-agnostic, and fully automated.

## Metadata
- **Published**: 2026-10-13T10:14:23Z
- **Authors**: Sirui Zhang, Fangyun Wei, Dong Chen, Jinjing Zhao, Yitong Wang, Yunuo Chen, Baining Guo, Zheng-Jun Zha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18097v1)