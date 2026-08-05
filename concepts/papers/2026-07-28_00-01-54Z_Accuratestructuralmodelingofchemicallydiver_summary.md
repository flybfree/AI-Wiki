# Summary: 2026-07-28_00-01-54Z_Accuratestructuralmodelingofchemicallydiversemolec.md
Saved: 2026-07-28 22:26
Source: 2026-07-28_00-01-54Z_Accuratestructuralmodelingofchemicallydiversemolec.md
Model: None

---

## Summary  
The paper introduces Vilya‑2, a diffusion transformer that models peptide‑protein interfaces using an all‑atom representation, enabling accurate structural prediction across chemically diverse peptides and macrocycles. It achieves sub‑2 Å backbone RMSD for 59.1 % of predicted interfaces, outperforming conventional co‑folding baselines even when the bound receptor is provided as a template. Vilya‑2 also excels in small‑molecule docking and generalizes to novel protein‑small‑molecule complexes and large macrocyclic molecules. The model serves as a foundation for de novo peptide design pipelines.

## Semantic links
- [[concepts/papers/2026-07-24_14-31-54Z_IQ_JEPA_AJoint_EmbeddingPredictiveArchitect_summary.md|Summary: 2026-07-24_14-31-54Z_IQ_JEPA_AJoint_EmbeddingPredictiveArchitecturewith.md]] — 3 title terms overlap; 1 backlink; 12 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 2 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-20_16-43-54Z_DoLanguageModelsDreamofBindingMolecules_Ben_summary.md|Summary: 2026-07-20_16-43-54Z_DoLanguageModelsDreamofBindingMolecules_Benchmarki.md]] — 3 title terms overlap; 12 summary/topic terms overlap; semantic match 0.09

## Key Contributions  
- [Finding 1] Vilya‑2 achieves sub‑2 Å backbone RMSD on 59.1 % of peptide interfaces, surpassing typical co‑folding models.  
- [Finding 2] It generalizes to novel protein‑small‑molecule complexes and large macrocycles not seen in training data.  
- [Finding 3] The model can be fine‑tuned as a foundation model for hit‑to‑lead optimization.

## Methodology  
Vilya‑2 extends the all‑atom representation of its predecessor, Vilya‑1, to capture interactions between peptides and protein targets. It employs a diffusion transformer architecture trained on co‑evolutionary statistics across diverse peptide classes, generating multiple structural ensembles per input complex and ranking them with calibrated confidence scores.

## Results  
The model recovers 59.1 % of interfaces within sub‑2 Å RMSD, outperforming a representative co‑folding model that uses the bound receptor as a template. It also demonstrates state‑of‑the‑art performance in small‑molecule docking and extends to macrocycles and disulfide‑stapled miniproteins larger than any training example.

## Significance  
By unifying high accuracy with broad chemical generalizability, Vilya‑2 provides a versatile foundation for de novo peptide therapeutics, reducing reliance on protein templates and accelerating drug discovery pipelines.

## Related Concepts  
diffusion transformer, all‑atom representation, co‑evolutionary statistics, RMSD, foundation model, hit‑to‑lead optimization.
