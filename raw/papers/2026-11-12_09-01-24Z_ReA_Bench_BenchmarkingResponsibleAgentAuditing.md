---
title: ReA-Bench: Benchmarking Responsible Agent Auditing
published: 2026-11-12T09:01:24Z
authors: Zipeng Ye, Shenyu Dai, Yong Xie, Kun Wang, Jiyang Guan, Zhikai Chen, Jiaqi Weng, Jialing Tao, Hui Xue
url: http://arxiv.org/abs/2611.16493v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReA-Bench: Benchmarking Responsible Agent Auditing

## Abstract
As agents perform tasks autonomously in local and cloud environments, auditing their execution trajectories can help service providers identify risks and improve agent harnesses and foundation models. Our analysis of production and red-team trajectories shows that some risks are repeatedly missed across auditing configurations. Overall recall obscures which risks are missed and whether higher recall comes with more false positives on legitimate behavior. Existing benchmarks offer limited insight into these failures. Generated trajectories can contain inconsistent tool calls and responses, conspicuous risky actions, or repetitive attack patterns. Grouping results by risk type also makes it difficult to tell whether auditors overlooked evidence, accepted an unsupported conclusion, or lacked information needed to make a judgment.   We introduce ReA-Bench, a diagnostic benchmark for auditing responsible agent behavior. It organizes auditing challenges into six tiers: internal safety knowledge, contradictions within trajectories, evidence retrieval in long contexts, verification of sources and reasoning, indirect steering, and missing information. It includes challenging benign cases in which actions resemble risky ones but are consistent with the task and its authorization. It also provides paired trajectory versions to test whether auditors detect the same risks more reliably when the trajectory is shortened or missing information is supplied. Most samples are drawn from real production trajectories, with scenarios manually selected and adapted to preserve realistic tasks and risks that could plausibly arise during execution.

## Metadata
- **Published**: 2026-11-12T09:01:24Z
- **Authors**: Zipeng Ye, Shenyu Dai, Yong Xie, Kun Wang, Jiyang Guan, Zhikai Chen, Jiaqi Weng, Jialing Tao, Hui Xue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.16493v1)