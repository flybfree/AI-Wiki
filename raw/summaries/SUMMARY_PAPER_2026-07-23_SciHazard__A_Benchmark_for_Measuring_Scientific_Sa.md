---
title: SciHazard: A Benchmark for Measuring Scientific Safety Risks with Decomposed Harm Scoring
url: http://arxiv.org/abs/2607.18665v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_03-25-01Z_SciHazard_ABenchmarkforMeasuringScientificSafetyRi.md
generated_at: 2026-07-23 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SciHazard, a benchmark that measures scientific safety risks by decomposing harm scores into severity, refusal behavior, and response-level risk. It evaluates 31 frontier LLMs on 2400 hazardous questions across 12 disciplines, showing deep research agents have higher harmfulness than standard models. The DeHarm-Score framework improves expert agreement by 90.17% over baselines.

## Key Takeaways
- SciHazard provides a real-world grounded dataset of 2400 hazardous and 600 oversafety questions spanning twelve scientific fields, grounding queries in regulated entities and documented failure scenarios.
- The DeHarm-Score decomposition separates query hazard severity, model refusal behavior, and response-level risk into Executability and Net-new risk components using dynamic checklists and retrieval‑augmented verification.
- Deep research agents achieve a 32.3% higher mean DeHarm-Score than standard LLMs, highlighting autonomous agents as a critical blind spot in current safety defenses.

## Context
Current AI safety benchmarks often use templated queries that do not reflect actual scientific hazards and rely on LLM‑as‑a‑Judge without domain grounding. This limits their ability to detect real risk. The need for domain‑aware, comprehensive evaluation is therefore urgent as models are deployed in regulated research environments.

## Implications
For researchers, SciHazard offers a standardized metric to assess safety across disciplines, guiding model selection and prompting design. For industry, the finding that autonomous agents pose higher risks calls for stricter safeguards before deployment of self‑learning scientific tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18665v1)
