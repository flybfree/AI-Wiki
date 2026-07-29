# Summary: 2026-07-28_10-01-30Z_AMPBench_MT_AHomology_ControlledBenchmarkforAntimi.md
Saved: 2026-07-28 22:41
Source: 2026-07-28_10-01-30Z_AMPBench_MT_AHomology_ControlledBenchmarkforAntimi.md
Model: None

---

## Summary  
The paper introduces AMPBench‑MT, a homology‑controlled benchmark that jointly evaluates binary recognition of antimicrobial peptides (AMPs) and their species‑conditioned potency, spectrum, and safety endpoints using canonical peptide records. It argues that current benchmarks lack integration of these multi‑faceted assay‑derived signals, leading to misleading leaderboard performance. The benchmark integrates multiple assay‑derived signals to provide a holistic view of peptide performance.  

## Key Contributions  
- AMPBench‑MT provides a provenance‑preserving benchmark standardizing binary recognition, pMIC regression, endpoint‑specific potency, and safety‑facing readouts across canonical peptide records.  
- Empirical evaluation across 161 model evaluations shows high binary accuracy does not guarantee correct assay‑endpoint behavior; frozen language‑model embeddings dominate error clusters while graph and classical regressors perform better.  
- Spectrum labeling reveals that PR‑oriented metrics can be misleading under scarce observed negatives, whereas low‑toxicity, HC50 hemolysis, and selectivity expose smaller but more assay‑facing signals.  

## Methodology  
The authors organized canonical peptide records into three modalities: (1) binary recognition of AMP activity, (2) species‑conditioned pMIC regression, and (3) endpoint‑specific potency and safety readings. They used frozen protein‑language‑model embeddings as the primary feature representation, supplemented with graph‑based and classical regressor components. Model evaluations were performed across 161 assay endpoints to compare performance relative to each other.  

## Results  
Binary classification models achieved high accuracy but poor correlation with actual assay outcomes; pMIC regression errors clustered around frozen embeddings. Spectrum metrics suffered from label sparsity issues, making PR‑oriented scores unreliable. Sensitivity analyses identified low‑toxicity, HC50 hemolysis, and selectivity as informative signals despite lower magnitude. The analysis also demonstrates that PR‑oriented metrics can be misleading under scarce observed negatives, while low‑toxicity, HC50 hemolysis, and selectivity expose smaller but more assay‑facing signals.  

## Significance  
This work shifts AMP evaluation beyond recognition leaderboards to endpoint‑aware evidence auditing, highlighting the need for holistic assessment of peptide potency, spectrum, and safety. By integrating multiple assay‑derived signals, AMPBench‑MT enables researchers to make more reliable predictions that reflect real experimental behavior.  

## Related Concepts  
Antimicrobial peptides (AMPs), homology‑controlled benchmarking, binary recognition, pMIC regression, endpoint‑specific assays, PR‑oriented metrics, frozen language‑model embeddings, graph regressors, HC50 hemolysis, selectivity.
