---
title: Approximate Speculative Decoding
url: http://arxiv.org/abs/2608.03447v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_10-45-24Z_ApproximateSpeculativeDecoding.md
generated_at: 2026-08-05 01:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Approximate Speculative Decoding (ASD) which replaces the binary first-mismatch truncation used in standard speculative decoding with a budgeted longest-prefix selection mechanism. By using a target-logit regret gate and exception caps, ASD can accept certain mismatches while reusing contiguous target-greedy suffixes without extra forward passes. Experiments show throughput gains of 3% to 15% over strict verification across various Qwen3-14B + DSpark-14B tasks.

## Key Takeaways
- The verifier uses a per-block exception cap and a persistent request-level regret budget instead of binary truncation.
- Selected mismatches are accepted only if the local target-logit regret is within acceptable limits, allowing reuse of suffix tokens that remain greedy under the realized prefix.
- ASD reduces to standard greedy verification when the budget is zero, preserving compatibility with existing systems.

## Context
Speculative decoding aims to speed up autoregressive generation by reusing parts of a draft model’s output. Traditional methods discard large portions after first mismatch, limiting efficiency gains. This work introduces a training-free verifier that balances acceptance and reuse, addressing a key limitation in current approaches.

## Implications
For industry practitioners, ASD offers a practical way to boost inference throughput without retraining or new models. The modest budgeted approach can be integrated into existing speculative decoding pipelines, delivering measurable speed improvements on large language model serving systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03447v1)
