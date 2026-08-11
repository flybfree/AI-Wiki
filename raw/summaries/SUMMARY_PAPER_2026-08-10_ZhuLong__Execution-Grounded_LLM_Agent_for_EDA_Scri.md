---
title: ZhuLong: Execution-Grounded LLM Agent for EDA Scripting with Offline API Self-Exploration
url: http://arxiv.org/abs/2608.07925v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_05-05-38Z_ZhuLong_Execution_GroundedLLMAgentforEDAScriptingw.md
generated_at: 2026-08-10 22:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ZhuLong, an execution-grounded LLM agent that handles EDA scripting for PyAether and SKILL by integrating API retrieval, documentation inspection, and sandbox execution through unified MCP tools. It also adds an offline self-exploration mechanism that infers undocumented API behaviors via counterfactual experiments. The complete system achieves 78.5% Pass@1 on the EDA-Eval-PyAether benchmark, far exceeding a pure LLM baseline.

## Key Takeaways
- Sandbox execution is the dominant performance driver, causing a 41.2 pp drop when removed.
- The self-exploration mechanism adds 3.2 pp accuracy gain and reduces per-task tool calls by 22.1%.
- ZhuLong reaches 60.0% Pass@1 on PyAether and 50.0% on SKILL for interactive tasks with unsaved layouts.

## Context
This work addresses a long-tail bottleneck in LLM coding where tool-specific APIs are often undocumented, limiting practical deployment of AI assistants in real-world EDA environments. By combining execution grounding with offline self-exploration, the approach demonstrates a more robust and efficient alternative to traditional prompting.

## Implications
For industry practitioners, ZhuLong shows that integrating sandboxed execution can significantly boost LLM performance in specialized domains like electronic design automation. The reduction in tool calls also lowers computational overhead, making such agents viable for interactive workflows where latency matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07925v1)
