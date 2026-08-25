---
title: Noise Floor Audit for Agent Benchmarks
url: http://arxiv.org/abs/2608.22331v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_10-00-11Z_NoiseFloorAuditforAgentBenchmarks.md
generated_at: 2026-08-24 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits measurement variability for three native tool‑call endpoints across two providers using matched AST grading at temperature zero. It finds reruns are highly deterministic with low ever‑flip fractions and high correlation scores. Semantics‑preserving prompt perturbations increase the noise floor, especially compared to rerun variations.

## Key Takeaways
- Ever‑flip fractions for reruns are 0.7%, 2.0% and 2.7% respectively across Groq endpoints and a thinking‑enabled Gemini setting.
- Mean run correlations are 0.997, 0.966 and 0.961 indicating strong consistency.
- Malformed‑output failures account for 30%, 7% and less than 1% of task failures across the same endpoints.

## Context
This work addresses a longstanding challenge in benchmarking AI agents: distinguishing measurement noise from true performance differences. By quantifying variability at temperature zero, researchers can better assess whether observed accuracy gaps stem from instability or genuine capability gaps.

## Implications
For practitioners, the findings suggest that prompt engineering and endpoint selection should consider not only average scores but also stability metrics to avoid misleading conclusions. The industry may benefit from adopting rigorous noise‑floor audits when evaluating model reliability in production.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22331v1)
