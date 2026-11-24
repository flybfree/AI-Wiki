---
title: When Tools Fail, Agents Fabricate: Silent Failure and Verification-First Oversight in Tool-Using LLM Agents
url: http://arxiv.org/abs/2611.28341v1
type: paper-summary
date: 2026-11-23
source_paper: 2026-11-20_21-47-43Z_WhenToolsFail_AgentsFabricate_SilentFailureandVeri.md
generated_at: 2026-11-23 21:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how tool-using LLM agents behave when tool calls fail, introducing RetryRealistic, a sandboxed testbed that injects controlled faults across eight tools and nine fault types over 30 multi-step tasks. The authors find that agent recovery is unreliable (19–68% correct) and that a significant fraction of runs (6–26%) end in "confident fabrication," where the agent asserts a wrong answer as fact. They identify "silent ingestion" as the core failure mechanism and demonstrate that a verification-first Monitor can substantially reduce fabrication and improve correct recovery.

## Key Takeaways
- Recovery from tool failures is highly unreliable across all four evaluated agents, with only 19–68% of faulted runs producing correct answers, and 6–26% ending in confident fabrication where the agent presents a wrong answer as established fact. The dominant failure mechanism is "silent ingestion": the agent accepts faulted or partial data as valid on first contact without retrying or flagging the problem, then constructs a fabricated answer on top of that corrupted input.
- The fault type governs the failure mode more than the underlying model. Faults that return partial data drive fabrication rates up to 38%, while hard denials (such as permission errors) tend to produce honest failure where the agent acknowledges it cannot complete the task. This distinction suggests that partial, ambiguous failures are far more dangerous than outright rejections because they are harder for the agent to detect.
- A verification-first Monitor that grounds checks in structured tool outputs and issues corrective directives rather than hard blocks raises correct recovery from 45.6% to 56.3% and reduces fabrication from 17.3% to 10.8%. Additionally, removing chain-of-thought reasoning increases fabrication by 8.3 percentage points, indicating that deliberation serves as a protective mechanism against silent ingestion.

## Context
As LLM agents increasingly rely on external tools—databases, APIs, file systems, and shell commands—to perform multi-step tasks, understanding how they handle tool failures becomes critical for safe deployment. Prior work has largely focused on tool selection and planning, leaving the recovery and fault-handling behavior of agents underexplored. This paper fills that gap by providing a controlled, reproducible fault-injection benchmark and a mechanistic account of why agents fabricate rather than recover, situating the problem within the broader literature on hallucination, tool-use reliability, and agent oversight.

## Implications
For practitioners building production agent systems, the findings argue that tool-failure handling cannot be left to the model's implicit reasoning; explicit verification layers and structured grounding checks are necessary to prevent silent fabrication from propagating into downstream decisions. The result that chain-of-thought removal worsens fabrication also cautions against optimizing agents for speed by stripping deliberation steps. Industry deployments involving databases, file permissions, or external APIs should treat partial-data faults as the highest-risk failure mode and instrument agents with monitoring that flags unverified tool outputs before they are incorporated into final answers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.28341v1)
