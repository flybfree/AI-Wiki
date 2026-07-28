---
title: Generative Artificial Intelligence (GenAI) to convert images of queuing networks into verifiable simulation models: an open-weight LLM workflow approach
url: http://arxiv.org/abs/2607.24259v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_10-50-37Z_GenerativeArtificialIntelligence_GenAI_toconvertim.md
generated_at: 2026-07-27 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Sketch2DES, an open-weight LLM workflow that transforms queuing network diagrams into verifiable discrete‑event simulation models. By separating translation, schema validation, and code generation into three stages, the method ensures intermediate artefacts are inspectable and automatically validated. Evaluation on eight varied diagrams shows high reliability and results indistinguishable from human‑coded benchmarks.

## Key Takeaways
- The workflow converts a visual diagram into a textual description using a multimodal LLM, preserving the original intent while allowing inspection of each step.  
- A reflection‑based verification loop validates that the generated JSON adheres to a schema before moving to code generation, guaranteeing structural correctness and reproducibility.  
- Deterministic transformation to executable simulation models is achieved through a software adapter, eliminating randomness and making the process transparent for non‑programmers.

## Context
LLMs are increasingly used to automate model building across scientific domains, yet most approaches generate code directly from text without safeguards. This limits verification and reproducibility, especially for users lacking coding skills. Sketch2DES addresses these gaps by embedding validation checks into a structured pipeline that can be audited and reproduced.

## Implications
The method offers a robust alternative to direct code generation, reducing reliance on programming expertise while maintaining scientific accuracy. It could become a template for other domain‑specific model conversion tasks, fostering trustworthy AI‑assisted workflows in engineering and data science.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24259v1)
