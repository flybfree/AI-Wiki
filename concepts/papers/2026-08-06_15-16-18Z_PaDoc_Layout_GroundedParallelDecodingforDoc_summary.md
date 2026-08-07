# Summary: 2026-08-06_15-16-18Z_PaDoc_Layout_GroundedParallelDecodingforDocumentPa.md
Saved: 2026-08-06 22:18
Source: 2026-08-06_15-16-18Z_PaDoc_Layout_GroundedParallelDecodingforDocumentPa.md
Model: None

---

## Summary  
The paper introduces PaDoc, a layout‑grounded parser that aims to combine the full‑page context of end‑to‑end document parsers with the parallel decoding benefits of crop‑based two‑stage models. By treating the predicted page layout as a branching structure over a shared representation, PaDoc eliminates sequential dependencies between regions and reduces the decoding depth to the longest layout‑content path. The authors achieve this factorization within a single multimodal language model (MLLM) using packed variable‑length ancestor attention and masked parallel decoding, which are served concurrently by vLLM’s backend.  

## Key Contributions  
- [Finding 1] PaDoc models the page as a branching layout structure that shares a common representation with its content regions, thereby decoupling layout prediction from regional decoding.  
- [Finding 2] The authors derive a prefix‑conditioned factorization that lets the layout stream and regional branches advance concurrently, limiting the maximum decoder depth to the longest path in the tree.  
- [Finding 3] PaDoc is implemented as a single MLLM with packed variable‑length ancestor attention; masked parallel decoding creates concurrent requests that reuse shared prefixes, enabling high throughput on vLLM.  

## Methodology  
Traditional document parsers either serialize all page elements into one autoregressive sequence (causing long decoding paths) or split the task into crop‑based two‑stage stages that repeat visual prefills and lose context. PaDoc bridges this gap by first generating a layout tree from the image, then factorizing the decoding process so that each branch of the tree processes its own region while reusing the same shared prefix. The factorization is realized within an MLLM: variable‑length ancestor attention packs all ancestors into a single token set, preserving visibility under standard next‑token training. Masked parallel decoding splits the output into independent sub‑requests that vLLM serves simultaneously, each retaining the cached shared prefix. This design preserves full‑page context while exploiting parallelism.  

## Results  
On OmniDocBench Full, PaDoc attains an Overall layout F1 of 91.1 and a top‑tier Overall score of 94.24, with Text Edit at 0.038 and Formula CDM at 95.59—outperforming all end‑to‑end baselines. In benchmarked experiments on a 384‑page subset using one A800 GPU, PaDoc is the fastest parser across five concurrency levels, boosting valid‑page throughput by 67.4–118% and cutting P95 latency by 39.2–54.9% relative to a same‑backbone sequential SFT baseline.  

## Significance  
By eliminating region dependencies through layout grounding, PaDoc improves both accuracy (higher F1) and efficiency (faster throughput, lower latency). The factorization enables scalable deployment of document parsers on large models without sacrificing the benefits of parallel decoding, making it a practical solution for real‑world applications such as OCR, form extraction, and knowledge retrieval.  

## Related Concepts  
layout‑grounded parsing, prefix‑conditioned factorization, MLLM (multimodal language model), variable‑length ancestor attention, masked parallel decoding, vLLM backend, document parsing, end‑to‑end parser, crop‑based two‑stage models, shared‑prefix reuse.
