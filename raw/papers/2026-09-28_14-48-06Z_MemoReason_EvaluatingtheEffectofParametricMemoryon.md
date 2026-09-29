---
title: MemoReason: Evaluating the Effect of Parametric Memory on Contextual Reasoning in LLMs
published: 2026-09-28T14:48:06Z
authors: Zineddine Tighidet, Andrea Mogini, Jiali Mei, Patrick Gallinari, Benjamin Piwowarski
url: http://arxiv.org/abs/2609.35312v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemoReason: Evaluating the Effect of Parametric Memory on Contextual Reasoning in LLMs

## Abstract
Large Language Models (LLMs) perform well on reasoning benchmarks, but it remains unclear whether this reflects genuine contextual reasoning or reliance on facts memorized in their parameters. We investigate this by distinguishing two possibilities: a broad \textit{memorization bias}, where familiar content improves reasoning performance, and the \textit{Strong Parametric Shortcut Hypothesis}, where models skip reasoning entirely and recall stored answers. To test these effects, we introduce \textbf{MemoReason}, a human-curated benchmark that pairs factual reasoning tasks with structurally identical \fictitiousterm{} versions where real entities like people, companies, or dates are systematically replaced by \fictitiousterm{} ones of the same type. This \scorerevision{preserves task structure and specified reasoning operations} while varying the familiarity of the context, allowing controlled measurement of how the parametric memory affects reasoning. \revision{Our evaluation of recent LLMs reveals consistent and statistically significant performance drops of up to 15.7\% in the fictitious setting, demonstrating a clear memorization bias.} However, a targeted analysis of \revision{questions failed in the fictitious setting} shows that models rarely respond with the corresponding factual answer, indicating that direct parametric shortcuts are not the dominant failure mode. These findings suggest that parametric memory influences reasoning through mechanisms more complex than simple factual recall. \textbf{MemoReason} provides a controlled framework for studying these mechanisms and for extending paired factual-fictitious{} evaluation to broader reasoning settings.

## Metadata
- **Published**: 2026-09-28T14:48:06Z
- **Authors**: Zineddine Tighidet, Andrea Mogini, Jiali Mei, Patrick Gallinari, Benjamin Piwowarski
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35312v1)