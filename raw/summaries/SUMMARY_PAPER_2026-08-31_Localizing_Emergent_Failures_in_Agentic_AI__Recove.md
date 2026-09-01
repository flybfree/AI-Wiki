---
title: Localizing Emergent Failures in Agentic AI: Recovering Minimal Repair Families via Counterfactual Replay
url: http://arxiv.org/abs/2608.29228v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_12-34-08Z_LocalizingEmergentFailuresinAgenticAI_RecoveringMi.md
generated_at: 2026-08-31 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of identifying minimal repair families in agentic AI systems where failures stem from interactions among multiple large language model agents. By introducing Minimal Repair Family Recovery (MRFR) and a method called Graph‑Constrained Joint Replay (GCJR), the authors recover all inclusion‑minimal event sets that restore task success within a size bound, achieving perfect family exact match on benchmark tests while cutting average replay calls by over half.

## Key Takeaways
- MRFR defines a formal framework to capture all minimal repair families whose counterfactual replay can bring an agentic AI system back to success, respecting a declared size limit.  
- GCJR slices failure‑relevant events from an execution dependency graph, builds graph‑feasible singleton and pair candidates, and verifies them through paired clean replays, guaranteeing exactness within the specified graph domain.  
- On 90 in‑scope cases from a 120‑DAG benchmark, GCJR matches exhaustive search results (1.000 Family Exact Match) yet reduces mean replay calls from 56.3 to 25.3 (a 55.1% reduction), and on a four‑agent LLM pilot it cuts calls from 21.0 to 10.0, demonstrating that single‑event replays miss jointly necessary repairs.

## Context
Agentic AI systems increasingly rely on coordinated actions among multiple large language models, making failure analysis complex due to joint dependencies. Traditional pointwise attribution methods fail to capture these interactions, leading to incomplete repair strategies. This work contributes a systematic approach to recover minimal repair families, addressing a gap in fault‑diagnosis and system robustness.

## Implications
For practitioners developing multi‑agent AI pipelines, the paper offers a scalable method to pinpoint exact repair sets without exhaustive search, reducing model call overhead and improving reliability. Industry adoption could enhance deployment resilience, lower operational costs, and provide clearer failure narratives for continuous learning loops.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29228v1)
