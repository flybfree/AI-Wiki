---
title: Don't Repeat Yourself: Stopping Verbatim Loops at Sampling Time
url: http://arxiv.org/abs/2608.22761v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_03-33-39Z_Don_tRepeatYourself_StoppingVerbatimLoopsatSamplin.md
generated_at: 2026-08-24 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Don't Repeat Yourself DRY, a sampling-time logit adjustment that prevents verbatim loops in large language model text generation. Experiments show it cuts suffix-extension rate by 47% and improves lexical diversity across models from 1.5B to 120B parameters. The approach is effective on both full‑precision and quantized versions.

## Key Takeaways
- DRY penalizes a token only when adding it would create an exact continuation of a span seen earlier in the context, targeting the structural cause of looping.
- The method reduces suffix-extension rate by 47% while preserving or improving lexical diversity across nine prompt families and human studies.
- An intervention-matched placebo shows no effect, confirming that suffix matching is the operative mechanism.

## Context
Large language models generate text autoregressively and often produce verbatim loops where a token sequence repeats an earlier span. Traditional defenses such as repetition penalties focus on token recurrence rather than structural continuity, leading to side effects on fluency and formatting. This paper addresses that limitation by focusing on the exact match of suffixes.

## Implications
For practitioners, DRY offers a lightweight way to reduce looping without harming performance metrics like MT-Bench or MMLU. Its adoption in open-source inference frameworks suggests it will become standard practice for high-quality text generation across commercial and research settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22761v1)
