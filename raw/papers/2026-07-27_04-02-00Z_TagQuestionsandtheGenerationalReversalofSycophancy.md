---
title: Tag Questions and the Generational Reversal of Sycophancy Across 45 Language Models
published: 2026-07-27T04:02:00Z
authors: Tapan Parikh
url: http://arxiv.org/abs/2607.23976v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tag Questions and the Generational Reversal of Sycophancy Across 45 Language Models

## Abstract
Appending a two-word confirmation tag to a decision question -- "Is X the better choice?" versus "X is the better choice, right?" -- changes whether a language model endorses the choice. We measure this tag effect on 20 frozen, ground-truth-free decisions between two defensible options, counterbalanced so a model's own preferences cancel, scored by exact match on clamped yes/no replies -- no LLM judge, no embeddings. Across 45 models the effect spans +32% to -32% -- a 64-point swing on one word -- with 5 models significantly sycophantic and 17 significantly resistant (BH-FDR q=.10). The sign is a clock: within model families the effect crosses from positive to negative as generations advance (GPT +4 to -28; Claude +7 to -32; Qwen and Grok likewise), roughly -6 points per year, a reversal robust to vendor tier; one lineage (DeepSeek) never crosses, and two releases during the study window (Claude Opus 5, Gemini 3.6 Flash) land on the trend out-of-sample. A full-panel ablation localizes the resistance as a double dissociation: a synonym tag reproduces each model's response almost exactly (r=0.89), while planting the same preference without a tag produces resistance in no resistant model (stance effects +6 to +49; r=0.23 with tag effects). The resistance is keyed to the surface construction of a tacked-on agreement bid, not the user's stance -- a pattern-match, not a principle. And the tag's polarity matters more than its presence: swap one word -- "X is the better choice, maybe?" -- and agreement rises above the neutral baseline in 45 of 45 models (+19.6 points), with ten models affirming both mutually exclusive options at 90-100%. Agreement tracks how sure the user sounds, in opposite directions at the two poles. The instrument is one word, one dollar, and judge-free; run per release, it reads the field's anti-sycophancy training directly off model behavior.

## Metadata
- **Published**: 2026-07-27T04:02:00Z
- **Authors**: Tapan Parikh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23976v1)