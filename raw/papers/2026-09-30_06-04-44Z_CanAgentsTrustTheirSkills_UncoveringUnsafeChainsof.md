---
title: Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents
published: 2026-09-30T06:04:44Z
authors: Yan Wang, Zhihao Zhang, Ke Chen, Kai Chen, Yaqin Zhang, Duohe Ma, Jun Dai, Xiaoyan Sun
url: http://arxiv.org/abs/2609.39065v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents

## Abstract
LLM agents increasingly rely on installable skills, which are packages of instructions, code, and resources that equip them with task-specific capabilities and, once installed, can be automatically invoked across subsequent user tasks. This creates a chain of trust in which users delegate authority to agents, while agent frameworks admit skill-provided content into the agents' context with insufficient validation, allowing malicious skills to influence agent behavior under that delegated authority. Yet, little is known about whether this trust model adequately constrains untrusted skill content before it reaches security-sensitive operations, or how frequently such trust violations arise in real-world agents. We present TrustProbe, a framework for uncovering unsafe chains of trust in skill-based LLM agents. First, TrustProbe analyzes agent source code to identify source-to-sink call paths from skill-controlled inputs to security-sensitive operations. Second, it generates semantically realistic SKILL.md seeds with injected canaries and evolves them through feedback-guided scheduling and mutation. Finally, it validates vulnerabilities using an oracle that confirms attacker-controlled flows and verifies observable harm. Across 11 open-source agents, eight with more than 10,000 GitHub stars, TrustProbe identifies 104 taint-style vulnerabilities. Validation on a large corpus of real-world skills collected from public hubs such as ClawHub further shows that 25.1% of skill-agent trials exercise the identified vulnerable paths, with payload injection successfully weaponizing 15 of the vulnerabilities. These results reveal a systematic trust failure in skill-based LLM agents: untrusted skill content can reach security-sensitive operations and exercise authority delegated by users to their agents.

## Metadata
- **Published**: 2026-09-30T06:04:44Z
- **Authors**: Yan Wang, Zhihao Zhang, Ke Chen, Kai Chen, Yaqin Zhang, Duohe Ma, Jun Dai, Xiaoyan Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39065v1)