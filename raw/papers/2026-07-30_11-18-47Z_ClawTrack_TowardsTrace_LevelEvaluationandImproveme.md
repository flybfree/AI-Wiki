---
title: ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents
published: 2026-07-30T11:18:47Z
authors: Xingjian Wu, Xuhang Zhu, Xingchen Liu, Junlin Liu, Jianing Wang, Linsen Guo, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
url: http://arxiv.org/abs/2607.28037v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents

## Abstract
As LLM-based agents are deployed in complex, multi-step workflows, a critical evaluation gap has emerged: most existing benchmarks judge only final outcomes, unable to distinguish reliable reasoning from lucky success or attribute failures to specific process deficiencies, hindering attribution in long-horizon tasks.   In this work, we present ClawTrack, a dual-assessment benchmark that simultaneously measures what an agent achieves (Task Score) and how it achieves it (Process Score). ClawTrack comprises 320 tasks across 8 domains with 25+ deterministic mock services. A Process Grader scores each reasoning turn along four dimensions (goal alignment, efficiency, information utilization, and result verification), anchored by 12,541 task-specific rubric items. Evaluating 21 models over 16,000+ trials, we find that: (1) process scores effectively attribute success and failure to specific reasoning dimensions, filtering lucky passes invisible to outcome-only evaluation; (2) the four dimensions are complementary, with result verification as the systematic bottleneck; (3) the framework is robust to evaluator choice across different judge LLMs; and (4) process-based trajectory filtering yields consistent post-training improvements across model scales.

## Metadata
- **Published**: 2026-07-30T11:18:47Z
- **Authors**: Xingjian Wu, Xuhang Zhu, Xingchen Liu, Junlin Liu, Jianing Wang, Linsen Guo, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28037v1)