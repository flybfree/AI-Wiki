---
title: Learning to Coordinate Symbolic Tools: LLM Agents for Verified Sum-of-Squares Certificates
published: 2026-07-31T22:26:45Z
authors: Bohan Chen, Shivam N. Patel, Richard Hoffmann, Sam Looi, Tony Yue Yu
url: http://arxiv.org/abs/2608.00326v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Coordinate Symbolic Tools: LLM Agents for Verified Sum-of-Squares Certificates

## Abstract
Tool calling allows large language models (LLMs) to invoke external computation during problem solving, a useful capability in various fields including AI for mathematics. We study this setting through weighted sum-of-squares (SOS) decomposition, a machine-checkable route to proving polynomial nonnegativity and hence polynomial inequalities. A candidate decomposition can be checked exactly, but finding one requires choosing among non-unique regroupings and coordinating multiple symbolic transformations. We develop an agent that combines algebraic task training, symbolic tools, and verifier-grounded optimization for this task. Rather than training only on the composite SOS task, we construct 1.35 million synthetic examples covering eight supporting polynomial tasks together with weighted-SOS decomposition. We first apply supervised fine-tuning (SFT) to direct algebra problems and simulated symbolic traces, and then use Group Relative Policy Optimization (GRPO) with task-specific symbolic rewards. The SFT corpus contains no native tool-calling messages; at evaluation, the agent uses native SymPy calls for expansion, collection, reordering, and factorization. Every final SOS answer is checked by exact expansion and coefficient comparison. On held-out, same-generator synthetic problems, the full SFT+GRPO+tools system is the strongest of four evaluated configurations, reaching 78.96% verified success on weighted SOS, compared with 44.73% for the base model with the same tools, and 91.75% macro accuracy across nine polynomial tasks. Within this controlled setting, our work provides a case study of combining domain-specific skill training, executable tools, and verifier feedback, and may inform the design of tool-calling agents in other domains with exactly checkable outputs.

## Metadata
- **Published**: 2026-07-31T22:26:45Z
- **Authors**: Bohan Chen, Shivam N. Patel, Richard Hoffmann, Sam Looi, Tony Yue Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00326v1)