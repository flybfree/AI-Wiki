---
title: Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents
url: http://arxiv.org/abs/2610.23254v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_10-26-23Z_Ignored_NotRefused_WhatLowPrompt_InjectionSuccessR.md
generated_at: 2026-10-18 20:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper challenges the standard evaluation methodology for indirect prompt injection (IPI) attacks against tool-using language agents, revealing that low Attack Success Rates (ASR) reported by benchmarks like InjecAgent and AgentDojo do not indicate genuine security defenses. Through an audit of 33,000 trajectories across eleven open-weight agents (2–14B parameters), the authors demonstrate that the vast majority of "failed" attacks are silently ignored by the agent rather than actively refused, and that a low ASR can mask a failure to complete the user's original task. The authors introduce the Attack-Task Outcome Matrix (ATOM) to disentangle security outcomes from task-completion outcomes.

## Key Takeaways
- A label-blind LLM judge applied to 33,000 agent trajectories shows that 76–80% of failed IPI attacks are "ignored" (the agent simply does not act on the injected instruction) rather than "refused" (the agent actively rejects the injection). Only 17–18% of failures involve genuine refusal behavior, meaning current ASR metrics conflate two fundamentally different failure modes and overstate agent robustness.
- With identical model weights, merely changing the system prompt shifts the InjecAgent ASR from 0.2% to 43%, demonstrating that reported security scores are highly sensitive to prompt configuration rather than reflecting intrinsic model robustness. This undermines the reliability of benchmark-based security claims for small tool-using agents.
- The Attack-Task Outcome Matrix (ATOM) reveals that in 21.7% of AgentDojo episodes, the agent remained "safe" from injection attacks but simultaneously failed to complete the user's intended task. A low ASR therefore does not guarantee functional reliability, and evaluations that report only ASR miss a substantial category of task failures that users would experience as broken agent behavior.

## Context
Indirect prompt injection is a recognized security threat for autonomous agents that ingest untrusted external content such as web pages, emails, or tool outputs. The field has largely standardized on ASR as the primary security metric, assuming that any attack not changing the agent's tool call constitutes a successful defense. This paper situates itself within the growing critique of benchmark-based evaluation in LLM security, showing that the binary success/failure framing of ASR obscures the behavioral mechanism by which agents handle injections. The work targets small open-weight models (2–14B parameters), which are increasingly deployed in production agent pipelines where computational constraints limit the use of larger, more robust models.

## Implications
For practitioners deploying tool-using agents in production, the findings indicate that a low ASR on public benchmarks should not be interpreted as evidence of security: agents may simply be ignoring injected content while also failing to complete user tasks, producing silent degradation rather than visible attacks. Benchmark designers and security evaluators should adopt multi-dimensional reporting that separates refusal from ignorance and tracks task-completion rates alongside ASR, as the authors recommend. The release of the labeled corpus, judge prompt, and analysis code provides a reproducible foundation for re-evaluating existing agent security claims and for designing more faithful evaluation protocols in future agent safety research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23254v1)
