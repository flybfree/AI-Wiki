---
title: MOSAIC-FL, a micro-service based privacy-preserving framework with application to genomics
url: http://arxiv.org/abs/2607.25107v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_22-09-46Z_MOSAIC_FL_amicro_servicebasedprivacy_preservingfra.md
generated_at: 2026-07-28 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MOSAIC-FL, a micro‑service architecture that enables privacy‑preserving federated learning for sensitive domains such as genomics. The framework combines gRPC communication, a finite state machine, and a threshold CKKS homomorphic cryptosystem to achieve secure model aggregation with minimal network overhead.

## Key Takeaways
- MOSAIC-FL uses a fault‑tolerant secure aggregation protocol that requires only t out of N active clients to decrypt the aggregated model, reducing communication costs.  
- IND‑CPA‑D security is provided through noise flooding and key material renewal each round to counter key‑recovery attacks on synchronized decryptors.  
- The framework supports diverse tasks from image classification (EMNIST) to genomic breast cancer subtyping on TCGA datasets, evaluating performance across thresholds and model scales.

## Context
Federated learning promises collaborative AI without sharing raw data, but real‑world applications like genomics demand strong privacy guarantees. Existing FL solutions often suffer from high communication latency or vulnerability to cryptographic attacks, limiting adoption in regulated fields.

## Implications
MOSAIC-FL offers a scalable blueprint for deploying FL in healthcare and biotech where regulatory compliance is critical. Practitioners can leverage its modular micro‑service design to integrate custom models while maintaining confidentiality and resilience against emerging threats.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25107v1)
