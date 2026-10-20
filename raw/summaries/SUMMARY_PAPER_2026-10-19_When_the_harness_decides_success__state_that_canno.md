---
title: When the harness decides success: state that cannot be re-observed
url: http://arxiv.org/abs/2610.26632v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_15-59-13Z_Whentheharnessdecidessuccess_statethatcannotbere_o.md
generated_at: 2026-10-19 23:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how agent harnesses—the systems that control what a language model sees across conversation turns—directly determine whether an agent succeeds or fails, rather than merely affecting computational cost. Through a pre-registered synthetic probe and decomposition of the ARC-AGI-3 benchmark, the author demonstrates that context management choices such as truncation, summarization, and reasoning replay produce dramatically different success outcomes, with a 92.5-percentage-point swing depending on whether critical information can be re-observed.

## Key Takeaways
- In a pre-registered synthetic probe, truncating the context window had zero effect on a low-cost reasoning model's success when a needed fact could be looked up again, because the model simply re-queried the fact. However, when the fact could not be re-observed, success dropped to chance level, producing a 92.5-percentage-point penalty (90% CI [89.5, 95.5]). A replication on a model from a second provider confirmed the same contrast, and the model chose to abstain rather than guess once the fact was lost.
- On ARC-AGI-3, the benchmark's Standard harness trails its Provider Adapter harness by a 63-point gap. Decomposing this gap component by component for one model across four games, the author finds that summarizing old turns instead of dropping them—while preserving the Standard harness's invitation to take notes—recovers 86% of the gap without replaying the model's reasoning. Removing the invitation recovers only 43%, and adding the provider's native reasoning replay recovers the remaining 57%. These are point estimates from single counted runs per configuration.
- In both published and the author's own runs, the Adapter's advantage in clearing a level already reached is larger at deep levels than at early ones. The author explicitly cautions that this largely restates where runs stopped and does not cleanly separate a growing advantage from a constant one.

## Context
As large language model agents are deployed in increasingly complex multi-turn workflows, the harness layer—the scaffolding that decides which prior turns, summaries, and reasoning traces are fed back to the model—has become a critical but under-studied component. Most benchmarking work treats the harness as a fixed, neutral wrapper, yet this paper shows that harness design choices are themselves decisive determinants of agent performance. The ARC-AGI-3 benchmark, designed to test abstract reasoning and generalization, becomes a case study in how harness architecture can inflate or deflate apparent model capability by tens of percentage points, raising questions about what benchmark scores actually measure.

## Implications
For practitioners building agent pipelines, this work argues that harness configuration should be treated as a first-class engineering variable alongside model selection, because the same model can succeed or fail entirely based on whether its context management permits re-observation of critical facts. For the research community, the findings caution against interpreting benchmark gaps as purely model-quality differences when they may be substantially attributable to harness design choices such as summarization versus truncation or the presence of note-taking invitations. Industry teams deploying agents in production should audit their harnesses for scenarios where information loss is irreversible, since the penalty in those cases is not a gradual degradation but a collapse to random performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26632v1)
