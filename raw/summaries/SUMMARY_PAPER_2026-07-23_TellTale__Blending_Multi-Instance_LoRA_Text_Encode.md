---
title: TellTale: Blending Multi-Instance LoRA Text Encoders and a Zero-Shot LLM Judge for Ambivalence/Hesitancy Recognition in Videos
url: http://arxiv.org/abs/2607.16635v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-18_04-37-20Z_TellTale_BlendingMulti_InstanceLoRATextEncodersand.md
generated_at: 2026-07-23 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TellTale, a text‑only method for detecting ambivalence or hesitancy in interview videos using only the transcript. The approach combines two fine‑tuned multilingual encoders with LoRA adapters and a zero‑shot instruction LLM to produce three probability streams that are merged into a single decision.

## Key Takeaways
- TellTale leverages multiple-instance learning (MIL) to score individual transcript chunks under the supervision of video‑level labels, allowing efficient training without full video inputs.  
- The system integrates a quantized 14B instruction LLM that evaluates each transcript for ambivalence with no fine‑tuning, providing an unsupervised third probability stream.  
- On the private test set, TellTale reaches a macro‑F1 of 0.7364 and average precision of 0.7940, outperforming the vision‑based baseline’s macro‑F1 of 0.2827.

## Context
The study addresses a growing need for interpretable human behavior analysis in video data where visual cues are limited to text transcripts. By focusing on language patterns rather than visual frames, it demonstrates that large language models can capture subtle affective signals when combined with lightweight adapters.

## Implications
This work shows that hybrid multimodal pipelines—mixing trained encoders and zero‑shot LLMs—can achieve competitive performance in real‑world video analysis tasks. Practitioners may adopt such approaches to reduce computational cost while maintaining high accuracy, especially in multilingual interview settings where visual data is sparse.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16635v1)
