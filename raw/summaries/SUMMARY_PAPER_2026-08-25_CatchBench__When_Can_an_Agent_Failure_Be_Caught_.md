---
title: CatchBench: When Can an Agent Failure Be Caught?
url: http://arxiv.org/abs/2608.22808v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_05-09-41Z_CatchBench_WhenCananAgentFailureBeCaught.md
generated_at: 2026-08-25 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CatchBench, a benchmark that evaluates how well an agent can detect its own failures by probing three information states—pre‑run configuration (PRE), live trace prefix (LIVE), and post‑run trace (POST). It finds that most existing benchmarks only score one of these states, leading to incomplete insights. The study reports that 72 out of 118 entrant methods are scored, with a rule that flags every capability declared after the first, achieving perfect F1 on one configuration source.

## Key Takeaways
- CatchBench scores methods across three distinct telemetry points (PRE, LIVE, POST) rather than fixing one state.  
- The benchmark includes seven task contracts each with its own labels and metrics, separating evidential from Gold‑derived mechanism diagnostics.  
- A rule that ignores all names and permissions flags every capability after the first, achieving perfect F1 on a single configuration source, indicating that scores may reflect corpus construction rather than reasoning quality.

## Context
CatchBench addresses a gap in AI safety research where failure detection is limited to post‑hoc analysis of trace logs. By evaluating agents at multiple stages, it provides a more holistic view of robustness and helps identify when failures are observable versus hidden. This aligns with the growing need for transparent, reproducible benchmarks that can be applied across diverse model families.

## Implications
For practitioners, CatchBench offers a framework to test whether failure detection mechanisms rely on superficial shortcuts rather than genuine understanding. For industry, it encourages building audits that consider pre‑run configuration and live trace data, not just final outputs, fostering more reliable AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22808v1)
