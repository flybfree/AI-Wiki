---
title: LAGO: Language Agents with Reusable Growing Options
published: 2026-10-14T09:12:47Z
authors: Yuran Wu, Mengkang Hu, Qionglin Qiu, Fanqing Meng, Qiguang Chen, Yuhang Zhou, Qiudan Zhang, Xu Wang
url: http://arxiv.org/abs/2610.19843v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LAGO: Language Agents with Reusable Growing Options

## Abstract
Long-horizon tasks expose a weakness of monolithic tool-use loops: one agent must decompose, execute, and verify a task within a single trajectory. We introduce LAGO, which treats specialized language agents as reusable temporally extended options. A meta-agent retrieves options from a persistent library or spawns new ones, dispatches sub-tasks, verifies results, and admits successful novel options. The library grows across tasks without updating model weights. On 500 SWE-bench Verified tasks, frozen Qwen3.5-35B-A3B in both roles resolves 58.6% under single-attempt evaluation with the official Docker evaluator. On a fixed 150-task subset, we re-run mini-SWE-agent, Terminus 2, and LAGO with the same policy, temperature, task IDs, and evaluator; their resolve rates are 49.3%, 57.3%, and 60.3%, respectively. Cross-model experiments provide evidence consistent with a role for decomposition quality. A 50-task component ablation finds four fewer resolved tasks without decomposition, two fewer with shuffled reused content, and six fewer without the library. These results support reusable agent-options as a practical abstraction for task streams, while leaving component-level causality task- and model-dependent.

## Metadata
- **Published**: 2026-10-14T09:12:47Z
- **Authors**: Yuran Wu, Mengkang Hu, Qionglin Qiu, Fanqing Meng, Qiguang Chen, Yuhang Zhou, Qiudan Zhang, Xu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19843v1)