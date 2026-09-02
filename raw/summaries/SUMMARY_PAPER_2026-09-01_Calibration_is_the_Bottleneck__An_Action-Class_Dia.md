---
title: Calibration is the Bottleneck: An Action-Class Diagnostic of Multi-Turn Tool-Calling
url: http://arxiv.org/abs/2609.00949v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_09-08-15Z_CalibrationistheBottleneck_AnAction_ClassDiagnosti.md
generated_at: 2026-09-01 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a diagnostic framework for multi‑turn tool calling that separates model failures into two orthogonal modes: action‑class miscalibration and execution failure. It demonstrates that accuracy can exceed the gold action recall bound (Acc > GAR), exposing hidden miscalibration, while large slack (GAR ≫ Acc) localizes problems to TOOL_CALL actions.

## Key Takeaways
- Action‑class miscalibration manifests as Acc > GAR, a violation that the state grader masks.  
- Large bound slack indicates execution failure confined to TOOL_CALL actions when GAR >> Acc.  
- Context‑only perturbations can shift accuracy by up to +11.5 pp or –21.0 pp across families depending on the perturbation mechanism.

## Context
Multi‑turn tool calling is a central challenge for LLM agents, yet existing benchmarks aggregate performance and obscure imbalances between failure modes. This work moves beyond aggregate scores toward finer diagnostic granularity.

## Implications
Practitioners must adopt action‑class diagnostics to calibrate models accurately and avoid overstating capabilities; the framework offers targeted guidance for improving tool‑calling agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00949v1)
