---

title: Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching
published: "2026-05-28T17:59:01Z"
authors: Alaa Khamis, Alaa Maalouf
url: http://arxiv.org/abs/2605.30337v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching



**Source**: [Original Paper](http://arxiv.org/abs/2605.30337v1)
## Abstract
Test-time finetuning (TTFT) is a rapidly evolving paradigm that adapts a language model to each prompt by retrieving related sequences, updating the model on them, and then evaluating the prompt. However, TTFT is only practical if it is fast: selection and finetuning both happen per query, making each a direct bottleneck. Existing methods trade speed for quality: fast retrieval is often redundant, while stronger diversity-aware selection adds prohibitive per-query cost. We introduce HullFT, a geometric approach to TTFT that addresses both bottlenecks. Given a query, HullFT first represents the query embedding as a sparse convex combination of few training sequences, using efficient projection-free Frank-Wolfe optimization. This yields a support set that is inherently relevant and diverse. We then convert the fractional convex weights into an exact integer multiset for finetuning through a geometric integerization procedure. The resulting multiplicities naturally create repeated examples, which we exploit with Gradient Reuse to amortize forward-backward computation across repeated finetuning steps. Our experiments show that HullFT improves the quality-efficiency tradeoff over current state-of-the-art TTFT methods, achieving lower bits-per-byte at substantially lower total runtime.

## Metadata
- **Published**: 2026-05-28T17:59:01Z
- **Authors**: Alaa Khamis, Alaa Maalouf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.30337v1)