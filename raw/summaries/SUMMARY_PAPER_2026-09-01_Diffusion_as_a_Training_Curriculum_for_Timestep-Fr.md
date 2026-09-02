---
title: Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning
url: http://arxiv.org/abs/2609.01449v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-55-01Z_DiffusionasaTrainingCurriculumforTimestep_FreeIter.md
generated_at: 2026-09-01 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a persistent hidden state that eliminates timestep conditioning from diffusion denoisers, enabling an anytime solver that can run to arbitrary depth without parallel rollouts or external verifiers. Experiments show exact Sudoku‑Extreme solves at 99.90% and high rates on Maze‑Unique, demonstrating that progressive corruption is unnecessary during inference.

## Key Takeaways
- A shared hidden state allows the denoiser to operate independently of diffusion timesteps, producing an anytime solver that improves with depth beyond training rollout lengths.  
- Accuracy reaches 99.90% exact solve on Sudoku‑Extreme and 98.93% solve rate on Maze‑Unique, far exceeding prior iterative reasoning methods.  
- Keeping corruption at maximum by injecting fresh Gaussian noise each step yields near‑perfect solving without parallel rollouts or candidate selection.

## Context
Iterative reasoning models often rely on parallel rollouts that consume significant compute and memory. Diffusion’s sequential nature offers a more efficient alternative, especially when limited resources are available. This work bridges the gap between diffusion training and real‑time inference by removing unnecessary complexity.

## Implications
The anytime solver can be deployed in resource‑constrained environments where parallel computation is impractical. Its simplicity—using only a single trajectory with noise injection—makes it attractive for industry applications requiring fast, accurate reasoning without large infrastructure. Practitioners may adopt this approach to build scalable AI assistants that solve complex problems on the fly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01449v1)
