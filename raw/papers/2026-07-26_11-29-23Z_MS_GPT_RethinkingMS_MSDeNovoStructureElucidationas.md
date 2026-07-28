---
title: MS-GPT: Rethinking MS/MS De Novo Structure Elucidation as Spectrum-Induced Posterior Querying of a Molecule-Language Model
published: 2026-07-26T11:29:23Z
authors: Xin Zhao, Yumin Liu, Zhuo Li, Weichu Zheng, Feng Zhu, Xiaokang Yang, Yaohui Jin, Yanyan Xu
url: http://arxiv.org/abs/2607.23607v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MS-GPT: Rethinking MS/MS De Novo Structure Elucidation as Spectrum-Induced Posterior Querying of a Molecule-Language Model

## Abstract
Molecular structure elucidation from tandem mass spectra (MS/MS) is a central inverse problem in analytical chemistry. Most existing approaches to MS/MS identification remain tied to reference libraries or predefined candidate sets, whereas de novo methods aim to generate structures directly from spectra. A common de novo route predicts a molecular fingerprint from the spectrum and then decodes structures from it, enabling decoder pretraining on large molecule-only corpora. However, this paradigm creates a training-inference mismatch: the decoder is trained on oracle fingerprints computed from molecules, but at inference it is queried with a noisy spectrum-induced fingerprint posterior that is typically collapsed to a single thresholded fingerprint. We introduce MS-GPT, which recasts fingerprint-mediated de novo elucidation as spectrum-induced posterior querying of a conditional molecule-language model. MS-GPT conditions a molecule-language model on fingerprints and formulas, then converts the spectrum-induced posterior into a band of fingerprint queries near the oracle-fingerprint manifold through active-bit density calibration. Candidates sampled across this band are pooled and ranked by generation-frequency consensus. A lightweight LoRA adapter further mitigates domain-specific posterior bias while preserving the pretrained molecular prior. On NPLIB1 and MassSpecGym, MS-GPT sets a new state of the art, reaching Top-1/Top-10 exact-match accuracy of 29.8\%/41.1\% and 23.9\%/28.7\%, respectively. Candidate-pool scaling shows that efficient autoregressive molecular generation continues to improve recall with a little additional inference cost. The source code and model checkpoints are available at https://github.com/VIKI623/MS-GPT.

## Metadata
- **Published**: 2026-07-26T11:29:23Z
- **Authors**: Xin Zhao, Yumin Liu, Zhuo Li, Weichu Zheng, Feng Zhu, Xiaokang Yang, Yaohui Jin, Yanyan Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23607v1)