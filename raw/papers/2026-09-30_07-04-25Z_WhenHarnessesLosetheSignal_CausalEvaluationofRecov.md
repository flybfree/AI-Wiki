---
title: When Harnesses Lose the Signal: Causal Evaluation of Recovery in LLM Agents
published: 2026-09-30T07:04:25Z
authors: Shuyao Xiao, Shengling Wang, Xuan Chen, Ke Chao, Ming Cui, Feifei Qian, Chaoyang Mei, Fanlin Meng, Ziming Yu, Junxi Yin
url: http://arxiv.org/abs/2610.00372v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Harnesses Lose the Signal: Causal Evaluation of Recovery in LLM Agents

## Abstract
Large language model agents rely on external harnesses to pass information between the model and its environment and to recover from execution errors. Yet recovery is usually judged only by average task success. This hides an important tension. The same operation can rescue a failing trajectory or disrupt one that would otherwise succeed. We frame recovery as a causal decision problem. Starting from the same execution state, we compare what happens with and without recovery, separate rescue from harm, and study how the value of recovery changes over time. We then introduce the Causal Intervention Router (CIR), a lightweight policy that uses information available before recovery to decide when intervention is worthwhile. On long-horizon ALFWorld tasks with Qwen3-14B, CIR raises success from 70.33% to 73.33%, a gain of 3.00 percentage points. It leaves all evaluated trajectories with correct observations untouched. Additional controls show that the benefit of recovery cannot be explained solely by the new observation returned by the environment. These results provide a practical way to evaluate recovery and apply it selectively.

## Metadata
- **Published**: 2026-09-30T07:04:25Z
- **Authors**: Shuyao Xiao, Shengling Wang, Xuan Chen, Ke Chao, Ming Cui, Feifei Qian, Chaoyang Mei, Fanlin Meng, Ziming Yu, Junxi Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00372v1)