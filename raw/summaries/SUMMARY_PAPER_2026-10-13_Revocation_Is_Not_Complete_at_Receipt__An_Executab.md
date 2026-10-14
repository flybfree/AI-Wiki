---
title: Revocation Is Not Complete at Receipt: An Executable Outcome Contract for Distributed Agent-Tool Gateways
url: http://arxiv.org/abs/2610.15991v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-11_23-41-18Z_RevocationIsNotCompleteatReceipt_AnExecutableOutco.md
generated_at: 2026-10-13 21:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that revocation of delegated authority in distributed agent-tool gateway systems is not complete merely upon receipt at a gateway, and introduces a bounded outcome contract (C0–C5) that spans from issuer commit through verified effect prevention. Through experiments involving Keycloak 26.7, eight physical agent-tool gateways across 16 AWS hosts in three availability zones, and an external MCPMark agent executing 60 closed-loop task arms, the authors show that transport acknowledgment and receiver persistence can succeed while nearly half of calls (49.78%) are still admitted and all their effects commit, proving that conventional completion signals are insufficient for establishing true revocation enforcement.

## Key Takeaways
- The authors define a six-stage bounded outcome contract (C0–C5) that tracks authority revocation from issuer commit through verified effect prevention, implemented as a persistent monitor over a frozen gateway set, call set, and observation window. Treating intermediate stages such as C3 or C4 as completion produces seven or five false positives respectively in a derived audit of eight semantic cases, whereas the full C0–C5 verdict eliminates all false positives, establishing that only the terminal stage of confirmed effect prevention constitutes true revocation completion.
- In the primary experiment using Keycloak 26.7 with eight physical agent-tool gateways, Filesystem and PostgreSQL effects, and 16 AWS hosts across three availability zones, receiver-selective non-delivery causes transport acknowledgment and receiver persistence to report success while 112 of 225 calls (49.78%) are admitted and all 112 effects commit in every treatment block. A separately provisioned execution reproduces this result, confirming the finding is not an artifact of a single configuration.
- An unmodified external MCPMark agent executing 60 closed-loop task arms demonstrates the boundary on real agent workflows: normal C4 denies all 31 exposed post-barrier calls and commits no effect, while selective C3 allows 344 calls and commits 145 effects across Filesystem and PostgreSQL. OPA/Toxiproxy and a live three-role LLM workflow with networked MCP tools independently reproduce the persisted-but-not-enforced boundary on narrower surfaces, confirming the problem generalizes across architectures.

## Context
As agentic AI systems increasingly rely on distributed tool gateways to mediate access to external resources, delegated authority caching at those gateways creates a critical gap between the moment a revocation is issued and the moment all downstream effects are actually prevented. Existing security and access-control frameworks typically treat token revocation or policy update acknowledgment as sufficient evidence of enforcement, but this paper shows that in multi-gateway, multi-receiver topologies, that assumption produces systematic false positives. The work sits at the intersection of distributed systems verification, AI agent safety, and formal contract-based monitoring, addressing a gap that becomes more acute as agentic workflows scale across availability zones and heterogeneous tool backends.

## Implications
For practitioners deploying agentic AI systems with tool gateways, this work demonstrates that transport-layer success metrics and receiver persistence checks are necessary but not sufficient for confirming that a revoked authority has stopped producing effects, meaning current operational dashboards and alerting pipelines may silently miss enforcement failures. The C0–C5 contract provides a concrete, implementable monitoring pattern that organizations can adopt to audit revocation completeness across gateway fleets, and the 14-case fault matrix offers a reproducible methodology for validating that monitoring under restart, selective non-delivery, and sticky-violation conditions. For the broader field, the findings challenge the assumption that identity-provider commit or policy-engine acknowledgment constitutes a security boundary, urging the community to treat effect prevention as the only admissible completion signal in safety-critical agent architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15991v1)
