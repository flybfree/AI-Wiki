---
title: On-Policy Delta Distillation for Multilingual Math Reasoning
url: http://arxiv.org/abs/2608.05802v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_09-37-49Z_On_PolicyDeltaDistillationforMultilingualMathReaso.md
generated_at: 2026-08-06 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates On‑Policy Delta Distillation (OPD²) as an advanced method for improving large language model performance on multilingual mathematical reasoning tasks. Experiments with the Qwen3 model demonstrate that OPD² consistently outperforms baseline On‑Policy Distillation, especially in Korean and Japanese, while also narrowing the performance gap between English and Korean results.

## Key Takeaways
- The probability gap between a post‑trained teacher and its base model serves as an effective learning signal for OPD², leading to measurable gains across all three languages.  
- Korean and Japanese benefit from OPD² with pronounced improvements, whereas the English‑Korean performance gap narrows significantly after applying this method.  
- Using only English data for distillation can raise scores in Korean and Japanese but often causes responses to shift toward English, underscoring the need for multilingual data.

## Context
The rise of large language models has created a demand for efficient post‑training techniques that preserve or enhance performance without extensive fine‑tuning. OPD² addresses this by leveraging internal model differences rather than external datasets, offering a lightweight alternative to full reinforcement learning pipelines in AI research.

## Implications
For industry practitioners, OPD² provides a scalable way to boost multilingual reasoning capabilities with minimal computational overhead, supporting applications that require accurate calculations across diverse language markets. Researchers can explore further how delta‑based signals generalize beyond math tasks to other domain‑specific challenges.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05802v1)
