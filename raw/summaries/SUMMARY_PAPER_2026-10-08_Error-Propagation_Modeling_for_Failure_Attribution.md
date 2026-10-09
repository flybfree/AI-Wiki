---
title: Error-Propagation Modeling for Failure Attribution in LLM-Based Multi-Agent Systems
url: http://arxiv.org/abs/2610.11600v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_09-44-59Z_Error_PropagationModelingforFailureAttributioninLL.md
generated_at: 2026-10-08 21:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces EMFA (Error-Propagation Modeling for Failure Attribution), a method designed to identify the decisive error in LLM-based multi-agent systems by modeling how errors propagate through cascading interactions and persistent loops. The authors define the attribution target as the specific agent-step pair whose correction would recover a failed execution, and they demonstrate that EMFA achieves state-of-the-art step-level attribution accuracy on the Who&When benchmark, improving previous best results by 3.45 and 4.40 percentage points on Hand-Crafted and Algorithm-Generated subsets respectively.

## Key Takeaways
- The paper defines the "decisive error" as the agent-step pair whose correction would recover the failed execution, distinguishing it from downstream failure symptoms. Existing approaches identify suspicious steps but fail to model how errors propagate across interactions or persist in unresolved loops, making it difficult to separate root causes from cascading consequences.
- EMFA constructs a structured representation of the failed trajectory and explicitly models both cascading propagation and persistent interaction loops. It then applies propagation-aware candidate screening followed by counterfactual verification to pinpoint the decisive agent-step pair, providing a principled pipeline rather than heuristic suspicion ranking.
- On the Who&When benchmark, EMFA achieves state-of-the-art step-level attribution accuracy while remaining competitive at the agent level, with measurable improvements of 3.45 percentage points on Hand-Crafted subsets and 4.40 percentage points on Algorithm-Generated subsets over prior best methods.

## Context
LLM-based multi-agent systems are increasingly deployed for complex tasks involving coordinated reasoning, tool use, and external resource interaction, yet debugging and attributing failures in these systems remains a significant open challenge. The observed output of a failed multi-agent execution rarely reveals which specific agent or interaction step introduced the critical error, because downstream agents may propagate, amplify, or mask the original mistake. This gap between observable symptoms and root causes hinders systematic debugging, automated repair, and reliability engineering for multi-agent pipelines.

## Implications
For practitioners building and deploying multi-agent LLM systems, EMFA offers a structured methodology for automated failure diagnosis that can reduce debugging time and improve system reliability by pinpointing the exact agent-step responsible for a failure rather than flagging numerous downstream symptoms. For the broader research community, the explicit modeling of error propagation and persistent loops provides a transferable framework applicable to any sequential or interactive multi-component system, potentially informing future work in automated repair, self-improving agent architectures, and safety-critical multi-agent deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11600v1)
