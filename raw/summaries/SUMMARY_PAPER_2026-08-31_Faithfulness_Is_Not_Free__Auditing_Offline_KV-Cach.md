---
title: Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation
url: http://arxiv.org/abs/2608.30996v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_15-47-23Z_FaithfulnessIsNotFree_AuditingOfflineKV_CacheQuant.md
generated_at: 2026-08-31 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether quantizing offline key-value caches used in retrieval-augmented generation degrades factual faithfulness, using Qwen2.5-7B-Instruct with INT8 and INT4 quantization on RGB and HotpotQA. It finds that INT8 is near-lossless for both accuracy and faithfulness while INT4 reduces accuracy and causes a large drop in faithfulness, especially when retrieval is noisy or many chunks are retrieved.

## Key Takeaways
- INT8 quantization preserves both accuracy and factual faithfulness across evaluation tasks, showing it is effectively lossless. - INT4 quantization leads to a significant reduction in answer correctness and introduces negative changes in faithfulness for over 90% of retained answers, indicating that compression harms the model's grounding in retrieved evidence. - The detrimental effect on faithfulness grows under noisy retrieval conditions and with more retrieved chunks, suggesting that compressed caches can produce misleading or unsupported outputs.

## Context
Retrieval-augmented generation relies on precomputed key-value caches to keep context efficient, but compression is often applied without assessing its impact on factual consistency. This paper addresses a gap by providing empirical evidence that quantization can silently degrade the reliability of generated responses.

## Implications
For practitioners deploying retrieval systems, auditing compressed caches before deployment is essential to avoid hallucinations and maintain trust in AI outputs. The findings highlight the need for fairness checks beyond accuracy metrics when evaluating model compression strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30996v1)
