---
title: When the Judge Should Not Decide: Evidence-Locked, Non-Compensatory Selection Bounds LLM-Judge Failure in Reasoning Pipelines
url: http://arxiv.org/abs/2608.07813v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-07_23-23-00Z_WhentheJudgeShouldNotDecide_Evidence_Locked_Non_Co.md
generated_at: 2026-08-10 22:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how an LLM judge embedded in a reasoning pipeline influences the final answer selection, showing that its impact is driven more by the decision rule than by the judge’s accuracy. On frozen candidate pools from four GRPO policies, an unconstrained DeepSeek‑R1‑7B judge barely improves over simple majority voting, while a task‑adaptive non‑compensatory rule called Evidence‑Locked Derive‑Gate‑Repair (EL‑DGR) can boost performance without ever converting a correct consensus into a wrong answer. The authors also demonstrate that the channel decomposition used for gated training rewards does not contribute to these gains.

## Key Takeaways
- Unconstrained scalar DeepSeek‑R1‑7B judge adds only +1.0 pp on 500 GSM8K questions and +0.34 EM on 300 HotpotQA, indicating negligible benefit over answer‑level majority vote.
- EL‑DGR improves GSM8K to 58.2% (vs 56.8% judge) and HotpotQA EM to 17.33/25.46 (vs 15.67/23.49), overturning consensus only on eight of thirty pilot questions, never reversing a correct answer.
- The seven‑channel decomposition used as a step‑level gated reward is ineffective; channel‑drop analyses yield p = 1.0 for each channel, showing no single channel is necessary.

## Context
Reasoning pipelines increasingly rely on LLM judges to rank or select answers, yet the literature often assumes that higher accuracy directly translates to better outcomes. This work reveals that the decision rule—specifically whether a judge can be overridden by evidence‑based constraints—plays a crucial role in performance, highlighting the need for principled admissibility mechanisms rather than merely maximizing judge confidence.

## Implications
For researchers, the findings suggest focusing on non‑compensatory rules that respect evidence certificates to limit the judge’s blast radius. For industry practitioners, deploying judges with bounded decision thresholds can prevent costly errors while still leveraging their strengths in ranking.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07813v1)
