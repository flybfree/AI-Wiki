---
title: Learning When to Withdraw: Curriculum Coverage and Rule-Specific Failures in Fine-Tuned Language Agents
published: 2026-10-15T00:38:39Z
authors: Mohamed Abouzahra
url: http://arxiv.org/abs/2610.21045v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning When to Withdraw: Curriculum Coverage and Rule-Specific Failures in Fine-Tuned Language Agents

## Abstract
Tool-using language agents must revise prepared actions when evidence changes or authority is revoked. Selective withdrawal means suspending affected actions, preserving supported work, and resuming only after sufficient repair. We study supervised fine-tuning in NAQD-Env, a synthetic environment with explicit dependencies and a deterministic reference policy. Four LoRA checkpoints of Qwen2.5-3B-Instruct compare an original curriculum with an enriched one, the latter under three system-prompt framings with identical views and targets. Three instruction-tuned baselines and all four checkpoints are evaluated under three inference prompts on fresh validation cases, held-out dependency families, and held-out structural combinations. Under the naqd prompt, SFT checkpoints reach decision agreement of 0.77-0.92 and withdrawal recall of 0.46-0.86, versus 0.45-0.63 and at most 0.06 for the baselines. Rule-level diagnostics qualify these gains. The original-curriculum checkpoint wrongly withdraws 26 of 34 actions with surviving alternative support; enriched checkpoints withdraw 0-1. Conversely, all SFT checkpoints narrow prohibited combinations less often than the 7B and 8B baselines, a case absent from both curricula. Delegation results show more withdrawal but poorer preservation of independently authorized actions, and all four checkpoints omit valid event reports. Framing contrasts vary across metrics and splits and do not establish a reproducible advantage or equivalence. One training run per arm, jointly changed curriculum properties, prior evaluation exposure, and baseline-SFT quantization differences limit causal attribution. The contribution is a method for detecting rule-specific regressions that aggregate accuracy can conceal, not evidence that fine-tuning alone ensures agent safety.

## Metadata
- **Published**: 2026-10-15T00:38:39Z
- **Authors**: Mohamed Abouzahra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21045v1)