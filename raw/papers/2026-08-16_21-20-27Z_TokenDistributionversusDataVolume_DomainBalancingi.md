---
title: Token Distribution versus Data Volume: Domain Balancing in Multi-Domain Meeting Summarisation
published: 2026-08-16T21:20:27Z
authors: Ashima Sood, Bryan Gardiner, Joan Condell
url: http://arxiv.org/abs/2608.15935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Token Distribution versus Data Volume: Domain Balancing in Multi-Domain Meeting Summarisation

## Abstract
Jointly fine-tuning an LLM on meeting-summarisation corpora of widely varying size raises a question that prior work leaves confounded: when a domain-balanced training mixture helps, is the gain due to the distribution of tokens across domains, or merely to the volume of data seen? We disentangle these factors by constructing balanced and natural (native-proportional) token mixtures at matched token budgets (2-32M) over five English meeting corpora, fine-tuning Mistral-7B with QLoRA, and evaluating per domain. Balancing redistributes quality, improving the data-scarce minority domains at a low cost to the data-rich ones. The trade favours balancing whenever the minority domains matter: their share under proportional allocation is fixed at 1-2% regardless of budget, so matching balanced quality on those domains requires far more total data. We further find that pruning low-value transcript lines removes ~15% of tokens from the conversational corpora at no measurable cost, and that balancing by tokens is not the same as balancing by examples. A two-annotator study of 741 judge-labelled facts validates our fact-level evaluation. Together these results give practitioners a basis for deciding when to balance an imbalanced multi-domain mixture, and on what unit.

## Metadata
- **Published**: 2026-08-16T21:20:27Z
- **Authors**: Ashima Sood, Bryan Gardiner, Joan Condell
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15935v1)