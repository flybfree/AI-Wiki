# Summary: 2026-07-27_15-28-52Z_LOCKS_Page_LocalCompactKeySummariesforEfficientLon.md
Saved: 2026-07-27 21:45
Source: 2026-07-27_15-28-52Z_LOCKS_Page_LocalCompactKeySummariesforEfficientLon.md
Model: None

---

## Summary  
The paper LOCKS addresses a critical bottleneck in long-context language model decoding: the full read of the attention key-value (KV) cache at every step, which is computationally expensive and limits scalability to very long documents. The authors propose a novel method that replaces dense attention with compact, page-local summaries, enabling efficient long-document processing while preserving high-quality output. By focusing on local structure within pages rather than global interactions, LOCKS reduces memory usage and decoding latency without sacrificing performance. This approach is particularly effective for tasks requiring extensive reasoning over long inputs, such as QA and math problem solving.

## Key Contributions  
- [Finding 1] Each page in the document has its own low-rank spectral summary that captures the essential attention dynamics locally, reducing the KV cache size to about one-tenth of the original while retaining critical information.  
- [Finding 2] The method reconstructs within-page logits using a compact basis and estimates each page’s attention mass via log-sum-exp, allowing selective attention only to top pages without reading full candidate keys or values.  
- [Finding 3] LOCKS achieves near-optimal performance on long-context benchmarks like LongBench-v1 QA and AIME26 reasoning tasks, matching FullKV quality at 100K+ token contexts while attending only about 2% of tokens, with a twofold reduction in per-token decode latency.

## Methodology  
The authors approach the problem by recognizing that attention keys are locally low-rank: shared low-rank bases dominate across pages, but each page has unique high-rank components. LOCKS generates a spectral summary per page using these local bases, which is much smaller than the full KV cache. During decoding, the method computes an attention mass for each page via log-sum-exp of the summary and selects only the top pages to attend to. This selection process does not require reading any candidate keys or values from memory. The within-page logits are reconstructed using the compact basis, ensuring that the output remains faithful to the original dense attention. The entire process is implemented as a drop-in plugin for vLLM, enabling batched decoding with full CUDA graph optimization.

## Results  
On LongBench-v1 QA tasks, LOCKS tracks the read-every-key oracle on retrieval-dense RULER down to minimal budgets and maintains strong margins on long-form reasoning benchmarks like AIME26 and MATH-500, where baseline selectors fail. At a 2048-token budget, LOCKS matches FullKV’s aggregate quality at 100K+ context length while attending only about 2% of tokens. Crucially, it halves per-token decode latency—from 2.0× faster at 1M tokens compared to dense attention—and runs efficiently within CUDA graphs for batched inference.

## Significance  
This work is significant because it tackles the scalability limit of long-context LLMs by decoupling global attention from local summaries, enabling efficient decoding without sacrificing quality. By reducing memory footprint and computation time, LOCKS opens the door to deploying large models on longer contexts with lower resource requirements—critical for real-world applications involving extensive text processing.

## Related Concepts  
- KV cache: The memory structure storing key-value pairs used in attention computations during decoding.  
- Spectral decomposition: A method of representing matrices as sums of outer products, enabling low-rank approximations.  
- Log-sum-exp: A function that combines multiple values into a single summary, useful for estimating attention mass.  
- Long-context decoding: The challenge of efficiently processing very long input sequences in language models.
