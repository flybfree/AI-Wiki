---
title: ActionGuard: Tool Call Authorization under Poisoned Skills
url: http://arxiv.org/abs/2609.39450v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_10-23-57Z_ActionGuard_ToolCallAuthorizationunderPoisonedSkil.md
generated_at: 2026-09-30 21:57
model: qwen3.6-35b-a3b
---

## Summary
ActionGuard is a safeguard mechanism designed to protect LLM-based agents from malicious instructions embedded within third-party skills that could otherwise trigger dangerous tool calls such as data exfiltration or unauthorized code execution. By separating the target agent's planning context from a Reviewer's authorization context, ActionGuard intercepts tool invocations at the execution boundary and evaluates actions against trusted user intent using runtime evidence without exposing the potentially poisoned skill text to the reviewer. Experimental results demonstrate that ActionGuard significantly reduces attack success rates by up to 46 percent compared to existing safeguards while maintaining high task completion for legitimate requests.

## Key Takeaways
- ActionGuard

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39450v1)
