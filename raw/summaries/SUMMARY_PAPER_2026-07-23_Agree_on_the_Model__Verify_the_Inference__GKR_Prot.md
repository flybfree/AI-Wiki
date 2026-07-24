---
title: Agree on the Model, Verify the Inference: GKR Protocols for HND-Based Transformer Inference
url: http://arxiv.org/abs/2607.21162v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_10-52-53Z_AgreeontheModel_VerifytheInference_GKRProtocolsfor.md
generated_at: 2026-07-23 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GKR-HND, a protocol that ensures the integrity of polynomial backbone models in HND-based Transformers by registering model components and delegating heavy public evaluations to a trusted worker. It demonstrates that with honest parties, the verifier can accept only when the worker’s signed response matches the proof claims, validating both the transcript and weight openings without performing dense matrix replay.

## Key Takeaways
- The protocol separates verification of internal GKR transcripts from costly public model evaluation, reducing client exposure to substitution attacks. 
- It relies on a non‑collusive worker that signs request‑bound responses, allowing the verifier to trust only when signatures align with proof claims. 
- Experiments confirm that pretrained HND models can be validated under delegation without dense‑matrix replay, preserving computational efficiency.

## Context
In AI inference systems, model substitution and incomplete execution are persistent threats that undermine reliability. Direct replay of computation defeats the purpose of homomorphic nonhomomorphic decomposition by requiring full matrix operations on the client side. This work addresses those issues by formalizing a registration protocol that can be applied to transformer architectures.

## Implications
For practitioners deploying HND‑based transformers, GKR-HND offers a practical way to certify model integrity without sacrificing performance gains from delegation. The approach could enable secure AI services where clients trust only signed worker responses, fostering adoption in high‑stakes applications such as medical diagnostics or financial forecasting.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21162v1)
