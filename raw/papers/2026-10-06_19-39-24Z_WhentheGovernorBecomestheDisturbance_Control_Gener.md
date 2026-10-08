---
title: When the Governor Becomes the Disturbance: Control-Generated Disturbance and Cost-Aware Backoff in Governed Tool-Using Agents
published: 2026-10-06T19:39:24Z
authors: Veronique Ziegler
url: http://arxiv.org/abs/2610.09037v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When the Governor Becomes the Disturbance: Control-Generated Disturbance and Cost-Aware Backoff in Governed Tool-Using Agents

## Abstract
Supervisory governors can interfere with the tool-using agents they regulate. We study this possibility in a controlled file-recovery environment where increases in regulatory intensity trigger experimentally imposed tool failures. A cost-blind governor can turn these failures into persistent blocking that prevents task completion. We compare this governor with a backoff rule that reduces intervention probability using a moving average of known induced events. On a hand-coded stochastic-policy agent, the failure pattern appears under both result replacement and execution of corrupted tool arguments. For the persistent policy, adaptive backoff improves completion relative to a fixed weak governor with approximately matched intervention frequency. A Gemini 2.5 Flash experiment comprising 576 episodes across 6 tasks also shows reduced blocking and improved completion under backoff; among the tested settings, intermediate backoff strength achieves the highest observed aggregate success. These results identify an interaction between intervention cost and persistent action blocking, together with a possible mitigation. The cost mechanisms are imposed and their induced events are directly observable to the backoff rule; applicability beyond this controlled environment remains an empirical question.

## Metadata
- **Published**: 2026-10-06T19:39:24Z
- **Authors**: Veronique Ziegler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09037v1)