---
title: RealCADBench: Benchmarking Parametric CAD Modeling from Industrial Design Intents
url: http://arxiv.org/abs/2609.03773v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_12-43-23Z_RealCADBench_BenchmarkingParametricCADModelingfrom.md
generated_at: 2026-09-03 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
RealCADBench introduces a comprehensive benchmark for evaluating parametric CAD modeling from real industrial design intents, presenting 12,632 tasks across multiple input modalities and comparing nine frontier large models. The study finds that no single model excels on all evaluation metrics, highlighting variability in executability, IoU scores, and visual‑semantic identity.

## Key Takeaways
- Executability scores for Part modeling range from 0.565 to 0.812 across regimes, yet the highest composite score comes from a different model than the one with top component metrics.  
- Solid IoU and Surface IoU values are low (0.2841–0.5379 for Solid IoU, 0.112–0.217 for Surface IoU), indicating substantial geometric mismatches between generated models and intended designs.  
- On the assembly benchmark RCB‑Assm25, Codex with GPT‑5.5 improves executability and IoU but reduces the visual‑semantic Judge score by 6.98 percentage points.

## Context
This work addresses a gap in AI evaluation where CAD performance is often measured with synthetic or limited input data, neglecting real industrial intents. By integrating diverse modalities such as text descriptions, drawings, product pictures, and rendered images, RealCADBench provides a more realistic benchmark that reflects actual manufacturing workflows.

## Implications
For practitioners, the findings suggest that relying solely on executability is insufficient; visual‑semantic fidelity must also be considered when selecting or deploying CAD models. The industry can use these results to calibrate expectations for large language model agents in real‑world design automation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03773v1)
