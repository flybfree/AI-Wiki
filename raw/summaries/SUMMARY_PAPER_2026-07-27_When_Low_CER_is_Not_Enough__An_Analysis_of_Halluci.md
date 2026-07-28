---
title: When Low CER is Not Enough: An Analysis of Hallucinations in Vision-Language OCR Systems on Historical Uruguayan Documents
url: http://arxiv.org/abs/2607.24077v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_07-19-00Z_WhenLowCERisNotEnough_AnAnalysisofHallucinationsin.md
generated_at: 2026-07-27 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates both traditional OCR and vision-language model approaches on the Berrutti dataset of Uruguayan dictatorship-era documents, showing that while VLM-based systems achieve lower character error rates, they also generate systematic errors such as orthographic normalization, spurious content, and semantic substitutions. These hidden failures are not captured by standard CER and WER metrics.

## Key Takeaways
- The Berrutti dataset reveals that VLM OCR improves quantitative accuracy but introduces invisible semantic distortions, especially for named entities.
- Errors like orthographic normalization can replace correct characters with similar-looking ones without raising error rates.
- Spurious content generation adds irrelevant text that preserves fluency yet changes meaning.

## Context
Vision-language models have become dominant in multimodal AI tasks, delivering state‑of‑the‑art results on benchmark datasets. However, their deployment in archival transcription is rarely assessed beyond character‑level metrics, leaving a gap between reported performance and real‑world reliability.

## Implications
Practitioners must adopt evaluation frameworks that measure semantic fidelity rather than only CER or WER to ensure accurate historical transcriptions. Ignoring these hidden failures could lead to misinterpretations of sensitive archival information and erode trust in AI‑driven digitization projects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24077v1)
