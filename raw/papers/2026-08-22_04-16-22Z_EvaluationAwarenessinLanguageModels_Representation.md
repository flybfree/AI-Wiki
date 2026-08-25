---
title: Evaluation Awareness in Language Models: Representation, Verbalization, and Control
published: 2026-08-22T04:16:22Z
authors: Farzaneh Heidari, Amin Memarian, Guillaume Rabusseau
url: http://arxiv.org/abs/2608.21766v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluation Awareness in Language Models: Representation, Verbalization, and Control

## Abstract
Both capability and safety benchmarks rest upon the assumption that the behavior of language models undergoing a test is informative about their behavior in deployment. This assumption can fail, should models infer that they are being evaluated and condition their response on such context. This hypothesis, termed ``evaluation awareness'', has been observed in frontier and open-weight language models alike. We provide a systematic study of this phenomenon, by probing for it across six language models (from four families and three sizes) and three metrics. More precisely, we examine whether (i) being under evaluation is linearly represented within the models' activations space, (ii) it is verbalized in their output tokens (as scored by an LLM-as-judge), and (iii) steering causally affects their behavior. For the open-checkpoint Olmo models, we further test these measures at every training stage. In doing so, we report that evaluation awareness is linearly decodable from the residual streams of every model (best AUROC $\geq 0.7$). By contrast, these representations align only in part with verbalization: their correlations and mutual information are nonzero in some settings, yet vary substantially across models, layers, and readout choices. Nevertheless, steering along probe-derived directions can shift the verbalization scores. Finally, a comparison across the Olmo checkpoints reveals that evaluation awareness is already present within base models, becomes amplified throughout the stages of supervised fine-tuning, and remains stable thereafter---unlike the effects of steering, that grow more pronounced at every successive training stage. These results show the need for evaluations to account for the disjunction between what models represent internally, what they verbalize, and their steering.

## Metadata
- **Published**: 2026-08-22T04:16:22Z
- **Authors**: Farzaneh Heidari, Amin Memarian, Guillaume Rabusseau
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21766v1)