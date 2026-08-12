---
title: Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents
url: http://arxiv.org/abs/2608.11110v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_16-18-34Z_ActionsSpeakLouderthanWords_MeasuringCross_Lingual.md
generated_at: 2026-08-11 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how tool-using language models retain their action policies when the same task is presented in different languages, focusing on measuring cross‑lingual policy retention rather than just final answers. Across eight frontier models, six benchmarks and 41 languages it finds that naive trace similarity is unreliable due to five confounds, and after correcting them every model retains roughly 71–73 % of its original action policy under greedy decoding.

## Key Takeaways
- Naive trace similarity is misleading because short traces score higher, empty traces score perfectly, unrelated traces agree by chance over half the time, and a single repeated question can produce different answers, undermining any baseline. - The effect persists across models: four frontier models keep 71‑73 % of their action policy in every language, with model identity explaining only 5.7 % of variance, indicating structural rather than sampling noise. - Below roughly ten billion parameters the retention breaks down and ordering becomes a chance floor measured by permutation.

## Context
Current AI research often evaluates multilingual performance by comparing final outputs while ignoring the underlying procedural actions that drive those outputs. This omission can mask failures in tool usage that affect cost, latency, and system robustness. The paper’s focus on action policy measurement aligns with efforts to make AI behavior auditable and reproducible across languages.

## Implications
For practitioners, measuring action retention provides a more honest picture of model reliability when deployed globally. It signals that even large models have language‑specific quirks that must be addressed before trusting cross‑lingual tool use. Future work should adopt these correction methods to avoid overstating performance gains from simple trace extraction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11110v1)
