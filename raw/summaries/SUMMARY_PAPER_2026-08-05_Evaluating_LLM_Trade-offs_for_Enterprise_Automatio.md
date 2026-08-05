---
title: Evaluating LLM Trade-offs for Enterprise Automation: Lessons from Workflow Generation in a Production Enterprise Platform
url: http://arxiv.org/abs/2608.03311v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_08-18-38Z_EvaluatingLLMTrade_offsforEnterpriseAutomation_Les.md
generated_at: 2026-08-05 01:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates six large language models for generating AI‑driven workflows in a real enterprise setting, measuring structural success rates and trade‑offs such as cost and latency across 29 automation scenarios. The redesigned piecewise pipeline improves performance dramatically compared with the monolithic approach.

## Key Takeaways
- The monolithic pipeline yielded structural success rates between 31.5% and 82.8%, while most models failed on complex JSON generation.  
- Switching to a piecewise decomposition raised success rates to 74.1%–97.8% for all models, enabling smaller models like mistral‑small to reach production viability at low cost.  
- Mistral‑medium‑2505 achieved the highest structural success (96.1%) but carries a 19× higher cost than mistral‑small.

## Context
Enterprise compliance demands rapid adaptation to changing regulations, and static orchestrators cannot keep pace in hybrid cloud environments where automation must respond within seconds. This study demonstrates how LLM trade‑offs can be optimized for production workflow generation beyond typical research benchmarks.

## Implications
The findings suggest that model selection should prioritize cost efficiency over raw capability when structural validity is the primary metric, and that pipeline design can mitigate performance bottlenecks. Practitioners can adopt piecewise decomposition to build scalable, affordable automation systems without relying on expensive frontier models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03311v1)
