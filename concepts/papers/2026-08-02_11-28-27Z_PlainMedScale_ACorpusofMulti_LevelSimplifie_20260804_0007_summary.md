# Summary: 2026-08-02_11-28-27Z_PlainMedScale_ACorpusofMulti_LevelSimplifiedMedica.md
Saved: 2026-08-04 00:07
Source: 2026-08-02_11-28-27Z_PlainMedScale_ACorpusofMulti_LevelSimplifiedMedica.md
Model: None

---

## Summary  
PlainMedScale is a newly created corpus that provides medical texts in German and English at four distinct levels of simplicity, ranging from professional reference material to lay‑person access information. The authors move beyond the conventional expert‑lay dichotomy by mapping each tier onto specific communicative functions: reference, explanation, decision support, and access. Their pilot studies reveal that existing readability metrics calibrated on binary registers do not reliably capture the full gradient of comprehension across all four levels. Moreover, they demonstrate that even state‑of‑the‑art open‑weight large language models prompted to generate plain language still retain noticeable difficulty from their source texts.

## Key Contributions  
- [Finding 1] The corpus spans four comprehensibility tiers in both German and English, each aligned with a distinct medical communicative purpose.  
- [Finding 2] Readability metrics developed for prior binary expert‑lay corpora fail to generalize across the full gradient of PlainMedScale’s levels.  
- [Finding 3] A current open‑weight LLM prompted for plain language still partially preserves the original difficulty of its input, indicating that simplification is not fully automatic.

## Methodology  
The authors assembled texts from four sources: MSD (professional and consumer), Gesund.Bund, Apotheken Umschau Einfache Sprache, and the NHS. These were categorized into four tiers—reference, explanation, decision support, and access—based on their intended audience and cognitive load. To evaluate the corpus’s impact, they conducted two pilot studies that aligned source texts with model‑generated plain language outputs. Readability metrics such as Flesch‑Kincaid and Gunning Fog were computed for both original and generated texts, while qualitative assessments measured perceived difficulty.

## Results  
The experiments show a non‑linear relationship between text level and readability scores; metrics optimized for the highest (professional) tier underestimate difficulty at lower tiers. Conversely, the LLM’s output retains higher complexity than its source, suggesting that plain‑language generation does not fully neutralize original technical content. These findings confirm that current evaluation tools are insufficient for assessing multi‑level simplification.

## Significance  
This work provides a nuanced resource for researchers studying medical communication, cognitive load reduction, and language modeling. By exposing the limitations of binary readability assessments and revealing persistent difficulty in AI‑generated plain text, it guides more accurate design of educational and patient‑facing health information systems.

## Related Concepts  
Plain Language, Readability Metrics (Flesch‑Kincaid, Gunning Fog), Multimodal Text Alignment, Large Language Models (LLMs), Cognitive Load Theory, Medical Communication, Corpus Construction, Open‑Weight AI.
