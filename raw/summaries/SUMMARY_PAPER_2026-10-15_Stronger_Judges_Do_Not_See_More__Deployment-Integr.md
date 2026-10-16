---
title: Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation
url: http://arxiv.org/abs/2610.21135v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_02-44-08Z_StrongerJudgesDoNotSeeMore_Deployment_IntegrityBli.md
generated_at: 2026-10-15 22:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces DIB-Bench, a benchmark designed to expose a critical blind spot in LLM-agent evaluation: the inability of output-only evaluators to detect tampered deployment configurations that preserve evaluated outputs. The authors demonstrate that stronger evaluators, including GPT-5-nano, actually accept more tampered outputs than weaker rule-based scorers, revealing that deployment-integrity blindness worsens with evaluator sophistication. The work formalizes this limitation through a PAC-style information-theoretic bound and proposes a manifest-hash identity channel as a zero-sample detection mechanism.

## Key Takeaways
- Stronger evaluators are paradoxically more permissive of tampered deployments: mean acceptance of tampered outputs rises from 88.6% with rule-based scorers to 94.1% with GPT-5-nano across 7,560 scored examples spanning six tamper types, meaning that investing in more capable judges actively worsens deployment-integrity detection rather than improving it.
- A trigger-conditional tamper that is completely invisible on the evaluation suite can produce 48–100% harmful outputs in production, and this harmfulness scales upward with model capability, creating a dangerous gap between benchmark performance and real-world safety for increasingly powerful models.
- The authors prove via a PAC-style bound that tampers producing zero output shift are fundamentally undetectable from output observations at any sample size, while a manifest-hash identity channel can detect such tampers with zero samples, establishing that output-based evaluation has an irreducible information-theoretic ceiling and that structural identity verification is necessary.

## Context
This paper addresses a foundational gap in the rapidly growing field of LLM-agent evaluation, where benchmarks increasingly rely on behavioral scoring and LLM-as-judge paradigms without verifying the integrity of the underlying runtime stack—model weights, inference engines, quantization layers, and serving infrastructure. As agentic systems are deployed in safety-critical domains, the assumption that output fidelity implies deployment fidelity becomes a critical vulnerability that existing evaluation frameworks do not address.

## Implications
For practitioners deploying LLM agents in regulated or safety-critical environments, this work signals that current evaluation pipelines cannot guarantee that the system being tested is the system being served, and that upgrading to stronger judges may mask rather than reveal deployment tampering. The proposed graded deployment-identity descriptor and manifest-hash verification channel offer concrete mechanisms for evaluation reports to include structural integrity checks, which could become essential compliance requirements as agentic AI systems scale into production.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21135v1)
