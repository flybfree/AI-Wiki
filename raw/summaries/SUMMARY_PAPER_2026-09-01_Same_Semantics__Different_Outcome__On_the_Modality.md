---
title: Same Semantics, Different Outcome: On the Modality Robustness of Multimodal LLMs under Knowledge Conflict
url: http://arxiv.org/abs/2609.00550v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_01-37-18Z_SameSemantics_DifferentOutcome_OntheModalityRobust.md
generated_at: 2026-09-01 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how multimodal large language models handle evidence that conflicts with their internal knowledge when presented in different modalities such as text or image. It tests thirteen MLLMs on two datasets and discovers that the models are not robust to this conflict, showing systematic biases toward contradictory information.

## Key Takeaways
- When an image contradicts a model’s stored facts, the model is more likely to follow the visual cue than the textual description.
- If both a conflicting text and image are given at the same time, the model’s choice of which modality to trust becomes essentially random, varying with how the inputs appear in order, which model is used, or which dataset provides the data.
- Simple prompting strategies such as steering or direct preference optimization fail to stabilize the behavior; only supervised fine‑tuning yields a modest improvement.

## Context
Multimodal models are central to applications like retrieval‑augmented generation where images and text must be fused. Their reliability directly impacts system performance and user trust.

## Implications
For practitioners, this instability means that even well‑designed pipelines can produce erratic outputs when faced with conflicting evidence, undermining confidence in automated decision making. It also highlights the need for robust training practices across multiple stages of model development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00550v1)
