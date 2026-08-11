# Summary: 2026-08-08_13-56-39Z_TokenPrint_ACalibratedToken_SpaceFingerprintforLan.md
Saved: 2026-08-10 22:55
Source: 2026-08-08_13-56-39Z_TokenPrint_ACalibratedToken_SpaceFingerprintforLan.md
Model: None

---

## Summary  
The paper tackles the governance challenge of tracing a language model’s provenance—its base checkpoint and any overlap in training data—without relying on metadata alone. It proposes **TokenPrint**, a training‑free fingerprint that extracts token‑space similarity from the top‑k vocabulary projections of late hidden states induced by 250 fixed knowledge probes, measured via Jaccard overlap over decoded strings. The method is evaluated across 32 open‑weight models spanning nine families and architectures to demonstrate its utility for provenance inference. By showing a persistent “similarity ladder” that reflects shared training data even before task competence emerges, TokenPrint reveals hidden relationships invisible from coarse metadata.

## Key Contributions  
- [Finding 1] A similarity ladder across independently trained models on identical data scores 0.48 raw and 0.35 vocabulary‑corrected, persisting across three organizations, two tokenizer families, and two architecture classes, indicating shared training data beyond capability convergence.  
- [Finding 2] As a nearest‑neighbor lineage‑retrieval method, TokenPrint ranks the documented base among the top two candidates for all five R1 distillations (mean rank = 1.8, MRR = 0.60), including a math‑specialized base not identifiable from coarse metadata.  
- [Finding 3] Depth ablation shows lineage group discrimination strengthens toward the output distribution; AUC rises from 0.72 at quarter depth to 0.90 at full depth, and using only the top 5 output tokens retains AUC = 0.87.

## Methodology  
The authors approached provenance inference by treating each model’s latent token space as a set of strings derived from its top‑k vocabulary projections. For every knowledge probe they compute these projections on late hidden states, decode them to token sequences, and compare the resulting sets with Jaccard similarity. This creates a training‑free fingerprint that can be compared across models without access to their checkpoints or fine‑tuned weights. The fingerprints are evaluated for stability under quantization (int8/int4) and for lineage retrieval tasks.

## Results  
The experimental results reveal a clear similarity ladder: raw Jaccard ≈ 0.48, vocabulary‑corrected ≈ 0.35; shared‑base fine‑tunes drop to 0.39/0.33; same‑developer relatives to 0.38/0.28; unrelated models to 0.22/0.17. TokenPrint’s nearest‑neighbor retrieval ranks the true base in the top two for all R1 distillations (mean rank = 1.8, MRR = 0.60). Depth analysis shows AUC improvement from 0.72 to 0.90 with full hidden‑state use; even restricting to the first five output tokens retains AUC ≈ 0.87. Quantization does not degrade performance dramatically: Jaccard remains ~0.92 (int8) and 0.82–0.85 (int4), well above the maximum cross‑model similarity observed in the calibration pool (~0.81).

## Significance  
TokenPrint matters because it provides a robust, training‑free fingerprint that uncovers provenance beyond what metadata can convey, exposing shared data across organizations and architectures. Its lineage‑retrieval capability enables precise identification of base models even when only coarse descriptions are available, supporting responsible AI deployment and auditability. The method’s stability under quantization suggests practical applicability in resource‑constrained settings.

## Related Concepts  
token‑space fingerprints, Jaccard similarity, latent space analysis, knowledge probes, lineage retrieval, fine‑tuning provenance, open‑weight models, quantization effects, depth ablation, model distillation.
