---
title: Trust the Brand, Lose Control: How Identity Hijacks LLM Agent Orchestration
published: 2026-09-26T13:53:33Z
authors: Xutao Mao, Rui Qian, Linghan Chen, Yudong Gao, Junchi Liao, Jiulin Cai, Jinman Zhao, Cong Wang
url: http://arxiv.org/abs/2609.32635v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trust the Brand, Lose Control: How Identity Hijacks LLM Agent Orchestration

## Abstract
LLM agents now execute tasks end to end with permission to change real systems and increasingly orchestrate subagents that differ in capability and cost. Prior work treats the choice of subagent as an optimization problem. Yet the orchestrator makes this choice from the identities that subagents display, and an attacker can spoof them. Displayed identity thus decides operational authority, meaning who is trusted to check the work and who is allowed to change it. As a result, a risky subagent can keep authority over execution even after other evidence contradicts it. We introduce TrustFork, an LLM agent safety benchmark with 1,890 tasks and 27,826 valid trajectories across 16 agent systems. These systems run eight orchestrators under the OpenCode, OpenClaw, and Pi harnesses. In each task, one subagent carries a risky goal while the other three stay aligned with the user, so contradicting evidence can exist. A task can also change the identity a subagent displays without changing the model behind it, which lets us trace a shift in authority to the label. Our analysis shows that even when another subagent contradicts the risky response, the orchestrator still acts on it in 72.0% of cases on average, most often in the systems with the least terminal harm. Swapping the family labels nearly triples how often the orchestrator obtains the risky response. A safer response is available in 84.0% of tasks, yet it decides the outcome in only 25.0%. The harness also decides which responses reach the orchestrator. Among three runtime defenses, hiding identity cues helps most consistently, while verifying before action helps only when the harness returns enough evidence. TrustFork shows that production agent orchestration must bind authority to evidence before execution causes harm. Our project is in https://henrymao2004.github.io/agent-orchestration-safety/.

## Metadata
- **Published**: 2026-09-26T13:53:33Z
- **Authors**: Xutao Mao, Rui Qian, Linghan Chen, Yudong Gao, Junchi Liao, Jiulin Cai, Jinman Zhao, Cong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32635v1)