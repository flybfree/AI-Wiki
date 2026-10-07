---
title: From Evidence to Action: How Tool-Using Agents Fail
url: http://arxiv.org/abs/2610.07753v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_04-50-29Z_FromEvidencetoAction_HowTool_UsingAgentsFail.md
generated_at: 2026-10-06 21:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper studies how tool-using agents can produce correct outcomes while still failing to act on evidence established beforehand. It analyzes the evidence-to-action chain across deciding whether to act, executing single actions, and completing dependent workflows. The main finding is that failures often occur before execution, when agents stop after incomplete investigation or act before required evidence is established.

## Key Takeaways
- Across ten model-harness configurations, strong static action assessment can coexist with much weaker interactive execution, showing that a model’s ability to judge whether an action is appropriate does not reliably translate into correct behavior in an interactive tool-use setting.
- Failures often begin before execution: agents may stop with incomplete investigation or act before required evidence is established. Once required evidence is obtained, single-action execution is usually reliable, but multi-action workflows expose unresolved prerequisites and incomplete execution.
- The authors introduce SafeActBench, with 656 cases across six operational domains and five protocols progressing from static action judgment to investigated non-action, single-action, and multi-action workflows. A provenance-bound Evidence Ledger and deterministic trajectory evaluator track established information, action timing, and downstream dependency satisfaction.

## Context
Tool-using agents increasingly operate in environments where actions change external state, so correctness depends not only on final outcomes but also on whether actions are grounded in prior evidence. This paper matters because it separates evidence establishment from action execution and shows that agent evaluation must examine the full chain from investigation to dependent workflows.

## Implications
For practitioners, these results suggest that agent benchmarks should measure evidence grounding, prerequisite resolution, and workflow completion rather than only final task success. For industry, safer deployment of autonomous agents requires monitoring whether agents have established required evidence before acting and whether multi-step workflows satisfy downstream dependencies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07753v1)
