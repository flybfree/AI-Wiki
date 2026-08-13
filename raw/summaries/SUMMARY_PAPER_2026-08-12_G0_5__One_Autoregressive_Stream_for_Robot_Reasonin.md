---
title: G0.5: One Autoregressive Stream for Robot Reasoning and Action
url: http://arxiv.org/abs/2608.11739v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_07-26-47Z_G0_5_OneAutoregressiveStreamforRobotReasoningandAc.md
generated_at: 2026-08-12 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces G0.5, a pretrained autoregressive Vision‑Language‑Action model that jointly generates reasoning and action tokens in a single transformer decoder. By integrating a shared action vocabulary, chain‑of‑thought task decomposition, and a visual memory module, the model can follow instructions directly without additional fine‑tuning. Experiments show G0.5 outperforms prior approaches across seven robotics regimes.

## Key Takeaways
- The model uses a learnable cross‑embodiment action tokenizer to map diverse robot actions into one vocabulary, enabling seamless multimodal tokenization.
- Reasoning and action are interleaved in a single chain‑of‑thought stream that includes task decomposition, object grounding, and action hints, all produced by the same transformer weights.
- A visual memory module injects multi‑second history into the vision encoder, allowing the model to reason over extended temporal contexts.

## Context
G0.5 represents a shift from separate vision‑language models and discrete action experts toward unified foundation models that handle perception, language, and behavior jointly. This approach aligns with trends in multimodal pretraining where single objectives reduce complexity and improve transferability across tasks.

## Implications
For robotics developers, G0.5 offers a ready‑to‑use model that can be prompted to perform specific actions without retraining, lowering deployment costs. Practitioners can leverage its fine‑grained control over task horizon and out‑of‑distribution handling to build more adaptable autonomous agents in real‑world settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11739v1)
