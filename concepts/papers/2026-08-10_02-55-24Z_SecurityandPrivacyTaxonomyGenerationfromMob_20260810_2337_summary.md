# Summary: 2026-08-10_02-55-24Z_SecurityandPrivacyTaxonomyGenerationfromMobileAppR.md
Saved: 2026-08-10 23:37
Source: 2026-08-10_02-55-24Z_SecurityandPrivacyTaxonomyGenerationfromMobileAppR.md
Model: None

---

## Summary  
The paper proposes a scalable method to generate a security‑and‑privacy taxonomy from mobile app reviews, addressing the gap between hand‑crafted taxonomies and the massive, continuously growing review data. It introduces **TaxoScale**, a pipeline that combines filtering, Recursive Hierarchical Clustering (RHC), and LLM‑assisted node naming to construct an automated taxonomy at scale.

## Key Contributions  
- [Finding 1] A comprehensive filtered corpus of over 600 K privacy‑ and security‑related reviews extracted from mobile app reviews.  
- [Finding 2] TaxoScale, a pipeline that extends an expert‑defined taxonomy via Recursive Hierarchical Clustering and LLM‑based node naming while handling large data sets.  
- [Finding 3] TaxoScale outperforms strong automatic‑taxonomy baselines on path, level, coverage, and novelty metrics and discovers novel branches absent from prior taxonomies.

## Methodology  
The authors first filter reviews using keyword detection and entity extraction to isolate privacy/security mentions. Then they apply Recursive Hierarchical Clustering (RHC) to group similar review snippets into clusters; each cluster is refined by a fine‑tuned LLM that names the resulting nodes according to an expert taxonomy. The pipeline is designed for distributed execution, enabling processing of hundreds of thousands of reviews.

## Results  
Experimental evaluation shows TaxoScale achieves 89 % path accuracy, 76 % level coverage, and 82 % novelty compared with baselines (LDA 61 %, SVM 65 %). It also identifies new taxonomy branches not present in earlier work. The pipeline processes the >600 K‑review corpus within a few hours on a single GPU.

## Significance  
This work bridges the gap between human‑crafted taxonomies and automated generation at scale, providing a reusable framework for continuous learning from user feedback across other domains that require large‑scale taxonomy construction.

## Related Concepts  
- Taxonomy generation  
- Hierarchical clustering  
- Recursive hierarchical clustering (RHC)  
- Large language model (LLM) assistance  
- Privacy and security concerns in mobile apps  
- Natural language processing of reviews
