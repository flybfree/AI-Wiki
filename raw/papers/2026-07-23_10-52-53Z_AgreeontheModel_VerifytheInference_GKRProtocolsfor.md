---
title: Agree on the Model, Verify the Inference: GKR Protocols for HND-Based Transformer Inference
published: 2026-07-23T10:52:53Z
authors: Xiaolong Liang, Juanjuan Li, Rui Qin, Yisheng Lv
url: http://arxiv.org/abs/2607.21162v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agree on the Model, Verify the Inference: GKR Protocols for HND-Based Transformer Inference

## Abstract
Outsourced Transformer inference exposes clients to model substitution and incomplete execution, while direct replay removes the computational benefit of delegation. We present GKR-HND, a registered-model protocol for verifying the polynomial backbone of Homomorphic--Nonhomomorphic Decomposition Transformers. The retained verifier checks the GKR transcript and registered-weight openings, but delegates expensive public evaluations to an assigned computation worker. Assuming an honest retained verifier and prover--worker non-collusion, the verifier accepts only when the worker's signed, request-bound response agrees with the proof claims. Experiments with pretrained HND models validate the proof path and the delegated public computation without dense-matrix replay.

## Metadata
- **Published**: 2026-07-23T10:52:53Z
- **Authors**: Xiaolong Liang, Juanjuan Li, Rui Qin, Yisheng Lv
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21162v1)