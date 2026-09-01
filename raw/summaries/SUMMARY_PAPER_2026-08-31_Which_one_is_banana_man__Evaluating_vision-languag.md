---
title: Which one is banana man? Evaluating vision-language models in multi-turn pragmatic interpretation
url: http://arxiv.org/abs/2608.29571v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_05-36-41Z_Whichoneisbananaman_Evaluatingvision_languagemodel.md
generated_at: 2026-08-31 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how vision‑language models handle multi‑turn pragmatic reasoning by playing iterated reference games with humans. The authors find that while human participants consistently succeed, the evaluated models can use prior context but fail to accumulate it effectively for later turns. Their results highlight a gap in the models’ ability to build and maintain relevant linguistic context.

## Key Takeaways
- Humans reliably track referents across multiple game rounds, whereas vision‑language models often lose track of earlier references when new information is introduced.  
- The models can access some prior context but struggle to integrate it with current descriptions to infer the intended meaning.  
- This limitation suggests that current multimodal systems lack a core skill for efficient collaborative language understanding.

## Context
The study contributes to AI research on contextual reasoning by showing that multi‑turn pragmatic tasks remain challenging for vision‑language models despite advances in image and text understanding. It underscores the need for better mechanisms that preserve and update conversational state across turns, which is essential for natural human‑AI interaction.

## Implications
For developers building chatbots or assistants, this research warns against assuming that prior context will automatically guide model responses; explicit strategies are needed to maintain referential coherence. In industry practice, it may lead to more robust dialogue systems that prioritize stateful memory over static inference.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29571v1)
