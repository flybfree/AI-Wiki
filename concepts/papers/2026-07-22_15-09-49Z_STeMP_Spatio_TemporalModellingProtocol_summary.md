# Summary: 2026-07-22_15-09-49Z_STeMP_Spatio_TemporalModellingProtocol.md
Saved: 2026-07-24 02:02
Source: 2026-07-22_15-09-49Z_STeMP_Spatio_TemporalModellingProtocol.md
Model: None

---

## Summary  
The paper introduces **STeMP** (Spatio‑Temporal Modelling Protocol), a standardized reporting framework designed to address the lack of transparent guidelines for spatio‑temporal machine‑learning models in environmental research. By providing both metadata and detailed methodological guidance across three sections—Overview, Model & Prediction—the protocol aims to enhance trust, transparency, and comparability among model studies. The authors host the protocol on GitHub and deliver an R‑package that includes a web application capable of filling the report either manually or semi‑automatically from existing modelling objects.

## Key Contributions  
- STeMP provides a standardized reporting framework for spatio‑temporal ML models.  
- The protocol integrates both metadata and methodological guidance across its Overview and Model/Prediction sections.  
- An open‑source R package with a web interface enables manual or semi‑automated completion of the report, issuing warnings on common pitfalls.

## Methodology  
The authors began by analysing the existing literature to identify gaps in reproducibility and transparency for spatio‑temporal modelling. They then designed a three‑section protocol that separates high‑level metadata (Overview) from technical details (Model & Prediction). The design was implemented as an R package, with a companion web app that parses model objects, suggests parameter choices, and flags issues such as data leakage or inappropriate cross‑validation splits. Contributions are encouraged via GitHub to keep the protocol evolving.

## Results  
The STeMP protocol is publicly available at https://github.com/LOEK-RS/STeMP, containing a set of metadata fields (model type, predictors, software), detailed methodological sections, and an interactive web tool. When fed with typical modelling objects, the app generates a complete report and highlights potential pitfalls, demonstrating that the protocol can be applied to existing workflows without requiring extensive new code development.

## Significance  
STeMP matters because it bridges the gap between research output and practical application by ensuring that spatio‑temporal models are reported in a uniform, interpretable manner. Reviewers will have clearer criteria for assessing model quality, while authors can more easily communicate their work to interdisciplinary audiences. By reducing bias from ad‑hoc reporting choices, STeMP promotes reproducibility and trustworthiness across the environmental science community.

## Related Concepts  
- Spatio‑temporal modelling  
- Machine learning in environmental research  
- Model transparency and reproducibility  
- Standardisation of scientific protocols  
- R package development  
- GitHub contributions
