---
title: Beyond Predefined Sinks: Security-Aware Dependency Analysis for LLM Agents
url: http://arxiv.org/abs/2610.03014v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_08-48-09Z_BeyondPredefinedSinks_Security_AwareDependencyAnal.md
generated_at: 2026-10-04 21:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces AgentSecGraph, a security-aware static analysis framework that moves beyond predefined sensitive operations as anchors for analyzing LLM agent security risks. By constructing a Security-Aware Agent Dependency Graph (Security-ADG) for each security-sensitive operation candidate, the framework augments operation identity with agent relevance, source and dependency evidence, trust-boundary context, guard evidence, and external-effect semantics. The evaluation demonstrates that security-aware dependency and contextual evidence enable distinctions in security behavior that cannot be recovered from sensitive-operation identity alone, achieving 91.1% context preservation compared to 20.0% for a sink-only view.

## Key Takeaways
- The framework constructs a candidate-centered Security-ADG for each security-sensitive operation, augmenting operation identity with agent relevance, source and dependency evidence, trust-boundary context, guard evidence, and external-effect semantics. This multi-dimensional approach addresses the fundamental limitation that operation identity alone is insufficient to determine security implications in LLM agent systems.
- AgentSecBench provides a corpus of 67 real-world LLM-agent repositories spanning 11 ecosystems and 37,542 source files. The analyzer identifies 23,866 static security-sensitive operation candidates across 65 repositories, recovering source-to-operation dependency evidence for 9,821 candidates (41.15%) and potential guard evidence for 3,075 (12.88%), completing in 50.8 minutes.
- In a reproduction-backed evaluation layer, the authors establish 22 security-sensitive behaviors across 13 repositories, including one confirmed vulnerability, one pending disclosure candidate, and 20 guarded behaviors. In nine held-out cases, Security-ADG preserves 91.1% of reference context and all five observed guards, vastly outperforming a sink-only view (20.0%) and a simplified ADG (40.0%).

## Context
LLM-based agents increasingly connect model-generated decisions to security-sensitive software capabilities such as command execution, filesystem access, network communication, browser control, and external tools. Existing security analyses in this space typically rely on predefined sensitive operations as anchors, treating operation identity as the primary signal for risk assessment. This paper addresses a critical gap in the field by demonstrating that such an approach systematically misses the contextual, dependency, and guard information necessary to distinguish genuinely dangerous behaviors from properly guarded ones, which is essential as agentic AI systems proliferate across production software ecosystems.

## Implications
For practitioners building and auditing LLM agent systems, this work provides a practical static analysis methodology that can identify confirmed vulnerabilities, pending disclosures, and properly guarded behaviors without requiring full runtime execution, enabling earlier and more accurate security triage. For the broader AI safety and software security community, the findings challenge the prevailing assumption that identifying sensitive operations is sufficient for security assessment, suggesting that future tooling and benchmarks must incorporate dependency-aware and context-aware analysis to meaningfully evaluate agent security posture at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03014v1)
