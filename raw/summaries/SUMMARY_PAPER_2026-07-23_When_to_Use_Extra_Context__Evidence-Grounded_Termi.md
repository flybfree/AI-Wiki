---
title: When to Use Extra Context: Evidence-Grounded Terminology Adaptation for Simultaneous Speech Translation
url: http://arxiv.org/abs/2607.17766v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_10-00-46Z_WhentoUseExtraContext_Evidence_GroundedTerminology.md
generated_at: 2026-07-23 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EGTA, an Evidence‑Grounded Terminology Adaptation framework for simultaneous speech translation that improves quality on technical talks without fine‑tuning the full model. Experiments on MCIF‑dev and ACL60/60‑dev show gains in BLEU, XCOMET‑XL, named‑entity recall, and acronym recall.

## Key Takeaways
- EGTA builds a document terminology memory and selects compact candidate terms conditioned on the current streaming state to adapt both ASR and decoder decision spaces.  
- The framework yields BLEU improvements of +1.05 (En→Zh) and XCOMET‑XL gains of +0.019, with named‑entity recall rising by 79 % relative to baseline.  
- Acronym recall improves by 0.099 on En→Zh and 0.171 on En→De, and external validation on ACL60/60‑dev confirms consistent gains without additional fine‑tuning.

## Context
This work tackles the problem of providing just enough context to boost translation quality in real‑time streaming while avoiding the inefficiency of injecting entire document contexts. It advances efficient adaptation techniques that preserve low latency and model simplicity, which are crucial for large‑scale deployment.

## Implications
Practitioners can integrate EGTA into existing SimulST pipelines with minimal overhead, delivering measurable quality gains for technical domains where terminology is critical. This supports scalable simultaneous translation in conferences and industry settings without requiring full model fine‑tuning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17766v1)
