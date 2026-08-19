---
title: When Writing Style Drifts: Benchmarking Authorship Verification under Distribution Shifts in Genre, Time and the AI-Era
published: 2026-08-18T16:29:24Z
authors: Lotta Kiefer, Brisca Balthes, Christoph Leiter, Yamen Ajjour, Elena Schmidt, Steffen Eger
url: http://arxiv.org/abs/2608.17979v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Writing Style Drifts: Benchmarking Authorship Verification under Distribution Shifts in Genre, Time and the AI-Era

## Abstract
Authorship verification (AV) assumes that an author's writing style remains sufficiently stable to distinguish it from that of other writers. In practice, however, this assumption is challenged by distribution shifts caused by changes in genre, time, and AI-assisted writing. Existing AV benchmarks typically study these factors in isolation and focus predominantly on English, limiting our understanding of model robustness under realistic conditions. We introduce AVShift, the first German benchmark for systematically evaluating AV under multiple distribution shifts. AVShift comprises over 150,000 text pairs spanning three genres and 21 years, enabling controlled evaluation of cross-genre, temporal, and AI-era shifts within a unified framework. We benchmark representative feature-based, embedding-based, and LLM-based approaches. Our experiments show that fine-tuned LLMs generalize best across genres and benefit substantially from stylistically diverse training data. We further demonstrate that temporal drift is one of the strongest factors affecting AV, with performance degrading significantly as the time gap between documents increases. In contrast, we find no evidence of a measurable AI-era distribution shift within AVShift. Finally, our feature analysis reveals stylistic features that remain stable across genres, while their relative importance varies depending on the specific genre transition. We release AVShift and our code for future research.

## Metadata
- **Published**: 2026-08-18T16:29:24Z
- **Authors**: Lotta Kiefer, Brisca Balthes, Christoph Leiter, Yamen Ajjour, Elena Schmidt, Steffen Eger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17979v1)