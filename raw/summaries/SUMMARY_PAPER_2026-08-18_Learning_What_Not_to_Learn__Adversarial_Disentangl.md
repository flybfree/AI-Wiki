---
title: Learning What Not to Learn: Adversarial Disentangled Prompt Tuning for Robust Vision-Language Models
url: http://arxiv.org/abs/2608.17306v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_03-00-27Z_LearningWhatNottoLearn_AdversarialDisentangledProm.md
generated_at: 2026-08-18 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ADAPT, an adversarial prompt tuning method that addresses overfitting to seen classes in vision‑language models. By using a dual‑prompt mechanism with decoy prompts that capture pseudo‑robust features and a target prompt forced orthogonal to them, the framework learns robust features while preventing degradation on unseen classes.

## Key Takeaways
- ADAPT employs decoy prompts to entrap diverse pseudo‑robust features, which are then isolated from the target prompt through an orthogonal loss.  
- The orthogonal loss provides a theoretical bound that limits how much these decoy features affect performance on unseen classes.  
- Experiments show that ADAPT markedly improves robustness of the target prompt when tested on adversarial examples of previously unseen classes.

## Context
Current robust training methods often overfit to the data seen during fine‑tuning, causing a sharp drop in generalization to novel inputs. This issue is especially pronounced in vision‑language models where prompts are crucial for aligning visual and textual information. The need for frameworks that separate genuine robustness from learned shortcuts remains an open challenge.

## Implications
For practitioners, ADAPT offers a practical way to maintain high accuracy while defending against adversarial attacks without sacrificing performance on new tasks. In industry, adopting such disentangled prompt tuning can lead to more reliable AI systems in safety‑critical applications where unseen scenarios are common.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17306v1)
