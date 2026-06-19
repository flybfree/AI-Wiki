---

title: Context Memorization for Efficient Long Context Generation
published: "2026-05-18T11:12:45Z"
authors: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
url: http://arxiv.org/abs/2605.18226v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Context Memorization for Efficient Long Context Generation



**Source**: [Original Paper](http://arxiv.org/abs/2605.18226v1)
## Abstract
Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.

## Metadata
- **Published**: 2026-05-18T11:12:45Z
- **Authors**: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.18226v1)