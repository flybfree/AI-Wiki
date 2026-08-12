---
title: VoxSumm: A Multilingual Corpus of Long-Form Spoken News for Joint Summarization and Translation
url: http://arxiv.org/abs/2608.10359v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_01-33-09Z_VoxSumm_AMultilingualCorpusofLong_FormSpokenNewsfo.md
generated_at: 2026-08-11 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces VoxSumm, a multilingual benchmark for joint speech summarization and translation (JSumT), which creates concise target‑language summaries directly from long spoken news articles. Experiments on 10,045 BBC article pairs across 24 languages show that Gemini3.1‑Pro yields the most consistent results, with English summaries outperforming non‑English ones and full‑document translation before summarization worsening instruction following.

## Key Takeaways
- VoxSumm provides a large cross‑lingual dataset of speech‑language pairs, enabling evaluation of both summarization and translation in one task.  
- The study demonstrates that language‑specific models exhibit varying performance, with English generation generally superior to other languages on the same model.  
- Performing translation before summarization introduces instruction‑following failures, highlighting the importance of joint processing rather than sequential steps.

## Context
This work addresses a gap between long‑form text summarization and multilingual speech research, where most efforts have focused on preserving source content or translating without compression. By integrating both tasks, VoxSumm offers a unified benchmark that reflects real‑world needs for concise, faithful cross‑lingual representations of audio news.

## Implications
For practitioners developing AI systems that must summarize and translate spoken media, the findings suggest prioritizing joint generation to improve consistency and reduce errors. The release of VoxSumm will guide future research on multilingual speech models, encouraging more robust evaluation protocols across languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10359v1)
