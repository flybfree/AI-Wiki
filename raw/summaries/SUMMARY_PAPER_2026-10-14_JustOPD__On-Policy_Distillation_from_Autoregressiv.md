---
title: JustOPD: On-Policy Distillation from Autoregressive to Diffusion Language Models
url: http://arxiv.org/abs/2610.17397v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_21-02-26Z_JustOPD_On_PolicyDistillationfromAutoregressivetoD.md
generated_at: 2026-10-14 00:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces JustOPD, an on-policy distillation method that transfers knowledge from a strong autoregressive language model (ARM) teacher to a weaker diffusion language model (DLM) student. The method addresses the fundamental mismatch between the left-to-right sequential decoding of ARMs and the flexible, non-sequential generation order of DLMs by using autoregressive rollouts during training to align the student's generation process with the teacher's decoding strategy. Experiments using Qwen3-14B as the teacher and Dream-7B as the student demonstrate consistent improvements in mathematical reasoning performance across multiple divergence choices.

## Key Takeaways
- On-policy distillation for DLMs remains significantly underexplored, with existing research primarily limited to DLM-to-DLM distillation. The scarcity of strong teacher DLMs and the inherent flexibility of DLM generation order create substantial technical barriers that this work directly confronts by leveraging the abundance of strong ARM teachers instead.
- The core technical challenge is the decoding-order mismatch: ARMs generate tokens strictly left-to-right, while DLMs can generate tokens in any order. JustOPD resolves this by using autoregressive rollouts during the training phase, effectively forcing the student DLM to follow the teacher's sequential generation pattern during learning, while crucially preserving the DLM's flexible generation-order capability at inference time.
- The method is validated empirically using Qwen3-14B as the ARM teacher and Dream-7B as the DLM student, showing consistent gains in mathematical reasoning benchmarks. The approach is robust across multiple divergence choices, suggesting that the alignment strategy is not dependent on a single specific training objective.

## Context
Diffusion language models represent a promising alternative to autoregressive transformers by enabling parallel and flexible token generation, yet they have historically lagged behind ARMs in capability due to limited training data and architectural maturity. On-policy distillation has emerged as a powerful post-training technique for transferring knowledge between models, but its application has been largely confined to same-architecture settings. This paper bridges a critical gap by enabling cross-architecture knowledge transfer from the well-established ARM ecosystem to the emerging DLM paradigm, drawing inspiration from prior work by Ni et al. (2026) on aligning generation processes across model families.

## Implications
For practitioners, JustOPD opens a practical pathway to upgrade smaller, faster DLMs using the vast ecosystem of existing strong autoregressive models without requiring equally strong DLM teachers, which are currently scarce. For the broader field, this work validates that cross-architecture distillation is feasible when generation-order mismatches are explicitly addressed during training, potentially accelerating the adoption of diffusion-based language models in production settings where parallel generation speed is advantageous. Industry stakeholders in model deployment may benefit from the ability to distill reasoning capabilities from large ARM models into compact DLMs suitable for latency-sensitive applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17397v1)
