---
title: MATE: Mobile Agent Trustworthy Execution for Safe and Efficient Mobile Control
published: 2026-11-19T05:26:45Z
authors: Minsuk Jang, Hee-Seon Kim, Hui-Cheol Yu, Changick Kim
url: http://arxiv.org/abs/2611.25526v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MATE: Mobile Agent Trustworthy Execution for Safe and Efficient Mobile Control

## Abstract
Mobile agents on personal smartphones can affect private data, payments, settings, and the foreground screen. We present MATE (Mobile Agent Trustworthy Execution), an execution-layer system that controls the boundary between agent action proposals and device effects without modifying the underlying model. MATE represents each UI primitive as a structured action record that combines the instruction, target app, screen context, primitive, and action fields. Runtime Guardrail (RG) maps this record to an allow, block, or user-approval decision; Predefined Task Routing (PTR) serves recurring requests through verified routes with post-execution screen checks; and a floating interface keeps execution in a compact overlay. On MobileSafetyBench, MATE raises high-risk blocking from 29.7% to 97.0% under GPT-4o. On AndroidWorld, it reduces LLM calls by up to 6x and raises recurring-use task success to 95.7%.

## Metadata
- **Published**: 2026-11-19T05:26:45Z
- **Authors**: Minsuk Jang, Hee-Seon Kim, Hui-Cheol Yu, Changick Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.25526v1)