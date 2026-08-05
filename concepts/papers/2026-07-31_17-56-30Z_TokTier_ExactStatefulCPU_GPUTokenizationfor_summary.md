# Summary: 2026-07-31_17-56-30Z_TokTier_ExactStatefulCPU_GPUTokenizationforAgentic.md
Saved: 2026-08-03 23:48
Source: 2026-07-31_17-56-30Z_TokTier_ExactStatefulCPU_GPUTokenizationforAgentic.md
Model: None

---

## Summary  
TokTier tackles the inefficiency of tokenization in LLM serving stacks that cache prompt KV state yet re‑tokenize the full request on every call, inflating latency despite a high prompt‑cache hit rate. It introduces a stateful CPU + GPU tokenization service whose emitted IDs match reference tokenization exactly, preserving continuity across session continuations. The solution reduces tokenization from 10 % to 64 % of total time‑to‑first‑token and lifts throughput dramatically under realistic workloads.

## Semantic links
- [[concepts/papers/2026-07-31_17-56-30Z_TokTier_ExactStatefulTokenizationforAgentic_20260803_1027_summary.md|Summary: 2026-07-31_17-56-30Z_TokTier_ExactStatefulTokenizationforAgenticLLMServ.md]] — 4 title terms overlap; 22 summary/topic terms overlap; semantic match 0.43
- [[concepts/papers/2026-07-31_17-56-30Z_TokTier_ExactStatefulTokenizationforAgentic_20260803_1029_summary.md|Summary: 2026-07-31_17-56-30Z_TokTier_ExactStatefulTokenizationforAgenticLLMServ.md]] — 4 title terms overlap; 21 summary/topic terms overlap; semantic match 0.38
- [[concepts/papers/2026-07-31_17-56-30Z_TokTier_ExactStatefulTokenizationforAgentic_summary.md|Summary: 2026-07-31_17-56-30Z_TokTier_ExactStatefulTokenizationforAgenticLLMServ.md]] — 4 title terms overlap; 21 summary/topic terms overlap; semantic match 0.38

## Key Contributions  
- [Finding 1] Tokenization overhead drops from a median 10 % contribution to 64 % of the time‑to‑first token, with GPU full tokenization encoding 1 M characters in 0.87 ms (491× faster than HF).  
- [Finding 2] Incremental repair repairs up to 3 million characters in 0.5–1.1 ms, a 491× speed‑up versus HF tokenization and 2.1× faster than the Gigatoken baseline.  
- [Finding 3] Four repair cores plus one GPU sustain 1,821 requests/s under a 50 ms P99 objective, compared with only 40 req/s for a 16‑core stateless front end.

## Methodology  
The authors built TokTier as a two‑mode pipeline: first they apply exact GPT‑family regex pre‑tokenization on the CPU, then offload the remaining BPE step to GPU. For session continuations only a small window around the append is re‑tokenized and spliced when a stable boundary is detected; otherwise the window widens or falls back. A sampled shadow verifier continuously checks live traffic against reference tokenizers.

## Results  
Across 153,951 agent calls with a 94.1 % prompt‑cache hit rate, tokenization accounts for 64 % of total latency. Differential campaigns over 17 tokenizer families (12.4 TB corpus, 93,000+ replayed steps) show zero divergence between TokTier and reference tokenizers. GPU full tokenization encodes 1 M characters in 0.87 ms; incremental repair from 100K to 3M characters takes 0.5–1.1 ms.

## Significance  
By eliminating redundant tokenization, TokTier reduces latency, increases request throughput, and lowers cost per inference, enabling higher‑throughput LLM serving stacks with minimal impact on accuracy or cache efficiency.

## Related Concepts  
- Tokenization (BPE, GPT regex pre-tokenization)  
- Stateful vs. stateless processing  
- GPU offload of tokenization  
- Incremental repair  
- Shadow verification
