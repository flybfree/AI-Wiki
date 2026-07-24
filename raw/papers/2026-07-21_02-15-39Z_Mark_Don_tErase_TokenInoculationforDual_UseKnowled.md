---
title: Mark, Don't Erase: Token Inoculation for Dual-Use Knowledge in LLMs
published: 2026-07-21T02:15:39Z
authors: Seunghyun Lee, Dongyoon Han, Sangdoo Yun
url: http://arxiv.org/abs/2607.18639v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mark, Don't Erase: Token Inoculation for Dual-Use Knowledge in LLMs

## Abstract
Safety interventions on dual-use knowledge typically choose between destroying hazardous content (e.g., unlearning, filtering) and suppressing it at the output layer (e.g., refusal training); both pay a tax in adjacent-domain competence or over-refusal. We argue that the right operation is conditioning, not reduction: we show that hazardous knowledge can be retained in the model and behaviorally gated by a privileged control token. Our method, Token Inoculation, introduces a binding-and-branching approach. First, during continued pre-training, we mark hazardous content by inserting a special token alongside dual-use documents, so the model binds the marker to the underlying semantics of the hazardous domain. Second, during supervised fine-tuning, we teach the model to answer hazardous queries correctly when the special token is present and to refuse them when it is absent, thereby enabling selective refusal without removing dual-use knowledge. On hazardous domain (e.g., WMDP-Bio), Token Inoculation reduces accuracy from 79% to 18% while retaining 93% of the base-model's benign-domain performance (e.g., MMLU), achieving the best safety-utility trade-off against unlearning and refusal-tuning baselines across 1B-14B model scales. We further show that refusal selectivity is controllable through the quality of the conditioning signal and that domain-specific semantic binding during pre-training is critical for the conditional behavior to generalize beyond memorized triggers. Our results suggest that safety alignment is better cast as a conditioning problem than a forgetting one: behavioral control is more precise when sensitive knowledge is retained under controlled access than when it is destroyed.

## Metadata
- **Published**: 2026-07-21T02:15:39Z
- **Authors**: Seunghyun Lee, Dongyoon Han, Sangdoo Yun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18639v1)