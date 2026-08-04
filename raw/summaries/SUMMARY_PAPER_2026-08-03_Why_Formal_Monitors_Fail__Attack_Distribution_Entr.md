---
title: Why Formal Monitors Fail: Attack Distribution Entropy as a Coverage Bound for LTL-Based LLM Agent Safety
url: http://arxiv.org/abs/2608.01388v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_17-08-21Z_WhyFormalMonitorsFail_AttackDistributionEntropyasa.md
generated_at: 2026-08-03 23:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why formal monitors based on Linear Temporal Logic (LTL) and finite automata achieve inconsistent coverage across different LLM architectures. It proves that recall is bounded by the entropy of the attack distribution, showing high concentration yields good coverage while dispersion leads to near‑zero recall regardless of monitor design.

## Key Takeaways
- The recall of any fixed‑invariant FSA monitor cannot exceed the fraction of attacks covered by the k most frequent trigger‑completion patterns, a bound tied to attack distribution entropy. - When attacks are highly concentrated (low Shannon entropy), a small invariant set can achieve high recall; when they disperse across many distinct patterns (high entropy), no tractable fixed invariant set can capture them. - Empirical tests on eight frontier LLM backends show GPT‑class models have H≈0.24 bits with one pattern covering 96% of attacks, yielding 68–75% recall, whereas Gemini variants have H≈2.81 bits and seven clusters each ≤7%, resulting in only 6–13% recall.

## Context
Runtime safety monitors are essential for deploying LLM agents safely, but their performance varies unpredictably across models. This paper provides a theoretical link between monitor coverage and the statistical properties of adversarial attacks, offering an objective metric that explains observed discrepancies without relying on model‑specific heuristics.

## Implications
Practitioners can now select or design monitors based on attack entropy rather than arbitrary capacity scores, improving reliability for high‑risk applications. The pre‑deployment entropy test enables architecture‑aware monitoring decisions, aligning safety guarantees with the actual risk landscape of each LLM system.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01388v1)
