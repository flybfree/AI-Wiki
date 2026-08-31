---
title: COVER: Identifiable Evaluation of Coalition Routing
url: http://arxiv.org/abs/2608.28475v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_16-01-07Z_COVER_IdentifiableEvaluationofCoalitionRouting.md
generated_at: 2026-08-30 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces COVER, a method to evaluate coalition routing effects by fixing downstream stack G and the legal team family, thereby providing exact regret bounds. Experiments on MuSiQue‑12 and HotpotQA‑4 demonstrate that controlled controls can reduce regret from 0.532 to 0.402 and from 0.313 to 0.110, confirming measurable improvement without universal gains.

## Key Takeaways
- COVER defines an evaluation contract that isolates routing impact via a fixed public information boundary and a finite legal team family.
- A pre‑specified positive control reduces regret on MuSiQue‑12 from 0.532 to 0.402, showing measurable improvement.
- The declared‑family oracle achieves 0.768 safe‑evidence completion while the router gets 0.637, failing its 0.10 criterion.

## Context
This work tackles the challenge of attributing performance changes in multi‑agent systems to routing mechanisms rather than downstream stack limitations. By offering a rigorous, auditable metric (regret) under controlled conditions, it advances transparent AI system evaluation and supports honest reporting of improvements.

## Implications
Practitioners can use COVER to audit whether team selection truly improves outcomes without overstating gains. The methodology encourages careful experimental design in AI collaboration research and highlights the need for controlled experiments when claiming routing superiority.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28475v1)
