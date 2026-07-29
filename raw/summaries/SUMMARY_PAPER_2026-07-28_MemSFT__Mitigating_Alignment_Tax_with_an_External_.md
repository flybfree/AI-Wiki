---
title: MemSFT: Mitigating Alignment Tax with an External Parametric Memory
url: http://arxiv.org/abs/2607.25614v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_11-45-34Z_MemSFT_MitigatingAlignmentTaxwithanExternalParamet.md
generated_at: 2026-07-28 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MemSFT, a method that reduces the alignment tax caused by domain‑specific fine‑tuning in large language models. By using an external parametric memory trained to imitate a non‑parametric retriever, MemSFT lets specialized knowledge be stored without updating the model’s backbone parameters.

## Key Takeaways
- The proposed plug‑and‑play parametric memory decouples domain specialization from backbone updates, preserving general task performance while adding new expertise.  
- A learned router fuses output distributions between the memory and the backbone at each decoding step, enabling selective invocation of domain knowledge.  
- Experiments across biology, geoscience, and law show MemSFT improves domain scores with negligible loss on unrelated tasks, unlike full SFT which causes severe forgetting.

## Context
Fine‑tuning LLMs for specialized domains often sacrifices their ability to handle general queries, a problem known as the alignment tax. Existing solutions either require large parameter budgets or suffer from catastrophic forgetting. MemSFT offers a lightweight alternative that can be applied across model sizes without retraining the core weights.

## Implications
For researchers and practitioners, MemSFT provides a practical path to deploy domain‑specific capabilities in existing models, accelerating product development while maintaining broad utility. This decoupling approach could become standard practice as organizations seek efficient, modular AI solutions for diverse use cases.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25614v1)
