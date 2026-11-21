---
title: Safe Personal RSI: Evaluating and Repairing Personal-Agent Updates
url: http://arxiv.org/abs/2611.23651v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-18_00-15-38Z_SafePersonalRSI_EvaluatingandRepairingPersonal_Age.md
generated_at: 2026-11-20 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Safe Personal RSI, an update-evaluation framework for Kicker, a personal health assistant, designed to safely manage recursive self-improvement restricted exclusively to prompt-level instruction updates while keeping model weights and runtime code fixed. The procedure systematically tests proposed instruction changes against a 29-case executable benchmark spanning email, calendar, health, and marketplace tasks, rejecting 20 of 21 risky update attempts across three models, and demonstrating that targeted repairs can eliminate attack violations and achieve full safe task completion.

## Key Takeaways
- The Safe Personal RSI procedure enforces a strict safety gate on prompt updates: it tests both proposed and current instructions, repeats failing cases, temporarily reverts changes to guide repairs, and validates safety and task performance before adoption. If no candidate version passes all checks, the existing instructions remain in use, ensuring the assistant never degrades silently.
- Quantitative results demonstrate strong rejection and repair capabilities. Across three models and two deliberately risky edits, 20 of 21 update attempts were rejected. A confirmed GPT-5.6 Luna repair reduced attack violations from 10.7% to 0% and raised safe task completion from 89.7% to 100%, while a broad handwritten authority rule matched these outcomes. Transfer of a repair from Qwen2.5-7B-Instruct to Qwen3-14B reduced violations from 69.0% to 17.9% and improved safe task completion from 19.5% to 64.4% under stronger attacks.
- The benchmark includes dedicated probes for authorization reuse, memory handling, and tool-output injection, and runtime probes identified missing local OAuth scope checks in the evaluated snapshot, highlighting that safety auditing must extend beyond prompt text to runtime behavior such as memory-entry deletion and scope validation.

## Context
Recursive self-improvement has long been a theoretical goal in AI systems, but practical implementations risk altering an agent's disclosure behavior, request-following logic, and action reporting in ways that compromise user safety. This paper addresses a critical gap by constraining RSI to prompt updates only and wrapping those updates in a rigorous evaluation-and-repair loop. It contributes to the growing body of work on agent safety, instruction robustness, and benchmark-driven validation for personal AI assistants that interact with sensitive domains like health and calendar management.

## Implications
For practitioners building personal AI assistants, this work provides a concrete, executable protocol for auditing and repairing instruction updates without retraining models, making safety validation accessible even to teams without large compute budgets. The finding that repairs can transfer across model scales suggests that safety patches discovered on smaller models may be portable, reducing the cost of maintaining safe behavior as models evolve. Industry developers deploying assistants in regulated domains such as healthcare should consider adopting similar update-gating procedures to prevent silent regressions in privacy, authorization handling, and tool-use safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.23651v1)
