---
title: Token Distribution versus Data Volume: Domain Balancing in Multi-Domain Meeting Summarisation
url: http://arxiv.org/abs/2608.15935v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_21-20-27Z_TokenDistributionversusDataVolume_DomainBalancingi.md
generated_at: 2026-08-17 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how token distribution and data volume affect domain balancing in multi-domain meeting summarisation. By creating balanced and natural token mixtures across five corpora, fine‑tuning Mistral‑7B with QLoRA, the authors show that rebalancing improves minority domains at low cost while preserving majority performance.

## Key Takeaways
- Balanced token allocation redistributes quality to scarce domains without degrading dominant ones, especially when those minorities are important.  
- Matching balanced quality on minority domains requires far more total tokens than proportional allocation because their share is fixed at 1‑2% regardless of budget.  
- Removing low‑value transcript lines cuts roughly 15 % of tokens with no measurable impact on evaluation.

## Context
This work addresses a longstanding challenge in large language model training: the trade‑off between data volume and token distribution across domains. Prior studies often conflate these factors, limiting practical guidance for practitioners seeking efficient, fair models.

## Implications
For developers building multi‑domain summarisation systems, the study provides a clear decision framework: prioritize balancing when minority domain performance is critical, and consider pruning low‑value data to reduce token load without harming quality. This can lead to more equitable and cost‑effective AI solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15935v1)
