---
title: CADWorld: Computer-Use Benchmark for Long-Horizon Computer-Aided Design
url: http://arxiv.org/abs/2609.16251v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_19-19-05Z_CADWorld_Computer_UseBenchmarkforLong_HorizonCompu.md
generated_at: 2026-09-15 20:14
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces CADWorld, a novel benchmark designed to evaluate AI agents on long-horizon computer-aided design tasks within the FreeCAD environment. Covering 200 diverse mechanical engineering workflows, the study reveals a significant performance gap where even the strongest existing agent achieves only 17.5% success compared to an expert reference rate of 87%, highlighting critical deficiencies in handling persistent, verifiable engineering artifacts and complex structural constraints.

## Key Takeaways
- CADWorld comprises 200 tasks across 11 mechanical-CAD workflow categories, including sketching, part modeling, assembly, CAM, FEM, measurement, mesh processing, and technical drawing, requiring agents to manipulate geometry and constraints over extended interaction horizons while producing valid native project files.
- Evaluation relies on task-specific executable checks over saved FreeCAD artifacts and auxiliary outputs, assessing geometric properties, parametric structure, constraints, manufacturing state, and simulation results rather than just visual similarity or simple GUI completion.
- Testing seven current agents shows that weaker models often fail to produce any valid artifact, while stronger agents struggle with structural integrity, geometric accuracy, and construction-process requirements, exposing a distinct gap between general GUI competence and reliable engineering workflow execution.

## Context
As AI agents expand into realistic desktop environments, existing benchmarks often focus on short-term interactions or lack the rigor required for professional engineering domains where outputs must be persistent and structurally sound. This work addresses a critical gap by introducing a specialized benchmark that tests an agent's ability to maintain state and adhere to complex constraints over long horizons, moving beyond simple task completion toward verifiable engineering validity.

## Implications
The findings suggest that current AI agents are not yet ready for autonomous mechanical design workflows without significant human oversight, as they struggle with the structural and geometric demands of professional CAD tasks. For practitioners and researchers, this highlights the urgent need for models capable of deep reasoning about parametric structures and persistent artifacts, driving future development toward more robust, engineering-grade automation tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.16251v1)
