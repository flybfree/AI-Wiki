---
title: Replacing Training with Memory: Listwise Selection for Text-to-SQL
url: http://arxiv.org/abs/2609.00834v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_07-35-00Z_ReplacingTrainingwithMemory_ListwiseSelectionforTe.md
generated_at: 2026-09-01 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a fine‑tuning‑free listwise selector for Text-to-SQL that replaces two traditional objectives with inference‑time strategies. By using structured memories to encode mapping criteria and aggregating rankings across input permutations, the approach improves selection accuracy while keeping token usage low. On BIRD‑dev it beats the state‑of‑the‑art selector by 2.02 execution accuracy points on average.

## Key Takeaways
- The method replaces fine‑tuning objectives with ordering and bias mitigation strategies that run at inference time, avoiding costly parameter updates.
- Memories distilled from training data serve as explicit decision criteria for evaluating candidate queries in a listwise manner.
- Aggregating rankings across multiple input permutations reduces unnecessary comparisons and improves stability without extra tokens.

## Context
Current Text-to-SQL systems rely on generate‑execute‑select pipelines where selecting the best query is often done by fine‑tuning expensive models. This paper addresses the inefficiency of such fine‑tuning by shifting selection logic to inference, which aligns with the trend toward parameter‑efficient AI deployment.

## Implications
Practitioners can adopt this approach to maintain high performance without retraining large language models, lowering computational cost and enabling faster iteration cycles in production. The reduction in token usage also makes the method more suitable for real‑time applications where latency matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00834v1)
