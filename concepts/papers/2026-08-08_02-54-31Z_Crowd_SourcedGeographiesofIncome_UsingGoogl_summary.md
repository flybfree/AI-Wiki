# Summary: 2026-08-08_02-54-31Z_Crowd_SourcedGeographiesofIncome_UsingGoogleMapsPo.md
Saved: 2026-08-10 22:45
Source: 2026-08-08_02-54-31Z_Crowd_SourcedGeographiesofIncome_UsingGoogleMapsPo.md
Model: None

---

## Summary  
The paper proposes a low‑cost, high‑frequency proxy for household income in São Paulo’s 26 625 census sectors by leveraging the composition of crowd‑sourced Google Maps Points of Interest (POIs). By extracting POI counts from a theoretically motivated set of categories and applying dimensionality‑reduction techniques such as PCA and non‑negative matrix factorization, the authors train regression models that predict census‑derived income. A spatial validation design is used to guard against data leakage, resulting in a best model with an R² of 0.65 on held‑out sectors. This work demonstrates that commercial geospatial data can complement costly decennial censuses during intercensal periods.

## Key Contributions  
- The crowd‑sourced POI composition can serve as a reliable proxy for sub‑municipal income with stable performance across feature methods.  
- NMF decomposition identifies specific POI types (e.g., commercial, residential) that carry the strongest income signal.  
- A spatial validation design reduces data leakage and yields robust R² estimates.

## Methodology  
The authors retrieve Google Places POI categories for each census sector in São Paulo and count the number of POIs belonging to each category, forming a high‑dimensional sparse matrix. Principal component analysis (PCA) is applied first to compress the dimensionality, followed by non‑negative matrix factorization (NMF) to extract interpretable latent factors that represent income‑related POI groups. Both feature‑extraction pipelines are used to train a sweep of gradient boosting regression models on census‑derived income values. Validation follows a leave‑one‑out spatial design: each sector is held out while all others are used for training, ensuring no leakage between test and training sets.

## Results  
The best performing model combines NMF with gradient boosting and achieves an R² of 0.65 on the held‑out validation set. Performance remains comparable across PCA and NMF feature extraction methods, indicating robustness to preprocessing choices. Interpretable NMF decompositions reveal that high‑variance POI types—particularly commercial establishments and residential clusters—dominate the income signal, confirming that certain POI categories are strong predictors of household wealth.

## Significance  
Providing accurate sub‑municipal income estimates without a decennial census is crucial for timely social policy interventions in middle‑income countries. This study fills the recent intercensal gap in São Paulo with a cheap, frequent data source and offers a template for other urban areas. The findings support multidimensional poverty assessments and align with capabilities‑based approaches that link economic resources to well‑being.

## Related Concepts  
- Sub‑municipal income estimation  
- Crowd‑sourced geospatial data  
- PCA/NMF dimensionality reduction  
- Spatial validation design  
- Multidimensional poverty measurement  
- Capabilities framework
