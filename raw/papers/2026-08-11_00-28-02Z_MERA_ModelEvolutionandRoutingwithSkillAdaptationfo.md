---
title: MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale
published: 2026-08-11T00:28:02Z
authors: Yuhang Yao, Zeyu Wang, Wanyi Chen, Tongyun Yang, Yuhang Han, Jie Xiao, Chengke Bao, Tianyi Zhao, Lynn Ai, Eric Yang, Tianyu Shi
url: http://arxiv.org/abs/2608.10333v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale

## Abstract
LLM agents execute heterogeneous sequences of model calls within a single task: some invocations require careful reasoning, while others are structured steps such as formatting or tool-argument construction. Prior routing methods exploit this asymmetry by assigning easy invocations to a cheaper small model and difficult ones to a large model. Such policies reduce inference cost, but they leave the small model's capability unchanged, so attainable savings remain bounded by the work the student can already solve. MERA instead improves the small model itself, using a single model invocation as the unit of adaptation. In each cycle, MERA replays failed student invocations to obtain execution-verified teacher demonstrations, distills recurring procedures into an iteratively updated SkillBook, and fine-tunes a student LoRA adapter via supervised learning and optional GRPO. Routing serves as supporting machinery for deployment: the improved student is served behind a cost-calibrated router with verifier-backed fallback, and a candidate SkillBook, adapter, or router is admitted only when joint replay preserves task quality. Empirically, four-cycle adaptation raises Qwen2.5-Coder-1.5B from 28.7% to 49.7% pass on held-out HumanEval+MBPP. Under verifier-backed fallback, the deployed policy retains 88.3% pass at 60.8% of always-Luna cost. On TAU-2, a fine-tuned Qwen3.5-2B improves from 14/35 to 18/35 and matches an unadapted 4B model. These results indicate that verifier-backed multi-cycle adaptation can increase small-model capability, rather than only routing around a fixed student.

## Metadata
- **Published**: 2026-08-11T00:28:02Z
- **Authors**: Yuhang Yao, Zeyu Wang, Wanyi Chen, Tongyun Yang, Yuhang Han, Jie Xiao, Chengke Bao, Tianyi Zhao, Lynn Ai, Eric Yang, Tianyu Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10333v1)