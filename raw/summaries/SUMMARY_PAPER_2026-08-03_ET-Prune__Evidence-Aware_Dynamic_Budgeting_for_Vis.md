---
title: ET-Prune: Evidence-Aware Dynamic Budgeting for Visual Token Pruning in Text-Rich MLLMs
url: http://arxiv.org/abs/2608.01979v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_09-42-34Z_ET_Prune_Evidence_AwareDynamicBudgetingforVisualTo.md
generated_at: 2026-08-03 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ET‑Prune, a training‑free method for visual token pruning in multimodal large language models that adapts to text‑rich inputs by allocating evidence tokens dynamically. Experiments show it achieves comparable or better performance while retaining roughly half the visual tokens across multiple benchmarks.

## Key Takeaways
- The framework treats pruning as an evidence allocation problem, extracting question‑conditioned evidence from a decoder‑side partial query‑key block to identify relevant text‑like regions that should be preserved.  
- It introduces a sample‑specific token floor derived from uncertainty and density of visual tokens, preventing the loss of decisive evidence such as labels or fields required for OCR tasks.  
- Three progressive middle‑layer events adjust token retention, favoring diffuse evidence while aggressively pruning concentrated evidence to reach a half‑token budget.

## Context
Visual token pruning aims to lower inference cost in multimodal models without sacrificing essential content, especially when text dominates the input. Traditional fixed‑ratio approaches ignore textual relevance, leading to degraded OCR accuracy on text‑rich data.

## Implications
ET‑Prune demonstrates that evidence‑aware dynamic budgeting can be applied out of the box, offering a practical path for deploying pruned models in real‑world OCR and vision‑language systems where token efficiency matters. Practitioners can adopt this approach to balance speed and accuracy without retraining large models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01979v1)
