---
title: From Recovery to Drop-off: How Action Post-training Reduces a VLM's Late-Layer Depth Decodability
url: http://arxiv.org/abs/2608.08904v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_20-31-52Z_FromRecoverytoDrop_off_HowActionPost_trainingReduc.md
generated_at: 2026-08-10 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how action post‑training degrades a vision‑language model’s ability to decode depth, a key spatiogeometric primitive. It discovers that while the base model improves depth decoding across its layers, the VLA built from it shows an additional late‑layer drop called the cliff, worsening performance at deeper stages.

## Key Takeaways
- The VLA consistently underperforms the base model on depth perception, a persistent gap termed the floor.  
- A later‑layer collapse, the cliff, is observed only in the VLA’s deep layers where MLP writes accumulate.  
- Ablating the late‑layer MLP recovers most of the terminal decodability loss, whereas interventions in attention or the base model do not.

## Context
The study highlights a tension between early and late layer behavior in large multimodal models after joint vision‑language‑action training. Understanding this divergence helps explain why certain capabilities persist while others vanish, offering insight into the stability of hierarchical representations under additional task constraints.

## Implications
For practitioners, the findings suggest that action post‑training can unintentionally harm deep spatial reasoning, prompting a need for regularization or selective layer interventions. In industry, models deployed in robotics must be monitored for such late‑layer regressions to maintain reliable depth perception.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08904v1)
