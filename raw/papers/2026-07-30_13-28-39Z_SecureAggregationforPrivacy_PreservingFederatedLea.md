---
title: Secure Aggregation for Privacy-Preserving Federated Learning on Clinical EEG Data
published: 2026-07-30T13:28:39Z
authors: Pouya Rajabi, Mohsen Toorani
url: http://arxiv.org/abs/2607.28191v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Secure Aggregation for Privacy-Preserving Federated Learning on Clinical EEG Data

## Abstract
Federated learning enables multiple institutions to train shared models without exchanging raw clinical EEG data, but it does not fully prevent privacy leakage from individual model updates. This paper presents a privacy-preserving federated learning framework for clinical EEG data using masking-based secure aggregation as the core protection mechanism. The framework combines graph-based communication, threshold secret sharing, dropout-resilient aggregation, local update clipping, an optional Bloom filter-based privacy-preserving record-linkage initialization module, and auxiliary-notary-based verifiability. It supports both semi-honest and malicious aggregation settings and is implemented using the Flower federated learning framework. The secure-aggregation variants are evaluated in a simulated cross-silo healthcare setting using TUH EEG-derived data under different client configurations. Under the stated assumptions, the secure variants hide individual updates from the aggregation server. The results show that these variants remain compatible with federated model training, although malicious-setting safeguards and lightweight consistency-checking mechanisms introduce additional computation, communication, and round-duration overhead. The semi-honest variant provides the lowest overhead among the secure configurations, while malicious and auxiliary-notary variants offer stronger consistency, integrity, and lightweight verification support at higher cost.

## Metadata
- **Published**: 2026-07-30T13:28:39Z
- **Authors**: Pouya Rajabi, Mohsen Toorani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28191v1)