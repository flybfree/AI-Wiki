---
title: Reading Right, Acting Wrong: Diagnosing Decision Failures of System One Models in Agent Loops
url: http://arxiv.org/abs/2610.18579v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_15-43-30Z_ReadingRight_ActingWrong_DiagnosingDecisionFailure.md
generated_at: 2026-10-14 00:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates why fast, single-pass "System One" models used in agent loops choose incorrect next actions, distinguishing between comprehension failures (misreading the state) and decision failures (reading correctly but acting wrongly). Through a frozen benchmark spanning simulated environments, customer-service policies, tool use, web navigation, and coding, the authors pair every next-action question with independent factual probes across seventeen fast systems and a reasoning model. The central finding is that most wrong actions follow correct reading, and the more accurate a system is, the more its errors take this decision-failure form rather than a comprehension-failure form.

## Key Takeaways
- Most action errors in System One models stem from correct state comprehension followed by incorrect action selection, not from misreading the agent's observed state. The factual probes reveal that models accurately answer questions about what they have seen yet still fail to translate that understanding into the correct next action, and this pattern intensifies as model accuracy improves.
- These decision failures are systematic rather than random noise: they cluster on the same agent decision states across models of every architecture and scale, indicating a shared structural weakness in how fast models combine correctly understood facts into coherent action plans.
- When probed facts provably determine the correct action, models that read every individual fact still fail to combine them into a valid decision. However, composing the models' own factual answers through external code repairs the failure, suggesting the bottleneck is in internal integration rather than information access. On real-world states, the missing element is often not a fact but the next sub-goal in a multi-step plan.

## Context
This work addresses a critical gap in understanding how fast, low-cost models behave inside agentic pipelines, where they are increasingly deployed for their speed and affordability. Prior evaluation frameworks typically treat model errors as monolithic, conflating perception failures with reasoning failures. By introducing paired factual probes as a diagnostic tool, this paper provides a behavioral methodology that separates what a model knows from what it does with that knowledge, offering a new lens for auditing agent systems in production environments where interpretability is otherwise unavailable.

## Implications
For practitioners building agent systems, this research suggests that improving model accuracy on individual comprehension tasks will not reduce action-selection errors and may even expose more of them, shifting the engineering focus toward explicit sub-goal decomposition and external fact-composition pipelines. For the broader field, the finding that decision failures cluster on shared states across diverse architectures implies a common representational limitation in single-pass models, motivating research into structured planning scaffolds, sub-goal generation modules, and hybrid architectures that separate reading from acting. Industry deployments of fast models in customer-service automation, tool orchestration, and web navigation should incorporate diagnostic probes to identify whether failures are perceptual or decisional before attempting costly model upgrades.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18579v1)
