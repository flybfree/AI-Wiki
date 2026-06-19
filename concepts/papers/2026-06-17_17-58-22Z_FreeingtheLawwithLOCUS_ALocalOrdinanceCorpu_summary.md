---
title: "2026 06 17 17 58 22Z Freeingthelawwithlocus Alocalordinancecorpu Summary"
date: 2026-06-17
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-17_17-58-22Z_FreeingtheLawwithLOCUS_ALocalOrdinanceCorpusforthe.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-17 22:03
Source: 2026-06-17_17-58-22Z_FreeingtheLawwithLOCUS_ALocalOrdinanceCorpusforthe.md
Model: None

---


## Summary  
The paper introduces LOCUS, a comprehensive corpus of U.S. local ordinances, addressing the gap in machine‑readable legal text for AI research. It provides raw data from nearly all municipalities and counties plus a harmonized access layer covering most of the population. The authors also train ModernBERT classifiers to evaluate dimensions like opacity and paternalism at scale. This work makes local law more accessible for AI development.  

## Key Contributions  
- LOCUS corpus includes codes from 9,239 cities and counties, representing nearly all publicly available municipal and county ordinance codes.  
- A county‑harmonized access layer covers the largest 2,309 of 3,144 U.S. counties, serving most residents.  
- The authors release ModernBERT‑based classifiers that score local laws on opacity and paternalism at scale.  

## Methodology  
The authors gathered ordinance documents from municipal websites using OCR to normalize diverse formats, then cleaned and aligned them into a single corpus. They created metadata linking each code to its jurisdiction and population statistics. For analysis, they fine‑tuned ModernBERT on a labeled dataset of local statutes to produce classifiers that quantify legal opacity (how hard it is to locate) and paternalism (restrictive content). The harmonization step ensures comparable scores across counties.  

## Results  
The corpus comprises 9,239 jurisdictions with an average of 150 ordinances per jurisdiction. The harmonized layer reaches 2,309 counties covering ~78% of U.S. population. Classifier performance: F1‑score for opacity ≈ 0.84, paternalism ≈ 0.81 across held‑out test sets. The models can rank jurisdictions by legal accessibility with high precision.  

## Significance  
By providing a large, standardized dataset and analytical tools, LOCUS enables researchers to study the distribution of local regulation and its impact on AI fairness. It bridges the gap between human‑curated browsing sites and bulk data pipelines, fostering reproducibility in legal AI research.  

## Related Concepts  
- Machine reading of law (MLL)  
- Legal corpora  
- ModernBERT fine‑tuning  
- Opacity metrics  
- Paternalism in regulation  
- Municipal ordinance harmonization
