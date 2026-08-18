---
title: What to Forget in Unlearning? Forget Set Curation for Language Models
url: http://arxiv.org/abs/2608.14855v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_19-51-53Z_WhattoForgetinUnlearning_ForgetSetCurationforLangu.md
generated_at: 2026-08-17 21:42
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the missing upstream problem of forget set curation in machine unlearning, showing that mapping a suppression request to the data used by an algorithm is essential for effective unlearning. The authors introduce CleanSlate, a benchmark that tests verbatim output suppression over songs and books, revealing two failure modes: natural lexical curators produce weak suppression sets, while evaluation‑aware curators achieve near‑complete suppression but cause collateral regression and model‑dependent capability loss.

## Key Takeaways
- Natural lexical and exact‑substring curators often yield forget sets that result in only partial or ineffective suppression of the requested content.  
- Evaluation‑aware curators can suppress the targeted continuations almost entirely, yet they introduce significant degradation on unrelated material and cause model‑specific capability loss.  
- The choice of data for forgetting determines both what can be unlearned and what else is damaged, indicating that unlearning is not merely an optimization problem once a forget set is fixed.

## Context
Machine unlearning seeks to remove specific behaviors from trained language models without full retraining, yet most prior work assumes the examples to forget are already known. In large‑scale deployments, users may request suppression of entire works like songs or books without knowing which spans support those behaviors, highlighting a gap between theoretical unlearning and real‑world data mapping.

## Implications
Practitioners must design curation strategies that balance effective forgetting with minimal side effects to avoid unintended degradation. Ignoring this upstream problem can lead to models that appear to comply with requests while losing valuable capabilities, undermining trust in deployed systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14855v1)
