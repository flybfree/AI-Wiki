---
title: Encoded but Not Actionable: Auditing the Decode-Generate-Steer Gap in Frozen LLMs for Geometric Constraints
url: http://arxiv.org/abs/2608.17843v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_14-40-28Z_EncodedbutNotActionable_AuditingtheDecode_Generate.md
generated_at: 2026-08-18 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits the gap between what frozen decoder-only LLMs encode about geometric constraints and whether that information can be decoded, generated, or steered. Using parametric CAD constraints they find decoding of local relations is strong but generation and control are weak.

## Key Takeaways
- Pretraining improves decoding of linear geometric relations while random representations already capture sketch-level DOF status with modest gains.
- Generated outputs often fail to reflect the encoded constraint information even when activation restoration at patched positions does not affect behavior.
- Mean-difference steering does not reliably control model output despite detectable decodable signals.

## Context
Large language models are expected to encode and act on structured knowledge, yet their internal representations remain opaque. This work provides a systematic method to test whether encoded geometric structures translate into actionable outputs in frozen models.

## Implications
Researchers can now distinguish between encoding failures and expression failures using controlled geometric probes. Practitioners should be cautious about assuming that detectable information will lead to reliable model behavior, especially when fine-tuning or steering interventions are applied.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17843v1)
