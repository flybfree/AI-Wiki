---
title: DAAF: From Failure Localization to Editable System Assets in LLM Agents
url: http://arxiv.org/abs/2609.32498v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_11-39-00Z_DAAF_FromFailureLocalizationtoEditableSystemAssets.md
generated_at: 2026-09-28 20:57
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces the Detection-Aware Attribution Framework (DAAF) to bridge the gap between failure localization and actionable repair in LLM agents by identifying which editable system assets should be modified to resolve errors. DAAF learns from controlled replays to attribute failures to specific versioned attributes, enabling it to recommend precise repairs or decide against intervention when evidence is insufficient. Evaluated on tau^2-bench Telecom tasks, the framework achieves high accuracy in targeting correct attributes while recovering a significant portion of failed executions with minimal regression on clean tasks.

## Key Takeaways
- DAAF shifts the focus of diagnosis from traditional execution locations to component-attribute failure attribution, targeting versioned and addressable system assets like routing rules or prompt instructions rather than just identifying where an error manifests in a trace.
- The framework combines sparse and noisy failure signals to determine if intervention is needed, learns the effects of valid attribute replacements through controlled replays evaluated by executable outcomes, and shares supervision across requests with compatible responses to amortize intervention evidence.
- At diagnosis time, DAAF operates without counterfactual replay or task rewards, returning a no_change decision, a specific repair target, or an unresolved state; it demonstrates strong performance on tau^2-bench Telecom tasks with 80.72% attribute Hit@1 and recovers 62.65% of failed executions while limiting regression to 3.23%.

## Context
As LLM agents become more complex and rely on persistent system assets for operation, the ability to automatically diagnose and repair failures is critical for reliability and maintainability. Current methods often excel at localization but lack mechanisms to map errors to editable components, creating a bottleneck in autonomous agent maintenance and deployment.

## Implications
This approach enables practitioners to implement self-healing agent systems that can autonomously adjust configuration and knowledge assets based on observed failures, reducing manual debugging overhead. By providing a structured method to attribute errors to specific versioned items, DAAF facilitates safer deployment of agents where interventions are grounded in evidence, minimizing the risk of introducing new regressions during repair attempts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32498v1)
