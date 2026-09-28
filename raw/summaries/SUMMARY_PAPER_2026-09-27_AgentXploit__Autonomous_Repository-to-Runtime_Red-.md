---
title: AgentXploit: Autonomous Repository-to-Runtime Red-Teaming for AI Agents
url: http://arxiv.org/abs/2609.31318v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-25_14-26-04Z_AgentXploit_AutonomousRepository_to_RuntimeRed_Tea.md
generated_at: 2026-09-27 21:16
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces AgentXploit, an autonomous two-role auditing system designed to perform repository-to-runtime red-teaming for AI agents by separating attack-path discovery from runtime exploitation. The Analyzer Agent identifies code-supported candidate attack paths by tracing inputs to sensitive operations, while the Exploiter Agent converts these paths into concrete attacks and refines them using runtime feedback. Evaluated on a new benchmark of 72 vulnerabilities across 12 open-source systems, AgentXploit achieves a 59.3% end-to-end success rate, significantly outperforming baseline models like Codex and demonstrating the distinct challenges of repository discovery versus runtime exploitation in agent security auditing.

## Key Takeaways
- AgentXploit employs a two-role architecture where the Analyzer Agent performs white-box analysis to trace attacker-controlled inputs and record candidate attack paths within the repository code, while the Exploiter Agent independently executes these paths as concrete attacks and iteratively revises strategies based on runtime feedback from a controlled environment.
- The authors release AgentXploit-Bench, comprising 72 reproducible vulnerabilities across 12 open-source AI-agent systems, where AgentXploit demonstrates superior performance with a 59.3% end-to-end success rate compared to 38.4% for Codex (and 46.3% under token-budget matching), highlighting the efficacy of the autonomous red-teaming approach over standard LLM-based auditing.
- The study underscores that

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.31318v1)
