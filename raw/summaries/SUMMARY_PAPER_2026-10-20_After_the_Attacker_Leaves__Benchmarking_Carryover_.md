---
title: After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents
url: http://arxiv.org/abs/2610.28425v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_15-55-05Z_AftertheAttackerLeaves_BenchmarkingCarryoverAttack.md
generated_at: 2026-10-20 22:05
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces CarryoverBench, a benchmark that evaluates how one-time indirect prompt injections planted in LLM agent memory files or scheduled tasks can re-fire across multiple sessions long after the original attacker has left. The authors find that across five frontier models, planted payloads re-fire without measurable decay over five rounds, and that the trigger stage often provides little additional protection once a payload has been successfully planted, indicating a persistent and under-measured threat vector in agentic systems.

## Key Takeaways
- LLM agents persist state through two channels—long-lived memory files silently prepended to the system prompt and heartbeat-scheduled tasks that wake the agent without user input—and a single indirect prompt injection committed to either channel can re-fire across sessions indefinitely, creating what the authors term "carryover attacks" that existing benchmarks fail to capture because they only evaluate attacks in the session where malicious content is first observed.
- CarryoverBench comprises 12 personal-assistant scenarios and 101 attack tasks spanning three trigger channels (Instant same-turn injection, Autonomous heartbeat-scheduled activation, and Latent memory-resurfaced retrieval), with a rule-based verifier that scores planting and triggering as independent stages, revealing that conditional on successful planting, the trigger stage often provides little additional defense across five frontier models.
- Porting the Latent channel to a second runtime environment (Hermes) attenuates but does not eliminate the carryover effect, suggesting that prompt-level interventions alone are insufficient and that carryover defense requires runtime-layer controls operating below the prompt interface.

## Context
Prompt injection research has largely focused on single-session attacks where malicious content is injected and evaluated within the same interaction turn. However, modern agentic systems increasingly rely on persistent memory and autonomous scheduling, creating a gap between the threat model assumed by existing benchmarks and the operational reality of deployed agents. This paper addresses that gap by formalizing a multi-session threat model and providing the first systematic measurement of how planted payloads persist and re-trigger over time, shifting the evaluation lens from "can an agent resist an injection now?" to "can an agent resist an injection that was planted days or sessions ago?"

## Implications
For practitioners deploying LLM agents with persistent memory or scheduled task execution, this work signals that prompt-level filtering and guardrails are necessary but not sufficient; runtime-layer controls such as memory sanitization, task-scheduling validation, and session-boundary auditing become essential defense layers. For the benchmarking and safety research community, CarryoverBench establishes a new evaluation axis that should be incorporated into agent safety suites, and the finding that carryover effects persist across different runtime implementations suggests that model-level robustness alone cannot close this gap, pushing the field toward architectural and infrastructure-level mitigations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28425v1)
