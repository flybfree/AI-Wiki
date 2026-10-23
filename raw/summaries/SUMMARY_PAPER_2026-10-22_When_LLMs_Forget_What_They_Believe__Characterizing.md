---
title: When LLMs Forget What They Believe: Characterizing State Integrity Collapse in Long-Horizon Dialogues
url: http://arxiv.org/abs/2610.31314v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_14-08-48Z_WhenLLMsForgetWhatTheyBelieve_CharacterizingStateI.md
generated_at: 2026-10-22 22:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates a critical failure mode in large language models during extended conversations: the ability to recall a stated constraint while simultaneously failing to comply with it in subsequent turns. The authors formalize this as "State Integrity Collapse" and introduce StateTrack-Bench, a benchmark spanning numerical, format, role/persona, factual-memory, and logical-rule constraints across seven model snapshots and dialogue depths up to 50 turns. Their central finding is that the majority of observed failures (88.6%) stem from behavioral drift rather than genuine forgetting, meaning models retain the memory of a rule but gradually stop enforcing it as dialogue state accumulates.

## Key Takeaways
- The authors define State Integrity Collapse as a recall-compliance dissociation where a model preserves a stated constraint in its internal representation but ceases to apply it operationally in later dialogue turns. This distinction between "remembering" and "obeying" is critical because it reveals a failure mode invisible to standard single-turn instruction-following evaluations.
- StateTrack-Bench tests five categories of constraints (numerical, format, role/persona, factual-memory, and logical-rule) across seven provider-pinned model snapshots and five dialogue-depth probes. Strict joint retention scores range from 62.4% to 100.0%, with degradation heavily concentrated in symbolic constraints and in one particularly brittle model, indicating that not all constraint types degrade equally.
- A forked recall audit demonstrates that 88.6% of failures are behavioral-drift failures rather than ordinary forgetting, and this diagnosis holds at 84.4% even after excluding the brittle outlier. Extended evaluations up to 50 turns confirm the dissociation persists beyond the core benchmark, while a proposed mitigation called Structured State Anchoring recovers up to 24.4 points on immutable constraints.

## Context
As LLMs are increasingly deployed in agentic workflows, multi-turn assistants, and long-running conversational systems, the assumption that a model reliably maintains its behavioral state over extended interactions has become a foundational but largely untested premise. Existing evaluation frameworks predominantly assess single-turn compliance or short-context instruction following, leaving a significant blind spot regarding how model behavior degrades as dialogue state grows. This paper fills that gap by providing a controlled, multi-constraint benchmark and a diagnostic methodology that separates memory failure from compliance failure, advancing the field toward more rigorous long-horizon reliability assessment.

## Implications
For practitioners building conversational agents, chatbots, or autonomous systems that must adhere to persistent rules over dozens of turns, this work demonstrates that reliability cannot be inferred from single-turn benchmarks and that evaluation pipelines must explicitly track whether remembered constraints remain operational as dialogue state grows. For the broader AI safety and alignment community, the finding that behavioral drift—not forgetting—drives most compliance failures suggests that mitigation strategies should target attention and behavioral consistency mechanisms rather than memory augmentation, and that Structured State Anchoring offers a promising but limited intervention that practitioners should consider integrating into production systems handling long-horizon interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31314v1)
