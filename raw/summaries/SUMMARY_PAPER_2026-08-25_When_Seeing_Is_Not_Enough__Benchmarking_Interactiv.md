---
title: When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs
url: http://arxiv.org/abs/2608.23978v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_02-12-31Z_WhenSeeingIsNotEnough_BenchmarkingInteractiveVisua.md
generated_at: 2026-08-25 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a framework to evaluate interactive visual grounding in LVLMs by varying the amount of target information provided upfront versus acquired through dialogue across multiple contexts and protocols. It finds that current models underperform human baselines especially when no initial description is given and confidence is misaligned with accuracy.

## Key Takeaways
- Interaction can improve grounding when follow‑up questions refine or repair an incomplete target description, yet LVLMs still struggle to locate the correct visual object without guidance.
- Models exhibit poor calibration, reporting high confidence even when their predictions are incorrect, indicating a disconnect between model certainty and empirical performance.
- The difficulty is most pronounced in zero‑shot scenarios where the model must acquire all needed information through questions, suggesting proactive grounding remains challenging.

## Context
Interactive visual grounding sits at the intersection of vision, language understanding, and dialogue systems, requiring models to match textual cues with ambiguous or incomplete visual evidence. This work highlights a gap between theoretical benchmarks and real‑world multimodal interaction where models must actively seek information.

## Implications
For practitioners, the findings warn against over‑reliance on confidence scores in interactive settings and call for better calibration mechanisms. The results also underscore the need for research into proactive grounding strategies that reduce reliance on human feedback loops.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23978v1)
