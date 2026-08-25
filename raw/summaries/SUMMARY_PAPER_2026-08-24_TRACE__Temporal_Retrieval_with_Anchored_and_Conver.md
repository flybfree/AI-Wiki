---
title: TRACE: Temporal Retrieval with Anchored and Convergent Evidence for Long-Horizon Video Understanding
url: http://arxiv.org/abs/2608.22516v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_17-31-43Z_TRACE_TemporalRetrievalwithAnchoredandConvergentEv.md
generated_at: 2026-08-24 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TRACE, a training-free agent that generates answers grounded in raw video clips while ensuring each answer is supported by evidence from frames covering all required events. The authors evaluate TRACE on VES‑Bench, showing it outperforms uniform decoding at low frame costs and achieves high accuracy when strict evidence coverage is enforced.

## Key Takeaways
- TRACE builds an evidence bundle round by round, stopping only when the answer stabilises across repeated passes over the same clips.
- Under a same‑backbone audit, TRACE answers 50.7% of questions correctly with at least two decoded frames inside every evidence interval, improving over uniform decoding at 128 frames.
- The method achieves the highest answer accuracy in the audit (63.5%) while using only 98.7 frames per question, which is 0.39x its frame cost compared to 256‑frame decoding.

## Context
Long‑horizon video understanding remains challenging because methods often rely on final decoded frames without auditing intermediate evidence coverage. Existing benchmarks lack strict criteria for event coverage, leading to overconfident but incomplete answers. TRACE addresses this gap by providing a rigorous benchmark and a transparent stopping criterion based on answer stability.

## Implications
For practitioners developing video‑aware agents, TRACE demonstrates that evidence‑driven grounding can boost accuracy without sacrificing efficiency. The approach offers a template for auditing temporal reasoning in AI systems, encouraging more reliable deployment of long‑video understanding tools in fields such as surveillance and autonomous navigation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22516v1)
