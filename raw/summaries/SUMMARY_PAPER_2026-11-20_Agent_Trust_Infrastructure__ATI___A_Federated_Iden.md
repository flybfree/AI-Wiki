---
title: Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents
url: http://arxiv.org/abs/2611.23202v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-17_18-44-25Z_AgentTrustInfrastructure_ATI__AFederatedIdentity_T.md
generated_at: 2026-11-20 21:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces the Agent Trust Infrastructure (ATI), a framework-independent security architecture designed to establish federated trust among autonomous AI agents operating across organizational boundaries. Built on Public Key Infrastructure, Zero Trust Architecture, and remote attestation, ATI validates agent identity, execution integrity, and authorization before requests are executed, increasing attack containment from 43% to 84% in simulated multi-organization environments while adding only approximately 174 microseconds of overhead per request.

## Key Takeaways
- ATI eliminates the need for a shared root authority by establishing federated trust through peer organizational certificate authorities called AgentCAs, enabling independent organizations to verify cross-organizational agent identity, execution integrity, and authorization without a centralized trust anchor. This federated PKI-based approach means each organization operates its own certificate authority while still participating in a shared trust network.
- Before any agent request is executed, ATI enforces three distinct policy checks: validating agent certificates, verifying approved model, tool, and system-prompt configurations, and enforcing authorization policies. This multi-layered enforcement is implemented as an external security layer that integrates with existing agent frameworks without modifying their underlying models, making it compatible with six different agent frameworks tested in the evaluation.
- The security evaluation involved a simulated federation of eight organizations deploying five-agent teams across six agent frameworks, testing 14 attack scenarios and six benign tasks across five agent models with multiple attack variations and repetitions. Results showed attack containment rising from 43% to 84% with all enforcement mechanisms enabled (40% to 80% for the 11 scenarios evaluated consistently), while a panel of judge models assessed outcomes. ATI uses IETF WIMSE workload token formats for identity verification and Entity Attestation Tokens for integrity verification, and is released as an open-source package.

## Context
As AI agents increasingly collaborate across organizational boundaries—invoking tools, delegating tasks, and interacting with agents operated by independent entities—the absence of a common mechanism for verifying cross-organizational agent identity, execution integrity, and authorization represents a critical gap in current agent frameworks. Existing frameworks support planning and coordination but do not address the security and trust challenges that arise when agents from different organizations interact, making ATI a timely contribution to the emerging field of multi-agent security infrastructure.

## Implications
For practitioners deploying multi-agent systems across organizational or vendor boundaries, ATI provides a practical, framework-independent security layer that can be adopted incrementally without redesigning existing agent architectures, offering a standardized path toward verifiable agent interactions. The use of IETF-standard token formats (WIMSE workload tokens and Entity Attestation Tokens) positions ATI for potential adoption as an industry standard, while the open-source release and minimal 174-microsecond overhead make it feasible for production deployments where cross-organization agent trust and accountability are essential.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.23202v1)
