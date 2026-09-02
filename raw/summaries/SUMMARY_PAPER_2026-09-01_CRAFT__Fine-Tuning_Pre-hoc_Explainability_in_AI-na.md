---
title: CRAFT: Fine-Tuning Pre-hoc Explainability in AI-native 6G RAN
url: http://arxiv.org/abs/2609.00590v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_02-30-02Z_CRAFT_Fine_TuningPre_hocExplainabilityinAI_native6.md
generated_at: 2026-09-01 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CRAFT, a data‑centric fine‑tuning method that aligns small language models in AI‑native 6G RAN with pre‑output causal reasoning traces. On telecom datasets the approach reaches up to 94.6% F1 accuracy without parse failures, far exceeding baseline methods while using 59% less energy than GRPO.

## Key Takeaways
- CRAFT autonomously creates verified (input, trace, label) triplets to resolve the cold‑start barrier where SLMs either output labels or traces but not both.  
- The LoRA fine‑tuning of CRAFT achieves 94.6% F1 on IC xApp with zero parse failures, demonstrating strong performance without costly RL training.  
- Energy consumption is reduced by 59% compared to GRPO baselines, making the solution sustainable for real‑world deployment.

## Context
Telecom networks are moving toward AI‑driven RAN where small language models must reason over live telemetry while providing transparent explanations. Existing RL techniques like GRPO struggle with cold‑start scenarios and high compute costs, limiting practical use in resource‑constrained edge devices.

## Implications
CRAFT offers a scalable pathway to deployable, auditable AI in 6G RAN by embedding reasoning directly into model outputs. Practitioners can leverage its low‑cost fine‑tuning as a foundation for further RL refinement, ensuring both performance and energy efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00590v1)
