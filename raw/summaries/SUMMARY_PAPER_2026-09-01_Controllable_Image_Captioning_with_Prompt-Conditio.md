---
title: Controllable Image Captioning with Prompt-Conditioned Scene Rewards
url: http://arxiv.org/abs/2609.00709v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_04-36-23Z_ControllableImageCaptioningwithPrompt_ConditionedS.md
generated_at: 2026-09-01 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FoCUS, a controllable image captioning method that lets users direct the model toward specific semantic emphases using natural‑language prompts. By aligning generated captions with scene‑graph components and weighting them according to the prompt, FoFUS achieves fine‑grained control over attribute, relation, or region focus. Experiments show improved controllability and quality without harming overall caption performance.

## Key Takeaways
- The method uses a prompt‑conditioned objective that parses captions to scene‑graph components and assigns differential weights, including negative weights, based on user emphasis.
- It employs GRPO for optimization and adds a stricter object validity threshold plus reasoning‑based verification to boost reliability of component scores.
- Evaluation via SCoPE demonstrates consistent gains in both target content coverage and out‑of‑scope suppression across two VLM backbones.

## Context
Controllable generation is a key challenge in multimodal AI, where models generate fluent text but lack user‑specified focus. FoFUS addresses this by integrating scene‑graph alignment with reinforcement learning, offering a principled way to steer outputs without sacrificing fluency. This approach aligns with trends toward interpretable and controllable generative systems.

## Implications
For developers, FoFUS provides a practical framework to create captions that highlight desired elements, improving user experience in applications like visual search or content moderation. Practitioners can leverage the method to produce more precise and reliable outputs, supporting higher‑value use cases where fine control is essential.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00709v1)
