---
title: MOSAIC-FL, a micro-service based privacy-preserving framework with application to genomics
published: 2026-07-27T22:09:46Z
authors: Paul Largillier, Karl Paygambar, Cédric Gouy-Pailler, Vincent Meyer, Mallek Mziou, Oana Stan
url: http://arxiv.org/abs/2607.25107v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MOSAIC-FL, a micro-service based privacy-preserving framework with application to genomics

## Abstract
Security and privacy are primordial requirements for Federated Learning (FL), especially in fields such as healthcare and genomics where sensitive information has to be analyzed. Our FL framework is designed to address these challenges while proposing a modular, flexible and micro-service architecture. More precisely, it integrates an efficient gRPC communication layer and a Finite State Machine to ensure robust component synchronization and threat detection, while relying on a fault-tolerant secure aggregation protocol using a Threshold variant of the CKKS homomorphic cryptosystem. This allows blind model aggregation by an orchestration server, requiring a minimum of $t$-out-of-$N$ active clients for decryption while minimizing communication overhead thanks to both cryptographic and network protocols. We ensure IND-CPA-D security through noise flooding and mitigate the recent key-recovery attack on synchronized decryptors by renewing the collective key material at every round. We demonstrate the framework's effectiveness through diverse use cases, ranging from standard image recognition (EMNIST) to complex genomic classification including breast cancer subtyping on TCGA, evaluating system performance across different threshold values and model scales.

## Metadata
- **Published**: 2026-07-27T22:09:46Z
- **Authors**: Paul Largillier, Karl Paygambar, Cédric Gouy-Pailler, Vincent Meyer, Mallek Mziou, Oana Stan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25107v1)