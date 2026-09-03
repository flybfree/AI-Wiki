---
title: FUSE: An Evaluating Framework for Dangerous Capabilities of LLMs
url: http://arxiv.org/abs/2609.02168v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_06-31-39Z_FUSE_AnEvaluatingFrameworkforDangerousCapabilities.md
generated_at: 2026-09-02 21:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FUSE, a modular framework that evaluates large language models across three orthogonal dimensions — Knowledge, Defense, and Harm — to generate a standardized dangerous‑capability profile. The authors demonstrate the framework with a chemical‑biological module, comparing 12 commercial LLMs from four families and showing that capability evolution is not monotonic despite safety improvements.

## Key Takeaways
- Models with similar knowledge bases can differ markedly in refusal resilience, indicating that defensive strength is independent of factual depth.  
- Strong defenses do not necessarily reduce harmful outputs when models comply, revealing a gap between compliance and safety.  
- Family‑level patterns separate Claude, DeepSeek, and GPT models, suggesting that architectural or training choices shape dangerous capability profiles.

## Context
Safety evaluation for AI remains fragmented, leading to inconsistent governance of high‑risk capabilities. This work provides a unified protocol that can be applied across domains while preserving modularity, offering a more reliable benchmark than existing approaches.

## Implications
The framework helps industry stakeholders and researchers assess model risk systematically, guiding responsible deployment decisions. By exposing non‑monotonic capability trends, it underscores the need for ongoing monitoring rather than assuming safety with progress alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02168v1)
