---
title: Foundation Agents Meet Agentic Deep Research: Evidence-Grounded Clinical Code Forecasting
url: http://arxiv.org/abs/2608.17075v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_19-24-57Z_FoundationAgentsMeetAgenticDeepResearch_Evidence_G.md
generated_at: 2026-08-18 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ICD-Deepresearch, a workflow that combines EHR foundation models with medical search and code semantics to forecast which ICD codes will appear at the next patient visit. On benchmark datasets it achieves higher precision and recall than existing local methods while physicians rate its retrieved documents as more useful than standalone GPT-5 or Medical Deep Research approaches.

## Key Takeaways
- The system generates candidate transitions by linking patient evidence, external clinical relations, and exact code semantics within a fixed top‑K budget.  
- It uses SparseEHR to create an EHR Prior that initiates two bounded research expansion rounds and supplements them with GPT‑5 Direct Forecast candidates.  
- Physicians rate 51% and 68% of the retrieved documents useful, outperforming standalone GPT‑5 web search (22%/39%) and Medical Deep Research (32%/41%).

## Context
The work addresses a prospective multi‑label prediction problem in clinical documentation where future diagnoses are unknown. It highlights how integrating structured EHR models with generative language models can improve evidence retrieval for medical AI tasks.

## Implications
For clinicians, ICD-Deepresearch offers a more reliable and useful diagnostic forecast than current tools, potentially reducing unnecessary follow‑up visits. For the industry, it demonstrates that combining foundation models with domain‑specific knowledge yields better performance in real‑world healthcare data challenges.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17075v1)
