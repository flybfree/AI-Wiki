---
title: How Benchmarks and Evaluation Protocols Shape Conclusions in Provenance-Based Intrusion Detection
url: http://arxiv.org/abs/2608.01454v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_19-27-49Z_HowBenchmarksandEvaluationProtocolsShapeConclusion.md
generated_at: 2026-08-03 23:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper re‑evaluates provenance‑based intrusion detection systems on public datasets to show how benchmark choices and evaluation protocols affect reported performance. It finds that alerting success can diverge from investigation utility and that many system claims rely on lexical novelty rather than richer provenance modeling. The analysis highlights the importance of temporal test separation, checkpoint calibration, and semantic signal quality when interpreting results.

## Key Takeaways
- Alerting success often diverges from investigation utility because systems may generate alerts without providing sufficient process‑level context for forensic work.
- Simple allowlists based on executable names match or exceed learned baselines on key operating‑point metrics, indicating that performance gains stem from lexical novelty rather than deeper provenance analysis.
- Semantic signal quality measured by feature completeness and field entropy explains why only some datasets reveal architectural differences between models.

## Context
Provenance‑based intrusion detection systems aim to reconstruct the origin of malicious activity for forensic investigation. Their evaluation is typically limited to standard benchmark metrics that do not capture real‑world investigative needs, leading to misleading conclusions about model capabilities.

## Implications
Researchers and practitioners must consider both dataset provenance and evaluation protocol when assessing PIDS performance. Ignoring these factors can result in overstated confidence in system effectiveness, undermining trust in security solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01454v1)
