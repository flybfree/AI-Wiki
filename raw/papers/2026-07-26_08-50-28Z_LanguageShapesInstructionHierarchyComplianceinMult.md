---
title: Language Shapes Instruction Hierarchy Compliance in Multilingual LLMs
published: 2026-07-26T08:50:28Z
authors: Jiwon Moon, Yerin Hwang, Kyomin Jung
url: http://arxiv.org/abs/2607.23545v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language Shapes Instruction Hierarchy Compliance in Multilingual LLMs

## Abstract
Instruction hierarchy (IH) requires models to prioritize instructions by source, ensuring that higher-priority instructions override lower-priority ones. Despite its importance for safe and controllable deployment, existing evaluations have focused almost exclusively on English, leaving it unclear whether IH compliance remains stable in multilingual settings. We introduce XIH-Bench, a benchmark for multilingual IH evaluation with both same-language and cross-language conflicts across six languages, four domains, and three IH settings. Across models, we find two consistent patterns. First, IH compliance exhibits a clear language-dependent asymmetry: a language that strengthens compliance in the higher-priority position can become disruptive in the lower-priority position. Second, cross-language conflicts yield higher compliance than same-language conflicts, a phenomenon we term the Language Boundary Effect. We further show that language specialization can make lower-priority instructions in model-favored languages harder to override, creating multilingual reliability and security risks.

## Metadata
- **Published**: 2026-07-26T08:50:28Z
- **Authors**: Jiwon Moon, Yerin Hwang, Kyomin Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23545v1)