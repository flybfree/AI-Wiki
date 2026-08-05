# Summary: 2026-07-24_16-19-04Z_Phylogeneticsignalinmarinemammalandbirdvocalizatio.md
Saved: 2026-07-26 21:54
Source: 2026-07-24_16-19-04Z_Phylogeneticsignalinmarinemammalandbirdvocalizatio.md
Model: None

---

## Summary  
The paper asks whether large‑scale audio foundation models encode evolutionary information that is not present in their training labels. By applying four state‑of‑the‑art embeddings to species vocalizations from two independent radiations (cetaceans and birds), the authors show that these models recover strong phylogenetic distances without any domain‑specific pretraining, suggesting that the benefit of such pretraining is limited.

## Semantic links
- [[concepts/2026-07-27_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-07-27]] — 6 title terms overlap; 3 backlinks; 6 summary/topic terms overlap
- [[concepts/llm-models/2026-07-10_OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 5 title terms overlap; 3 backlinks; 5 summary/topic terms overlap
- [[concepts/2026-06-30_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-06-30]] — 6 title terms overlap; 6 summary/topic terms overlap; semantic match 0.14

## Key Contributions  
- **Finding 1:** General‑purpose audio foundation models (CLAP, BEATs‑bio, AST) recover high phylogenetic signal for 32 cetacean species and 20 bird species, with correlation coefficients r≈0.82 (p<0.001).  
- **Finding 2:** The signal persists after reducing embeddings to 105 dimensions and after controlling for dominant frequency, indicating it is not an artifact of dimensionality or merely pitch‑based.  
- **Finding 3:** Adding domain‑specific pretraining (e.g., BirdNET) does not improve performance; the models already capture evolutionary information across independent radiations.

## Methodology  
The authors employed four large audio foundation models trained on diverse datasets: AST, CLAP, BEATs‑bio, and BirdNET. Phylogenetic distances were measured by computing Mantel statistics between species tree distances and pairwise embedding distances. To test for dimensionality or frequency artefacts, they projected every embedding onto a 105‑dimensional PCA space and performed partial Mantel tests that controlled for dominant frequency.

## Results  
For cetaceans: CLAP r=0.82 (p<0.001), BEATs‑bio r=0.82 (p<0.001), AST r=0.74 (p<0.001). For birds: AST r=0.55, CLAP r=0.52; BirdNET and BEATs‑bio gave lower coefficients around 0.32–0.36. Hand‑crafted MFCC features yielded a weak correlation r≈0.04 (p=0.338). The gap remains after PCA projection, and the partial Mantel controlling for frequency explains 97 % of variance with r=0.404.

## Significance  
These findings demonstrate that audio embeddings can encode deep evolutionary structure without requiring taxon‑specific pretraining, challenging the assumption that domain adaptation is necessary to capture phylogenetic signal in sound data.

## Related Concepts  
- Phylogenetic signal  
- Audio foundation models (AST, CLAP, BEATs‑bio)  
- Mantel test for spatial autocorrelation  
- Dimensionality reduction via PCA  
- Domain‑specific pretraining vs. general‑purpose embeddings  
- MFCC features and pitch analysis
