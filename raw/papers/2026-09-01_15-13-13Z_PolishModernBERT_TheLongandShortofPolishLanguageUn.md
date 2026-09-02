---
title: Polish ModernBERT: The Long and Short of Polish Language Understanding
published: 2026-09-01T15:13:13Z
authors: Michał Perełkiewicz, Sławomir Dadas, Rafał Poświata, Małgorzata Grębowiec
url: http://arxiv.org/abs/2609.01379v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Polish ModernBERT: The Long and Short of Polish Language Understanding

## Abstract
Encoder-only Transformers remain effective for discriminative and representation-learning tasks, yet Polish encoders still largely rely on BERT/RoBERTa-style architectures. We introduce \textbf{Polish ModernBERT}, a family of four Polish encoders available at Base and Large scales, each with 512-token and 8K context variants. We adapt the ModernBERT pretraining recipe through staged selection experiments and release a long-context benchmark covering legal topic classification, ideological decision-direction prediction, factual-consistency assessment over literary plot summaries, and human-rights violation assessment. Across 30 tasks, Polish ModernBERT achieves the best overall performance among the evaluated Polish encoders, reaching 83.99 and 85.11 for the Base-8K and Large-8K models, respectively. On long-context tasks, the 8K variants improve over matched Polish RoBERTa-8K baselines from 67.47 to 77.15 and from 75.88 to 78.49 at the Base and Large scales, respectively. The Base-8K model achieves this gain with 22\% fewer parameters (149M vs.\ 190M). Efficiency measurements in representative inference setups show lower peak memory usage and latency than matched Polish RoBERTa baselines in both 512-token and 8K settings. Polish ModernBERT-8K-Base additionally achieves the best result on a Polish retrieval benchmark among the evaluated encoders below 300M parameters.

## Metadata
- **Published**: 2026-09-01T15:13:13Z
- **Authors**: Michał Perełkiewicz, Sławomir Dadas, Rafał Poświata, Małgorzata Grębowiec
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01379v1)