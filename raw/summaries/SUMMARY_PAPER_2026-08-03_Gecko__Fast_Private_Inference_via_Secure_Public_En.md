---
title: Gecko: Fast Private Inference via Secure Public Encoder Offloading
url: http://arxiv.org/abs/2608.02378v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_15-21-45Z_Gecko_FastPrivateInferenceviaSecurePublicEncoderOf.md
generated_at: 2026-08-03 23:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Gecko, a method for fast private inference that offloads a public encoder while keeping the predictor encrypted. It shows that naive offloading can leak information through feature-space shortcuts, and Gecko mitigates this with frozen backbones, Fastfood projections, and gating. Experiments on image and audio tasks achieve 0.4-2.2 seconds inference with ≤10.8 MB communication while matching transfer-learning baselines.

## Key Takeaways
- Naive public encoder offloading can create feature-space shortcuts that allow extraction attacks to infer the private predictor's mapping more easily than the original model's input-output behavior.
- Gecko uses a frozen backbone, Fastfood projections, and private gating to preserve ideal independence and information preservation while limiting communication.
- Reusing the offloaded public encoder provides no significant advantage to model-extraction adversaries under evaluated attacks.

## Context
Private inference is essential for deploying models where both inputs and server models must remain confidential. Current solutions often sacrifice speed or security, making practical deployment challenging. This work addresses that trade‑off by combining efficient compression with cryptographic guarantees.

## Implications
For industry practitioners, Gecko offers a deployable framework that balances latency, bandwidth, and privacy without exposing model internals. It demonstrates that advanced attacks can be mitigated through architectural design, encouraging broader adoption of private inference in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02378v1)
