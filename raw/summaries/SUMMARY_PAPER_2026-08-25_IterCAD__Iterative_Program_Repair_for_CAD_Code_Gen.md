---
title: IterCAD: Iterative Program Repair for CAD Code Generation from Orthographic Views
url: http://arxiv.org/abs/2608.24020v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_03-22-10Z_IterCAD_IterativeProgramRepairforCADCodeGeneration.md
generated_at: 2026-08-25 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
IterCAD introduces an iterative repair framework for generating executable parametric CAD code from orthographic views, addressing the limitations of one‑shot vision‑language models. By repeatedly analyzing intermediate CAD results and deciding to REVISE or STOP, IterCAD progressively corrects structural and parametric errors, achieving higher executability and geometric fidelity than strong baselines.

## Key Takeaways
- The model treats code generation as a progressive repair process where each iteration inspects the current CAD output against target views.  
- A structured revise‑or‑stop supervision set enables learning of both correct final states and intermediate repairable states, supporting multi‑turn refinement.  
- Experiments on CADExpert demonstrate consistent improvements in code executability and geometric consistency over one‑shot approaches.

## Context
Current AI systems for CAD code generation rely on single‑pass predictions that lack feedback loops, leading to non‑executable or geometrically inconsistent outputs. IterCAD’s iterative design bridges the gap between visual understanding and procedural reasoning by incorporating a repair loop that can be learned end‑to‑end.

## Implications
This work opens a path toward more reliable CAD automation where generated code remains executable and faithful to source drawings, benefiting engineers who rely on precise parametric models. The methodology could be extended to other domain‑specific code generation tasks requiring iterative correction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24020v1)
