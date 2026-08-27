---
title: One Form to Transfer Them All: Pretraining Multilingual Language Models Beyond Native Orthography
published: 2026-08-26T15:23:18Z
authors: Muge Zhang, Aaron Jencks, Krishna Badikela, Yulia Tsvetkov, Sachin Kumar
url: http://arxiv.org/abs/2608.25904v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Form to Transfer Them All: Pretraining Multilingual Language Models Beyond Native Orthography

## Abstract
Multilingual language models transfer knowledge across languages through shared subword vocabulary, a mechanism that breaks down when related languages use different writing systems. Prior work addresses this via script equalization (romanization or IPA transcription), but direct comparisons are rare; the focus has been on encoder-only models, with most work adapting existing pretrained models. We systematically compare different input representations in autoregressive multilingual pretraining, comparing orthographic text, IPA, and romanization in a controlled setup across three scales (467M, 709M, and 1.03B) on eight languages in four typologically motivated pairs. Across a wide range of downstream tasks on seen and unseen languages, romanized pretraining yields the strongest cross-lingual transfer, and the advantage over text widens with scale. IPA improves over text in most settings but trails romanization. Surprisingly, finetuning a text-pretrained model on romanized data hurts performance on languages already covered by the base model, only marginally helping when the model lacks script coverage. Our results indicate that for multilingual models spanning typologically diverse scripts, to obtain maximum benefits, romanization should be treated as a core design choice applied at pretraining rather than a post hoc fix.

## Metadata
- **Published**: 2026-08-26T15:23:18Z
- **Authors**: Muge Zhang, Aaron Jencks, Krishna Badikela, Yulia Tsvetkov, Sachin Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25904v1)