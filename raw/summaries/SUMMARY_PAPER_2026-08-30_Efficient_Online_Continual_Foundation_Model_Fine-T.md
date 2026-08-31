---
title: Efficient Online Continual Foundation Model Fine-Tuning for Predictive Process Monitoring
url: http://arxiv.org/abs/2608.28237v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_11-53-26Z_EfficientOnlineContinualFoundationModelFine_Tuning.md
generated_at: 2026-08-30 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces COMPASS, an online continual fine‑tuning framework for foundation models applied to predictive process monitoring. The authors show that COMPASS adapts loss‑plateau drift detection to automatically discover task boundaries and preserves a single knowledge subspace that blends pre‑trained FM knowledge with new task updates. Experiments on nine event streams demonstrate that COMPASS outperforms three state‑of‑the‑art non‑FM methods and two update‑strategy baselines, especially on streams with recurrent drift and long‑running scenarios, while keeping computational overhead comparable to the competitors.

## Key Takeaways
- COMPASS adapts loss‑plateau drift detection to autonomously identify task boundaries in event streams.  
- It maintains a unified knowledge subspace that includes both pre‑trained FM directions and newly learned task‑specific updates.  
- The framework outperforms three SOTA non‑FM competitors and two update‑strategy baselines, achieving strong gains on recurrent drift and complex, long‑running cases with acceptable computational cost.

## Context
Foundation models provide rich representations but continual fine‑tuning remains difficult due to cold‑start issues. In process mining, concept drift can render task‑specific networks obsolete quickly. This work tackles the problem by enabling online continual learning that updates a single FM subspace without full retraining, reducing latency and resource consumption.

## Implications
For industry practitioners, COMPASS offers a practical way to keep predictive models current with minimal downtime and cost. By leveraging the robustness of foundation models, organizations can deploy PPM systems that adapt continuously, improving reliability in dynamic operational environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28237v1)
