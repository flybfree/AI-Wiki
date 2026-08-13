---
title: A 12-CNOT Double Qubit Excitation Gate
url: http://arxiv.org/abs/2608.11733v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_07-12-57Z_A12_CNOTDoubleQubitExcitationGate.md
generated_at: 2026-08-13 08:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a new circuit for the double qubit excitation operator that uses only twelve controlled‑not gates, achieving a lower CNOT count than previous state‑of‑the‑art results which required thirteen. The proposed decomposition also attains the smallest depth of ten CNOTs and a total circuit depth of sixteen, while adding just two one‑qubit gates beyond the minimal gate count reported earlier.

## Key Takeaways
- The circuit reduces the CNOT count from 13 to 12, which is the lowest among all prior SOTA implementations.  
- It also minimizes depth with ten CNOT layers and a total depth of sixteen operations, outperforming earlier solutions in both metrics.  
- Compared to the minimal one‑qubit gate count of eleven, this solution adds only two additional one‑qubit gates.

## Context
The quest for efficient quantum algorithms drives continuous improvements in gate decomposition, especially for multi‑qubit operations that are foundational to many AI‑relevant tasks such as variational circuits. Efficiently implementing high‑level operators like the double qubit excitation is crucial because it directly impacts the scalability and error profile of quantum processors used in machine learning models.

## Implications
For practitioners, this gate set can be integrated into existing hardware pipelines without major redesigns, lowering implementation complexity and cost. The reduced depth translates to faster execution times, which is essential for real‑time AI workloads that rely on quantum subroutines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11733v1)
