# Summary: 2026-07-21_08-25-32Z_HPD_Parsing_HierarchicalParallelDocumentParsing.md
Saved: 2026-07-24 00:53
Source: 2026-07-21_08-25-32Z_HPD_Parsing_HierarchicalParallelDocumentParsing.md
Model: None

---

## Summary  
Current Vision‑Language Model (VLM) based document parsers generate the entire page’s output through a single token‑by‑token autoregressive trajectory, which creates a sequential bottleneck that scales poorly with document length. This approach ignores the fact that document layout can be analyzed globally while individual block contents may be decoded in parallel. The authors propose HPD‑Parsing, a Hierarchical Parallel Decoding framework that replaces full‑page autoregressive generation with a hierarchical, parallel decoding paradigm. By doing so, it aims to dramatically increase parsing throughput without sacrificing accuracy.

## Key Contributions  
- [Finding 1] Full‑page autoregressive generation imposes a sequential bottleneck that grows linearly with document length.  
- [Finding 2] Document layout must be understood globally, whereas block‑level content can be parsed concurrently.  
- [Finding 3] HPD‑Parsing introduces a hierarchical parallel decoding scheme using a layout branch and progressive multi‑token prediction (P‑MTP) to achieve higher throughput.

## Methodology  
The authors design a main “layout branch” that first parses the overall document structure, assigning each block to independent sub‑branches. Within each sub‑branch, P‑MTP is employed to predict multiple tokens simultaneously, reducing the number of decoding steps per branch. The parallel branches run concurrently, and their outputs are merged to produce the final parsed document.

## Results  
HPD‑Parsing achieves a throughput of 4,752 tokens per second on public benchmarks—approximately $2.62\times$ faster than the fastest existing document parsing model and $3.06\times$ faster than the vanilla autoregressive baseline. Crucially, it maintains competitive parsing accuracy, demonstrating that hierarchical parallel decoding can be an effective alternative to full‑page autoregressive generation.

## Significance  
This work opens a new direction for efficient unified document parsing by showing that global layout analysis and block‑level parallelism can coexist with high token throughput. The results suggest that future VLM‑based parsers could leverage hierarchical, parallel decoding to meet real‑time application demands such as live transcription or rapid data extraction.

## Related Concepts  
Hierarchical Parallel Decoding, Layout Branch, Progressive Multi‑Token Prediction (P‑MTP), Autoregressive Generation, Vision‑Language Model (VLM) Parser, Token Throughput.
