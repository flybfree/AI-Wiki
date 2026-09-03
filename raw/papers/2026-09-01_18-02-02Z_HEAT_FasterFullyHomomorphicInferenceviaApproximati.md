---
title: HEAT: Faster Fully Homomorphic Inference via Approximations-Weights Co-Adaptation
published: 2026-09-01T18:02:02Z
authors: Alessandro Zirilli, Davide Marincione, Evgenios M. Kornaropoulos, Giuseppe Ateniese, Emanuele Rodolà
url: http://arxiv.org/abs/2609.01730v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HEAT: Faster Fully Homomorphic Inference via Approximations-Weights Co-Adaptation

## Abstract
Fully homomorphic encryption (FHE) allows a server to run a language model directly on encrypted user prompts, but current approaches remain prohibitively slow. Ciphertexts natively support only addition, multiplication, and rotation, and multiplications may be composed only to a bounded depth before a costly bootstrapping operation is needed to continue. Every nonlinearity must therefore be approximated by an iterative method, and each iteration uses multiplications. A higher iteration count buys precision but exhausts the available depth faster and triggers more bootstraps, which dominate latency. Existing approaches fix the iteration counts uniformly across the model rather than tailoring them to each site's error tolerance. We introduce Homomorphic Encryption-Aware Training (HEAT), a fine-tuning method that makes the per-nonlinearity iteration counts learnable, enabling them and the model weights to co-adapt during training. HEAT optimizes iterations with respect to the task objective, allowing the model to adapt to approximation errors encountered during inference without architectural changes or retraining from scratch. On encrypted GPT-2 decoding, HEAT reduces iterations by $3.1\times$, bootstraps by $1.6\times$, and end-to-end latency by $1.4\times$, while improving decode agreement over the calibrated baseline.

## Metadata
- **Published**: 2026-09-01T18:02:02Z
- **Authors**: Alessandro Zirilli, Davide Marincione, Evgenios M. Kornaropoulos, Giuseppe Ateniese, Emanuele Rodolà
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01730v1)