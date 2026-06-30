---
title: LeVo 2: Stable and Melodious Song Generation via Hierarchical Representation Modeling and Progressive Post-Training
url: http://arxiv.org/abs/2606.30642v1
type: paper-summary
date: 2026-06-30
source_paper: 2026-06-29_17-59-20Z_LeVo2_StableandMelodiousSongGenerationviaHierarchi.md
generated_at: 2026-06-30 01:00
model: nvidia/nemotron-3-nano-4b
---

## Summary  
LeVo 2 is a hybrid LLM‑diffusion framework designed for full‑length song generation that balances coherence and musicality. It first predicts mixed tokens for semantic planning, then refines vocal and accompaniment tokens in parallel, and finally reconstructs waveforms with a diffusion codec. The model achieves this by generating a semantic plan before refining audio details.

## Key Takeaways  
- It separates semantic planning with mixed tokens from vocal/accompaniment refinement, enabling detailed track‑specific acoustics.  
- The training schedule includes aesthetics‑guided alignment via music‑tier evaluation before DPO steps, reducing conflict between musicality and controllability.  
- Modular extension trains a Track‑Specific LM for acoustic refinement while preserving the aligned semantic planner.

## Context  
Song generation remains challenging because global coherence often conflicts with fine‑grained audio fidelity. This work addresses that trade‑off by integrating hierarchical modeling with diffusion reconstruction, offering a principled way to align text prompts with musical aesthetics.

## Implications  
The approach provides a scalable framework for controllable music synthesis, guiding future research toward better alignment of AI‑generated content with human musical preferences in the industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.30642v1)
