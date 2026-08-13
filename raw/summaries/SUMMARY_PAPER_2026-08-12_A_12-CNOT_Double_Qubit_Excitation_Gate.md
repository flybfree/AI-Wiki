---
title: A 12-CNOT Double Qubit Excitation Gate
url: http://arxiv.org/abs/2608.11733v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_07-12-57Z_A12_CNOTDoubleQubitExcitationGate.md
generated_at: 2026-08-12 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper reports the first implementation of a double qubit excitation gate decomposed into twelve CNOT gates. The new circuit reduces the number of CNOTs from the previous state‑of‑the‑art 13, achieves the lowest CNOT count (12), depth (10) and total depth (16), and adds only two extra one‑qubit gates compared with the best prior solution that used eleven one‑qubit gates.

## Key Takeaways
- The circuit uses twelve CNOT gates instead of thirteen, lowering both the gate count and the circuit depth.  
- Its maximum depth is ten, which is the smallest among all previously reported SOTA double qubit excitation circuits.  
- Compared with the lowest one‑qubit gate count (eleven), this solution adds only two additional one‑qubit gates while maintaining a total depth of sixteen.

## Context
Quantum algorithms for artificial intelligence often require multi‑qubit operations such as double qubit excitations, which are essential for entangling states and implementing error‑resilient protocols. Efficient gate decomposition directly influences the feasibility of scaling quantum processors to handle complex AI workloads without excessive overhead.

## Implications
For researchers developing fault‑tolerant quantum hardware, this 12‑CNOT circuit offers a practical path to reduce qubit usage and latency in AI‑focused algorithms. Practitioners can leverage the lower depth to design faster feedback loops, potentially accelerating training of quantum neural networks and improving overall system performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11733v1)
