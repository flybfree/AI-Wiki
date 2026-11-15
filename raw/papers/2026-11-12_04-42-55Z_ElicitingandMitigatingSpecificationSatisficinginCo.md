---
title: Eliciting and Mitigating Specification Satisficing in Coding Agents
published: 2026-11-12T04:42:55Z
authors: Ruixin Wang, Tianyi Zhang
url: http://arxiv.org/abs/2611.16289v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Eliciting and Mitigating Specification Satisficing in Coding Agents

## Abstract
Coding agents often fail to meet all requirements in the task description. In some of these failures, the agent considers an implementation choice that meets a requirement, but later decides to commit to another one that does not meet the requirement for a reason it finds acceptable. We call this specification satisficing. It is challenging to identify and mitigate specification satisficing because the agent accepts such choices for its own reasons, and existing self-correction methods are biased toward them. We propose SatisFix, which guides a coding agent to report these choices and their reasons, and then check each choice against the task description. We evaluate SatisFix on DeepSWE and SWE-bench Pro with five LLMs as backbones and two different agent frameworks, and compare it with three self-correction methods. SatisFix improves the pass@1 of the base agent by an average of 5.09% on DeepSWE and 7.06% on the hard subset of SWE-bench Pro. On DeepSWE, it outperforms the best baseline by 3.98%. Our ablation study shows that both steps of SatisFix contribute to the improvement.

## Metadata
- **Published**: 2026-11-12T04:42:55Z
- **Authors**: Ruixin Wang, Tianyi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.16289v1)