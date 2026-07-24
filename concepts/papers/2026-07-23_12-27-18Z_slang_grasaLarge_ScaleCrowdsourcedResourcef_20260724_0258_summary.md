# Summary: 2026-07-23_12-27-18Z_slang_grasaLarge_ScaleCrowdsourcedResourceforNon_S.md
Saved: 2026-07-24 02:58
Source: 2026-07-23_12-27-18Z_slang_grasaLarge_ScaleCrowdsourcedResourceforNon_S.md
Model: None

---

## Summary  
This paper introduces **slang.gr**, a large‑scale crowdsourced lexicon of Greek non‑standard language, and conducts the first systematic computational analysis of its linguistic structure and community dynamics. By mapping noisy folksonomic tags onto a structured multi‑layer taxonomy, the authors enable quantitative study of slang’s semantic categories and sociolinguistic metadata. The work reveals that Greek slang is dominated by person‑related and evaluative expressions, displays high morphological creativity, and is shaped by highly skewed participation with short user lifespans and overlapping communities. A community‑based confidence score for definitions is also introduced to improve interpretability while preserving meaningful behavioral signals.

## Key Contributions  
- [Finding 1] Greek slang is strongly centered on person‑related and evaluative language, indicating a core focus on interpersonal judgments rather than abstract or topical topics.  
- [Finding 2] The lexical resource exhibits high morphological creativity, with frequent derivational and inflectional innovations that go beyond standard morphology.  
- [Finding 3] Participation is highly skewed: users typically have short lifespans in the dataset, leading to overlapping communities whose contributions create a complex, non‑uniform user base.

## Methodology  
The authors assembled **slang.gr**, a crowdsourced lexicon that combines lexical entries with user‑generated folksonomic tags and interaction metadata. To make this noisy data usable for analysis, they built a structured multi‑layer taxonomy that maps each tag to semantic categories (e.g., “person”, “evaluation”) and sociolinguistic metadata (e.g., age group, region). This representation allows systematic clustering of slang items and tracking of user behavior. The study then analyzes the distribution of these tags across the lexicon and examines how confidence scores derived from user roles, interaction patterns, and moderation signals correlate with lexical quality.

## Results  
Empirical results show that person‑related and evaluative tags dominate the tag frequency distribution (≈70 % of all tags), confirming the personal focus identified in Finding 1. Morphological diversity is measured by a high entropy score for derivational forms, supporting Finding 2. User‑lifetime analysis reveals that only ~30 % of contributors have participated for more than six months, and many users belong to multiple overlapping communities, aligning with Finding 3. The community confidence score correlates strongly (r ≈ 0.78) with the proportion of tags contributed by high‑engagement users, demonstrating that the proposed representation improves interpretability while retaining meaningful behavioral signals.

## Significance  
This work establishes **slang.gr** as a computational resource for non‑standard Greek, providing a foundation for sociolinguistic NLP tasks such as bias analysis and informal language modeling in large language models (LLMs). By offering a structured taxonomy and confidence scoring mechanism, the dataset enables researchers to study slang’s role in cultural identity formation and its impact on algorithmic perception.

## Related Concepts  
- Slang  
- Crowdsourced lexicon  
- Folksonomic tags  
- Multi‑layer taxonomy  
- Community‑based confidence score  
- Sociolinguistics  
- Natural language processing (NLP)  
- Large language models (LLMs) bias analysis
