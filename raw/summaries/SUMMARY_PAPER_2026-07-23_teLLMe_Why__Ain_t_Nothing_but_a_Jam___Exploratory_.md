---
title: teLLMe Why (Ain't Nothing but a Jam): Exploratory Causal Analysis of Urban Driving Data
url: http://arxiv.org/abs/2607.15254v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_17-49-28Z_teLLMeWhy_Ain_tNothingbutaJam__ExploratoryCausalAn.md
generated_at: 2026-07-23 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces teLLMe, a system for exploratory causal analysis of urban driving data derived from dashcam videos. It combines causal structure learning with the PC algorithm and bootstrap stability checks to answer natural‑language questions about how treatments such as rain affect traffic density.

## Key Takeaways
- teLLMe maps user queries into structured causal queries using a schema‑aware LLM, allowing specification of treatment, outcome, and subpopulation.  
- The system returns a Causal Card summarizing effect estimates, adjustment sets, DAG support, and assumptions for each query.  
- Case studies show the tool surfaces plausible relationships involving weather, peak hours, and traffic density while making uncertainty explicit.

## Context
Urban traffic agencies handle large volumes of observational video data but lack methods to infer causal effects from it. This work provides an AI‑driven framework that can generate hypotheses without committing to definitive claims, bridging a gap in smart‑city research.

## Implications
Practitioners can use teLLMe to explore plausible causal links for evidence‑based policy and safety initiatives, supporting hypothesis generation rather than definitive conclusions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15254v1)
