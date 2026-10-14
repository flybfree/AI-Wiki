---
title: When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems
url: http://arxiv.org/abs/2610.16039v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-12_01-23-51Z_WhenAgentsTalk_SecretsTravel_Topology_DrivenLeakag.md
generated_at: 2026-10-13 21:44
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates a previously overlooked privacy-leakage problem in multi-agent LLM systems (MALS), where information shared with an authorized agent can propagate through routine coordination to unauthorized recipients purely due to system topology, without any compromise or malicious behavior. The authors evaluate 485 scenarios across three communication topologies and introduce RECONS, a recipient-conditioned sanitization framework that reduces residual disclosure from 96.7% to 29.25% while preserving 94.1% of authorized disclosures, demonstrating that privacy enforcement must reason about runtime communication paths rather than relying on sensitivity-based or topology-only assumptions.

## Key Takeaways
- Topology-driven leakage is a distinct and significant threat: while surface leakage remains nearly flat at 60.6–62.8% across topologies, disclosure to topology-introduced recipients surges from 0% to 52.2%, meaning that the communication graph itself silently creates new unauthorized recipients even when no agent behaves maliciously. This effect persists across four generator models and a second orchestration framework, though magnitude and relay paths differ, confirming the phenomenon is architecture-agnostic.
- RECONS operates as a Detect → Decide → Transform pipeline that conditions its intervention on the specific recipient and execution context rather than on information sensitivity alone. It achieves 94.1% preservation of authorized disclosures compared to only 20.5% under blanket redaction, showing that recipient-aware sanitization is far more effective than uniform filtering. However, detection coverage remains the dominant bottleneck, accounting for 95.5% of residual disclosures, indicating that the hardest unsolved problem is identifying what needs protection in the first place.
- Framework choice introduces a 150x leakage spread independently of topology, meaning that topology alone is insufficient as a privacy-enforcement assumption. Practitioners must account for both the orchestration framework and the runtime communication path realized during execution, as either factor can independently amplify or reshape leakage patterns.

## Context
As multi-agent LLM systems move from research prototypes into production deployments for enterprise workflows, software engineering, and autonomous coordination, the assumption that privacy can be enforced through static sensitivity labels or fixed access-control policies is increasingly inadequate. This paper sits at the intersection of AI safety, systems security, and multi-agent orchestration, addressing a gap where conventional data-protection frameworks were designed for single-agent or human-mediated pipelines and do not model the emergent propagation paths created by agent-to-agent communication graphs.

## Implications
For practitioners building MALS in regulated industries such as healthcare, finance, or legal services, these findings mandate that privacy controls be re-architected around runtime recipient identification and communication-path awareness rather than static classification rules. The 150x leakage spread driven by framework choice alone signals that vendor selection and orchestration-layer design carry direct privacy consequences, making RECONS-style recipient-conditioned sanitization a practical near-term mitigation while the field works toward closing the detection-coverage gap that currently dominates residual disclosure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16039v1)
