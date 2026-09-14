---
title: NDT Factory: Synthesizing Verified Network Digital Twins from Semantic Models via Multi-Agent LLM
url: http://arxiv.org/abs/2609.12170v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-10_19-58-43Z_NDTFactory_SynthesizingVerifiedNetworkDigitalTwins.md
generated_at: 2026-09-14 15:11
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces the NDT factory, a multi-agent software system that leverages Large Language Models to automatically synthesize executable behavioral Network Digital Twins from semantic models. Validated through a Call Admission Control case study, the framework demonstrates high reliability and adaptability for autonomous network management without requiring manually coded analytical logic. The system achieves near-perfect decision alignment with reference implementations while maintaining deterministic and verifiable execution across diverse service intents.

## Key Takeaways
- The NDT factory utilizes a multi-agent architecture to dynamically generate executable behavioral digital twins directly from semantic models, eliminating the rigid pre-defined analytical logic that traditionally limits adaptability in closed-loop network control systems.
- In a simulation evaluating 300 Network Service Intents, the synthesized twins achieved a 99.3% decision agreement with a reference implementation and correctly attributed all service rejections, proving robustness under varying operational conditions.
- The framework successfully employs parallel synthesis and orchestration to produce complete digital twin models that consistently achieve 100% compilation and test pass rates, ensuring deterministic execution aligned with TM Forum Level 4 autonomy standards.

## Context
As telecommunications networks grow increasingly complex, achieving true L4 autonomy requires adaptive systems capable of evaluating service intents without rigid, pre-programmed rules. This research bridges the gap between semantic modeling and executable network simulation by integrating multi-agent LLM orchestration with digital twin generation. It represents a significant step toward self-optimizing infrastructure that can dynamically adapt to evolving operational requirements while maintaining verifiable performance guarantees.

## Implications
The ability to automatically synthesize verified behavioral twins on demand could drastically reduce the engineering overhead required for autonomous network operations and closed-loop control systems. Network operators may leverage this framework to rapidly prototype, validate, and deploy adaptive management strategies without extensive manual coding or simulation setup. Ultimately, this approach paves the way for more resilient, self-healing telecommunications architectures that align with next-generation autonomy benchmarks and reduce dependency on static analytical logic.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.12170v1)
