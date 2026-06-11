---
title: LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems
url: http://arxiv.org/abs/2605.22786v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-21_17-42-12Z_LCGuard_LatentCommunicationGuardforSafeKVSharingin.md
generated_at: 2026-06-11 10:45
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LCGuard, a framework that protects sensitive information when large language model agents share transformer key-value caches. It shows that without safeguards, cache artifacts can leak agent-specific inputs to an adversary, and the authors propose representation-level transformations to reduce this leakage while preserving task performance.

## Key Takeaways
- The shared KV cache is treated as latent working memory whose content may contain sensitive inputs that an adversarial decoder could reconstruct.  
- LCGuard learns reversible transformations applied before cache sharing that compress or anonymize agent-specific information without affecting task semantics.  
- Empirical results demonstrate lower reconstruction success rates and reduced attack success compared to baseline KV-sharing methods.

## Context
Current multi-agent LLM systems rely on shared transformer caches for efficient coordination, but these caches inadvertently expose intermediate reasoning states. This paper addresses the security gap by formalizing leakage through reconstruction and proposing a training paradigm that mitigates it.

## Implications
For practitioners deploying collaborative AI agents, LCGuard offers a practical way to enhance privacy without sacrificing efficiency. The approach could become standard in secure multi-agent frameworks as data sensitivity grows with model complexity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.22786v1)
