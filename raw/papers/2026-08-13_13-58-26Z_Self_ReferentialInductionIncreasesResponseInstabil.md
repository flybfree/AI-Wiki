---
title: Self-Referential Induction Increases Response Instability Relative to Unresolvable and Verifiable Questions in Large Language Models
published: 2026-08-13T13:58:26Z
authors: Paras Balani, Subhrakanta Panda
url: http://arxiv.org/abs/2608.13258v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Referential Induction Increases Response Instability Relative to Unresolvable and Verifiable Questions in Large Language Models

## Abstract
Self-referential prompting has been shown to reliably induce large language models to produce first-person reports resembling subjective experience, but no prior work measures how consistent these reports are across repeated, independent trials, or how that consistency compares to the model's behavior on other kinds of open-ended questions. We measure response instability, defined as one minus the mean pairwise cosine similarity of sentence embeddings computed over a compressed core claim extracted from each response, for three groups of questions: self-referential prompts eliciting a subjective-experience report, unresolvable philosophical questions unrelated to self-reference, and questions with a verifiable correct answer. Using 30 independent responses per question (360 responses total, Gemini API, temperature 0.7) across four questions per group, we find that self-referential questions show the highest instability (0.343 +/- 0.047), unresolvable philosophy questions show intermediate and tightly clustered instability (0.192 +/- 0.008), and verifiable questions show the lowest instability (0.105 +/- 0.058). This provides a quantitative baseline for the induced subjective-experience report, showing that it occupies a distinct, less stable position in the model's output distribution than ordinary open-ended philosophical uncertainty.

## Metadata
- **Published**: 2026-08-13T13:58:26Z
- **Authors**: Paras Balani, Subhrakanta Panda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13258v1)