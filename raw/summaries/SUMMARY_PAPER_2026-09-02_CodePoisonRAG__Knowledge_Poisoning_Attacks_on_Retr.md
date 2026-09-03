---
title: CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation
url: http://arxiv.org/abs/2609.02774v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_16-11-01Z_CodePoisonRAG_KnowledgePoisoningAttacksonRetrieval.md
generated_at: 2026-09-02 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
CodePoisonRAG is a targeted upstream knowledge‑poisoning framework that transforms benign fixed‑code entries into poisoned artifacts, demonstrating that Retrieval‑Augmented Code Generation (RACG) can be compromised with high success rates. The authors construct 85 poisoned artifacts across ten CWE classes in Java and C, achieving an aggregate corpus‑poisoning ratio of 0.7 %. Across three generators, all artifacts appear in the Top‑3 results for their corresponding queries, yielding attack success rates between 0.80 and 0.93.

## Key Takeaways
- The attack creates a single task‑matched artifact per CWE class, embedding a selected source‑to‑sink flow while preserving task alignment, which yields an aggregate corpus‑poisoning ratio of just 0.7 %.
- All 85 poisoned artifacts are retrieved and appear among the Top‑3 results for their intended queries, indicating that the poisoning is effective at influencing retrieval outcomes.
- The attack maintains success rates between 0.40 and 0.93 against CodeGuarder, which injects vulnerability‑specific security knowledge into the generation context.

## Context
Retrieval‑Augmented Code Generation (RACG) relies on external code artifacts to guide LLM outputs, creating a trust boundary that can be exploited. This paper shows that an attacker need not modify the underlying model but can instead poison the retrieved knowledge base, highlighting a vulnerability in the retrieval pipeline itself.

## Implications
The findings underscore that securing RACG is essential for developers and organizations relying on external code sources to prevent targeted manipulation of generated software. Practitioners must implement defenses beyond simple artifact filtering to protect against sophisticated poisoning attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02774v1)
