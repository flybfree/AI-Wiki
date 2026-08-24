---
title: Vibe Coding and Web Application Security: A Twin-Prompt Study
published: 2026-08-21T10:34:41Z
authors: Darko Andročec
url: http://arxiv.org/abs/2608.20963v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Vibe Coding and Web Application Security: A Twin-Prompt Study

## Abstract
Large language models increasingly generate complete web applications from natural-language prompts, raising the question of whether explicitly requesting security best practice improves the result. We study six functionally distinct web applications, each generated in two prompt variants that are identical except for an appended security-requirements section: a baseline (A) and a security-aware (B) variant. All twelve programs were produced by the same agentic coding assistant and the same model version in a single, non-iterative generation round, and were then analyzed with static, dependency, dynamic and manual techniques, yielding 75 confirmed findings out of 85 candidates. The security-aware variant produced fewer confirmed findings in every application (24 versus 51) and contained no Critical or High issues; the most severe finding was detected only by manual testing. Because the corpus is small and each variant was generated once, we report descriptive observations rather than statistically established effects, and position the work as a preliminary study whose pipeline is being scaled to multiple models and repeated runs.

## Metadata
- **Published**: 2026-08-21T10:34:41Z
- **Authors**: Darko Andročec
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20963v1)