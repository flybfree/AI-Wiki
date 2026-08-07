---
title: MirrorNet: Can Medical Image Anonymization Really Protect Patient Identity?
published: 2026-08-06T12:06:27Z
authors: Attila Simkó
url: http://arxiv.org/abs/2608.05938v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MirrorNet: Can Medical Image Anonymization Really Protect Patient Identity?

## Abstract
Medical images are routinely de-identified---names, dates, and other metadata removed---and then shared for research, teaching, and public benchmarks under the assumption that this renders them anonymous. Such de-identification protects the metadata but not the pixels, and---apart from scans that directly contain facial structures---whether the image content itself identifies the patient has received little scrutiny. We investigate this question by learning a cycle-consistent correspondence between a cross-sectional medical image and a non-medical, patient-identifying image, using a pair of coupled, cycle-consistent variational autoencoders. From a held-out scan, the model recovers a recognisable likeness of the patient (identity-region MAE = 0.163); conversely, it synthesises a scan from such an image. These results indicate that a de-identified medical scan remains identifying---it is, in effect, a photograph of the patient---and that imaging data should be governed as biometric data rather than as anonymisable records. To support reproducibility, the code and trained models are shared at https://github.com/attilasimko/public-repository.

## Metadata
- **Published**: 2026-08-06T12:06:27Z
- **Authors**: Attila Simkó
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05938v1)