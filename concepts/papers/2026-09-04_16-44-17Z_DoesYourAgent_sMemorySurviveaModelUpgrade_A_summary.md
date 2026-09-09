# Summary: 2026-09-04_16-44-17Z_DoesYourAgent_sMemorySurviveaModelUpgrade_AControl.md
Saved: 2026-09-06 21:47
Source: 2026-09-04_16-44-17Z_DoesYourAgent_sMemorySurviveaModelUpgrade_AControl.md
Original paper: [arXiv:2609.05339](https://arxiv.org/abs/2609.05339)
Model: None

---

## Summary  
The paper investigates whether an agent’s memory survives a model upgrade by comparing four distinct memory representations across 48 synthetic histories. It finds that some structures—such as fixed‑schema knowledge graphs—transfer reliably, while others—like compressed notes and mixed retrieval embeddings—experience large accuracy drops due to embedding mismatches and information loss during construction. The study employs two open‑weight models under ten billion parameters with exact scoring to quantify these effects.

## Key Contributions  
- Fixed‑schema structures (KG‑fixed) transfer reliably, with only a minimal drift of +0.0004 ± 0.0020 in accuracy after a writer swap.  
- Compressed notes (NOTES) exhibit high model coupling, causing asymmetric shifts of up to ±13.28 percentage points depending on migration direction.  
- Retrieval‑augmented generation (RAG) gains are largely lost when using a 50/50 mixed embedding index; only a 4.96‑point improvement is observed versus the full re‑embedding gain of 11.90 points.

## Methodology  
The authors generate synthetic histories with randomized answer codes and evaluate four memory formats: long‑context reading (LC‑RAW), compressed notes, fixed‑schema knowledge graphs, and RAG retrieval. They perform migrations between two open‑weight models, compute exact accuracy changes, and decompose the observed deficits into construction loss versus retrieval failure using statistical decomposition.

## Results  
- KG‑fixed accuracy change: +0.0004 ± 0.0020.  
- NOTES shift: either +9.91 or –13.28 percentage points, indicating strong directionality.  
- RAG with mixed 50/50 embedding index yields a 4.96‑point gain; full re‑embedding achieves 11.90 points.  
- Store‑only repair of NOTES fails to reach the 90 % recovery target in all cases, whereas retaining raw source history recovers performance in 34 of 48 test cases for one direction.

## Significance  
These findings underscore that memory migration is not a simple copy‑and‑paste operation; it depends heavily on how information is encoded and retrieved. The results call for direction‑specific testing, strict isolation of embedding spaces, and preservation of the original source history to enable effective repair, which are critical for maintaining consistent agent behavior across model upgrades.

## Related Concepts  
Memory portability, model upgrade impact, knowledge graph (KG) fixed schema, retrieval‑augmented generation (RAG), embedding space alignment, synthetic evaluation, compression artifacts, accuracy drift, directionality of transfer.
