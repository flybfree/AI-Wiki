---
title: Lasting Effects of Abstract Pretraining Beyond Perplexity
published: 2026-09-30T01:48:40Z
authors: Zachary Shinnick, Hemanth Saratchandran, Damien Teney, Anton van den Hengel
url: http://arxiv.org/abs/2609.38764v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lasting Effects of Abstract Pretraining Beyond Perplexity

## Abstract
Language models are typically pretrained from random initialization. Recent work challenges this convention, showing that a brief warm-up on abstract, algorithmically generated data can provide a better starting point for subsequent learning of natural language. In this paper, we show that in small language models, such a warm-up improves specific capabilities that are not reflected in language-modeling perplexity. Our warm-up uses an abstract stack-manipulation task that requires compositional and state-tracking capabilities. Allocating as little as 1% of pretraining tokens to this data improves multi-hop question answering by up to 3.9 F1 points on MUSIQUE, with additional gains on HOTPOTQA and 2WIKIMULTIHOPQA despite comparable language-modeling perplexity. Controlled experiments show that the warm-up substantially accelerates the acquisition of deeper reasoning chains. We also explore what drives this transfer. First, the structure of the data matters: replacing the stack task with a queue fails to produce the same gains. Second, the gains are specific: performance improves on sequential reasoning chains, with no consistent benefit on tasks that combine or compare independent facts. Third, timing matters: mixing abstract data with natural language is far less effective than an initial dedicated phase, and exposure after pretraining completely removes the benefits. The early advantage persists through billions of subsequent language tokens. These results show that early abstract training can reliably shape the capabilities language models later acquire.

## Metadata
- **Published**: 2026-09-30T01:48:40Z
- **Authors**: Zachary Shinnick, Hemanth Saratchandran, Damien Teney, Anton van den Hengel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38764v1)