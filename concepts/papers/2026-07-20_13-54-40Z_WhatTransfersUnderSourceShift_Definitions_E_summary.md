# Summary: 2026-07-20_13-54-40Z_WhatTransfersUnderSourceShift_Definitions_Examples.md
Saved: 2026-07-24 00:20
Source: 2026-07-20_13-54-40Z_WhatTransfersUnderSourceShift_Definitions_Examples.md
Model: None

---

## Summary  
The paper tackles the challenge of climate disclosure classification across multiple sources and evaluates three adaptation strategies—definitions, examples, and fine‑tuning—under source shift. It reframes the task as a cross‑source adaptation problem and tests eleven open and closed‑source LLMs on two corpora that share labels but originate from different documents. The study demonstrates that all strategies improve performance when moving between sources, yet some in‑source strengths disappear after shifting. Simpler approaches such as few‑shot examples tend to retain their advantage more reliably than complex retrieval or fine‑tuning methods.

## Key Contributions  
- Finding 1: All adaptation strategies (definitions, examples, fine‑tuning) yield positive cross‑source gains on average.  
- Finding 2: In‑source strengths differ from cross‑source; similarity‑based retrieval and LoRA fine‑tuning dominate in‑source but lose most of that advantage under source shift.  
- Finding 3: Randomly selected few‑shot examples retain their advantage more reliably, while definitions transfer best when their granularity matches the target text.

## Methodology  
The authors construct two corpora of climate disclosures from distinct sources—annual reports and press releases—that share a common label space. They evaluate eleven open and closed‑source LLMs using three adaptation strategies: similarity‑based retrieval, few‑shot examples, and LoRA fine‑tuning. For each strategy they compute classification accuracy on a held‑out test set that simulates source shift by presenting the same label to documents from the other corpus.

## Results  
Average gains are modest (≈2–4% improvement). In‑source, retrieval and LoRA achieve the highest scores (~7.5%). After source shift, these drop to ~6.0%, while few‑shot examples stay around 6.8%. Definitions improve most consistently but only when their granularity aligns with target text length.

## Significance  
The study clarifies that adaptation strategies are not transferable; simpler methods like few‑shot examples are more reliable across source shifts, guiding practitioners to choose robust classification pipelines for multi‑source climate data.

## Related Concepts  
- Climate disclosure classification  
- Source shift / cross‑source adaptation  
- Fine‑tuning (LoRA)  
- Few‑shot prompting  
- Similarity‑based retrieval  
- Definition granularity
