---
title: ROBE: Reversed-Order-Biased-Experts for Extracting Extreme Long-tail Events from Historical Texts
published: 2026-08-25T08:56:21Z
authors: Stella Verkijk, Piek Vossen
url: http://arxiv.org/abs/2608.24268v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ROBE: Reversed-Order-Biased-Experts for Extracting Extreme Long-tail Events from Historical Texts

## Abstract
This paper proposes methods to extract over 50 types of events from a Dutch historical corpus spanning the 17th and 18th centuries. The methods we propose aim to tackle the impossible: extracting the long-tail of the long-tail. Historic data from before the 19th century is in itself a niche domain not covered in the pre-training of Large Language Models, and we aim to extract events only very scarcely annotated in the training data available for this domain. We propose creating expert classifiers for subgroups of the events present in the training data. We make these groupings based on similar frequency in the training data or on semantic relatedness. Experts trained on underrepresented events are assigned higher priority when predicting to avoid being dominated by frequency biases. We refer to this new way of combining classifiers, specifically tailored to protect the long-tail, as ROBE: Reversed-Order-Biased-Experts. We also propose a controlled method to create domain-specific synthetic data. Our two implementations of ROBE outperform a simple fine-tuned encoder model with a .10 increase in recall and a .16 increase in precision respectively. The best model achieves a .10 increase in f1 for a group of long-tail classes in our niche data set.

## Metadata
- **Published**: 2026-08-25T08:56:21Z
- **Authors**: Stella Verkijk, Piek Vossen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24268v1)