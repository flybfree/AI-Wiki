---
title: Capability-Stratified Degradation in Ternary Language Models
published: 2026-08-28T19:22:38Z
authors: Anirudh Malik, M Sparsh Mehra, Poojith Devan
url: http://arxiv.org/abs/2608.28809v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Capability-Stratified Degradation in Ternary Language Models

## Abstract
Extreme low-bit inference offers a route toward smaller models and constrained deployment. Ternary language models restrict weights to $\{-1,0,+1\}$, approaching the limit of $\log_2 3 \approx 1.585$ bits/weight. The practical question for a pretrained model is not simply whether weights can be quantised but which capabilities survive and whether it remains useful for adaptation. We explore this by converting Qwen3.5-0.8B (752M parameters) to ternary weights using 72.4M tokens of quantisation-aware training (QAT). The resulting model, Cloe, is evaluated across 29 benchmarks, representation diagnostics, and downstream fine-tuning. The evidence shows non-uniform degradation. A linear probe recovers 43.76% of MMLU answers from the full-precision teacher's representations but only 26.19% from Cloe (near chance), indicating specialist factual information is lost. However, Cloe retains measurable performance on ten tasks, averaging 77.1% of teacher performance. Crucially, fine-tuning raises Cloe to 89.8% on SST-2 (95.6% of the matched teacher) and reaches 79.4% teacher retention on XSum. We attribute degradation to a combination of quantisation-induced information loss and incomplete recovery due to the limited QAT budget. We also highlight an evaluation pitfall: standard answer-letter scoring failed (Cloe emitted "A" on 98.6% of MMLU questions), necessitating continuation scoring. Ultimately, ternary conversion is unsuitable as a drop-in general replacement yet remains valuable as a compact substrate for task-specific models.

## Metadata
- **Published**: 2026-08-28T19:22:38Z
- **Authors**: Anirudh Malik, M Sparsh Mehra, Poojith Devan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28809v1)