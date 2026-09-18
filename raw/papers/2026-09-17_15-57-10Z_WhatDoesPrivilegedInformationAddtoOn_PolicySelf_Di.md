---
title: What Does Privileged Information Add to On-Policy Self-Distillation?
published: 2026-09-17T15:57:10Z
authors: XiuYu Zhang, Wei Chow, Junfeng Fang, Zhenkai Liang, Tat-Seng Chua
url: http://arxiv.org/abs/2609.20612v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Does Privileged Information Add to On-Policy Self-Distillation?

## Abstract
On-policy self-distillation (OPSD) lets a language model learn from a frozen copy of itself that sees an answer or a worked solution. Giving the teacher this extra information seems to offer the student more to learn, but how much does it add beyond distillation itself? To isolate that contribution, we construct AMPLE-Math, a reusable suite of 5,319 mathematical problems with six reasoning views that share the same answer, and compare each view with matched reference-free distillation. With a thinking-enabled teacher supervising direct-response rollouts, reference-free distillation accounts for much of Qwen3-1.7B's improvement under thinking-enabled evaluation, both in domain and on external benchmarks. Evidence for an additional reference benefit is modest in Qwen, strongest for a polished solution, whereas complete traces add two percentage points in SmolLM3-3B at step 50. These benefits depend on the student being trained. At the same checkpoint, replacing short direct-response rollouts with long thinking-enabled rollouts turns gains into losses in both families while the problems, references, and evaluation stay fixed. Teacher profiles and matched loss interventions in Qwen further show that changing token-level supervision can leave student behavior largely unchanged. Together, these findings suggest that OPSD can improve access to existing reasoning capabilities through parameters shared by direct-response and thinking-enabled inference. The value of a privileged reference is what it adds to this cross-mode transfer, not how much of the solution it reveals.

## Metadata
- **Published**: 2026-09-17T15:57:10Z
- **Authors**: XiuYu Zhang, Wei Chow, Junfeng Fang, Zhenkai Liang, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.20612v1)