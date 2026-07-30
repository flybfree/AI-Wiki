---
title: Progressive Multimodal Alignment for Continual Instruction Tuning
url: http://arxiv.org/abs/2607.26947v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_14-15-55Z_ProgressiveMultimodalAlignmentforContinualInstruct.md
generated_at: 2026-07-29 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Progressive Multimodal Alignment (PMA) to address projector-level forgetting in multimodal continual instruction tuning. By detecting distribution shifts and expanding projector experts only when needed, PMA maintains alignment stability while allowing plasticity with sub‑linear parameter growth. Experiments show consistent gains over prior MCIT methods.

## Key Takeaways
- PMA detects multimodal distribution shifts using a lightweight representation descriptor.
- It progressively expands projector experts only when necessary to preserve previously learned alignment.
- The framework uses an expandable router that integrates expert outputs while retaining the original pretrained projector as a stable anchor, achieving sub‑linear parameter growth.

## Context
Multimodal Large Language Models aim to unify visual and textual understanding through shared projection layers. Continual instruction tuning adds complexity because visual inputs evolve over time, causing the fixed projector to become misaligned. Existing methods often ignore this drift, focusing solely on the LLM backbone.

## Implications
PMA offers a scalable solution that can be added to any MCIT pipeline without retraining the entire model. This reduces computational cost and enables long‑term deployment of multimodal assistants where visual inputs change frequently. Practitioners can benefit from improved alignment stability with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26947v1)
