---
title: How Context Attribution Handles What the Model Already Knows
published: 2026-07-26T19:06:29Z
authors: Quoc-Huy Trinh, Lin Zhu, Sebastian Szyller
url: http://arxiv.org/abs/2607.23804v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Context Attribution Handles What the Model Already Knows

## Abstract
Context attribution methods for large language models (LLMs) identify which input context contributes to the model response. Recent works show the initial success in attributing the con- tributive score of the contexts. However, we observe that when the context overlaps with the training data, these methods can- not disentangle in-context from in-weight (IW) contributions, producing unreliable scores. Based on this observation, in this work, we introduce: 1) an evaluation protocol that relies on four new metrics (base-model context attribution score (BCS), cross-model context attribution consistency (CAC), attribution preservation score (APS), source separation pre- cision (SSP)) and 2) a benchmark dataset (WMDP-Cyber++) with ground-truth provenance labels to systematically assess attribution under IW overlap. In our experiments across four well-known context attribution methods, we demonstrate that they provide unfaithful attribution when the knowledge from the context also exists in the weights. Finally, we adapt these methods for source separation (IW vs. in-context learning (ICL)) and show that they cannot do the disentanglement based on the contributive score

## Metadata
- **Published**: 2026-07-26T19:06:29Z
- **Authors**: Quoc-Huy Trinh, Lin Zhu, Sebastian Szyller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23804v1)