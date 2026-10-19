---
title: Robust Function Calling for LLM Agents Under Interface Drift
url: http://arxiv.org/abs/2610.23342v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_11-49-37Z_RobustFunctionCallingforLLMAgentsUnderInterfaceDri.md
generated_at: 2026-10-18 20:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses the reliability problem of tool-augmented language-model agents when their interface text—tool descriptions, argument schemas, and candidate tool lists—changes after deployment despite underlying tool semantics remaining fixed. The authors propose SchemaShield-Lite, a lightweight training-free repair layer combining schema validation, candidate-set retry for missing tool names, and one-shot constrained repair, which significantly improves function-calling accuracy on Qwen3.5-9B without retraining the base model.

## Key Takeaways
- Interface drift, defined as post-deployment changes to tool descriptions, argument schemas, and candidate tool lists while underlying tool semantics stay fixed, is a practical and underexplored reliability failure mode for function-calling systems in deployed LLM agents. The paper formalizes this problem and quantifies its impact on agent performance.
- SchemaShield-Lite achieves substantial accuracy gains: DICE-300 accuracy rises from 0.717 to 0.813 and BFCL-200 accuracy from 0.580 to 0.805 on Qwen3.5-9B, recovering 19 out of 22 and 33 out of 45 drift-induced failures respectively, with no observed repair harms. This demonstrates that a training-free validation-and-repair layer can meaningfully restore robustness without modifying the base model.
- Ablation analysis reveals that candidate-set drift, particularly the introduction of distractor tools, accounts for most observed damage, while description edits and schema edits alone are comparatively less harmful. Naive retry strategies do not explain the performance gains, indicating that structured validation and constrained repair are essential components of the solution.

## Context
Function calling and tool use are central capabilities enabling LLM agents to interact with external APIs, databases, and software systems in production environments. However, deployed systems frequently undergo interface updates—renamed tools, altered parameter schemas, or expanded tool catalogs—without any change to the underlying functionality. This paper fills a gap in the literature by systematically studying interface drift as a distinct failure mode and proposing a practical, model-agnostic mitigation strategy that does not require costly retraining or fine-tuning of the base language model.

## Implications
For practitioners deploying LLM-agent systems in production, this work demonstrates that a lightweight validation-and-repair layer can be integrated at inference time to guard against interface drift without retraining, reducing operational fragility and maintenance costs. The finding that distractor tools in candidate lists cause the most damage suggests that tool-selection infrastructure and prompt engineering should prioritize candidate-set hygiene. More broadly, the results position schema validation and constrained repair as a practical robustness layer that complements existing approaches to reliable tool use in agentic AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23342v1)
