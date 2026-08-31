---
title: What Makes Agent Memory Useful for Reliable Unanswerable Question Handling?
published: 2026-08-28T05:00:28Z
authors: Chuanyuan Tan, Junjie Yu, Yuxin Wang, Yining Zheng, Xipeng Qiu, Wenliang Chen
url: http://arxiv.org/abs/2608.27924v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Makes Agent Memory Useful for Reliable Unanswerable Question Handling?

## Abstract
Reliable handling of unanswerable questions (UAQs) is critical for trustworthy LLM-based agents. Although memory is widely used in agent systems, its role in reliable UAQ handling remains unclear. We present a systematic study of agent memory for UAQ handling under a unified agentic RAG framework, evaluating four representative memory methods across three UAQ-related datasets and two base models.   We find that memory can improve UAQ performance in some settings, but such gains are selective rather than universal and remain fragile under dataset shift. Interestingly, cross-model memory reuse is often more feasible than cross-dataset transfer, suggesting that shifts in answerability patterns pose a greater challenge to memory reuse than changes in the base model itself. We further find that UAQ gains are more strongly preserved through decision guidance than through trajectory shaping, and that memory effectiveness depends strongly on representation. In particular, procedural and rule-based memories often provide the most reliable support for UAQ handling, while memory composition is most effective when procedural guidance is combined with complementary behavioral signals. Overall, our findings suggest that reliable UAQ memory depends less on storing larger amounts of experience and more on preserving transferable behavioral guidance.

## Metadata
- **Published**: 2026-08-28T05:00:28Z
- **Authors**: Chuanyuan Tan, Junjie Yu, Yuxin Wang, Yining Zheng, Xipeng Qiu, Wenliang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27924v1)