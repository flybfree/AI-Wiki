---
title: TRIAGE: Three-level Routing and Intelligent Agent Guidance for Efficient Execution
url: http://arxiv.org/abs/2609.01428v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-40-09Z_TRIAGE_Three_levelRoutingandIntelligentAgentGuidan.md
generated_at: 2026-09-01 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TRIAGE, a three‑level routing framework that reduces token consumption for large language model agents by reusing historical execution trajectories. The authors show that 56 % of queries can be handled at zero cost through direct reuse or skill substitution, achieving up to 76 % token reduction across diverse domains.

## Key Takeaways
- Direct Reuse‑identical queries incur no tokens because the system retrieves an exact match from a stored trajectory.  
- Skill Substitution‑similar queries also use zero tokens by deterministically substituting parameters within pre‑defined skills extracted from past actions.  
- Full ReAct‑novel queries are automatically logged for future reuse, forming a positive feedback loop that improves efficiency over time.

## Context
The ReAct paradigm enables LLM agents to perform complex tasks via tool calls but suffers from redundant reasoning loops. TRIAGE addresses this inefficiency by abstracting past experiences into reusable skills, a concept known as “experience as a service.” This approach aligns with broader AI research focused on minimizing compute cost and maximizing token efficiency.

## Implications
For practitioners, TRIAGE offers a practical method to cut down inference costs in real‑time applications such as security monitoring. The framework’s scalability across multiple domains suggests it could become a standard component of efficient LLM deployment pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01428v1)
