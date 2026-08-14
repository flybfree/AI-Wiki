---
title: PIPES: Securing Agent Perception with Provenance and Priors
url: http://arxiv.org/abs/2608.12789v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_03-49-00Z_PIPES_SecuringAgentPerceptionwithProvenanceandPrio.md
generated_at: 2026-08-13 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PIPES, a screening framework that secures agent perception by enforcing provenance and prior constraints on tool responses. It demonstrates that PIPES reduces attack success rates from 84.7% to 2.3% while maintaining high benign utility across multiple benchmarks. The approach leverages static field contracts for structured data and dynamic trajectory analysis for open-ended inputs.

## Key Takeaways
- PIPES screens response units using semantic priors and source provenance, marking violations for removal or escalation.
- The framework reduces attack success rates from 84.7% to 2.3% on Gemma 4 31B IT across VitaBench and AgentDyn splits.
- It preserves benign utility at around 92.5%, only a slight drop from the baseline.

## Context
AI agents increasingly rely on external data sources that carry varying trust levels, creating vulnerabilities to state-corruption attacks where malicious inputs masquerade as legitimate information. This work addresses the need for robust perception safeguards in autonomous systems. Such defenses are essential as agents evolve toward more complex environments where trust assumptions become fragile.

## Implications
Practitioners can adopt PIPES to harden agent decision pipelines against adversarial manipulation while keeping performance high. The approach offers a scalable defense that integrates provenance checks into existing schema contracts without sacrificing utility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12789v1)
