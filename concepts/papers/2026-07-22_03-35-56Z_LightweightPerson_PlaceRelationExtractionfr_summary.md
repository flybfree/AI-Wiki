# Summary: 2026-07-22_03-35-56Z_LightweightPerson_PlaceRelationExtractionfromHisto.md
Saved: 2026-07-24 01:25
Source: 2026-07-22_03-35-56Z_LightweightPerson_PlaceRelationExtractionfromHisto.md
Model: None

---

## Summary  
The paper tackles the HIPE‑2026 shared task of extracting person‑place relations from multilingual historical newspapers without relying on large pretrained language models. It proposes a lightweight, interpretable system that leverages dependency parses to create document‑level graphs and combines proximity‑based and part‑of‑speech features for classification with tiny scikit‑learn ensembles or compact Graph Attention Networks, keeping the model under 847 K parameters. The approach achieves a macro recall of 0.5142 on the official test set, ranking third in the Efficiency profile while performing mid‑table on Accuracy among all participants.

## Key Contributions  
- [Finding 1] Minimum character distance alone captures most of the classification signal; adding further engineered features often yields inconsistent gains or even degrades performance, confirming that argument (character) distance dominates relation extraction.  
- [Finding 2] Document‑grouped cross‑validation is essential on this corpus because pair‑level splits inflate scores by 25–37 percentage points due to entity mentions recurring across documents, a data‑leakage effect removed by proper grouping.  
- [Finding 3] A lightweight model under 847 K parameters can reach respectable performance (macro recall ≈0.51) without any pretrained language model, demonstrating that small, interpretable systems are viable for historical newspaper NLP tasks.

## Methodology  
The authors construct a document‑level graph from the dependency parses of each newspaper article. For every candidate person‑place pair they extract two types of features: (i) proximity information measured by minimum character distance between the mentions, and (ii) part‑of‑speech tags of the surrounding tokens. These features are fed to either a small ensemble of scikit‑learn classifiers or a compact Graph Attention Network that operates on the graph structure. The entire pipeline is designed to stay under 847 K parameters, ensuring lightweight inference suitable for large archival collections.

## Results  
On Test A (the official newspaper test set) the best run achieved a macro recall of 0.5142, placing third in the Efficiency profile and mid‑table on Accuracy among the 17 competing teams at HIPE‑2026. The results indicate that the proposed feature engineering and lightweight classification can produce reliable outputs despite the absence of large language models.

## Significance  
This work shows that for historical newspaper person‑place extraction, a minimal set of engineered features—particularly character distance—can drive strong performance, while proper cross‑validation mitigates data leakage. It also proves that small, interpretable models are capable of delivering respectable results without the computational burden of massive pretrained language models, encouraging more efficient NLP pipelines for archival data.

## Related Concepts  
person‑place relation extraction, dependency graphs, proximity features, graph attention networks (GAT), historical newspaper NLP, data leakage, cross‑validation, lightweight machine learning, scikit‑learn ensembles.
