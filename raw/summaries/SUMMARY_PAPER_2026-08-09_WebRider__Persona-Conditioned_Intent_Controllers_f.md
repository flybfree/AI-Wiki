---
title: WebRider: Persona-Conditioned Intent Controllers for Live-Web Assistance
url: http://arxiv.org/abs/2608.06704v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_02-00-49Z_WebRider_Persona_ConditionedIntentControllersforLi.md
generated_at: 2026-08-09 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces WebRider, a system that treats delegating web tasks as an intent contract and audits both policy adherence and user experience. It shows that current agents finish tasks but violate policies often. The authors propose a hierarchical controller to enforce constraints throughout the browsing process.

## Key Takeaways
- A strong controller can complete 99.2% of tasks yet only honor all policy constraints in 38.8% of cases, indicating final answer does not guarantee fidelity.
- WebRider formalizes delegation as an intent contract that records goals, constraints, evidence obligations, answer form, and persona controls.
- The guarded middle interface provides a high‑quality training signal; an 8B action‑policy model trained on it outperforms executable‑only baselines under the same controller.

## Context
Live‑web assistants must respect user policies beyond delivering correct answers. Existing evaluations ignore these constraints, leading to systems that appear functional but behave inconsistently with user intent. This paper addresses that gap by treating policy as a formal contract and auditing both internal state and visible output.

## Implications
For practitioners, WebRider offers an auditable framework for building trustworthy web agents that can be judged by humans and improved via data‑driven training. In industry, it enables safer deployment of live‑web assistants where compliance is critical, reducing liability from policy violations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06704v1)
