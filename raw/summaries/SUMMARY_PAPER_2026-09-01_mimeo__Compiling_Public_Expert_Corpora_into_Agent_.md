---
title: mimeo: Compiling Public Expert Corpora into Agent Skills and Testing What Transfers
url: http://arxiv.org/abs/2609.00453v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_22-46-48Z_mimeo_CompilingPublicExpertCorporaintoAgentSkillsa.md
generated_at: 2026-09-01 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces mimeo, an open-source tool that compiles public expert corpora into structured files for AI agents and tests whether the extracted material improves performance. Experiments show that knowledge access is significantly better than closed-book conditions, while persona effects are limited and detectable. The authors conclude that mimeo provides a reliable reference but does not demonstrate genuine judgment transfer.

## Key Takeaways
- Knowledge access was clearest: mimeo answered all 20 obscure, quotation-heavy questions whereas the closed-book condition answered at most 10, indicating strong retrieval benefit.
- Grounding showed one clear benefit: personas written from model memory misstated a documented position on 1‑4 of 20 answers under every grader, while plain agents never did this.
- Every persona was easy to spot on short open prompts and adding task material lowered identification by 18‑23 points, suggesting limited transfer.

## Context
AI systems often rely on external knowledge that is not directly stored in the model. Tools like mimeo aim to bridge this gap by providing inspectable, human-sourced data. The study highlights how such corpora can be integrated without compromising model interpretability or performance.

## Implications
For developers, mimeo offers a lightweight way to augment agents with reliable expert references while keeping provenance transparent. Practitioners should treat these files as reference material rather than proof of learned expertise, avoiding over-reliance on AI-judged “sounds like the expert” scores.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00453v1)
