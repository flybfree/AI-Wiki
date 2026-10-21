---
title: Harness Self-Evolution for Long-Horizon Terminal Agents
url: http://arxiv.org/abs/2610.27435v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_00-36-49Z_HarnessSelf_EvolutionforLong_HorizonTerminalAgents.md
generated_at: 2026-10-20 22:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces RiseHarness, a framework that iteratively improves agent harnesses— the scaffolding and execution infrastructure surrounding a language model—without modifying the model's weights. The core insight is that long-horizon terminal agents often succeed on a task in one run but fail in repeated attempts due to stochastic errors propagating through actions, feedback loops, and context management. RiseHarness addresses this capability-versus-reliability gap by systematically analyzing both successful and failed execution traces, identifying recurring harness-level defects, and adapting mechanisms from other frameworks into a unified harness through a self-evolving loop.

## Key Takeaways
- RiseHarness operates by "flipping" tasks that exhibit both successful and failed runs under the same configuration, using the successful trajectories as reference points to diagnose why failures occur. This comparative analysis isolates harness-level bugs rather than attributing failures to model capability limitations, allowing targeted fixes to command execution, feedback handling, context management, and completion decisions.
- The framework integrates two evidence streams: agent trajectories (what the model did) and internal harness traces from a runtime monitor (how the execution infrastructure processed those actions). A "Harness Handbook" bridges this evidence to specific harness behaviors and source code, enabling identification of recurring problems in mechanisms shared across multiple tasks rather than task-specific quirks.
- RiseHarness performs a cross-framework search, looking at other harness implementations for relevant solutions and adapting them as design references tailored to the current model and execution protocol. Candidate changes are validated through behavioral checks and repeated task evaluation, and only versions with measured gains seed the next iteration. The authors evaluate across multiple models, ablate the execution evidence and external research components, and test transfer to unseen benchmarks to validate generalization.

## Context
This work sits at the intersection of agent scaffolding research and reliability engineering for large language model deployments. As terminal agents and coding agents are increasingly deployed for multi-step, long-horizon tasks, the community has focused heavily on improving model weights through training and fine-tuning. RiseHarness shifts attention to the execution harness—the command runners, context managers, feedback interpreters, and completion detectors that mediate between the model and the environment—treating it as a first-class optimization target. This is significant because even state-of-the-art models can be undermined by brittle or inconsistent harness behaviors, and fixing those behaviors does not require retraining.

## Implications
For practitioners building agentic systems, RiseHarness offers a practical methodology for hardening reliability without expensive model retraining, which is especially relevant for teams deploying agents in production where consistency matters more than peak capability. The cross-framework adaptation strategy suggests that the field can benefit from a shared, evolving "harness library" rather than each team reinventing execution scaffolding independently. For the broader research community, the paper reframes agent evaluation: reliability across repeated runs should be measured alongside single-run success, and harness-level ablations should be standard in agent benchmarking pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27435v1)
