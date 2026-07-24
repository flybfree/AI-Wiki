# Summary: 2026-07-23_12-27-18Z_slang_grasaLarge_ScaleCrowdsourcedResourceforNon_S.md
Saved: 2026-07-24 02:51
Source: 2026-07-23_12-27-18Z_slang_grasaLarge_ScaleCrowdsourcedResourceforNon_S.md
Model: None

---

## Summary  
The paper introduces **slang.gr**, a large‑scale crowdsourced lexicon of Greek non‑standard language, and presents the first systematic computational study of this dynamic linguistic phenomenon. It aims to model slang despite its irregularity by mapping noisy folksonomic tags into a structured multi‑layer taxonomy that captures both semantic categories and sociolinguistic metadata. The analysis reveals three striking findings: (1) Greek slang is dominated by person‑related and evaluative expressions, (2) it exhibits high morphological creativity, and (3) participation is highly skewed with short user lifespans and overlapping communities. A community‑based confidence score that integrates user roles, interaction patterns, and moderation signals is also introduced to improve interpretability.

## Key Contributions  
- [Finding 1] Slang in Greek is strongly centered on person‑related and evaluative language.  
- [Finding 2] The lexicon shows high morphological creativity, indicating frequent inventive word formation.  
- [Finding 3] Participation is highly skewed: users have short lifespans and overlapping communities dominate the dataset.

## Methodology  
The authors collected the **slang.gr** corpus, which contains lexical entries, user‑generated tags, and interaction logs from a crowdsourced platform. They mapped these noisy folksonomic tags to a structured multi‑layer taxonomy that simultaneously encodes semantic categories (e.g., “person”, “value”) and sociolinguistic metadata (e.g., age group, region). This representation enables systematic analysis of both linguistic structure and community behavior.

## Results  
The taxonomic mapping reveals that person‑related and evaluative tags constitute the majority of slang entries. Morphological analysis shows a high degree of innovation, with many compounds and neologisms. Participation data follow a power‑law distribution: only a few users generate the bulk of contributions, while most have brief active periods. The community confidence score correlates positively with user role (e.g., moderator vs. contributor) and interaction frequency, demonstrating that structured representations improve interpretability over raw tag strings.

## Significance  
This work provides a computational resource for non‑standard Greek that can be leveraged for sociolinguistic NLP tasks such as bias analysis and evaluation of informal language in large language models (LLMs). The taxonomy and confidence score framework also serve as a methodological template for handling noisy folksonomic data in other languages, advancing the study of informal language dynamics.

## Related Concepts  
- crowdsourced lexicon  
- folksonomics  
- multi‑layer taxonomy  
- community confidence score  
- sociolinguistics  
- morphological creativity  
- participation skew  
- NLP bias analysis
