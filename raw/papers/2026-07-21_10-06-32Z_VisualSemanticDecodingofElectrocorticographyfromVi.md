---
title: Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning
published: 2026-07-21T10:06:32Z
authors: Stella Ho, Joel Villalobos, Joseph West, Jingyang Liu, Weijie Qi, Haruhiko Kishima, Ryohei Fukuma, Takufumi Yanagisawa, Sam E. John, David B. Grayden
url: http://arxiv.org/abs/2607.18923v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning

## Abstract
ECoG-based visual semantic decoding enables inference of semantic interpretation of visual perception from complex, noisy brain activity. This study examines the feasibility of visual semantic decoding using an end-to-end deep learning framework using electrocorticography (ECoG). Specifically, the decoding task is to predict visual categories from video stimuli using time-series neural inputs. A previously collected ECoG dataset from participants ($n=17$) with drug-resistant epilepsy is used for analysis. With fewer than 50 training samples per visual category, this study evaluates multiple deep learning approaches, artificial neural network architectures, and frequency-band filtered inputs. The best-performing approach is analyzed to shed light on the discriminative information it relies on across spectral, temporal, and cortical dimensions. The selected decoding system uses mixup augmentation, a Transformer-based encoder, and high-gamma (80-150 Hz) inputs with a 900 ms post-stimulus window. Further analysis shows that early visual cortex (V2-V4), ventral stream visual cortex, MT+ complex with neighbouring visual areas, and lateral temporal cortex contributed substantially to decoding performance. This study demonstrates that an end-to-end deep learning framework can yield promising decoding performance from dynamic visual stimuli without handcrafted features, while the model behavior remains interpretable through spectral, temporal, and cortical dimensions, which are broadly consistent with established neuroscience knowledge.

## Metadata
- **Published**: 2026-07-21T10:06:32Z
- **Authors**: Stella Ho, Joel Villalobos, Joseph West, Jingyang Liu, Weijie Qi, Haruhiko Kishima, Ryohei Fukuma, Takufumi Yanagisawa, Sam E. John, David B. Grayden
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18923v1)