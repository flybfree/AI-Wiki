---
title: Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations
url: http://arxiv.org/abs/2607.20379v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_17-10-23Z_TraintheModel_NottheReader_DecodabilitySupervision.md
generated_at: 2026-07-23 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces decodability supervision to evaluate how faithful hidden activations are in language models, showing that standard reconstruction scores can be gamed and do not guarantee factual correctness. Experiments on Qwen-2.5-7B and Pythia-160M reveal that explanations often reconstruct well while specific claims are unreliable, and a new protocol RECAP trains auxiliary heads to keep designated content independently decodable.

## Key Takeaways
- The reconstruction score is structurally insensitive; flipping a claim does not affect the score if reconstruction remains unchanged, indicating it measures gist rather than factual accuracy.
- Under synthetic ground truth, the standard method creates private codes that depend on false wording, and fixing those without altering the model does not improve performance, showing the need for targeted supervision.
- RECAP achieves a negligible +0.001-nat cost while making content probe-decodable with high AUC (0.96) versus 0.82 in control, demonstrating that supervised decodability can detect lies even when reconstruction is optimized.

## Context
Current AI safety research focuses on model outputs and interpretability, but hidden activations remain opaque and manipulable. This work addresses the gap by proposing a method to verify internal content without relying solely on surface-level reconstructions, aligning with efforts to make models verifiable against independent probes.

## Implications
For practitioners, RECAP provides a lightweight audit protocol that can be integrated into model training pipelines to ensure that specific claims are not gamed. Industry adoption could lead to more trustworthy AI systems where explanations are both human-readable and machine-verifiable, reducing the risk of deceptive outputs in high-stakes applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20379v1)
