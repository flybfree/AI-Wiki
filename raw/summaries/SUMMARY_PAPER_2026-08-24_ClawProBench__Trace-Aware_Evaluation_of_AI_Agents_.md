---
title: ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts
url: http://arxiv.org/abs/2608.22510v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_17-09-02Z_ClawProBench_Trace_AwareEvaluationofAIAgentswithRu.md
generated_at: 2026-08-24 21:07
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces ClawProBench, a trace‑aware benchmark for evaluating AI agents on their live runtimes, demonstrating that final‑answer leaderboards often hide runtime failures. Experiments show native‑runtime tasks underperform workspace‑live tasks and that ranking metrics vary across evaluation views.

## Key Takeaways  
- The benchmark defines a full profile with live workspace and routing tasks, and a frozen holdout with JSON contracts, scoring traces via a safety‑gated formula.  
- Native‑runtime tasks score lower (0.5238) than workspace‑live tasks (0.6415), indicating runtime weaknesses are hidden in final‑answer leaderboards.  
- Pass@k‑any on holdout outperforms strict three‑trial pass, while full‑profile and holdout rankings show weak alignment.

## Context  
AI benchmarks often focus only on correctness of outputs, ignoring how agents interact with their runtimes. This limits detection of failures in evidence acquisition, routing, safety boundaries, and repeated execution, which are critical for robust deployment.

## Implications  
Practitioners must adopt trace‑aware evaluation to uncover hidden runtime issues, leading to more reliable agent deployments and better alignment between leaderboard rankings and real‑world performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22510v1)
