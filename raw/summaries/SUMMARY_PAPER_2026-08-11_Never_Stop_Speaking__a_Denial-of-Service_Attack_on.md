---
title: Never Stop Speaking: a Denial-of-Service Attack on End-to-End Speech Language Models
url: http://arxiv.org/abs/2608.10405v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_02-50-30Z_NeverStopSpeaking_aDenial_of_ServiceAttackonEnd_to.md
generated_at: 2026-08-11 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a denial-of-service attack for end-to-end speech language models that exploits imperceptible acoustic perturbations to force the model to generate excessively long outputs while keeping input length unchanged. Experimental results show stable attack success with substantial increase in generation time and GPU usage, highlighting a security gap.

## Key Takeaways
- The attack uses composite optimization that suppresses EOS generation and encourages prolonged decoding while preserving semantic consistency.
- It integrates weighted EOS loss, top-k logit loss, length loss, and semantic alignment loss to control output length.
- Voice activity detection is employed to inject perturbations only in voiced regions, enhancing stealth.

## Context
Speech-to-text and text-to-speech systems have become integral parts of real-time communication platforms, yet their security has received limited attention compared to pure text models. This research underscores the need for robust defenses as these models proliferate in consumer and enterprise applications.

## Implications
For developers, this paper calls for integrated VAD-aware perturbation checks when deploying E2E speech LLMs to mitigate resource exhaustion. Industry stakeholders should prioritize continuous security testing as these models become central to voice assistants and automated transcription services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10405v1)
