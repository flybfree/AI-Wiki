---
title: Deep and shallow biases in language models
url: http://arxiv.org/abs/2609.09901v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-09_08-57-22Z_Deepandshallowbiasesinlanguagemodels.md
generated_at: 2026-09-09 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a bias depth score to differentiate stable model preferences from prompt‑specific artifacts. Experiments across four large language models and 4,442 opinion prompts reveal that only about a quarter of concentrated answers persist when the scenario is reframed, labeling these as deep biases. The remaining responses are shallow biases tied to specific wording.

## Key Takeaways
- Deep biases represent stable preferences that survive prompt rephrasing, indicating they are likely inherited from pretraining and fine‑tuning processes.  
- Shallow biases depend on the exact phrasing of a single prompt and do not persist across different formulations.  
- The bias depth score consistently shows deep biases are harder to eliminate than shallow biases under both continued fine‑tuning and diversity‑focused debiasing.

## Context
Understanding whether model preferences stem from learned knowledge or temporary prompt effects is crucial for evaluating fairness in AI systems. This work contributes a quantitative metric that helps researchers isolate genuine bias from superficial artifacts, aligning with broader efforts to make language models more robust and equitable.

## Implications
For practitioners, the bias depth score offers a practical tool to prioritize debiasing efforts on persistent issues rather than transient prompt quirks. Industry adoption could improve model transparency and reduce unintended discriminatory outputs in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09901v1)
