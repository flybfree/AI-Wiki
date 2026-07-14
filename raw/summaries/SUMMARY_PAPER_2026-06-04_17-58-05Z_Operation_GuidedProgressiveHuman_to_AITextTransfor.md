---

title: "Summary: Operation-Guided Progressive Human-to-AI Text Transformation Benchmark for Multi-Granularity AI-Text Detection"
url: http://arxiv.org/abs/2606.06481v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-04_17-58-05Z_Operation_GuidedProgressiveHuman_to_AITextTransfor.md
generated_at: "2026-06-11 10:53"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-06-04 17-58-05Z Operation Guidedprogressivehuman To Aitexttransfor


## Summary
The paper introduces OpAI‑Bench, an operation‑guided benchmark for studying progressive human‑to‑AI text transformation across document, sentence, token, and span granularities. It constructs nine sequentially revised versions per sample under predefined AI coverage levels and five edit operations spanning four domains while preserving complete authorship provenance at multiple levels. The study demonstrates that AI‑text detectability is shaped by edit operation, domain, and cumulative revision history rather than solely by the proportion of AI‑edited content.

## Key Takeaways
- Mixed‑authorship intermediate versions often exhibit lower detectability than both fully human and heavily AI‑edited endpoints, revealing non‑monotonic detection patterns.  
- Detectability depends on edit operation, domain, and cumulative revision history beyond just the proportion of AI‑generated text.  
- The benchmark provides fine‑grained provenance tracking across four domains with 8 document‑level, 7 sentence‑level, and 2 token/span‑level detectors.

## Context
Existing AI text detection benchmarks focus only on final outputs, limiting insight into how authorship signals evolve during co‑editing. This work addresses that gap by modeling the progressive transformation process across multiple revisions and granularities.

## Implications
Practitioners can design more accurate detection systems that account for revision history and edit style rather than static content ratios. The benchmark supports research and industry efforts to understand AI collaboration dynamics in real workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.06481v1)
