---
title: Long-Horizon Embodied Decision-Making via Multimodal Memory Compression
url: http://arxiv.org/abs/2608.01456v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_19-29-48Z_Long_HorizonEmbodiedDecision_MakingviaMultimodalMe.md
generated_at: 2026-08-03 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DunphyBench, a benchmark that tests long‑horizon human‑centered decision making in embodied housing environments. The authors show that current VLM‑driven agents fall short of human performance and identify memory management as a key bottleneck. Their proposed solution MeMento compresses multimodal history using preference‑conditioned compression, boosting accuracy by 7.18% while cutting memory usage to 14.62% of the original.

## Key Takeaways
- DunphyBench reveals a large gap between agent performance and human decision making in long‑horizon tasks.  
- Raw multimodal history adds noise that degrades decision quality, highlighting memory as a bottleneck.  
- MeMento’s preference‑conditioned compression improves accuracy by 7.18% and reduces memory consumption by 85.38%.

## Context
Long‑term human‑centered AI requires agents to retain and interpret extensive multimodal evidence across extended interactions. Memory constraints limit the ability of large language models with vision capabilities to maintain coherent knowledge, a challenge that impacts real‑world applications such as virtual assistants and autonomous navigation.

## Implications
The findings suggest that efficient memory compression is essential for scaling human‑like decision making in embodied AI systems. Practitioners can leverage MeMento’s approach to build agents that are both accurate and resource‑efficient, paving the way for more reliable deployment in complex environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01456v1)
