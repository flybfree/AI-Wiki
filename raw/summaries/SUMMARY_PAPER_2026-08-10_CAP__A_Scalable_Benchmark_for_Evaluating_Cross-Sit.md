---
title: CAP: A Scalable Benchmark for Evaluating Cross-Site Browser Agents with Complex Actions and Perception
url: http://arxiv.org/abs/2608.08392v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_01-08-19Z_CAP_AScalableBenchmarkforEvaluatingCross_SiteBrows.md
generated_at: 2026-08-10 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CAP, a scalable benchmark designed to evaluate cross‑site browser agents on complex web tasks that involve rich user interfaces and dynamic visual perception. The authors demonstrate that state‑of‑the‑art agents achieve low success rates, highlighting perception as a major bottleneck in real‑world browsing.

## Key Takeaways
- CAP creates 420 tasks across 108 websites and 24 domains using a decomposition‑and‑recomposition pipeline that captures both functional operations and visual requirements.  
- The benchmark reveals that agents struggle with multi‑site workflows where actions must be coordinated across different sites, exposing gaps in their perception capabilities.  
- Fine‑grained diagnosis of each task component is possible because tasks are broken down into structured site cards, allowing precise feedback on failures.

## Context
The rapid deployment of large language models as autonomous agents has driven interest in evaluating their ability to perform human‑like web interactions. Existing benchmarks focus mainly on end‑to‑end success metrics, ignoring the nuanced challenges of UI manipulation and visual understanding that are common in multi‑site tasks.

## Implications
CAP provides a more realistic evaluation framework that can guide research toward agents capable of handling complex, perception‑intensive web workflows. Practitioners and developers will benefit from the fine‑grained insights CAP offers to improve agent design and reliability in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08392v1)
