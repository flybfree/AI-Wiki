# Summary: 2026-08-10_15-56-43Z_Cultivar_AContrastiveandLocale_OrientedTranslation.md
Saved: 2026-08-11 00:16
Source: 2026-08-10_15-56-43Z_Cultivar_AContrastiveandLocale_OrientedTranslation.md
Model: None

---

## Summary  
Cultivar is a new benchmark that treats translation evaluation as a source‑contrastive task, moving beyond the conventional English‑to‑target language pair paradigm. By creating a locale‑specific subset of FLORES and pairing each sentence with its unlocalized counterpart, the authors enable direct probing of data contamination and localisation robustness across 32 open‑weight models. The contrastive design reveals systematic weaknesses: some models overfit to the limited source material, while others perform poorly on non‑US locales. This work thus provides a more nuanced view of multilingual translation quality that accounts for cultural context.

## Key Contributions  
- [Finding 1] Source‑contrastive evaluation uncovers data contamination that accumulates over time in existing benchmarks.  
- [Finding 2] Models specialised for machine translation are less robust than generalist multilingual models, indicating a trade‑off between specialization and generalization.  
- [Finding 3] Translation quality is consistently higher for US‑origin content across languages, suggesting hidden locale bias that persists even when language pairs appear neutral.

## Methodology  
The authors constructed Cultivar by extracting a curated set of sentences from the FLORES dataset, translating them into each target language using locally appropriate resources, and then pairing every localized sentence with its unlocalized counterpart. Evaluation is performed through contrastive loss metrics that compare the model’s output to both versions, allowing a direct assessment of contamination (difference between localized and unlocalized scores) and localisation robustness (consistency across locales). The benchmark was applied to 32 open‑weight models, with performance measured on translation quality scores and robustness indicators.

## Results  
Experimental results show that MT‑specialised models exhibit the largest contamination gaps, indicating they rely heavily on memorising source pairs. A subset of generalist models overfit FLORES, producing inflated scores on localized data but poor generalization elsewhere. Crucially, all models translate US‑origin sentences more accurately than those from other locales, regardless of language pair, highlighting a persistent locale bias. The contrastive analysis quantifies contamination as up to 12 % lower for non‑US sources compared with US sources.

## Significance  
Cultivar challenges the assumption that translation benchmarks are culture‑neutral and provides empirical evidence of data contamination and localisation drift. By exposing these issues, it guides researchers toward more robust evaluation practices and model selection that respect cultural context, ultimately improving real‑world multilingual service quality.

## Related Concepts  
contrastive evaluation, locale‑specific benchmarking, data contamination, localisation robustness, multilingual translation models, FLORES dataset, open‑weight models.
