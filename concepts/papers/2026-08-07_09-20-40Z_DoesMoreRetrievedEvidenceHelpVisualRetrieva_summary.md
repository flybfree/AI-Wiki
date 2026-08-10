# Summary: 2026-08-07_09-20-40Z_DoesMoreRetrievedEvidenceHelpVisualRetrieval_Augme.md
Saved: 2026-08-09 22:52
Source: 2026-08-07_09-20-40Z_DoesMoreRetrievedEvidenceHelpVisualRetrieval_Augme.md
Model: None

---

## Summary  
The paper investigates whether expanding the set of retrieved evidence improves visual retrieval‑augmented generation (RAG) when using diffusion language models, finding that unconditionally passing all retrieved pages can actually degrade answer accuracy because of semantic conflicts among different sources. To address this, the authors introduce an Entropy‑Based Candidate Filter (ECF), a training‑free framework that selects only beneficial evidence while preserving retrieval coverage. Their analysis reveals a latent‑source interference mechanism that explains why additional pages cause problems and provides a way to assess evidence before decoding.

## Key Contributions  
- Unconditional evidence expansion degrades answer accuracy because retrieved visual sources can introduce semantic conflicts, leading to source‑coherence loss in the denoising process.  
- A latent‑source analysis demonstrates how position‑wise proposals from incompatible pages combine into unsupported answers, making it possible to evaluate evidence before generation.  
- The Entropy‑Based Candidate Filter (ECF) constructs multi‑granularity evidence units and uses blank‑controlled block confidence together with retrieval rank to decide which candidates should enter the final context, achieving a 2.62 pp average accuracy boost over the best fixed top‑k input.

## Methodology  
The authors compare three multimodal diffusion language models across five visual QA benchmarks. They evaluate two regimes: (1) unconditional inclusion of all retrieved pages and (2) selective admission guided by ECF’s confidence and rank criteria. The experiments measure answer‑page recall, answer accuracy, and the distribution of the first‑step answer blocks to detect interference early in decoding.

## Results  
Across the three DLMs, ECF improves average answer accuracy by 2.62 percentage points relative to the strongest fixed top‑k input. Specifically with LLaDA2.0‑Uni it outperforms the best training‑free competitor by 2.37 pp on each dataset. The improvement is consistent across all benchmarks, indicating that selective evidence admission consistently yields better performance than blind expansion.

## Significance  
The findings challenge the assumption that more retrieved evidence always helps visual RAG with diffusion models; instead, they demonstrate that strategic filtering can enhance accuracy while limiting harmful exposure to irrelevant or conflicting content. ECF offers a practical, training‑free solution for improving retrieval‑augmented generation in multimodal settings.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Diffusion language models (DLMs)  
- Latent‑source analysis  
- Source‑coherence loss  
- Evidence units and multi‑granularity filtering  
- Confidence‑based candidate selection  
- Multimodal visual QA benchmarks
