---
title: TransNRank: Towards Accurate Neoantigen Ranking with Transformer
published: 2026-08-03T08:57:43Z
authors: Zhiyin An, Yuenan Hou, Shumeng Duan, Yiming Zhou, Yuanting Zheng, Leming Shi
url: http://arxiv.org/abs/2608.01924v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TransNRank: Towards Accurate Neoantigen Ranking with Transformer

## Abstract
Personalized neoantigen prediction is challenging due to the scarcity of positive samples, the noise of the experimental data, the severe class imbalance trait and the complex of immunogenicity features. Prior arts, such as linear regression and XGBoost fail to model long-range dependencies and contextual relationships within peptide features, therefore the performance of neoantigen positive recall rate is limited. In this paper, we present a novel deep learning framework based on Transformer, coined as TransNRank. By leveraging the self-attention mechanism, our model captures both local and global feature contexts, enabling more accurate recognition of immunogenic neoantigens. A positive-aware training objective is utilized to handle the class imbalance problem, assigning more weights to those few positive samples. Extensive experiments are performed on NCI, TESLA and HiTIDE datasets. Notably, our TransNRank can push the upper bound top 20 recall rate of neoantigen prediction from 46.9% (45 from 96) to 53.1% (51 from 96), while reducing the training epochs from 200 epochs to 20 epochs. Furthermore, we analyze the features contribution based on TransNRank and find that the mutation at anchor and TCGA expression level play an unexpected important role in neoantigen prediction, and removing insignificant features to reduce the input dimensionality of peptides does not drastically impair the overall performance of the model. Our paradigm not only streamlines the prediction pipeline but also sets a new state-of-the-art for neoantigen discovery, with broad implications for accurate immuno-oncology.

## Metadata
- **Published**: 2026-08-03T08:57:43Z
- **Authors**: Zhiyin An, Yuenan Hou, Shumeng Duan, Yiming Zhou, Yuanting Zheng, Leming Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01924v1)