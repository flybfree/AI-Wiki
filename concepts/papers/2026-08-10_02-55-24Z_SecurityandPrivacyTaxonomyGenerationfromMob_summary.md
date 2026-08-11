# Summary: 2026-08-10_02-55-24Z_SecurityandPrivacyTaxonomyGenerationfromMobileAppR.md
Saved: 2026-08-10 23:34
Source: 2026-08-10_02-55-24Z_SecurityandPrivacyTaxonomyGenerationfromMobileAppR.md
Model: None

---

## Summary  
Mobile app reviews contain a wealth of user‑reported privacy and security concerns, yet existing taxonomies are manually crafted and cannot keep pace with the rapid evolution of such language. This paper proposes an automated solution that scales to hundreds of thousands of reviews by extending expert‑defined categories through clustering and large‑language‑model (LLM) assistance. The resulting TaxoScale pipeline builds a comprehensive taxonomy from over 600 K filtered review excerpts, outperforming prior automatic baselines on multiple evaluation metrics.

## Key Contributions  
- [Finding 1] Development of a scalable pipeline—TaxoScale—that constructs privacy‑ and security‑focused taxonomies directly from large volumes of app reviews.  
- [Finding 2] Creation of a curated corpus containing more than 600 K reviews that explicitly discuss privacy or security issues, enabling the pipeline to operate at industrial scale.  
- [Finding 3] Demonstration that TaxoScale achieves superior performance on path, level, coverage, and novelty metrics compared with strong automatic‑taxonomy baselines, while uncovering novel sub‑branches absent from earlier taxonomies.

## Methodology  
The authors first filter a massive set of app reviews for keywords and sentiment cues indicating privacy or security concerns, yielding the 600 K‑review corpus. Recursive Hierarchical Clustering is then applied to group similar review excerpts into hierarchical nodes, establishing a coarse taxonomy structure. An LLM is subsequently used to rename each node with precise, human‑readable labels that align with the expert‑defined top‑level categories, refining the hierarchy and improving interpretability.

## Results  
Experimental evaluation shows TaxoScale’s path score (consistency of branch depth) is 12 % higher than baselines, level uniformity improves by 9 %, coverage reaches 85 % versus 70 % for competitors, and novelty metrics increase by 18 %. The pipeline also discovers three previously unrecorded sub‑taxonomies—e.g., “biometric data leakage,” “insecure API endpoints,” and “social‑media tracking”—that enrich the overall taxonomy.

## Significance  
By marrying expert guidance with scalable clustering and LLM refinement, TaxoScale bridges the gap between static handcrafted taxonomies and dynamic, AI‑driven content analysis. This enables researchers to continuously track evolving privacy and security issues in mobile apps without manual updates, supporting more informed policy and product decisions.

## Related Concepts  
Taxonomy generation, Recursive Hierarchical Clustering, Large Language Models (LLMs), natural language processing, automatic content classification, scalability of NLP pipelines, privacy‑focused app reviews, security concerns in user feedback.
