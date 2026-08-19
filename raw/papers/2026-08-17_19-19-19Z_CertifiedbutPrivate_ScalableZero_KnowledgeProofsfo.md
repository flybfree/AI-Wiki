---
title: Certified but Private: Scalable Zero-Knowledge Proofs for Neural Network Guarantees
published: 2026-08-17T19:19:19Z
authors: Youwei Zhong, Ben Merbaum, Timos Antonopoulos, Ning Luo, Charalampos Papamanthou, Katerina Sotiraki, Ruzica Piskac
url: http://arxiv.org/abs/2608.17070v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Certified but Private: Scalable Zero-Knowledge Proofs for Neural Network Guarantees

## Abstract
With the growing deployment of machine learning models, formal guarantees of the robustness and fairness of these models have become increasingly important in safety-critical and legal-compliance settings. However, model parameters are often commercial secrets that cannot be disclosed to auditors or end users. To this end, we present PANDA, a scalable system that uses zero-knowledge proofs (ZKPs) to prove the robustness and fairness properties of a model without revealing its private parameters. PANDA is built on top of CROWN, an efficient robustness certification framework that is used in many state-of-the-art formal verification tools for neural networks. The core contribution of PANDA is a novel algorithm for proving linear relaxation bounds for non-linear activation layers, yielding simple, lightweight proofs. Remarkably, our system can generate proofs of local robustness for neural networks with more than 2.9M parameters in 5 minutes, and can verify them in 10 seconds. Prior ZKP-based robustness system rely on exponential-time algorithms that cannot scale to nontrivial networks. In contrast, PANDA scales polynomially in the number of neurons in a network, allowing us to support neural networks 4 orders of magnitude larger than previous approaches with significantly reduced prover overhead.

## Metadata
- **Published**: 2026-08-17T19:19:19Z
- **Authors**: Youwei Zhong, Ben Merbaum, Timos Antonopoulos, Ning Luo, Charalampos Papamanthou, Katerina Sotiraki, Ruzica Piskac
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17070v1)