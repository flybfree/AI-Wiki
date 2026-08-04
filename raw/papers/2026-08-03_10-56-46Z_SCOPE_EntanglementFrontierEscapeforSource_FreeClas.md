---
title: SCOPE: Entanglement Frontier Escape for Source-Free Class Unlearning
published: 2026-08-03T10:56:46Z
authors: Junhao Cai, Dohun Kim, Sung Il Choi, Juhyun Park, Chengjun Jin, Dowon Kim, Changhee Joo
url: http://arxiv.org/abs/2608.02058v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCOPE: Entanglement Frontier Escape for Source-Free Class Unlearning

## Abstract
Source-free class unlearning erases whole classes using only the forget data, judged at the representation level, where features can leak a class the head no longer predicts. Existing feature-space erasers answer with one fixed projection, yet forget and retain classes share a representation, so deleting one disturbs the other where they overlap. We prove this tension is a frontier. Every fixed projection that deletes pays a retain cost of at least the retain-readout energy along the forget-discriminant subspace, and erasing that subspace alone attains the floor. The leading source-free erasers all instantiate the form it binds, so the frontier limits the whole class. Conditioning the erasure on the input escapes it. Spectral Conditional Projective Erasure (SCOPE) does so with a single gate, suppressing the forget subspace chiefly on inputs its frozen head's weight scores read as a forget class. It is closed form, needs no retain data or gradient training, and costs orders of magnitude less than retraining. Across five object, face, and speaker benchmarks spanning two modalities and both convolutional and transformer backbones, the frontier predicts the measured retain cost. SCOPE leads the source-free erasers on every benchmark and forget-set size, and at the hardest setting it tops every unlearner, trained methods included.

## Metadata
- **Published**: 2026-08-03T10:56:46Z
- **Authors**: Junhao Cai, Dohun Kim, Sung Il Choi, Juhyun Park, Chengjun Jin, Dowon Kim, Changhee Joo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02058v1)