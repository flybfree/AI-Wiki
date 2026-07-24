# Summary: 2026-07-20_13-54-40Z_WhatTransfersUnderSourceShift_Definitions_Examples.md
Saved: 2026-07-24 00:24
Source: 2026-07-20_13-54-40Z_WhatTransfersUnderSourceShift_Definitions_Examples.md
Model: None

---

## Summary  
Climate disclosure classification is a core task for extracting environmental impact information from corporate reports, yet disclosures appear across multiple formats such as annual reports, press releases and earnings calls that differ in length, purpose and writing style. The authors reframe this problem as a cross‑source adaptation challenge and evaluate three common LLM adaptation strategies—definitions, examples, and fine‑tuning—across eleven open‑ and closed‑source models using two corpora that share the same label space but originate from different sources. Their work demonstrates that while all strategies yield positive gains when moving between sources, the most effective in‑source methods often degrade under source shift, suggesting a need for simpler, more robust approaches.

## Key Contributions  
- [Finding 1] All adaptation strategies—definitions, examples, and fine‑tuning—produce measurable cross‑source improvements over single‑source baselines.  
- [Finding 2] The strongest in‑source strategies (similarity‑based retrieval and LoRA fine‑tuning) lose most of their advantage when the source changes, indicating a loss of transferability.  
- [Finding 3] Simple few‑shot examples retain their cross‑source benefit more consistently than complex in‑source methods.

## Methodology  
The authors treat climate disclosure classification as an adaptation problem where a model trained on one source must perform on another. They compare three strategies: (1) **Definitions**, which provide explicit mapping of source‑specific terminology to universal labels; (2) **Examples**, where a few representative sentences from the target source are inserted into prompts; and (3) **Fine‑tuning**, using LoRA adapters fine‑tuned on the source data. Experiments are conducted on eleven open‑ and closed‑source LLMs, with two corpora that share labels but differ in style—annual reports versus press releases—and both in‑source and out‑of‑source performance is measured.

## Results  
Average gains across all strategies are positive, confirming that adaptation helps. However, similarity retrieval and LoRA fine‑tuning achieve the highest in‑source F1 scores (≈0.84) but drop to ≈0.62 when evaluated on the other source, reflecting a sharp loss of transferability. Few‑shot examples yield moderate gains both ways (≈0.71 in‑source, ≈0.68 out‑of‑source), and their advantage is more stable. Definitions improve only when granularity matches the target text; otherwise they provide negligible benefit. Thus, simpler prompting remains safer under source shift.

## Significance  
The study reveals that adaptation strategies are not invariant to source style, guiding practitioners away from complex in‑source fine‑tuning toward lightweight, robust methods such as few‑shot examples or well‑aligned definitions for climate disclosure analysis.

## Related Concepts  
Cross‑source adaptation, definition transfer, example‑based prompting, LoRA fine‑tuning, similarity retrieval, LLM evaluation, in‑source vs. out‑of‑source performance.
