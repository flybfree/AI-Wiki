---
title: Neural Regression with Embeddings for Numerical Attribute Prediction in Knowledge Graphs
published: 2026-08-27T07:21:48Z
authors: Rupesh Sapkota, Louis Mozart Kamdem Teyou, Moshood Yekini, Caglar Demir, Axel-Cyrille Ngonga Ngomo
url: http://arxiv.org/abs/2608.26729v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neural Regression with Embeddings for Numerical Attribute Prediction in Knowledge Graphs

## Abstract
In recent years, transductive knowledge graph embedding models have been applied to tasks such as link prediction and query answering. Although knowledge graphs often contain rich numerical attributes, most embedding models neglect them, limiting their ability to represent real-world knowledge graphs with diverse information. In this work, we propose a neural regression model (LitEm) that enables transductive knowledge graph embedding models to predict numerical attributes within knowledge graphs. Experimental results demonstrate that LitEm achieves the best or second-best results on most attributes across FB15K-237, YAGO15K, DB15K, and Mutagenesis. Furthermore, we propose a co-training framework that jointly trains state-of-the-art transductive knowledge graph embedding models with LitEm, which improves link prediction performance mainly for bilinear models and simultaneously enables them to predict numerical attributes. In addition, the literal-awareness evaluation demonstrates that co-training helps models to encode and exploit attribute information in a "literal-aware'' manner, suggesting that the observed gains are not merely due to additional parameters. We publicly release our implementation at https://github.com/dice-group/dice-embeddings.

## Metadata
- **Published**: 2026-08-27T07:21:48Z
- **Authors**: Rupesh Sapkota, Louis Mozart Kamdem Teyou, Moshood Yekini, Caglar Demir, Axel-Cyrille Ngonga Ngomo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26729v1)