---
title: VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models
url: http://arxiv.org/abs/2608.24302v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_09-27-47Z_VideoHarness_RSI_RecursiveHarnessSelf_Improvementf.md
generated_at: 2026-08-25 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces VideoHarness-RSI, a framework that recursively searches executable context constructors for frozen vision-language models to improve long‑video understanding. It demonstrates that improving the harness alone can boost performance beyond several hand‑crafted baselines and transfers gains to other benchmarks without further search.

## Key Takeaways
- The outer‑loop proposer generates candidate harnesses using prior programs, evaluation outcomes, and execution traces, then executes them end‑to‑end before retaining successful variants. 
- Recursive harness search consistently finds room for improvement even when starting from uniform sampling. 
- Starting from a stronger hand‑crafted baseline also yields further improvements, showing the process can refine existing structures.

## Context
Long‑video understanding is limited by model context length, prompting research on compression, retrieval, memory, and agentic acquisition. This work isolates the executable construction layer as a separate optimization problem, offering a controlled setting for harness discovery around frozen VLMs.

## Implications
The results suggest that harness design can be automated without retraining models, providing a reproducible baseline for researchers. Practitioners may adopt this approach to enhance long‑video tasks efficiently and transfer improvements across datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24302v1)
