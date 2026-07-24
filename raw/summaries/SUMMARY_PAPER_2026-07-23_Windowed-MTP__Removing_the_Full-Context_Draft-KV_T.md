---
title: Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context
url: http://arxiv.org/abs/2607.21535v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_17-21-44Z_Windowed_MTP_RemovingtheFull_ContextDraft_KVTaxatM.md
generated_at: 2026-07-23 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Windowed-MTP, a technique that mitigates the quadratic cost of full‑context draft attention in speculative decoding. By limiting the draft’s KV cache to a sliding window and reusing entries via a ring buffer, it reduces per‑decode‑step cost by 28–44 % at million‑token contexts while keeping the target’s output unchanged.

## Key Takeaways
- Draft attention is limited to a constant‑size window, dropping ~99 % of KV entries at 1M tokens and preventing linear growth in draft cost.  
- The technique is training‑free and lossless; full‑attention verification remains untouched, so accepted tokens are still decided by the target model.  
- Reclaimed unread KV (7.7–11 % of total) is stored in a compact ring buffer with no acceptance or quality penalty.

## Context
Speculative decoding aims to speed up autoregressive generation by generating cheap drafts and verifying them against an expensive target model. Traditional MTP implementations suffer from full‑attention reads that dominate cost at large contexts, undermining the benefit of speculation especially under hybrid attention architectures.

## Implications
Windowed-MTP offers a practical way to keep speculative decoding affordable as models scale to millions of tokens, preserving generation quality while reducing GPU memory pressure and latency. Practitioners can adopt it without retraining or architectural changes, making high‑throughput inference feasible on limited hardware.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21535v1)
