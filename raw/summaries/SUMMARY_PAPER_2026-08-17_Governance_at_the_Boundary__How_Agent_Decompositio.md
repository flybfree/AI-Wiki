---
title: Governance at the Boundary: How Agent Decomposition Degrades Policy Compliance
url: http://arxiv.org/abs/2608.16055v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_03-31-59Z_GovernanceattheBoundary_HowAgentDecompositionDegra.md
generated_at: 2026-08-17 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Fiducia-bench, a benchmark that measures whether an agent complies with financial policies such as escalation or abstention and leaves an auditable trail. Experiments show that decomposing agents into components reduces policy compliance dramatically, especially in orchestrator‑subagent setups where 85% of relevant facts are attenuated at the handoff boundary.

## Key Takeaways
- Decomposition causes a loss of policy‑relevant information: under a fixed pipeline 56% and under an orchestrator‑subagent architecture 85% of discovered facts fail to reach the acting component, while a single‑loop baseline retains 0% attenuation.  
- The effect varies with model strength; gpt‑4.1‑mini attenuates only 3–6% under the same conditions, indicating that more capable models mitigate some governance loss.  
- The same mechanism can lead to both under‑escalation and over‑escalation depending on whether the dropped fact signals risk or provides exculpatory evidence.

## Context
Agent decomposition is a common strategy for scaling AI systems by splitting tasks among specialized subagents, but prior work rarely evaluates how this affects policy adherence. The paper fills this gap by quantifying factual attenuation at component interfaces and linking it to governance outcomes in financial compliance scenarios.

## Implications
Practitioners must consider the trade‑off between modularity and policy enforcement when designing multi‑agent systems, as hidden information loss can erode regulatory safety. The findings suggest that more capable models may partially offset decomposition penalties, guiding future research on balancing scalability with compliance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16055v1)
