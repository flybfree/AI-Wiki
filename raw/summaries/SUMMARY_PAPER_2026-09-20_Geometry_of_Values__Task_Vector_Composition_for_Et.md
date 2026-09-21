---
title: Geometry of Values: Task Vector Composition for Ethical Preference Alignment in Language Models
url: http://arxiv.org/abs/2609.21094v1
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-17_21-12-43Z_GeometryofValues_TaskVectorCompositionforEthicalPr.md
generated_at: 2026-09-20 20:12
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates how Large Language Models (LLMs) navigate and resolve complex, conflicting moral dilemmas across different languages and cultures. By analyzing 12,000 instances of value conflicts—specifically Honesty, Justice, and Autonomy—the authors identify consistent underlying biases in current models and propose a novel "task vector transfer" method to isolate and manipulate specific ethical preferences within the model's weight space.

## Key Takeaways
- The researchers developed a comprehensive dataset of 12,000 two-option dilemmas covering three primary value conflicts: Honesty vs. Justice, Justice vs. Autonomy, and Autonomy vs. Honesty. This dataset includes translations into Hindi, Arabic, Spanish, and Chinese to rigorously probe how cross-lingual nuances affect the model's ability to maintain consistent moral reasoning.
- Benchmarking revealed that GPT-5-mini consistently favors Honesty over Autonomy across all five languages when no specific policy is provided. Conversely, while Llama-3.2 models exhibited a strong first-option bias, the study demonstrated that both plain fine-tuning and Direct Preference Optimization (DPO) could effectively eliminate this bias, increasing accuracy to over 98%.
- The paper introduces a "task vector transfer" method where researchers compute task vectors for specific value preferences and then orthogonalize them against general instruction-following vectors. This technique successfully isolates the direction of specific moral preferences, allowing for "task arithmetic" that can flip a model's stance on a specific value without degrading its overall performance or instruction-following capabilities.

## Context
As LLMs are increasingly deployed in global applications that require nuanced ethical judgment, understanding and controlling hidden biases is critical for AI safety. This paper matters because it moves the conversation from simply identifying bias to providing a geometric framework for how these values are encoded and manipulated within model weights across different languages.

## Implications
For researchers and practitioners, this work provides a methodology to decouple specific moral preferences from general instruction-following capabilities, allowing for more precise control over AI behavior. It offers a pathway toward creating "steerable" models where ethical stances can be adjusted systematically, which is essential for developing culturally sensitive AI systems that can adapt to diverse societal norms without requiring full model retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.21094v1)
