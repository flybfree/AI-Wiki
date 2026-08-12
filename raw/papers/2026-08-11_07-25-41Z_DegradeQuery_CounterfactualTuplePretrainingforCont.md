---
title: DegradeQuery: Counterfactual Tuple Pretraining for Context-Aware PROTAC Degradation Prediction
published: 2026-08-11T07:25:41Z
authors: Dong Xu, Zhangfan Yang, Jiantao Wu, Zexuan Zhu, Jianqiang Li, Junkai Ji
url: http://arxiv.org/abs/2608.10595v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DegradeQuery: Counterfactual Tuple Pretraining for Context-Aware PROTAC Degradation Prediction

## Abstract
Proteolysis-targeting chimeras (PROTACs) induce protein degradation by recruiting a target protein to an E3 ubiquitin ligase, making degradation a joint outcome of the degrader molecule and its biological context. Although public databases contain thousands of structured molecule-target-E3 records, degradation measurements are available for only a small fraction of them. Existing supervised approaches therefore leave most recorded chemical-biological relationships unused. We introduce DegradeQuery, a context-aware prediction framework that converts these label-missing records into a pretraining signal. Its counterfactual tuple pretraining objective contrasts recorded tuples with alternatives formed by replacing the target, the E3 ligase, or both, enabling the model to learn contextual associations without assigning activity pseudo-labels. The resulting representation is then fine-tuned to predict degradation from the complete molecule-target-E3 context. On the official PROTAC-8K benchmark, DegradeQuery achieves an area under the receiver operating characteristic curve of 0.9065 and an accuracy of 0.8500, outperforming the compared methods. Controlled analyses further show that the improvement is primarily attributable to tuple-level pretraining, can be recovered using only label-missing records, and remains complementary to protein language model representations. These findings demonstrate that incompletely labeled PROTAC databases contain useful relational supervision and provide a practical route for learning context-aware degradation predictors from scarce experimental labels.

## Metadata
- **Published**: 2026-08-11T07:25:41Z
- **Authors**: Dong Xu, Zhangfan Yang, Jiantao Wu, Zexuan Zhu, Jianqiang Li, Junkai Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10595v1)