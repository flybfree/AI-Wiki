---
title: EdiTikZ: Scientific Figure Editing from Revision Trajectories
url: http://arxiv.org/abs/2609.01409v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-29-52Z_EdiTikZ_ScientificFigureEditingfromRevisionTraject.md
generated_at: 2026-09-01 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DaEdiTikZ, a dataset of revision-derived TikZ edits for scientific figure editing. It trains two compact Qwen3.5 models to reconstruct and edit figures using reinforcement learning, achieving state‑of‑the‑art performance on benchmarks and human evaluations.

## Key Takeaways
- DaEdiTikZ is the first large‑scale dataset of 781K directed TikZ edits inferred from 391K plausible pairs across arXiv, GitHub, and TeX SE.  
- The models jointly learn reconstruction and editing with RL rewards for rendered fidelity and edit application, outperforming GPT‑5.6‑Sol in human ratings.  
- Performance remains competitive under severe out‑of‑distribution shifts near the 2K sequence‑length limit.

## Context
Scientific figure generation relies on vision‑language models that can create diagrams from text or images but lack iterative refinement capabilities. Existing solutions are either proprietary, evaluation‑only, or rely on synthetic supervision, limiting scalability and accessibility for researchers.

## Implications
This work demonstrates that leveraging natural revision trajectories can provide robust, scalable supervision for figure editing without costly agents. Practitioners can adopt the models to generate publication‑ready figures directly from textual prompts, accelerating scientific communication.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01409v1)
