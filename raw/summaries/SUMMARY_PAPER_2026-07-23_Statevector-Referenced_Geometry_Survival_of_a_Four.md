---
title: Statevector-Referenced Geometry Survival of a Four-Qubit ZZ Quantum Kernel on IBM Quantum Hardware: A Fixed-Subset Diagnostic Across Three Execution Configurations
url: http://arxiv.org/abs/2607.20377v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_17-05-42Z_Statevector_ReferencedGeometrySurvivalofaFour_Qubi.md
generated_at: 2026-07-23 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether a frozen four-qubit ZZ quantum kernel survives execution on IBM hardware and how different error mitigation techniques affect its geometry. It reports that all three configurations produce finite positive-semidefinite Gram matrices with CKA alignment between 0.933 and 0.989, indicating substantial but incomplete preservation of the centered statevector geometry.

## Key Takeaways
- The frozen four-qubit ZZ kernel yields a complete finite positive-semidefinite Gram matrix across three error mitigation configurations (baseline, dynamical decoupling alone, gate twirling alone) on ibm_fez with 1024 shots per circuit.
- Gate twirling provides the most faithful geometry preservation, improving CKA and reducing mean absolute error compared to baseline and dynamical decoupling, which shows no improvement over baseline at this scale.
- The observed hardware distortion is non-affine and leads to a normalization that reverses fidelity and label alignment, suggesting the small uplift may be an artifact rather than true signal.

## Context
Quantum kernel methods rely on preserving geometric structure of data through statevector transformations; hardware noise can degrade these structures. This study demonstrates that even with error mitigation, geometry survival is partial and context-dependent, highlighting challenges in mapping quantum algorithms to classical diagnostics.

## Implications
For practitioners, this work underscores the need for both implementation fidelity checks and task relevance assessment when evaluating quantum machine learning on noisy devices. It also calls for clearer reporting of hardware-specific distortions rather than assuming universal algorithmic performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20377v1)
