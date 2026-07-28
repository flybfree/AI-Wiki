# Summary: 2026-07-25_16-15-50Z_WhatCLIPKnowsbutCannotSay_RecoveringNegationfromFr.md
Saved: 2026-07-27 22:37
Source: 2026-07-25_16-15-50Z_WhatCLIPKnowsbutCannotSay_RecoveringNegationfromFr.md
Model: None

---

## Summary  
Contrastive vision‑language models such as CLIP map semantically opposite phrases to nearly identical embeddings, causing them to ignore negation. The authors attribute this failure to a phenomenon they call **Representational Collapse**, where compositional syntax is encoded in intermediate layers but collapses into the final frozen representation. To recover the lost negation signal without retraining or altering CLIP’s parameters, they introduce **PeakPatch**, a lightweight post‑hoc correction system that intercepts the encoder at its compositional peak and injects a corrected deviation vector. The method adds only 5.2 M parameters (3.5 % of the backbone) while preserving the standard cosine similarity interface.

## Key Contributions  
- **Finding 1**: CLIP exhibits *Representational Collapse*, causing negation to be invisible in its final embeddings because visual alignment overwhelms syntactic composition.  
- **Finding 2**: The compositional syntax resides at a specific “peak” layer, which can be exploited for correction without fine‑tuning the whole model.  
- **Finding 3**: A joint training of an Embedding Correction Network (ECN) and a Score Correction Network (SCN) recovers negation with minimal added parameters, achieving strong gains on benchmark tasks.

## Methodology  
The authors first analyze CLIP’s text encoder to locate the layer where compositional divergence is maximal—the *compositional peak*. An **Embedding Correction Network (ECN)** employs cross‑attention to pull a negation‑specific signal from this peak into the final embedding space, anchored by a stable baseline. Simultaneously, a **Score Correction Network (SCN)** predicts bounded scalar offsets for downstream discriminative tasks. Both modules are trained end‑to‑end while CLIP’s weights remain frozen, resulting in only 5.2 M extra parameters.

## Results  
On the NegBench benchmark, PeakPatch reaches **74.3 %** on COCO MCQ, which is **+35.1** over raw CLIP and **+17.8** over the best encoder fine‑tuning method. It also scores **65.5 %** on VOC MCQ. Crucially, it outperforms all fine‑tuning baselines on fully out‑of‑distribution negation retrieval while training only 3.5 % of CLIP’s parameters. The corrected embeddings improve text‑to‑image generation by **+18.4** negation score and generalize across ViT‑B/32, ViT‑L/14, and SigLIP backbones.

## Significance  
Preserving the ability to detect negation is essential for robust multimodal systems that rely on contrastive similarity. By correcting frozen embeddings with a tiny post‑hoc module, PeakPatch demonstrates that large language models can be enhanced without costly fine‑tuning or architectural changes, offering a scalable path toward more faithful representation of semantic opposites.

## Related Concepts  
- **CLIP** (Contrastive Language‑Image Pretraining)  
- **Representational Collapse** – loss of syntactic structure in final embeddings  
- **Frozen intermediate features** – using untrained layers for correction  
- **Embedding Correction Network (ECN)** – cross‑attention based signal injection  
- **Score Correction Network (SCN)** – scalar offset prediction for tasks  
- **Cosine similarity interface** – unchanged similarity computation after correction
