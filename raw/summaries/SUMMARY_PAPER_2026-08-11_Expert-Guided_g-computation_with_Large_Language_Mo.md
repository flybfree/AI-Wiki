---
title: Expert-Guided g-computation with Large Language Models for Estimating Causal Effects on Timings: Applications to Hospital Quality Improvement
url: http://arxiv.org/abs/2608.10339v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_00-42-58Z_Expert_Guidedg_computationwithLargeLanguageModelsf.md
generated_at: 2026-08-11 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces expert‑guided g‑computation, also called egg‑computation, to estimate the causal average time saved from hospital quality improvement interventions by combining Gantt chart representations with causal DAG reasoning. Using a large language model to guide expert input for unidentifiable components, the method produces scalable estimates that align closely with human judgments in simulated and real data settings.

## Key Takeaways
- The framework links patient flow Gantt charts to causal DAGs, allowing identification of effects only when data cannot fully specify certain steps.  
- An LLM‑assisted pipeline reliably scales expert reasoning for complex interventions where traditional g‑computation would require manual graph construction.  
- In the study of eleven QI candidates at a safety‑net hospital, the model’s time‑saving estimates were highly concordant with those derived from human experts.

## Context
This work addresses a longstanding challenge in causal inference: estimating average treatment effects when interventions are hypothetical and lack historical data. By integrating qualitative expert knowledge with scalable AI tools, it demonstrates how LLMs can augment traditional statistical methods to handle complex clinical mechanisms beyond what pure data‑driven models can capture.

## Implications
Hospital administrators can now obtain evidence‑based rankings of QI proposals without extensive simulation effort, improving resource allocation and patient outcomes. The approach also offers a template for other time‑intensive domains where Gantt charts describe workflows, highlighting the broader impact of AI‑augmented causal analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10339v1)
