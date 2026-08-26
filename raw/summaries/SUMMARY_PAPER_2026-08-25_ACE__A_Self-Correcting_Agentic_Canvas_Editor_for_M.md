---
title: ACE: A Self-Correcting Agentic Canvas Editor for Multi-Slide Presentation Automation
url: http://arxiv.org/abs/2608.24103v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_06-05-17Z_ACE_ASelf_CorrectingAgenticCanvasEditorforMulti_Sl.md
generated_at: 2026-08-25 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ACE a self-correcting agentic canvas editor that automates multi-slide presentation creation using hierarchical scene-graph representations and an instruction-following judge without ground truth. It demonstrates that adding a feedback loop improves instruction following performance and reduces cost while maintaining speed. The system handles legacy flat layouts by recomputing coordinates and uses content-aware routing to limit input tokens.

## Key Takeaways
- ACE operates on a hierarchical scene-graph with 98 presentation tools allowing single-turn editing comparable to iterative HTML pipelines.
- Self-correction driven by natural-language critique raises instruction following scores from 3.81 to 4.23 on the benchmark and improves win-rate for raters.
- The system reduces input token usage by about 89% through content-aware routing and halts after one pass in most cases.

## Context
Large language model agents are being used to edit design documents but face challenges with flat element positions and lack of unique ground truth. Traditional metrics penalize valid variations and require costly iterative pipelines. This work addresses these issues by building a scene-graph based editor that can produce correct outputs in one turn while learning from human feedback.

## Implications
For designers the tool offers faster, cheaper automation without sacrificing quality or requiring manual iteration. For AI research it shows that self-correcting agents can outperform single-turn models and provide reliable ranking across diverse judges. Practitioners can adopt ACE to streamline presentation creation pipelines with measurable efficiency gains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24103v1)
