---
title: Learning When to Withdraw: Curriculum Coverage and Rule-Specific Failures in Fine-Tuned Language Agents
url: http://arxiv.org/abs/2610.21045v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_00-38-39Z_LearningWhentoWithdraw_CurriculumCoverageandRule_S.md
generated_at: 2026-10-15 23:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether supervised fine-tuning (SFT) of language agents can teach them to selectively withdraw prepared actions when evidence changes or authority is revoked, using a synthetic environment called NAQD-Env with explicit dependencies and a deterministic reference policy. The study compares four LoRA-tuned Qwen2.5-3B-Instruct checkpoints trained on original versus enriched curricula against instruction-tuned baselines, finding that SFT checkpoints achieve substantially higher decision agreement and withdrawal recall but also introduce rule-specific regressions—such as over-withdrawing actions that retain alternative support and under-withdrawing in prohibited combinations absent from training curricula.

## Key Takeaways
- Under the naqd prompt, SFT checkpoints achieve decision agreement of 0.77–0.92 and withdrawal recall of 0.46–0.86, dramatically outperforming three instruction-tuned baselines that reach only 0.45–0.63 agreement and at most 0.06 withdrawal recall, demonstrating that targeted fine-tuning can teach agents a withdrawal behavior they otherwise lack.
- Rule-level diagnostics reveal critical failures hidden by aggregate accuracy: the original-curriculum checkpoint wrongly withdraws 26 of 34 actions that still have surviving alternative support, while enriched checkpoints reduce this error to 0–1 cases. Conversely, all SFT checkpoints under-perform 7B and 8B baselines on narrowing prohibited combinations—a scenario absent from both training curricula—showing that fine-tuning can create blind spots in unrepresented rule categories.
- Delegation evaluations expose a trade-off: SFT checkpoints show more withdrawal behavior but poorer preservation of independently authorized actions, and all four checkpoints omit valid event reports entirely. The authors explicitly caution that one training run per arm, jointly changed curriculum properties, prior evaluation exposure, and quantization differences between baselines and SFT models limit causal attribution, framing the contribution as a detection method for rule-specific regressions rather than proof that fine-tuning ensures agent safety.

## Context
As language agents increasingly interact with external tools, APIs, and authority structures, the ability to revise or suspend actions when upstream evidence changes is a core safety requirement. Most current agent research focuses on improving task completion or tool-use accuracy, leaving selective withdrawal and dependency-aware reasoning underexplored. This paper addresses that gap by constructing a controlled synthetic environment with explicit dependency graphs and a deterministic reference policy, enabling precise measurement of when agents correctly suspend versus incorrectly preserve or over-withdraw actions.

## Implications
For practitioners deploying tool-using agents in regulated or multi-authority settings, this work demonstrates that aggregate accuracy metrics can conceal dangerous rule-specific regressions introduced by fine-tuning, making per-rule diagnostics essential before production deployment. It also signals that curriculum design for agent training must explicitly cover edge cases like prohibited combinations and independently authorized actions, since models trained on incomplete curricula will systematically fail in unrepresented scenarios. The finding that larger instruction-tuned baselines outperform smaller fine-tuned models on certain rules further cautions against assuming that domain-specific fine-tuning universally improves agent safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21045v1)
