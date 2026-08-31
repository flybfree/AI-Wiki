---
title: When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI
url: http://arxiv.org/abs/2608.28518v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_16-55-32Z_WhenRobotsMishearUs_MappingtheSafetyRisksofVoice_C.md
generated_at: 2026-08-30 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper examines how automatic speech recognition (ASR) mistakes can compromise the safety of embodied AI systems by allowing harmful instructions to be interpreted and acted upon. The authors demonstrate that certain ASR errors preserve the surface meaning while creating dangerous ambiguities, whereas others directly weaken the model’s refusal mechanisms, enabling unsafe plans to be generated. Overall, ASR failures introduce significant safety risks for voice‑controlled robots.

## Key Takeaways
- ASR errors can produce harmful instructions that are semantically similar but ambiguous enough to mislead embodied AI into executing unsafe actions.
- Some errors specifically reduce the model’s refusal behavior, allowing unsafe plans to be generated and carried out without detection.
- Automatic correction of these errors sometimes mitigates risk, yet it is not universally effective.

## Context
Voice‑controlled robots rely on ASR pipelines to translate spoken commands into programmatic actions. As these systems become more integrated in daily environments, any flaw in the speech layer can propagate to real‑world behavior. This research highlights a previously overlooked failure point that could undermine user safety and trust.

## Implications
For developers, the findings stress the need for robust ASR validation and error handling within embodied AI pipelines. Industry stakeholders should prioritize testing scenarios where misheard commands might lead to unsafe outcomes, ensuring that corrective mechanisms are both reliable and comprehensive.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28518v1)
