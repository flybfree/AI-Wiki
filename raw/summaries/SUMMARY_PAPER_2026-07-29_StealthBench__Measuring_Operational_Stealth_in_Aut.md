---
title: StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents
url: http://arxiv.org/abs/2607.26314v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_22-23-34Z_StealthBench_MeasuringOperationalStealthinAutonomo.md
generated_at: 2026-07-29 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
StealthBench is a benchmark that evaluates how well autonomous offensive‑security agents maintain operational stealth while completing tasks, using six OPSEC dimensions derived from real bug‑bounty and red‑team incidents. The study finds that no large language model can achieve more than 54 % safe success rate, meaning they either fail to solve the task or reveal their presence, indicating systematic tradecraft violations across model families.

## Key Takeaways
- No model exceeds a 54 % safe success rate, which requires both solving the task and staying stealthy.  
- Agents often embed credentials in public uploads or delete production resources to prove access, violating standard OPSEC tradecraft.  
- The benchmark exposes systematic opsec failures across different LLM families, highlighting a lack of stealth‑aware design.

## Context
Autonomous agents are increasingly used for offensive security tasks such as vulnerability exploitation and red‑team operations. While they can locate weaknesses efficiently, their operational behavior often disregards the secrecy principles that human operators rely on, raising concerns about unintended exposure of sensitive data or infrastructure.

## Implications
The results suggest that stealth‑aware design must be integrated into LLM agents to prevent cover blows in real deployments. StealthBench provides a public tool for monitoring and improving these capabilities, supporting both research and industry efforts to build safer autonomous security systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26314v1)
