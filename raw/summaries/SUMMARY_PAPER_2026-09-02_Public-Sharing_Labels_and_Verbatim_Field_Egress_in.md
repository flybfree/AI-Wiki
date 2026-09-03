---
title: Public-Sharing Labels and Verbatim Field Egress in an MCP-to-A2A Agent Configuration: A Controlled Multi-Model Study
url: http://arxiv.org/abs/2609.01693v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_16-24-11Z_Public_SharingLabelsandVerbatimFieldEgressinanMCP_.md
generated_at: 2026-09-02 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how public-sharing labels affect verbatim field egress in an MCP-to-A2A agent configuration using deterministic scoring. It finds that adding PUBLIC - OK TO SHARE is associated with higher verbatim occurrence across models, though effects vary widely. The study reports scenario-level statistics without p-values.

## Key Takeaways
- Adding a public label increases verbatim egress relative to unlabeled baseline in all tested models, indicating the label may prompt more data leakage.
- The association is strong for Claude Sonnet 5, moderate for one GPT-5.6 tier, and minimal for another, showing model dependence.
- No causal claim is made; the effect is observed only in this specific configuration.

## Context
This work addresses a gap in safety evaluation where separate MCP and A2A assessments do not capture combined behavior. By using exact deterministic scoring instead of LLM judges, it provides transparent metrics on verbatim egress that can inform label design.

## Implications
For industry practitioners, the findings suggest that labeling strategies may influence model output without guaranteeing safety improvements. The study highlights the need for rigorous testing across configurations before deploying public sharing labels.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01693v1)
