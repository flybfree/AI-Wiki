---
title: Measurement-Driven Sub-Network Selection for On-Premise Retrieval-Augmented Factory Agents
url: http://arxiv.org/abs/2609.02760v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_16-00-05Z_Measurement_DrivenSub_NetworkSelectionforOn_Premis.md
generated_at: 2026-09-02 23:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of fitting large language models to on‑premise factory assistants, showing that model size does not reliably correlate with answer quality after adaptation. The authors propose a selection framework that evaluates sub‑networks based on judged retrieval‑augmented performance and on‑device throughput, using a supernetwork trained via sandwich‑style in‑place distillation for efficient deployment.

## Key Takeaways
- General capability drops almost linearly with parameter count, yet retrieved answer quality remains stable across compressed models.  
- Deployment decisions must balance size, speed, and quality under a configurable memory budget, as optimizing any single metric sacrifices the others.  
- The sandwich‑style in‑place distillation reduces extraction loss to 13.7 % of the unpruned model’s quality, bringing it back within 4.6 %, while allowing the same assistant to run on three edge tiers using only 1.3–5 watts standby.

## Context
The work highlights a growing need for AI agents that operate locally in resource‑constrained environments such as manufacturing floors, where bandwidth and power are limited. By decoupling model capacity from performance, it aligns with trends toward efficient inference and edge computing.

## Implications
Practitioners can now deploy high‑quality retrieval‑augmented assistants without sacrificing speed or memory constraints, enabling scalable AI integration across diverse factory equipment. This approach reduces the cost of customizing large models for each device while preserving conversational utility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02760v1)
