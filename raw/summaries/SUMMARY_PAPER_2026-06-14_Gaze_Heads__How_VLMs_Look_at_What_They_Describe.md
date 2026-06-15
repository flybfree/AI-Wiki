---
title: Gaze Heads: How VLMs Look at What They Describe
url: http://arxiv.org/abs/2606.14703v1
type: paper-summary
date: 2026-06-14
source_paper: 2026-06-12_17-59-57Z_GazeHeads_HowVLMsLookatWhatTheyDescribe.md
generated_at: 2026-06-14 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper discovers that vision-language models develop gaze heads—a subset of attention heads that focus on the image region being described, enabling targeted control over generation without retraining. This finding shows that these heads are not random but serve as a dedicated mechanism for describing specific visual areas.

## Key Takeaways
- Gaze heads constitute less than 9% of all attention heads and their attention vectors align precisely with the image tokens the model is currently generating, allowing precise targeting.
- By applying an attention mask to only these gaze heads, the model can be steered to describe any chosen comic panel at 83.1% accuracy, whereas masking random heads has no effect and masking all heads collapses generation.
- The same intervention works on natural COCO images and across model sizes from 2B to 32B parameters, indicating a robust and scalable mechanism.

## Context
Vision-language models generate textual descriptions of visual scenes but lack explicit mechanisms to prioritize which parts of the image should be emphasized. This paper uncovers an internal attention structure that can be manipulated at inference time, offering a new way to influence model behavior without retraining or architectural changes.

## Implications
For researchers and industry practitioners, this mechanism provides a lightweight tool for interactive applications where precise control over generated content is needed. It demonstrates that mechanistic insights from forward passes can translate into practical levers, potentially reducing reliance on costly fine‑tuning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.14703v1)
