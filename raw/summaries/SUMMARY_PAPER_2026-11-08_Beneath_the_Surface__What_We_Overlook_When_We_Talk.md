---
title: Beneath the Surface: What We Overlook When We Talk About Agent Evolution
url: http://arxiv.org/abs/2611.07624v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-05_08-06-37Z_BeneaththeSurface_WhatWeOverlookWhenWeTalkAboutAge.md
generated_at: 2026-11-08 21:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether agent harness evolution—a form of recursive self-improvement (RSI) that modifies the scaffolding around a language model rather than its weights—produces improvements that are reliable, efficient, and transferable. Through systematic evaluation of four evolution methods across general and coding task pools, the authors demonstrate that evolved agents consistently trade off previously covered capabilities for newly acquired ones, that higher benchmark scores do not guarantee the broadest practical improvement, and that transfer of gains across task domains is highly selective. The authors propose preservation-aware evaluation protocols and introduce EvoAudit, a constructive revision of the select-analyze-mutate-gate pipeline, as a corrective framework.

## Key Takeaways
- Every one of the sixteen evolved agents gained previously uncovered tasks while simultaneously losing previously covered ones, revealing a fundamental trade-off in harness evolution: improvement is not purely additive but involves capability displacement. In one general-task case, reliability increased by 5.2 benchmark points even as ten previously covered tasks were lost, showing that aggregate scores can mask significant regressions.
- Reliability gains from harness evolution typically increase deployment cost, and specific, targeted modifications to agent components outperform generic prompting reminders. However, the benefits of individual changes can shift or cancel when combined, meaning naive composition of improvements is unreliable. The highest-scoring agent in any pool did not produce the largest mean improvement across tasks, and stricter admission criteria during evolution can discard genuinely useful alternative strategies.
- Transfer of evolved capabilities is highly selective and context-dependent. Coverage generally declined on the general-task target across both harness types and paradigms, but rose on the coding target when only the outer-layer harness was evolved. This asymmetry underscores that transferability cannot be assumed and must be explicitly tested under defined applicability conditions.

## Context
Recursive self-improvement through harness or scaffolding evolution has emerged as a practical alternative to fine-tuning model weights, enabling agents to iteratively refine their tool-use strategies, planning loops, and evaluation gates without costly retraining. This paper matters because the field has largely celebrated benchmark-score gains from such evolution without interrogating whether those gains are stable, whether they regress previously solved capabilities, or whether they transfer across domains. By introducing controlled agent expansion, component interventions, admission replays, and repeated evaluations, the authors expose systematic failure modes that prior work has overlooked, shifting the conversation from "does evolution improve scores?" to "what exactly is being gained, lost, and transferred?"

## Implications
For practitioners building self-improving agent systems, this work argues that evaluation pipelines must incorporate preservation-aware metrics—tracking not just new task coverage but the retention of previously solved tasks—before accepting evolved harnesses into production. Industry teams deploying agent frameworks should treat benchmark leaderboards as insufficient evidence of robust improvement and instead adopt tested decision rules with explicit applicability conditions for transfer. The proposed EvoAudit framework offers a concrete, implementable revision to standard evolution loops, giving engineers a diagnostic-to-revision workflow that can reduce the risk of silent capability regressions in continuously evolving agent systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.07624v1)
