---
title: Food Critic: An Agentic Visualization System for Auditable Restaurant-Safety Reasoning
url: http://arxiv.org/abs/2611.15843v1
type: paper-summary
date: 2026-11-14
source_paper: 2026-11-11_18-57-07Z_FoodCritic_AnAgenticVisualizationSystemforAuditabl.md
generated_at: 2026-11-14 21:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces Food Critic, an agentic visualization system for restaurant-safety decision support that combines public health inspection records with crowd review data to help diners assess food-safety risks. It evaluates three grounding modes—database-only ReAct, retrieval-augmented access to food-safety regulations, and ontology-guided structured reasoning—to show how externalized visual evidence can make generative-agent recommendations auditable. The main finding is that grounding agent reasoning in inspectable visual provenance improves trustworthiness and supports human-agent collaboration in high-stakes consumer choices.

## Key Takeaways
- The central contribution is an agentic visualization system rather than a generic recommendation model: Food Critic embeds generative agents into a visual interface where users can search data, invoke tools, summarize evidence, and inspect the reasoning behind recommendations.
- The paper distinguishes three grounding conditions: a database-only ReAct agent, a retrieval-augmented agent with access to food-safety regulations, and an ontology-guided agent that produces structured hypotheses and typed evidence, showing that grounding changes both answer quality and auditability.
- It frames restaurant choice as a concrete case for studying visual provenance of agent reasoning, arguing that useful answers are insufficient when users cannot verify how those answers are grounded in public health records and crowd review data.

## Context
Generative AI agents increasingly act as decision-support systems, but their outputs often lack transparent evidence chains. This paper matters because it connects agentic reasoning, retrieval, ontology, and visualization in a safety-critical consumer domain, where hallucination or unsupported claims can affect health and trust.

## Implications
For practitioners, the work suggests that restaurant-safety tools should expose inspection records, regulatory context, and crowd-review evidence as inspectable visual artifacts rather than opaque summaries. For industry and research, it provides a concrete evaluation framework for grounded GenAI decision support, human-agent collaboration, and visual interfaces that make agent reasoning auditable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.15843v1)
