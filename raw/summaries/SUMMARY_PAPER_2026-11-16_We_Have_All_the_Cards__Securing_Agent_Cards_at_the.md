---
title: We Have All the Cards: Securing Agent Cards at the Operational Trust Boundary of the Agent2Agent Protocol
url: http://arxiv.org/abs/2611.18887v1
type: paper-summary
date: 2026-11-16
source_paper: 2026-11-13_19-46-07Z_WeHaveAlltheCards_SecuringAgentCardsattheOperation.md
generated_at: 2026-11-16 21:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses a critical security gap in the Agent2Agent (A2A) protocol, where Agent Cards containing attacker-controllable natural-language metadata can influence agent selection before a provider is actually invoked. The authors introduce SECCARD, a layered validation framework that combines protocol-level checks, deterministic analysis, and LLM-based semantic reasoning to detect manipulations in Agent Cards. Their evaluation demonstrates that SECCARD can achieve up to 97.0% security recall against controlled attacks while maintaining a low false-positive rate, though performance varies dramatically depending on the underlying LLM judge selected.

## Key Takeaways
- The A2A protocol's Agent Cards introduce a pre-invocation trust problem: attacker-controllable natural-language fields in machine-readable metadata can manipulate orchestrator decisions before any provider is invoked, creating a discovery-time attack surface that existing protocol checks do not adequately address. The authors formalize this threat through a taxonomy of ten distinct Agent Card manipulation attack categories.
- SECCARD employs a layered defense combining protocol conformance checks, deterministic rule-based analysis, and LLM-based semantic reasoning. On a 660-card real-card perturbation benchmark with matched benign controls, the strongest semantic judge achieves 97.0% security recall at only a 1.7% false-positive rate, demonstrating that benign Agent Cards are largely preserved while malicious manipulations are caught.
- Performance is highly model-dependent: across nine different LLM judges evaluated on a 260-card synthetic adversarial benchmark spanning all ten attack categories, security recall ranges from 25.8% to 92.3%. This wide variance reveals that the choice of underlying LLM judge is a critical deployment decision, not merely an implementation detail, and that no single judge provides uniformly robust protection.

## Context
As AI agent interoperability protocols like A2A gain traction for enabling orchestrators to discover and invoke external agents through machine-readable metadata, the trust boundary shifts from runtime execution to discovery time. This paper matters because it is among the first to systematically characterize and benchmark the discovery-time attack surface specific to agent metadata cards, moving beyond runtime sandboxing concerns to address how untrusted natural-language descriptions can poison selection logic before any code is executed. The empirical measurement of 36.1 million Internet domains and collection of 310 deployed Agent Cards grounds the work in the emerging real-world A2A ecosystem rather than purely theoretical threat modeling.

## Implications
For practitioners deploying multi-agent systems, this work signals that Agent Card validation must be treated as a first-class security control at the operational trust boundary, not an afterthought handled by protocol conformance alone. Organizations integrating A2A-compatible agents should implement layered validation pipelines and carefully benchmark their chosen LLM judge against adversarial benchmarks before trusting discovery-time filtering. The stark model-dependent performance variation also implies that current LLM-based semantic judges cannot yet be treated as interchangeable security components, and that protocol designers should consider deterministic or hybrid approaches to reduce reliance on any single model's judgment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.18887v1)
