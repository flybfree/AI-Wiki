---
title: Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors
url: http://arxiv.org/abs/2608.23873v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_22-26-58Z_SemanticOverlays_MitigatingPromptInjectionwithAnno.md
generated_at: 2026-08-25 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes Semantic Overlays as a method to mitigate prompt injection by adding non‑textual annotations that the model can interpret beyond token boundaries. The approach trains small adapters placed at specific positions in the residual stream to encode span identity and instructions, allowing the model to follow complex payloads while preserving readability.

## Key Takeaways
- Semantic Overlays create an out‑of‑band annotation channel that cannot be replicated by tokens, providing a new way for the model to understand which parts of the input are under control. - The technique is trained and adaptable, enabling overlays to carry complex semantics such as language changes or imperatives that steer behavior without altering the underlying text. - Composable overlays allow transparent reading of original content while still executing designated instructions, achieving high exact‑copy rates (92.5%) on marked spans.

## Context
Language models rely heavily on token sequences to maintain context, making them vulnerable when an attacker can manipulate span boundaries. Traditional defenses focus on syntactic parsing or input sanitization, which often fail against sophisticated injection attacks that exploit the model’s internal state transitions.

## Implications
Semantic Overlays offer a practical upgrade for developers seeking robust prompt handling without sacrificing performance. By integrating these lightweight adapters into serving pipelines, organizations can protect critical applications from malicious inputs while maintaining seamless user experience and readability of content.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23873v1)
