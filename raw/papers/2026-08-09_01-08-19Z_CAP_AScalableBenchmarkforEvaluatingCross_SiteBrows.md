---
title: CAP: A Scalable Benchmark for Evaluating Cross-Site Browser Agents with Complex Actions and Perception
published: 2026-08-09T01:08:19Z
authors: Zejun Xu, Taiyi Chen, Jin Li, Yongtong Gu, Qi Cheng, Aixuan Lv, Shuai Zhu, Pengfei Zhu, Kaichen Yang, Boyu Sun, Yixian Yang, Mulong Xie, Xin Liu, Dagang Li, Xiaoteng Ma, Hongru Wang
url: http://arxiv.org/abs/2608.08392v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CAP: A Scalable Benchmark for Evaluating Cross-Site Browser Agents with Complex Actions and Perception

## Abstract
Large language models are increasingly deployed as autonomous agents that interact with the web through browsers. While recent progress has been driven by benchmarks that evaluate end-to-end task success, these evaluations largely overlook two fundamental sources of difficulty in real web browsing: complex actions over rich user interfaces and visual perception of dynamically rendered content, especially in workflows that span multiple websites. We introduce CAP, a scalable benchmark for evaluating browser agents on cross-site, human-like web tasks that require non-trivial UI interactions and visual understanding. Specifically, we adopt a decomposition-and-recomposition pipeline that first abstracts each website into a structured site card capturing user-facing functions, complex execution operations, and perceptual requirements, and then recomposes these components into realistic cross-site workflows. Each task is therefore grounded in multiple specific operations on each website, enabling fine-grained diagnosis. Built on this framework, we construct 420 tasks across 108 real-world websites and 24 domains under careful quality control. Experiments on state-of-the-art browser agents using our verifiable agent-as-a-judge evaluation framework show low success rates and reveal that perception-heavy interactions remain a major bottleneck, exposing substantial gaps between current agents and real-world web browsing demands.

## Metadata
- **Published**: 2026-08-09T01:08:19Z
- **Authors**: Zejun Xu, Taiyi Chen, Jin Li, Yongtong Gu, Qi Cheng, Aixuan Lv, Shuai Zhu, Pengfei Zhu, Kaichen Yang, Boyu Sun, Yixian Yang, Mulong Xie, Xin Liu, Dagang Li, Xiaoteng Ma, Hongru Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08392v1)