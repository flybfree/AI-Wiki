---
title: An Agentic Workflow for Legacy HPC Modernization: Converting the Two-Electron-Integral Core of GAMESS
url: http://arxiv.org/abs/2608.12249v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_16-48-47Z_AnAgenticWorkflowforLegacyHPCModernization_Convert.md
generated_at: 2026-08-12 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper describes an agentic workflow that converts the two-electron‑integral core of GAMESS from fixed‑form Fortran 77 to free‑form Fortran 2008. The authors used three Claude Code roles in isolated worktrees across four model generations, with human oversight limited to a few gates. All twelve source files reproduced the canonical test suite bit‑for‑bit and passed 51 validation runs, showing zero chemistry‑relevant differences.

## Key Takeaways
- Agents can manage large codebases by operating under a version‑controlled specification that they authored and revised, with an exact verification oracle defining safe delegation boundaries.  
- The workflow achieves bit‑for‑bit energy reproduction as the merge criterion, where even a deviation in the twelfth decimal place is treated as a failure.  
- The project spanned four Claude model generations while maintaining continuous integration via Jenkins tests.

## Context
The paper situates AI agents within the broader context of software modernization, showing that large, routine transformations—such as updating legacy Fortran codebases—can be delegated to autonomous systems without sacrificing correctness. This approach highlights how generative AI can handle repetitive, high‑volume tasks that traditionally require extensive human effort and expertise.

## Implications
For the field, this work demonstrates a scalable path for integrating AI into continuous integration pipelines, reducing risk through oracle‑driven verification. Practitioners can leverage similar agentic workflows to modernize other legacy scientific software, accelerating adoption of newer languages and standards while preserving computational accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12249v1)
