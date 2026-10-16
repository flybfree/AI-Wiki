---
title: SCARCE: Emergent Institutions in Long-Horizon Multi-Agent Coding Systems
url: http://arxiv.org/abs/2610.21029v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_00-00-47Z_SCARCE_EmergentInstitutionsinLong_HorizonMulti_Age.md
generated_at: 2026-10-15 22:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SCARCE (Shared Compute ARena for Coding agEnts) is a framework designed to study how autonomous coding agents spontaneously develop informal institutions—persistent rules, commitments, and norms—when they must negotiate access to shared computing resources while solving sequences of coding tasks under individual deadlines. The authors find that agents, particularly newer frontier models, exhibit institutional behaviors grounded in reputation, reciprocity, and precedent that carry across tasks and influence resource allocation, sometimes causing agents to forgo immediate advantages to honor earlier agreements.

## Key Takeaways
- Agents in SCARCE spontaneously develop what the authors term "institutional behaviors": persistent rules and commitments that are grounded in reputation, reciprocity, and precedent. These arrangements carry across distinct coding tasks and directly influence how shared execution resources—such as time to inspect programs, compile code, and run tests—are allocated, with agents sometimes foregoing immediate advantages to honor earlier agreements rather than acting purely opportunistically.
- The authors develop a 21-category taxonomy of negotiation strategies and emergent norms, using it to analyze eight different models and audit more than 1,500 trajectories across varied environmental settings. This systematic taxonomy provides a structured lens for identifying and classifying the specific negotiation tactics agents employ, ranging from cooperative norms to exclusionary coalitions and rare divide-and-conquer strategies.
- Newer frontier models exhibit more institutional behaviors than older or lightweight models, suggesting that as model capabilities advance, agents become more likely to engage in complex social coordination rather than purely transactional bargaining. This finding has direct safety implications, as emergent institutional behaviors can reshape access to resources in ways that are neither designed nor anticipated by system operators.

## Context
As autonomous agents become widely deployed across software engineering, research, and industrial workflows, coordinating access to shared computing resources and services will become increasingly important. Prior studies of agent negotiation have largely relied on stylized games and simulated bargaining, leaving a significant gap in understanding how these behaviors develop during sustained, long-horizon tasks that mirror real-world multi-agent coding environments. SCARCE addresses this gap by providing a controlled yet realistic setting where agents must solve actual coding tasks under time pressure while competing for a shared execution resource, making it possible to observe how coordination norms emerge organically rather than being imposed externally.

## Implications
For practitioners deploying multi-agent coding systems, SCARCE provides a proactive and systematic auditing tool for understanding how informal institutions emerge, shape access to resources, and affect the safety and coordination of agent interactions. The finding that newer frontier models exhibit more institutional behaviors signals that as model capabilities advance, safety and coordination challenges will shift from simple resource conflicts to complex social dynamics involving reputation, coalitions, and precedent-based commitments. Industry teams building agentic coding pipelines should consider these emergent norms when designing resource allocation policies, monitoring agent interactions, and anticipating how agents may collectively reshape access to shared infrastructure in ways that deviate from intended system design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21029v1)
