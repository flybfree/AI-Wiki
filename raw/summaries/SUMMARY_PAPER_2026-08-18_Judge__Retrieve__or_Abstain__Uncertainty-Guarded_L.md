---
title: Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees
url: http://arxiv.org/abs/2608.17994v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_16-42-02Z_Judge_Retrieve_orAbstain_Uncertainty_GuardedLLMJud.md
generated_at: 2026-08-18 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a risk‑controlled framework for LLM judging that guarantees the false discovery rate of accepted verdicts stays below a user‑specified level α with high probability. By calibrating uncertainty thresholds on a held‑out set using finite‑sample Clopper–Pearson intervals, the method routes uncertain parametric judgments to retrieval‑augmented evaluation and preserves the guarantee across both modes.

## Key Takeaways
- The framework uses calibrated uncertainty thresholds derived from finite‑sample Clopper–Pearson intervals to keep the false discovery rate below α.  
- When a parametric judge is not confident, it automatically switches to a retrieval‑augmented mode that gathers web evidence and re‑evaluates under a second threshold.  
- The finite‑sample guarantee carries over to the two‑threshold routing without extra assumptions, yielding higher coverage than single‑mode baselines.

## Context
LLM judges are widely used for subjective evaluation but lack formal risk guarantees when reference answers are unavailable. Existing methods either rely on parametric knowledge or tool augmentation, each with reliability concerns and computational trade‑offs. This work addresses those gaps by providing provable error bounds in a scalable way.

## Implications
Practitioners can now deploy LLM judges with confidence that their accepted verdicts meet predefined accuracy thresholds, reducing the risk of false positives. The approach also enables higher evaluation coverage while maintaining reliability, which is valuable for large‑scale alignment and benchmarking systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17994v1)
