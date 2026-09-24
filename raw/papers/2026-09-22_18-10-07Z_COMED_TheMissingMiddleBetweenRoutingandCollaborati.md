---
title: COMED: The Missing Middle Between Routing and Collaboration in Multi-LLM Inference
published: 2026-09-22T18:10:07Z
authors: Norah Alballa, Wenxuan Zhang, Salma Kharrat, Fares Fourati, Zafar Ayyub Qazi, Mohamed Elhoseiny, Marco Canini
url: http://arxiv.org/abs/2609.26913v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# COMED: The Missing Middle Between Routing and Collaboration in Multi-LLM Inference

## Abstract
No single Large Language Model (LLM) is uniformly reliable across queries, motivating multi-model inference systems that either route among models or combine their outputs. However, routing stops after selecting an initial model, while dense collaboration invokes peers on every query. We show that collaboration is non-monotonic: peers can recover failures that no model solves alone, but can also corrupt initially correct answers. We introduce COMED (Controlled Model Escalation for Multi-LLM Deliberation), a post-anchor controller for selective cross-model collaboration. COMED uses anchor self-consistency, router margin, and a lightweight peer probe to accept confident answers, verify ambiguous cases, and escalate only when collaboration is likely beneficial. We formalize this trade-off with a rescue-harm decomposition showing that selective collaboration improves when rescued errors outweigh collaboration-induced harms. Across medical, scientific, and general reasoning benchmarks, COMED improves fixed and routed anchors in all 16 open-weight settings, with gains up to +10.7 percentage points on MedQA while invoking fewer models and using fewer decoded tokens than dense collaboration. On HLE with frontier models, COMED improves GPT-5.5 from 23.1% to 28.1%, outperforming dense collaboration and achieving the best results.

## Metadata
- **Published**: 2026-09-22T18:10:07Z
- **Authors**: Norah Alballa, Wenxuan Zhang, Salma Kharrat, Fares Fourati, Zafar Ayyub Qazi, Mohamed Elhoseiny, Marco Canini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.26913v1)