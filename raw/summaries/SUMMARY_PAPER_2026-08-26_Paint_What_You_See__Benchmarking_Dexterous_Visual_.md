---
title: Paint What You See: Benchmarking Dexterous Visual Tool Use in Multimodal Agents
url: http://arxiv.org/abs/2608.25417v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_06-19-28Z_PaintWhatYouSee_BenchmarkingDexterousVisualToolUse.md
generated_at: 2026-08-26 20:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces EASEL, a benchmark that evaluates multimodal agents’ ability to perform dexterous visual tool use by having them paint a canvas to match a reference image. The study finds that current models struggle with reconstruction accuracy and exhibit unstable closed‑loop execution, while semantic tasks such as region annotation and path planning reveal sharp capability boundaries. Training on the curated EASEL‑Data improves performance, with the 9B model beating the base by about 6.3% and ranking third among all tested agents.

## Key Takeaways
- Reconstruction similarity drops to 0.40–0.54 at low levels, indicating poor visual evidence interpretation.
- Trajectory diagnostics show early saturation or post‑peak degradation, revealing closed‑loop instability in tool use.
- Semantic tasks exhibit sharp precision limits, especially in annotation and path planning.

## Context
The shift from static QA to agentic environments demands agents that can translate visual input into precise physical actions. EASEL addresses a gap where visual evidence directly controls execution parameters, highlighting the need for benchmarks that capture fine‑grained control rather than coarse UI interaction.

## Implications
For industry practitioners, EASEL provides a realistic test of whether multimodal models can reliably guide tools, influencing design of assistive and robotic systems. Practitioners should prioritize closed‑loop stability and visual reconstruction before deploying such agents in production workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25417v1)
