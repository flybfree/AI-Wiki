---
title: Adversarial Prompts for Acceptance Collapse in Speculative Decoding
url: http://arxiv.org/abs/2607.21804v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_20-42-41Z_AdversarialPromptsforAcceptanceCollapseinSpeculati.md
generated_at: 2026-07-26 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ADSD, a prompt‑suffix attack that exploits speculative decoding’s reliance on draft‑target alignment to force the verifier to reject valid outputs. By generating suffixes that shift draft probability mass toward tokens unlikely to be accepted by the target model, ADSD collapses acceptance while keeping task performance high. Experiments on GSM8K show a 62.3% increase in mean sample time with no drop in accuracy.

## Key Takeaways
- ADSD is the first attack that systematically reduces verifier acceptance through suffix manipulation.
- The attack leverages Soft‑Collapse, a verifier‑aligned surrogate derived from asymmetric speculative rules, to push draft probabilities toward rejected tokens.
- Results demonstrate the vulnerability across various domains, decoding strategies, and model architectures.

## Context
Speculative decoding aims to accelerate language models by generating drafts that align with target outputs, but this alignment is fragile. The paper highlights a hidden operational weakness that could undermine the promised speedups of such methods in real‑world applications.

## Implications
If speculative decoding becomes widely adopted, attackers may exploit these vulnerabilities to degrade system reliability without compromising output quality. Practitioners must consider adversarial robustness when deploying speculative inference pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21804v1)
