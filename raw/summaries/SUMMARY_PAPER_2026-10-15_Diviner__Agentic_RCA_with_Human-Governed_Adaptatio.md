---
title: Diviner: Agentic RCA with Human-Governed Adaptation for Large-Scale Infrastructure
url: http://arxiv.org/abs/2610.21281v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_05-20-23Z_Diviner_AgenticRCAwithHuman_GovernedAdaptationforL.md
generated_at: 2026-10-15 22:21
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Diviner is an agentic root-cause analysis system deployed at Meta that addresses the challenge of diagnosing incidents across service, data, configuration, compute, and organizational boundaries in large-scale distributed infrastructure. Rather than relying on generic language-model agents that struggle with stale context, misinterpreted queries, and observability overload, Diviner structures the RCA process around a four-stage reliability lifecycle—Encode, Execute, Evaluate, and Adapt—that integrates reviewed incident corpora, service-owner expertise, and human-governed knowledge updates to produce evidence-linked, verifiable causal hypotheses.

## Key Takeaways
- Generic language-model agents fail at large-scale RCA not because they lack tool access, but because they use stale or mistimed context, treat failed queries as absent symptoms, report unsupported system state, and overload observability services designed for human-paced interaction. Diviner explicitly designs around these failure modes rather than assuming tool access alone solves the problem.
- The Encode stage combines a large corpus of reviewed incidents with service-owner expertise to produce scoped, versioned skills, workflows, typed tools, and an incident knowledge graph. The Execute stage then uses an adaptive Lead agent coordinating context-isolated workers to apply this curated knowledge to point-in-time evidence while maintaining evidence-linked hypotheses, ensuring that reasoning stays grounded in verifiable data rather than hallucinated system state.
- The Evaluate and Adapt stages close the loop through human governance: saved investigation trajectories are compared against responder-reviewed outcomes to measure exact cause identification, useful diagnostic direction, and Groundedness. Recurring gaps and on-call feedback generate focused operational-knowledge updates that are admitted only after replay validation, quality checks, and explicit owner approval, preventing unverified knowledge from propagating into the agent's decision-making.

## Context
This paper sits at the intersection of agentic AI systems and production reliability engineering, addressing a well-known gap in the literature: most agentic frameworks assume tool access is sufficient for complex reasoning, yet real-world infrastructure diagnosis requires cross-boundary causal reasoning, temporal awareness, and organizational knowledge that generic agents cannot infer from prompts alone. Diviner contributes a concrete, deployed architecture that demonstrates how human-in-the-loop governance and structured knowledge encoding can make agentic systems viable in high-stakes operational environments where incorrect diagnoses carry significant cost.

## Implications
For practitioners operating large-scale cloud or distributed systems, Diviner offers a blueprint for deploying agentic RCA without surrendering accountability to opaque model reasoning, since every hypothesis is evidence-linked and every knowledge update passes through owner approval. For the broader AI research community, the paper signals that agentic systems for complex operational tasks require domain-informed knowledge encoding and evaluation frameworks that measure Groundedness and useful direction—not just task completion—shifting the design conversation from "can the agent use tools?" to "can the agent reason verifiably within organizational constraints?"

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21281v1)
