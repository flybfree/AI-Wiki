---
title: Defending Retrieval-Augmented Intrusion Detection Against Knowledge Poisoning and Prompt Injection
url: http://arxiv.org/abs/2608.08100v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_12-29-47Z_DefendingRetrieval_AugmentedIntrusionDetectionAgai.md
generated_at: 2026-08-10 22:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces RAG‑IDS, a three‑agent intrusion detection framework that mitigates knowledge poisoning and prompt‑injection attacks in retrieval‑augmented generation pipelines. Experiments on the CIC‑UNSW‑NB15 dataset demonstrate robust classification recovery ranging from 1.0 at 1 % poisoning to 0.57 at 30 %, while leaky prompts cause only modest label‑flip rates (0.6–2.4 %). The results show that the defense preserves clean performance with negligible overhead.

## Key Takeaways
- Soft trust scoring and label‑embedding consistency checking (LECC) enable the system to recover classification quality even when up to 30 % of retrieved data is poisoned, keeping the relative recovery ratio above 57 %.  
- Multi‑document retrieval limits successful prompt injection to 0.6–2.4 % label flips, a stark contrast to single‑document retrieval which suffers 35–55 % flips.  
- LECC is identified as the primary contributor to robustness, outperforming hard filtering, while soft trust‑based demotion provides a more effective alternative.

## Context
Retrieval‑augmented generation (RAG) combines large language models with external knowledge bases to improve reasoning and factual grounding in AI systems. However, the reliance on vector similarity introduces new attack surfaces where adversarial data can corrupt embeddings or manipulate prompts. This work addresses those vulnerabilities by embedding defense mechanisms directly at the retrieval boundary.

## Implications
For intrusion detection practitioners, RAG‑IDS offers an explainable, resilient pipeline that can be deployed alongside high‑throughput classifiers without sacrificing performance. The findings suggest that multi‑agent architectures with soft trust and consistency checks are essential for maintaining trustworthy AI in dynamic threat environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08100v1)
