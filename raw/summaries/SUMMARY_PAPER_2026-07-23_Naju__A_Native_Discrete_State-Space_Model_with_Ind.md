---
title: Naju: A Native Discrete State-Space Model with Independent Retention and Writing for Long-Sequence Memory
url: http://arxiv.org/abs/2607.21000v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_07-34-07Z_Naju_ANativeDiscreteState_SpaceModelwithIndependen.md
generated_at: 2026-07-23 22:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Naju, a native discrete state‑space model that separates memory retention and overwriting into independent components. By parameterizing the recurrence directly rather than discretizing a continuous system, Naju achieves strong long‑range memory while maintaining linear time and memory scaling. Experiments show it outperforms Mamba baselines at four times longer training horizons.

## Key Takeaways
- The model factorizes the update as \(x_n = f_n\odot x_{n-1} + i_n\odot(B_n u_n)\), where a sigmoid pole \(f_n\) enforces Schur stability and limits retention to near‑lossless recall.  
- Decoupling \(f_n\) from \(i_n\) removes the constraint \(|r|+w \le 1\), allowing high retention without sacrificing writing efficiency.  
- Naju remains strong on both tasks at four times longer sequences, preserving linear‑time and linear‑memory complexity.

## Context
State‑space models like Mamba have set new standards for long‑range reasoning but often sacrifice one aspect of memory trade‑off. This work highlights that native discrete designs can capture the full spectrum of retention and overwriting without artificial regularizers or compromises, aligning with the community’s push toward interpretable and efficient architectures.

## Implications
For practitioners developing long‑context AI systems, Naju offers a blueprint for balancing memory and update operations directly within the model, potentially reducing reliance on external attention mechanisms. The field can adopt this decoupled design to improve both performance and interpretability in large‑scale language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21000v1)
