---
title: HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks
published: 2026-07-21T08:58:36Z
authors: Haozhe Jia
url: http://arxiv.org/abs/2607.18867v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks

## Abstract
Large language models leak parametric knowledge of realized outcomes into historical financial decision tasks. Existence is settled; what users lack is a cheap way to audit a given model for it. We present HindsightBench, a black-box behavioral audit protocol that profiles parametric hindsight in any time-indexed LLM decision task at probe-level cost (no backtests, no logprobs, no corpus access). The protocol chains a four-arm date-manipulation matrix (revealed/date-only/masked/transplanted), dual memory probes (date recovery; outcome recall), and six per-model metrics -- trigger strength, transplant effect, post-cutoff placebo, recoverability, behaviorally effective knowledge cutoff, and a recall-accuracy dissociation coefficient -- with explicit gates where identifiability is data-dependent. Applying it to 15 models from seven vendors on a 258-node vintage-correct macro panel yields three headline patterns: (i) the date-trigger reflex tracks training generation, not scale -- absent across the 2024 open-weight generation from 1B to 70B, present in every tested 2026-generation model, and switching on within one vendor lineage (Qwen3 -> Qwen3.6) at fixed MoE architecture and 3B active parameters; (ii) effective cutoffs span 22 months across vendors and precede vendor-reported dates by up to eight months, invalidating calendar-window placebo designs; (iii) audit results are not invariant to serving -- BF16 serving of an FP8-referenced model breaks the trigger estimate's stability while AWQ-INT4 preserves it, and a provider-locked reasoning regime makes one probe non-convergent -- so the protocol ships with operational requirements (pin quantization and thinking regime; disclose parser and sampling policy). We release the panel, frozen preregistrations, per-model audit rows with measured dollar costs, transcripts, and one-command regeneration.

## Metadata
- **Published**: 2026-07-21T08:58:36Z
- **Authors**: Haozhe Jia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18867v1)