---
title: When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization
url: http://arxiv.org/abs/2609.02964v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_07-13-40Z_WhenOptimizationBecomesManipulation_DefendingGener.md
generated_at: 2026-09-03 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GEO Defender, a two‑stage defense that mitigates malicious generative engine optimization (GEO) attacks without fine‑tuning the target language model. Experiments show the defense cuts attack success from 50.32 % to 6.20 % while preserving answer quality and factual use.

## Key Takeaways
- GEO rewrites documents to boost citation relevance, making fact verification and perplexity filtering ineffective because both are amplified by high‑quality content.
- The proposed Shield Reranker adds a preference‑based residual that demotes GEO‑rewritten docs while keeping benign relevance judgments intact.
- Training‑Free Shield Generation distills defense outcomes into an experience library that steers the LLM’s source use at inference, enabling generalization to unseen attacks.

## Context
Malicious manipulation of generative search results threatens the trustworthiness of AI‑driven information retrieval. As GEO techniques become automated and agentic, existing defenses relying on post‑hoc checks fall short, highlighting a need for model‑agnostic solutions that integrate seamlessly into LLM pipelines.

## Implications
GEO Defender demonstrates that robust defense can be achieved without retraining large models, offering practitioners a practical tool to safeguard AI systems from subtle attacks. This work encourages the community to prioritize privacy‑preserving, fine‑tuning‑free defenses in generative search development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02964v1)
