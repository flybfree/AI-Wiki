---
title: AgentTime: Can Agents Estimate and Control Their Own Runtime?
url: http://arxiv.org/abs/2610.09944v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_12-26-24Z_AgentTime_CanAgentsEstimateandControlTheirOwnRunti.md
generated_at: 2026-10-07 21:34
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AgentTime is a benchmark comprising 222 tasks from 18 sources designed to evaluate whether AI agents can follow requested work durations, predict their own runtime in advance, and estimate elapsed time after task completion. The study reveals that agents struggle significantly with time control: Fable 5.1 in Claude Code deviates from requested runtimes by a typical factor of 2.9×, while GPT-6 Astra in Codex deviates by only 1.2×, and agents frequently sleep or stop working before the requested duration is met.

## Key Takeaways
- Duration-following accuracy varies dramatically across models and harnesses: Fable 5.1 in Claude Code deviates from requested runtimes by a typical factor of 2.9×, compared with only 1.2× for GPT-6 Astra in Codex, showing that the agent harness itself heavily influences time control ability.
- Matching a requested runtime does not guarantee continued productive work: among 158 reviewed Astra runs with classifiable transcripts, 14 explicitly slept after appearing to finish the task, meaning agents may superficially satisfy a time constraint without genuinely engaging with the task for the full duration.
- Agents systematically overestimate their natural runtimes in forecasting experiments, and removing temporal information more than doubles deviation for Sol and Astra and nearly doubles it for Fable in retrospective estimation, indicating that agents lack a robust internal sense of elapsed time.

## Context
Prior research on AI agents has explored time-awareness in isolation, but duration-following and runtime control within native agent harnesses—where agents autonomously execute multi-step workflows—remained unexplored. AgentTime fills this gap by testing agents across coding, computer use, agentic work, and automated research tasks, spanning requested durations from about a minute to multiple days. This matters because long-horizon autonomous agents are increasingly deployed in production settings where predictable runtime is a safety and reliability requirement.

## Implications
For practitioners deploying autonomous agents in production pipelines, this work demonstrates that task completion capability does not imply time control capability, meaning agents cannot be trusted to run reliably over long horizons without explicit runtime evaluation. Industry teams building agentic systems must evaluate both task accuracy and duration compliance as separate metrics, since an agent that finishes early or sleeps mid-task can silently undermine workflow reliability, safety guarantees, and cost predictability in real-world deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09944v1)
