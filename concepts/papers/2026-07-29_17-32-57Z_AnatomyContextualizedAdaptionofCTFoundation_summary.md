# Summary: 2026-07-29_17-32-57Z_AnatomyContextualizedAdaptionofCTFoundationModels.md
Saved: 2026-07-29 23:02
Source: 2026-07-29_17-32-57Z_AnatomyContextualizedAdaptionofCTFoundationModels.md
Model: None

---

## Summary  
The paper proposes Anatomy Contextualized Adaptation (ACA), a lightweight framework that adapts frozen CT foundation models for anatomy‑level vision‑language alignment while preserving global contextualization. It addresses the trade‑off between fine‑grained anatomical signals and whole‑volume context, avoiding full re‑training of the model. ACA extracts anatomy embeddings with TotalSegmentator, refines them through an inter‑anatomy transformer, and aligns both per‑anatomy and scan‑level text from radiology reports to these visual features.

## Key Contributions  
- [Finding 1] ACA consistently outperforms frozen CT foundation model baselines and existing fine‑grained methods on zero‑shot classification tasks.  
- [Finding 2] The framework requires less than one hour of training once embeddings are cached, making it computationally efficient.  
- [Finding 3] Attention weights learned by ACA’s inter‑anatomy transformer indicate plausible cross‑anatomy context routing.

## Methodology  
The authors decompose CT volumes into anatomy‑level embeddings using TotalSegmentator, then refine these embeddings with a transformer that captures relationships across anatomies. Both per‑anatomy and scan‑level textual descriptions extracted from radiology reports are aligned to the visual features. Because only embedding refinement is trained, the adaptation process is lightweight.

## Results  
ACA achieves higher accuracy than both frozen foundation model baselines and prior fine‑grained approaches on Merlin and CT‑RATE zero‑shot classification datasets. Training completes in under one hour after embedding caching. Moreover, the attention maps reveal cross‑anatomy routing that aligns with textual cues extracted from reports.

## Significance  
This work demonstrates that fine‑grained anatomical adaptation can be performed efficiently without sacrificing global context, offering a scalable solution for radiology AI systems. It reduces computational cost and enables richer multimodal alignment, which is valuable for clinical decision support tools.

## Related Concepts  
CT foundation models, vision‑language pre‑training, TotalSegmentator, anatomy‑level embeddings, inter‑anatomy transformer, zero‑shot classification, radiology report text extraction.
