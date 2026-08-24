---
title: Knowing but Not Saying: Preventing Factual Access Failures in LLM SFT via Recall-Anchored Distillation
url: http://arxiv.org/abs/2608.20794v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_07-11-36Z_KnowingbutNotSaying_PreventingFactualAccessFailure.md
generated_at: 2026-08-23 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper identifies a specific type of factual degradation in large language models after supervised fine-tuning, called factual access failure, where models can still retrieve correct answers under constrained tests but fail to generate them freely. It proposes Recall-Anchored Distillation (RAD) as a method that aligns the adapted model with the original base’s soft continuation distribution on out‑of‑distribution text without needing gold answers or external judges.

## Key Takeaways
- The degradation is not mere forgetting but an access failure where models retain correct rankings yet produce no answer in open generation.  
- Benchmark probes reveal that failures include wrong‑answer generations, verbosity, formatting mismatches and exact‑match artifacts.  
- RAD uses base‑anchored self‑distillation to preserve out‑of‑domain recall by matching the adapted model’s soft distribution on unlabeled OOD text.

## Context
Factual consistency is a recurring challenge in domain adaptation of large language models, where fine‑tuning often sacrifices general knowledge. This work contributes a theoretical framework for understanding access failures and offers a practical distillation technique that does not require additional labeled data or external evaluation.

## Implications
For practitioners, RAD enables safer fine‑tuning pipelines by preserving factual recall without compromising domain adaptation. The approach could be adopted in medical, legal, or any knowledge‑intensive applications where correct answer generation is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20794v1)
