---
title: Text2DSL: LLM-Based Code Generation for Domain-Specific Languages
published: 2026-06-21T16:44:20Z
authors: Alexander V. Kozachok, Alexander M. Nazimov, Shamil G. Magomedov
url: http://arxiv.org/abs/2606.22586v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Text2DSL: LLM-Based Code Generation for Domain-Specific Languages

## Abstract
Domain-specific languages (DSLs) are widely used for managing operating system security policies, yet manually authoring rules in such languages demands high expertise and is error-prone. This paper formalises the task of automatic DSL code generation from natural language descriptions - Text2DSL - as a distinct problem class, separate from Text-to-SQL and general-purpose code generation. We introduce the PolkitBench dataset comprising 4,204 verified natural-language-to-Polkit-rule pairs, each validated through a three-level AST-based pipeline. Controlled prompt experiments on two MoE models of different scale and provenance - GigaChat-10B-A1.8B (1.8B active parameters) and Nemotron-3-Nano-30B-A3B (3B active) - demonstrate the critical role of structured context (BNF grammar, API specification, permitted identifier vocabulary) for LLM-based DSL code generation. Across both models, supplying context raises syntactic validity to 98.6-99.4%, structural validity by +9.7 to +35.5 pp, and the CodeBLEU score by +60% to +95%. The consistency of the effect across models of different scale and provenance indicates that, for the Text2DSL class of problems, injecting a formal target-language specification into the prompt context is a robust enabling factor for high-quality generation without model fine-tuning.

## Metadata
- **Published**: 2026-06-21T16:44:20Z
- **Authors**: Alexander V. Kozachok, Alexander M. Nazimov, Shamil G. Magomedov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.22586v1)