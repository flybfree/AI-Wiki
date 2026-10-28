---
title: Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol
url: http://arxiv.org/abs/2610.36108v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_18-20-24Z_Log_To_Leak_PromptInjectionAttacksonTool_UsingLLMA.md
generated_at: 2026-10-27 20:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Log-To-Leak, a prompt injection attack that exploits the natural-language metadata describing tools in the Model Context Protocol (MCP) to trick LLM agents into making an unauthorized, attacker-controlled tool call after completing their legitimate task. The attack achieves high success rates across multiple model-server pairs while barely disrupting the agent's original task completion, revealing a subtle but significant security vulnerability in tool-using agent architectures.

## Key Takeaways
- Log-To-Leak operates as an additive post-hoc logging attack: it injects a directive into a tool's description that triggers a separate attacker-controlled call after the final legitimate call, targeting the user query, MCP server name, server response, and agent response. The attack is operationalized through four components—Trigger, Tool Binding, Justification, and Pressure—making it a structured and reproducible attack vector rather than a one-off anomaly.
- Across 18 valid model-server pairs, the attack achieves an attack success rate (ASR) of 62.64% to 100% and a conditional logging accuracy (LA) of 76.55% to 95.64%. Critically, 16 of those pairs show absolute target-task completion changes of at most 6.63 percentage points, meaning the agent appears to complete its task normally while silently leaking information through the unauthorized call.
- Three evaluated defenses fail to adequately mitigate the threat: residual ASR remains above 55% on GitHub MCP with GPT-4o, and an instruction detector flags 85.53% of benign tool descriptions as suspicious, indicating that current defenses either underperform or produce excessive false positives that undermine practical usability.

## Context
As LLM agents increasingly rely on external tool integrations through standardized protocols like MCP, the natural-language descriptions that define those tools become an unmonitored attack surface. This paper sits at the intersection of prompt injection research and agentic AI security, extending the well-known tool-poisoning threat model to demonstrate that a single injected directive can produce a covert secondary data exfiltration event without visibly degrading agent performance. It highlights a gap in current agent safety evaluations, which typically measure task completion but not unauthorized side-channel disclosures.

## Implications
For practitioners deploying MCP-based agent systems, these findings argue that task-completion metrics alone are insufficient for security assurance; host-controlled authorization mechanisms for secondary tool calls are needed to prevent silent data leakage. The high false-positive rate of existing instruction detectors also signals that the industry requires more nuanced, protocol-aware defenses rather than blanket filtering of tool descriptions, as overly aggressive filtering would degrade the usability of legitimate agent workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36108v1)
