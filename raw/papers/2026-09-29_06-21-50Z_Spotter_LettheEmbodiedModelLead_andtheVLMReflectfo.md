---
title: Spotter: Let the Embodied Model Lead, and the VLM Reflect for It
published: 2026-09-29T06:21:50Z
authors: Long Li, Qichao Zhao, Yue Yang, Fan Xu, Zhe Wang, Alan Wee-Chung Liew, Chao Qu, Heng Tao Shen, Shirui Pan
url: http://arxiv.org/abs/2609.36808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spotter: Let the Embodied Model Lead, and the VLM Reflect for It

## Abstract
Current embodied models do not respond to their own failures, although what just went wrong could inform a small adjustment on the next attempt, the kind of reflection behind the gains of thinking in language models. We test whether they can repair a known error, which requires producing a correction and judging whether it is right. Stopped at a failure and allowed to retry, they seldom repair it through their own randomness or from a language description of the error, and best-of-N selection cannot pick the successful candidate after a failure. We attribute this to training only on successful demonstrations and to inputs too narrow to show what went wrong, and conclude that reflection must come from a vision-language model (VLM), which takes in far more information, such as the episode history and text, and is more general. Prior VLM-led work has the VLM plan every step and invoke the embodied model as a tool, placing the VLM on the critical path. We propose Spotter, which reverses the roles: the embodied model leads and executes continuously, while the VLM runs in parallel, monitors through a lightweight local screener, intervenes only when an error is detected, reflects on and corrects it, and returns control. We run Spotter with Qwen and with GPT as the VLM, and both improve the embodied models; with GPT, Spotter improves Cosmos Policy and $π_{0.5}$ by 5.6 and 7.5 percentage points on RoboCasa, and raises $π_{0.5}$ from 47.2% to 57.0% on the Hard setting of RoboTwin 2.0 and from 53% to 83% on a real robot. Because the VLM steps in only when an error is confirmed, a successful episode with Qwen takes only 13 to 16 s longer than with the embodied model alone and about 70% less time than with a VLM-led baseline using the same model. Our code is available at https://github.com/zqc3117/Spotter.

## Metadata
- **Published**: 2026-09-29T06:21:50Z
- **Authors**: Long Li, Qichao Zhao, Yue Yang, Fan Xu, Zhe Wang, Alan Wee-Chung Liew, Chao Qu, Heng Tao Shen, Shirui Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36808v1)