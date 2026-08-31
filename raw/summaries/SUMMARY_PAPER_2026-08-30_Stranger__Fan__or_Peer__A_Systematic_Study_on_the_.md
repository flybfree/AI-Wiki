---
title: Stranger, Fan, or Peer? A Systematic Study on the Role of Interlocutor in Persona-Based Dialogue Generation
url: http://arxiv.org/abs/2608.28467v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_15-53-14Z_Stranger_Fan_orPeer_ASystematicStudyontheRoleofInt.md
generated_at: 2026-08-30 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the visibility of speaker biographies during training, inference, and evaluation influences persona-based dialogue generation. It finds that training-time biography visibility is more decisive than inference-time visibility in determining whether models express traits or copy text, and that asymmetric disclosure leads to leakage into interlocutor turns.

## Key Takeaways
- Training-time visibility matters more than inference-time visibility for persona expression; when biographies are visible during training the model generates traitful dialogue, but if only visible at inference it defaults to copying biographical text.
- Changing biography visibility solely at inference time has a weaker and less consistent impact on output compared with altering both training and inference stages.
- When only the interlocutor sees the target’s biography, traces of that biography appear in the interlocutor's generated turns more often, making those dialogues easier for the judge to detect.

## Context
Persona-based dialogue systems rely on speaker biographies to shape responses, yet most research treats biography visibility as a single factor across all stages. This work highlights that separating training, inference, and evaluation can reveal hidden artifacts in model behavior.

## Implications
Practitioners must design data pipelines that control biography exposure at each stage to avoid unintended text copying and leakage. Ignoring this factor could degrade system performance and create misleading evaluations of persona fidelity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28467v1)
