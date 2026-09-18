---
title: Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents
published: 2026-09-17T02:14:53Z
authors: Alex Remedios, Simon Storf, Fabien Roger, John Hughes
url: http://arxiv.org/abs/2609.19587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents

## Abstract
To keep coding agents from going off the rails, production systems now review each proposed action with a blocking monitor that can reject it before it runs (Auto Mode in Claude Code, Guardian in OpenAI's Codex). Prior evaluations of such monitors largely measure robustness to accidental harm or prompt injections from untrusted sources looking to hijack the agent. Less understood is how they hold up when the agent they monitor is persistently misaligned. To understand this risk, we task an adversarial agent with evading production blocking monitors and causing catastrophic harm, e.g. by exfiltrating its own weights. We find that when instructed with high-level attack strategies, adversarial agents can succeed through several distinct mechanisms, such as agent-generated prompt injection against the monitor, multi-agent attacks, and malicious compaction. In particular we find that in 79% of trials, the agent can use an injection attack against Auto Mode and Guardian to run arbitrary bash commands. We also find that it is possible to greatly improve Auto Mode through design changes like enhancements to tool coverage, transcript formatting and an agentic monitor stage. Even with these improvements, preventing multi-context attacks at an acceptable cost remains an open problem. By detailing our red-teaming methodology and highlighting new attack vectors, we aim to help defenders evaluate their mitigations against the possibility of persistent malign coding agents. Code is available at https://github.com/safety-research/red-teaming-auto-mode.

## Metadata
- **Published**: 2026-09-17T02:14:53Z
- **Authors**: Alex Remedios, Simon Storf, Fabien Roger, John Hughes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19587v1)