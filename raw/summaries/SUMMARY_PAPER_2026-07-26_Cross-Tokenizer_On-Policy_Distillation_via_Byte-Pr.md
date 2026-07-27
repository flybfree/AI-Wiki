---
title: Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization
url: http://arxiv.org/abs/2607.22334v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_14-12-54Z_Cross_TokenizerOn_PolicyDistillationviaByte_Prefix.md
generated_at: 2026-07-26 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes Byte-Prefix Marginalization (BPM), a method that enables on-policy distillation between open-weight language models using different tokenizers by re‑expressing the teacher’s next‑token distribution over a shared byte space. BPM assigns each teacher token’s probability to the longest student token whose byte representation is a prefix of the teacher token, aggregates overlapping masses, and places unmatched mass in an explicit residual category, yielding a vocabulary‑complete target that preserves all probability mass.

## Key Takeaways
- BPM re‑expresses the teacher's next‑token distribution over the student vocabulary using a shared byte space, ensuring no loss of probability mass.  
- The method aggregates probabilities assigned to the same student token and routes unmatched masses into an explicit residual category, achieving a complete target distribution.  
- Empirically, BPM improves six benchmark averages by 3.7–6.6 points over existing cross‑tokenizer methods on mathematics and programming tasks.

## Context
Open-weight language models from diverse families often have complementary strengths but cannot be distilled directly because they use different tokenizers. Existing approaches either discard teacher probability mass or map it to unrelated student tokens, limiting the quality of the distilled model. BPM addresses this by aligning token representations at the byte level while preserving all information.

## Implications
The technique offers a practical pathway for integrating heterogeneous models into a single, high‑performing student without sacrificing performance. Practitioners can leverage BPM to streamline training pipelines and reduce resource costs in large‑scale model fusion projects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22334v1)
