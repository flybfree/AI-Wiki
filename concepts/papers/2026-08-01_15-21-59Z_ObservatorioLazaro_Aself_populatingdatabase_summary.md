# Summary: 2026-08-01_15-21-59Z_ObservatorioLazaro_Aself_populatingdatabaseofangli.md
Saved: 2026-08-03 21:28
Source: 2026-08-01_15-21-59Z_ObservatorioLazaro_Aself_populatingdatabaseofangli.md
Model: None

---

## Summary  
The paper introduces **Observatorio Lázaro**, a self‑populating database that monitors unassimilated English anglicisms in the Spanish digital press from April 2020 onward. It creates a continuously updated diachronic record of more than two million borrowings across 1.88 million articles and 993 million running tokens (2020‑2026). The system combines automated neural detection with manual audits to ensure high accuracy, delivering open access via API and a web interface. This resource complements static borrowing dictionaries by providing real‑time, large‑scale data on neological trends.

## Key Contributions  
- Detection pipeline achieves span‑level F1 = 0.86 on held‑out data.  
- Statistical analysis shows 58.7 % of anglicism types are unique (once‑attested), indicating a growing lexicon; after correcting for detection precision this rises to 53.6 %.  
- The anglicism frequency remains stable at roughly two per thousand tokens, with the highest density in fashion, technology and lifestyle sections.

## Methodology  
The authors built an end‑to‑end pipeline that acquires daily news texts from a collection of outlets covering 993 million running tokens, runs a neural sequence‑labeling model to label potential borrowings, post‑processes predictions for quality control, stores the results in a relational database, and exposes them through a public API and web interface. They also measured inter‑annotator agreement on the training corpus (Cohen’s κ = 0.91) and performed a manual precision audit of 1,000 spans to validate the automated detector.

## Results  
The detector’s held‑out performance is span‑level F1 = 0.86; inter‑annotator agreement is Cohen’s κ = 0.91; manual audit shows high alignment with predictions. Statistical analysis reveals a stable anglicism rate of about two per thousand tokens, highest in fashion, technology and lifestyle sections, lowest in political and institutional news.

## Significance  
This continuously updated database fills a gap in Spanish neology monitoring that static corpora cannot capture, offering researchers and lexicographers a living record of borrowing trends. It supports studies on language change, cultural influence, media linguistics, and the evolution of the Spanish lexicon over time.

## Related Concepts  
- Anglimism (unassimilated English borrowings)  
- Diachronic lexicon  
- Neural sequence labeling  
- Inter‑annotator agreement  
- Open lexical database  
- Neology monitoring observatory  
- Spanish press digital corpus
