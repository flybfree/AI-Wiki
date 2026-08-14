---
title: Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion
url: http://arxiv.org/abs/2608.13457v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_16-41-48Z_Symmetry_BreakingDeNovoCrystalGenerationviaMarkovi.md
generated_at: 2026-08-13 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Symmetry-breaking Crystal Diffusion (SbCD), a diffusion model that generates full crystallographic specifications by reversing from low‑symmetry priors using a Markovian jump‑diffusion process. The method models spontaneous symmetry breaking in crystals, allowing transitions between different space groups during generation. Experiments on MP20 and MPTS‑52 show SbCD outperforms existing symmetry‑preserving generators.

## Key Takeaways
- The model explicitly incorporates inter‑space‑group transitions through a Markovian jump‑diffusion mechanism, moving from low‑symmetry states to higher‑symmetry ones during reverse diffusion.  
- Generating crystals only up to site symmetries is replaced by full structure specifications, capturing global symmetry and structural dependencies.  
- The approach leverages spontaneous symmetry breaking as an inspiration, enabling a physically motivated generation process that surpasses prior state‑of‑the‑art methods.

## Context
Generative AI for materials has focused on producing partial or approximate crystal structures, often missing the complete space‑group information essential for reliable material design. This work bridges that gap by modeling the underlying physical dynamics of symmetry breaking, offering a more realistic representation than purely empirical sampling.

## Implications
For researchers and industry practitioners, SbCD provides a framework to generate complete, physically plausible crystals, accelerating discovery pipelines in materials science. The method’s ability to navigate space‑group transitions could lead to novel material properties that were previously inaccessible through conventional generative models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13457v1)
