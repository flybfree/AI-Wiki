---
title: ROCS: Request-Oriented Compute Sharing for Efficient Large-Scale Recommendation
url: http://arxiv.org/abs/2607.27744v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_06-33-50Z_ROCS_Request_OrientedComputeSharingforEfficientLar.md
generated_at: 2026-07-30 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Request-Oriented Compute Sharing (ROCS), a new inference paradigm that improves recommendation model efficiency by postponing candidate‑specific computations and sharing request‑side features across many candidates. The approach uses Generalized Layer Masking for feature‑interaction models and Deep Cross Attention for sequence models, supported by an in‑kernel broadcast optimization that speeds up GPU execution. Experiments demonstrate substantial quality‑efficiency gains on both benchmarks and production workloads.

## Key Takeaways
- ROCS defers request‑candidate interactions as late as possible, allowing the same request features to be reused across many candidates, which reduces redundant computation.
- The Generalized Layer Masking technique isolates candidate‑dependent representations in feature‑interaction architectures, ensuring that each candidate’s representation is computed only once per request batch.
- In‑Kernel Broadcast Optimization (IKBO) accelerates ROCS inference on GPUs by broadcasting shared tensors directly within the kernel, achieving up to a threefold increase in queries per second without sacrificing prediction quality.

## Context
Modern recommendation systems face a tradeoff between model accuracy and computational cost as they scale. Traditional models compute candidate‑specific features for each request, leading to high latency and resource consumption. This paper contributes a novel architectural and optimization strategy that decouples the heavy lifting of inference from the per‑candidate evaluation, aligning with trends toward efficient large‑scale AI deployment.

## Implications
For industry practitioners, ROCS offers a practical path to lower infrastructure costs while maintaining or improving recommendation quality, enabling faster response times for billions of user requests. The methodology can be adapted across various recommendation backbones and stages, from retrieval to ranking, making it a versatile tool for scaling modern AI systems in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27744v1)
