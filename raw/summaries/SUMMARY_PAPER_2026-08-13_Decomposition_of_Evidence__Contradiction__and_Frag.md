---
title: Decomposition of Evidence, Contradiction, and Fragility in Perturbation Responses
url: http://arxiv.org/abs/2608.12935v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_08-13-22Z_DecompositionofEvidence_Contradiction_andFragility.md
generated_at: 2026-08-13 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DECAF (Decomposition of Evidence, Contradiction, And Fragility) to dissect how perturbation responses break down into evidence, contradiction, and fragility components. The authors show that the decomposition preserves the original magnitude exactly while offering a more interpretable view than raw response size alone.

## Key Takeaways
- The contrast between paired inputs evolves as they are revealed, and the final contrast is used to interpret the entire trajectory of responses.
- A single magnitude can simultaneously support a factual difference, oppose it, or even vanish at the endpoint, highlighting the need for component‑level analysis.
- Short forward‑only DECAF trajectories outperform general‑purpose baselines on FunnyBirds and ImageNet‑1k while achieving 4.75× lower wall time and 2.36× lower peak memory in a 1B‑scale DINOv2 model.

## Context
Perturbation methods are central to AI interpretability, yet they often rely solely on magnitude which is insufficient for understanding model behavior. This work contributes a principled decomposition that aligns with endpoint‑relative axioms and can be applied across vision and tabular domains.

## Implications
Providing evidence, contradiction, and fragility components enables more reliable debugging and design decisions in large language and vision models. Practitioners can use the decomposition to prioritize which aspects of model responses are most fragile or contradictory, leading to faster iteration cycles and reduced computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12935v1)
