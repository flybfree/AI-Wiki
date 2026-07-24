---
title: Detecting LLM-Generated Tokens in Human--LLM Coauthored Text
url: http://arxiv.org/abs/2607.21458v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_16-01-16Z_DetectingLLM_GeneratedTokensinHuman__LLMCoauthored.md
generated_at: 2026-07-23 22:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a token‑level detection method for identifying LLM‑generated portions within human‑LLM coauthored texts, smoothing adjacent scores to lower variability and using an adaptive bandwidth rule based on authorship structure. The approach requires no labeled token data and achieves favorable mean square error in estimating the underlying signal.

## Key Takeaways
- The method operates at the token level, smoothing adjacent detection scores to reduce noise while preserving signal.
- It employs an adaptive Lepski‑type rule that selects bandwidth dynamically according to local authorship patterns.
- The approach is fully unsupervised and does not need token‑level labeled data for training.

## Context
Human‑AI collaborative writing creates mixed‑authorship documents where pinpointing AI contributions is essential. Current detection tools focus on whole‑document classification, limiting their usefulness for precise localization.

## Implications
Fine‑grained token detection enables editors, researchers, and developers to assess authenticity locally, improving trust in AI‑assisted content and informing policy on automated review systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21458v1)
