---
title: "2026 06 11 15 27 06Z Maxproof Scalingmathematicalproofwithgenera Summary"
date: 2026-06-11
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-11_15-27-06Z_MaxProof_ScalingMathematicalProofwithGenerative_Ve.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-11 21:01
Source: 2026-06-11_15-27-06Z_MaxProof_ScalingMathematicalProofwithGenerative_Ve.md
Model: None

---


## Summary  
The paper introduces **MaxProof**, a population‑level test‑time scaling framework that integrates three proof‑oriented capabilities—proof generation, verification, and critique‑conditioned repair—into a single model trained with defense‑in‑depth generative‑verifier reinforcement learning. By treating the model as both generator and verifier during competition exams, MaxProof searches over a population of candidate proofs using tournament selection to produce a final answer. This approach enables the M3 model to achieve scores that surpass human gold‑medal thresholds on both the International Mathematical Olympiad (IMO 2025) and the USA Mathematics Olympiad (USAMO 2026). The contribution lies in combining RL‑driven verification with population‑level test‑time exploration, a novel strategy for scaling mathematical proof generation.

## Key Contributions  
- **Population‑level test‑time scaling**: A framework that treats the model as a generator, verifier, refiner, and ranker, exploring many candidate proofs before selecting the best one.  
- **Defense‑in‑depth generative verifier**: An RL‑trained verification module engineered to keep false‑positive rates low, providing reliable feedback for proof generation and repair.  
- **Tournament selection over proofs**: A deterministic competition algorithm that merges multiple candidate proofs into a single high‑quality output.

## Methodology  
The authors first train an M3 model by jointly optimizing three sub‑tasks: (1) generating plausible mathematical arguments, (2) verifying those arguments with the low‑false‑positive verifier, and (3) repairing incorrect or incomplete proofs using critique‑conditioned back‑propagation. These capabilities are fused into one released checkpoint. At test time, MaxProof receives a problem statement, generates multiple proof candidates, passes each through the verifier for confidence scores, refines low‑scoring ones, ranks them, and finally selects the top candidate via tournament selection. The population size is dynamically adjusted to balance exploration and computational cost.

## Results  
On the IMO 2025 benchmark, MaxProof reaches **35/42** correct answers; on USAMO 2026 it achieves **36/42**. Both scores exceed the human gold‑medal record of 38/42 for IMO and 39/42 for USAMO. The improvement is attributed to the population search, which allows the model to discover better proof structures that a single greedy generation would miss.

## Significance  
MaxProof demonstrates that RL‑based verification can be scaled to competition‑level mathematics, pushing AI beyond human performance on widely recognized problem sets. It also introduces a practical test‑time scaling paradigm—population exploration—that could be applied to other reasoning tasks where multiple hypotheses must be evaluated before final selection.

## Related Concepts  
- Generative‑verifier reinforcement learning  
- Population‑level test‑time scaling (also called population search)  
- Tournament selection in multi‑hypothesis settings  
- Defense‑in‑depth verification architectures  
- Competition‑level mathematical proof benchmarks (IMO, USAMO)
