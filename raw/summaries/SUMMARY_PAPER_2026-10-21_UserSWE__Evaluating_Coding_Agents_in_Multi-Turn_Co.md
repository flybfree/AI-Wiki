---
title: UserSWE: Evaluating Coding Agents in Multi-Turn Conversations with Dynamic Users
url: http://arxiv.org/abs/2610.29822v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_14-46-22Z_UserSWE_EvaluatingCodingAgentsinMulti_TurnConversa.md
generated_at: 2026-10-21 23:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
UserSWE introduces a benchmark designed to evaluate coding agents' ability to fix repository-level bugs through multi-turn interactions with simulated dynamic users, addressing a critical gap in existing single-turn evaluation frameworks. The benchmark constructs multi-turn tasks from repository history and existing benchmarks, using information pools and persona chains calibrated on over 20,000 development sessions to simulate realistic user behavior. Evaluating eleven agents across 72 tasks reveals that agent rankings shift dramatically depending on the interaction budget, demonstrating that single-turn performance is an inadequate proxy for interactive coding ability.

## Key Takeaways
- Existing coding benchmarks present complete issue reports in a single turn without interaction, producing both false positives (accepting incorrect patches) and false negatives (rejecting correct ones), making them inadequate for evaluating agents in realistic multi-turn debugging workflows where developers iteratively refine their requests.
- UserSWE's construction pipeline uses information pools to constrain what a simulated user can reveal at each turn, while a persona chain sampled from a transition model calibrated on 20,859 real development sessions governs how the user speaks, ensuring realistic interaction dynamics rather than scripted prompts.
- Execution-grounded verdicts are produced at every turn by a pair of agents from different model families, using test results as primary evidence and model judgment only for aspects tests cannot resolve, providing a more reliable evaluation signal than purely model-based scoring.
- Agent rankings change with interaction budget: Claude Fable 5.1 resolves the most tasks in one turn, GPT-6-Astra resolves the most by the eighth turn, and Claude Opus 5 leads at intermediate budgets, showing that no single agent dominates across all interaction scenarios.

## Context
As coding agents like Claude, GPT, and Gemini become increasingly deployed in software development workflows, the dominant evaluation paradigm remains single-turn benchmarks such as SWE-bench that present a complete bug report and expect a single patch. This misaligns with how developers actually interact with coding assistants, where they iteratively provide feedback, clarify requirements, and refine solutions across multiple conversational turns. UserSWE addresses this methodological gap by grounding evaluation in execution results at each turn and simulating realistic user behavior drawn from large-scale development session data, representing a shift toward ecologically valid agent evaluation.

## Implications
For practitioners deploying coding agents in production, this work signals that selecting agents based on single-turn benchmark scores may lead to suboptimal choices for interactive debugging workflows, as different agents excel at different interaction budgets. For the research community, UserSWE establishes a template for building execution-grounded, multi-turn evaluation harnesses that could extend to other agentic coding scenarios, pushing the field toward benchmarks that better reflect real-world developer-agent collaboration and informing how organizations should allocate interaction budgets in agent-assisted software engineering pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29822v1)
