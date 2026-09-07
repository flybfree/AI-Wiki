---
title: Safety for Whom? Boundary-Aware Self-Distillation for Controlled LLM Safety Refusal
published: 2026-09-03T21:03:45Z
authors: Alejo López-Ávila, Iker García-Ferrero, Jezabel Garcia, Antonio Tiene, Román Orús
url: http://arxiv.org/abs/2609.04482v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safety for Whom? Boundary-Aware Self-Distillation for Controlled LLM Safety Refusal

## Abstract
Safety alignment is usually posed as a topic-level question: is this subject harmful? Deployments ask a narrower one. A civics tutor and a public-sector assistant may share a base model yet need different boundaries inside the same topic, refusing targeted political manipulation while still answering factual questions about the same election. We formulate this as narrow-boundary safety and introduce an offline self-generated framework combining controlled topic generation, coverage repair, in-distribution compensation data, and harmful-benign pairs for training and evaluation. Single-shot generation leaves 19.88% of prompts without accepted refusal traces, whereas escalating retries leave 0.20%. On political persuasion with Qwen3-8B, training on refusal data completed through Escalate increases target-domain refusal from 9.47% to 84.75% and reduces the mean unsafe-response rate across three broader harmfulness benchmarks from 26.26% to 0.14%, but increases XSTest over-refusal from 2.00% to 74.00%. In a separate matched comparison, replacing external responses with verified target-model responses reduces over-refusal from 15.20% to 5.20%. Boundary-pair data reduces comply-side over-refusal on held-out pairs from 32.94% to 4.16%, while harmful-side refusal decreases only from 91.88% to 87.72%. These results show that data composition controls the safety and usability trade-off, and that safety alignment should be evaluated on both sides of the intended refusal boundary.

## Metadata
- **Published**: 2026-09-03T21:03:45Z
- **Authors**: Alejo López-Ávila, Iker García-Ferrero, Jezabel Garcia, Antonio Tiene, Román Orús
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04482v1)