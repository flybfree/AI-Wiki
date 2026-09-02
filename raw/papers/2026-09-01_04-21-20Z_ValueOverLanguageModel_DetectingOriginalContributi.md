---
title: Value Over Language Model: Detecting Original Contribution in Writing
published: 2026-09-01T04:21:20Z
authors: Vibhhu Sharma, Thorsten Joachims, Sarah Dean
url: http://arxiv.org/abs/2609.00700v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Value Over Language Model: Detecting Original Contribution in Writing

## Abstract
LLMs have been rapidly adopted across writing tasks, prompting the development of tools for detecting LLM-generated text. Yet, these tools largely measure how much of a document's surface text was written by an LLM and aren't fundamentally designed to measure how much of the information content or ideas originated from the LLM itself rather than being supplied by the user in the prompt. In this work, we design a framework that measures how much value a person adds on top of what a language model could have easily produced by itself. The method requires no training or labeled data and never scores the document's surface text, insulating it from stylistic confounders. Instead, it extracts the document's content at increasing levels of granularity, uses an LLM to reconstruct the document from each partial representation, and compares these reconstructions with those produced from the task description alone. We call this framework Value Over Language Model (VOLM), which measures a document's contribution relative to a replacement-level document that an LLM could produce from the task description alone. We evaluate VOLM with a specific instantiation of this framework across three domains: news articles, ICLR peer reviews, and argumentative essays. VOLM separates human-authored documents from matched LLM-generated documents produced from generic task descriptions, while remaining substantially invariant to content-preserving transformations, including LLM-based reconstruction and round-trip translation. We further find that increasingly constrained content extractors reduce residual differences between LLM-generated and humanized text, demonstrating the importance of disentangling informational content from stylistic variation. We hope these results encourage further work on specialized instantiations of the framework and on assessing human contributions in LLM-assisted writing more generally.

## Metadata
- **Published**: 2026-09-01T04:21:20Z
- **Authors**: Vibhhu Sharma, Thorsten Joachims, Sarah Dean
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00700v1)