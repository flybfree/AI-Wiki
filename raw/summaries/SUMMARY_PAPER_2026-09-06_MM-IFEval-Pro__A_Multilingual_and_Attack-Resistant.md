---
title: MM-IFEval-Pro: A Multilingual and Attack-Resistant Benchmark for Instruction-Following in Vision-Language Models
url: http://arxiv.org/abs/2609.04859v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_08-18-00Z_MM_IFEval_Pro_AMultilingualandAttack_ResistantBenc.md
generated_at: 2026-09-06 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MM‑IFEval‑Pro, a multimodal instruction‑following benchmark that covers Chinese and English tasks along with adversarial hijacking scenarios. The dataset comprises four task categories, twenty‑four subcategories, eight instruction categories, and fifty‑two subcategories, each sample containing about three constraints to simulate complex instructions. Reinforcement‑learning training on the set boosts model performance and transfers well to other multimodal benchmarks.

## Key Takeaways
- MM‑IFEval‑Pro provides a comprehensive multilingual benchmark with adversarial cases, addressing limited language coverage in existing tools.
- The reinforcement‑learning enriched instruction set markedly improves model accuracy and enables cross‑task generalization across languages.
- Each sample’s average of three constraints reflects realistic complexity, enhancing the realism of evaluation.

## Context
Current multimodal benchmarks often neglect multilingual support and safety‑critical scenarios, limiting their usefulness for real‑world applications. This work fills those gaps by integrating Chinese language tasks with adversarial instructions, offering a more balanced evaluation platform.

## Implications
For researchers, MM‑IFEval‑Pro sets a new standard for evaluating instruction‑following reliability in diverse settings. For industry practitioners, the benchmark can guide the development of safer, multilingual vision‑language systems that perform consistently under complex and potentially malicious prompts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04859v1)
