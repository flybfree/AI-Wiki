---
title: Candidate supply and answer selection shape the value of LLM judging in multi-agent systems
url: http://arxiv.org/abs/2608.25937v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_15-52-20Z_CandidatesupplyandanswerselectionshapethevalueofLL.md
generated_at: 2026-08-26 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how candidate generation, peer communication, and answer selection interact in multi‑agent systems when an LLM judge supplies correctness signals. It finds that correct answers often exist among candidates but may still be reported incorrectly, and that the reliability of the judge depends on task difficulty and rarity of correct answers.

## Key Takeaways
- A correct answer is frequently generated but can be outnumbered by popular errors, leading to wrong selection despite its presence.
- Judge reliability varies with the specific question set, generator model, and how rare the right answer is, rather than being a static property.
- Adding more candidates that make correct answers visible improves final accuracy from 63.82% to 70.82‑70.95% by rescuing under‑represented correct options.

## Context
Multi‑agent reasoning systems rely on iterative generation and selection, yet current designs often lack mechanisms to protect high‑quality answers from being drowned out by common mistakes. This work provides a diagnostic framework for understanding these dynamics across diverse benchmarks.

## Implications
Designers can prioritize candidate diversity and integrate judge signals that reflect rarity to boost system accuracy. The findings guide architecture choices in MAS, ensuring correct reasoning is not lost in consensus formation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25937v1)
