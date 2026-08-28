---
title: The Reasoning Tax: Token Economics of LLM Reasoning Across Task Types and Deployment Contexts
published: 2026-08-26T17:44:50Z
authors: Sachin Gopal Wani, Ajay Dholakia, David Ellison
url: http://arxiv.org/abs/2608.26235v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Reasoning Tax: Token Economics of LLM Reasoning Across Task Types and Deployment Contexts

## Abstract
Accuracy-only benchmarking of reasoning-capable large language models misses a central deployment question: when do extended thinking tokens earn their cost? We introduce the Token Economy Score (TES), a marginal benchmarking metric that measures the accuracy gain of a reasoning model over a non-reasoning baseline, normalized by the generated-token multiplier. We define paired and approximated TES variants for model families with reasoning toggles and frontier models without direct non-reasoning counterparts. We then conduct an empirical benchmarking analysis across 151 model-benchmark evaluation runs on seven benchmarks spanning mathematics, code generation, science reasoning, instruction following, expert knowledge, knowledge recall, and research-level physics. The analysis examines three deployment-facing dimensions: which task structures yield positive marginal reasoning efficiency, how increasing reasoning effort changes TES within model families, and how deployment context changes economic viability. Results show that task structure predicts reasoning efficiency better than nominal difficulty: sequential inferencechain tasks such as AIME 2025 and LiveCodeBench show high TES, while knowledge-recall tasks such as MMLU-Pro show low TES despite their difficulty. We also find systematic diminishing returns at higher reasoning effort levels, including cases where additional thinking reduces accuracy. Finally, Reasoning Cost Share (RCS) shows that inference spend is often dominated by internal thinking, while Deployment Cost Multiplier (DCM) shows how on-premises deployment can change the economics of otherwise costly reasoning workloads. These findings support a benchmarking-driven model-selection rule: enable reasoning selectively by task type, effort level, and deployment context rather than treating it as a universally beneficial mode.

## Metadata
- **Published**: 2026-08-26T17:44:50Z
- **Authors**: Sachin Gopal Wani, Ajay Dholakia, David Ellison
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26235v1)