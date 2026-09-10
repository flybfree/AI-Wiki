---
title: From Retrieval to Weights: Parametric Individualization of Small Language Models with Individual Text Corpora
published: 2026-09-09T13:32:04Z
authors: Christoph Wigbels, Ali Abusaleh, Markus T. Jansen, Alexander Mehler, Markus J. Hofmann
url: http://arxiv.org/abs/2609.10155v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Retrieval to Weights: Parametric Individualization of Small Language Models with Individual Text Corpora

## Abstract
We approach a cognitive simulation perspective on episodic and semantic memory in multiple-choice question answering by incorporating text from individual text corpora (ITC) into retrieval-augmented generation and DoRA fine-tuning. We web-crawl the search histories of 515 participants who answered 36 multiple-choice knowledge items and analyze a stratified subsample of 150 participants. For each participant, one DoRA adapter consolidates their ITC into a small language model (SLM) whose baseline correctness falls below the participants' lowest quartile. The adapter measurably writes the ITC into the weights: it fits its own participant's held-out text better than other participants' texts (dz =1.27), an individuality effect that increases with ITC size in rank order. On the generalized knowledge test, however, the adapter adds knowledge rather than alignment with the individual: log-loss match improves, whereas match accuracy under a bias-corrected PMI readout does not, and retrieval adds nothing on top. Our results demonstrate that ITCs can be consolidated into the weights of SLMs, an encouraging basis for individualized tutoring agents, and we discuss how to move from there toward a realistic simulation of episodic and semantic memory at the individual level.

## Metadata
- **Published**: 2026-09-09T13:32:04Z
- **Authors**: Christoph Wigbels, Ali Abusaleh, Markus T. Jansen, Alexander Mehler, Markus J. Hofmann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.10155v1)