---
title: MedLLM: An Open Medical Language Model at the Sub-Billion Scale
published: 2026-07-29T22:10:40Z
authors: Maxx Richard Rahman, Asim Ahmed, Mihan Mohagheghzadeh, Wolfgang Maass
url: http://arxiv.org/abs/2607.27490v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MedLLM: An Open Medical Language Model at the Sub-Billion Scale

## Abstract
Open medical language models have converged on a single scale: every widely used system runs at 7B parameters or more, leaving the sub-billion regime uncharacterized. We present MedLLM, an open 0.1B-parameter medical language model trained through a fully open three-phase pipeline: general pretraining with curriculum sequence-length scheduling, domain fine-tuning on MedFineWeb, a reference-guided medical corpus we release that is selected from general web data by embedding similarity to medical question-answering (QA) data, and preference-aligned fine-tuning combining SFT with direct preference optimization (DPO). Across medical benchmarks, MedLLM shows a pattern visible only at sub-billion scale: medical competence does not degrade uniformly under compression but splits by task type. On context-grounded QA it comes within $2.9$pp of a medically adapted 7B model and surpasses the instruction-tuned and general-purpose 7B baselines; on knowledge-recall QA it stays near the task floor on clinical-vignette MedQA yet significantly exceeds every 7B and sub-7B baseline on MedMCQA, indicating that where recall fails the constraint is model capacity rather than adaptation. This dissociation is masked at 7B, where both capabilities are present, and surfaces only when capacity is scarce.

## Metadata
- **Published**: 2026-07-29T22:10:40Z
- **Authors**: Maxx Richard Rahman, Asim Ahmed, Mihan Mohagheghzadeh, Wolfgang Maass
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27490v1)