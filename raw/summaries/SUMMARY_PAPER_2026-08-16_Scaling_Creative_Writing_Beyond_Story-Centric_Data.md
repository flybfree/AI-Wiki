---
title: Scaling Creative Writing Beyond Story-Centric Data with Attribute-Guided Genre Expansion
url: http://arxiv.org/abs/2608.13947v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_04-38-29Z_ScalingCreativeWritingBeyondStory_CentricDatawithA.md
generated_at: 2026-08-16 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an attribute‑guided genre expansion framework that moves creative writing data beyond story‑centric sources to include diverse formats such as rap, lyrics and game design. The authors demonstrate that fine‑tuned models on their 50 K‑example Multi‑Genre Collection outperform both base LLMs and existing writing benchmarks.

## Key Takeaways
- Human‑authored story prompts are used as seeds while manually curated genre attributes enforce distinct structural, stylistic, and formatting conventions for each creative format.  
- The framework produces strong LLM responses that are filtered to retain only high‑quality, genre‑faithful pairs, showing a clear link between controlled expansion and robust performance.  
- Genre‑count ablations reveal that expanding the variety of genres is more effective than merely scaling story data.

## Context
Current large language model training relies heavily on narrative text, which limits their ability to generate content that follows non‑story conventions. This work addresses a gap in the AI literature by providing a systematic method for generating high‑quality examples across multiple creative domains.

## Implications
The approach can be adopted by developers seeking diverse output from LLMs without sacrificing quality, and it may inspire new datasets that balance thematic richness with genre specificity to improve real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13947v1)
