---
title: HydroAgent: Formalizing Forecaster Expertise into Skill-Orchestrated Flood Forecasting Workflows
url: http://arxiv.org/abs/2607.23983v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_04-18-36Z_HydroAgent_FormalizingForecasterExpertiseintoSkill.md
generated_at: 2026-07-27 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HydroAgent, a skill-orchestrated agent that integrates large language models into flood forecasting workflows. It shows that embedding explicit expert rules improves forecast accuracy and decision support. The framework achieves high correlation with observed peaks across multiple LLMs in the South Yamhill River basin.

## Key Takeaways
- Prior judgment captures observed peak flow within 5% tolerance for most events, demonstrating strong alignment between expert intuition and model output.
- Guided scheme selection using a high-baseline library further improves key geometric error by up to 0.154, enhancing both simulated peak flow and flood volume predictions.
- All five LLMs execute the workflow with comparable judgment accuracy ranging from 40% to 80%, highlighting moderate performance variation.

## Context
Operational flood forecasting relies on tacit expert knowledge that is hard to codify or audit. Traditional AI methods improve prediction but often ignore rule‑based checkpoints linking model outputs to warnings. This paper addresses the gap by formalizing those checkpoints within a structured agent framework, showing how explicit skill boundaries can guide language models toward reliable decisions.

## Implications
The results suggest that integrating human expertise into AI pipelines can produce auditable and reproducible flood forecasting tools. Practitioners may adopt HydroAgent to streamline workflows, reduce decision latency, and maintain safety margins without replacing forecasters. The approach offers a scalable model for other domains where tacit knowledge meets automated systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23983v1)
