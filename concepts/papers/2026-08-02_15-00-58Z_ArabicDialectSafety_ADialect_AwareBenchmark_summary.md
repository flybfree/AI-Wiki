# Summary: 2026-08-02_15-00-58Z_ArabicDialectSafety_ADialect_AwareBenchmarkforArab.md
Saved: 2026-08-03 23:28
Source: 2026-08-02_15-00-58Z_ArabicDialectSafety_ADialect_AwareBenchmarkforArab.md
Model: None

---

## Summary  
ArabicDialectSafety introduces a human‑curated dataset of 25,071 Arabic prompts spanning six dialects (Modern Standard, Syrian, Egyptian, Algerian, Palestinian, Moroccan) annotated with dialect labels and seven fine‑grained harm categories. The work proposes a dual‑task evaluation framework that simultaneously performs binary safe/unsafe detection and granular harm classification across all dialects. By benchmarking both supervised models and frontier generative LLMs, the authors demonstrate that representation‑level dialect conditioning yields the best performance while still leaving low‑resource Maghrebi dialects under‑represented. The release of the dataset and code aims to standardize safety evaluation for Arabic content in multilingual settings.

## Key Contributions  
- [Finding 1] ArabicDialectSafety is a comprehensive, human‑annotated benchmark covering six Arabic varieties with seven fine‑grained harm categories.  
- [Finding 2] Fine‑tuned MARBERTv2 achieves the strongest results: Macro‑F1 = 0.95 for binary classification and 0.90 for granular classification, outperforming prompted frontier LLMs.  
- [Finding 3] Dialect conditioning at the representation level is most effective; however, performance gaps persist for low‑resource Maghrebi dialects.

## Methodology  
The authors curated a dataset of 25,071 prompts, each tagged with its dialect and one of seven harm categories. They introduced a dual‑task evaluation that runs binary safe/unsafe detection alongside fine‑grained classification across all dialects. The benchmark evaluates seven supervised models (including MARBERTv2) and seven generative LLMs, integrating dialect conditioning at the representation level to condition model outputs on dialectal cues.

## Results  
The best model attains Macro‑F1 scores of 0.95 for binary safety detection and 0.90 for granular harm classification. When frontier LLMs are prompted with harmful dialectal Arabic prompts, unsafe generation rates remain below 5 %. Nevertheless, the benchmark reveals significant performance disparities for low‑resource Maghrebi dialects, indicating that representation‑level conditioning does not fully close these gaps.

## Significance  
This work provides the first dialect‑aware Arabic safety benchmark, enabling fair and comparable evaluation across linguistic varieties. By exposing systematic weaknesses in low‑resource dialects, it guides future model development to reduce bias and improve safety for diverse Arabic speakers.

## Related Concepts  
- Dialect awareness  
- Fine‑grained harm classification  
- Representation‑level conditioning  
- Binary vs. granular classification  
- Supervised generative modeling  
- Arabic language safety
