---
title: TempCloze: Can Video-LLMs Identify the Missing Middle?
url: http://arxiv.org/abs/2609.01515v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_16-45-02Z_TempCloze_CanVideo_LLMsIdentifytheMissingMiddle.md
generated_at: 2026-09-01 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TempCloze, a video cloze benchmark designed to test visual temporal reasoning in Video‑LLMs by asking models to select the correct missing middle from four candidates given only the start and end clips. Evaluation across 10 proprietary and 21 open‑source models shows that while many systems can infer plausible events and local progression, they frequently fail at aligning these elements with the actual timing of the video.

## Key Takeaways
- The benchmark reduces linguistic shortcuts by using same‑source distractors that match semantic asks, alignment probes, and progression tests while sharing scenes and objects to limit visual cues.  
- Alignment is identified as the main bottleneck: models often generate correct content but misplace it in time relative to the video’s actual sequence.  
- Error analysis across TempCloze‑Mixed and TempCloze‑Hard reveals that candidate order, context direction, visible span length, frame density, and test‑time scaling all influence model choices.

## Context
Video‑LLMs aim to understand temporal dynamics in visual sequences, a capability essential for applications like video summarization and action recognition. Prior benchmarks rely heavily on language cues, which can mask true reasoning errors; TempCloze addresses this by focusing purely on visual timing. The findings highlight a persistent gap between content understanding and precise temporal placement.

## Implications
For researchers, TempCloze offers a systematic way to compare Video‑LLM performance across diverse models and datasets. Practitioners should prioritize alignment improvements in their video reasoning pipelines to achieve more reliable outputs for time‑critical tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01515v1)
