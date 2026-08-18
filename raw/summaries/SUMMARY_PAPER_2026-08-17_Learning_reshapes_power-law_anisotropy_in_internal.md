---
title: Learning reshapes power-law anisotropy in internal representations
url: http://arxiv.org/abs/2608.15239v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_13-56-28Z_Learningreshapespower_lawanisotropyininternalrepre.md
generated_at: 2026-08-17 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how power‑law anisotropy in internal representations emerges during learning. It solves exact dynamics of a two‑layer linear network with power‑law inputs and teachers, revealing nonmonotonic evolution of the exponent across training modes.

## Key Takeaways
- The local power‑law exponent changes over time and can take up to four distinct asymptotic values depending on mode and training duration.
- In the lazy regime the exponent stays constant, indicating that learning dynamics are not always responsible for anisotropy shifts.
- Similar exponent dynamics appear in realistic nonlinear networks, suggesting a broader applicability beyond linear models.

## Context
Understanding power‑law anisotropy is crucial because it reflects how high‑dimensional data are compressed and processed in neural systems. This work bridges theoretical analysis with concrete learning protocols, offering a quantitative view of a long‑standing geometric property.

## Implications
For practitioners, the findings highlight that training dynamics can reshape representation geometry, which may affect model interpretability and robustness. Industry applications could leverage these insights to design more stable or efficient models by controlling input statistics and task structure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15239v1)
