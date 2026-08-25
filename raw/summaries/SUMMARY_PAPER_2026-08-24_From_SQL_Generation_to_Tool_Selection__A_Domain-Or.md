---
title: From SQL Generation to Tool Selection: A Domain-Oriented Pattern for MCP Servers
url: http://arxiv.org/abs/2608.22063v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_18-08-59Z_FromSQLGenerationtoToolSelection_ADomain_OrientedP.md
generated_at: 2026-08-24 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a Domain‑Oriented Tooling Pattern that replaces on‑the‑fly SQL generation with a selection from a small set of domain‑specific tools, thereby lowering the model tier required to serve routine requests. Evaluation on the Sakila database shows that a verticalized domain pack achieves a pooled mean score of 0.939, outperforming raw SQL (0.666) and a generic tool pack (0.605). The smallest model improves from 0.583 to 0.929, matching or exceeding larger configurations while reducing cost per correct answer by an order of magnitude.

## Key Takeaways
- The pattern selects domain‑aligned tools instead of synthesizing SQL at query time, which reduces the necessary model tier for routine tasks.
- Model Demotion is observed: intent classification can replace full SQL synthesis, enabling lower‑tier models to handle common requests efficiently.
- A verticalized domain pack reaches a pooled mean score of 0.939 versus 0.666 for raw SQL and 0.605 for the generic pack, with the smallest model improving from 0.583 to 0.929.

## Context
LLM agents increasingly access enterprise data via the Model Context Protocol (MCP), where many servers expose a single generic SQL tool. This approach limits flexibility because schema navigation and business rules are handled by the model, which can be costly and less accurate for specialized domains.

## Implications
The findings suggest that domain‑specific tooling can significantly boost performance of smaller LLMs in MCP environments, lowering operational costs while maintaining high accuracy. Practitioners may adopt this pattern to design scalable, cost‑effective data access layers without relying on large models or monolithic SQL execution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22063v1)
