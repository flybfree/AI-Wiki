---
title: Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection
url: http://arxiv.org/abs/2609.32691v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_14-53-42Z_SilentFailuresinAgenticSecurityEvaluation_AValidat.md
generated_at: 2026-09-28 20:33
model: qwen3.6-35b-a3b
---

## Summary
This paper audits existing benchmarks for evaluating defenses against indirect prompt injection in LLM agents, exposing critical defects that generate misleading security metrics and invalidate prior claims. By quantifying distortions caused by issues like silent payload failures and flawed scoring mechanisms, the author demonstrates that reported attack success rates can be drastically inflated or deflated due to evaluation artifacts rather than actual model behavior. A validated harness is released to enforce rigorous validation standards, overturning previous findings about model capabilities and providing accurate measures for agent security, tool-calling utility, and defense efficacy.

## Key Takeaways
- The audit identifies four defect classes in IPI evaluation harnesses, including silent payload non-delivery where attacks fail to reach the model but are counted as successes, and scoring based on tool identity rather than malicious arguments, which yields implausibly high

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32691v1)
