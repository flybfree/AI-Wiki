# Summary: 2026-07-22_03-35-56Z_LightweightPerson_PlaceRelationExtractionfromHisto.md
Saved: 2026-07-24 01:32
Source: 2026-07-22_03-35-56Z_LightweightPerson_PlaceRelationExtractionfromHisto.md
Model: None

---

## Summary  
The paper tackles person‑place relation extraction from multilingual historical newspapers without relying on pretrained language models, aiming for a lightweight, interpretable solution that can process archives at scale. It constructs a document‑level dependency graph, extracts proximity‑based and part‑of‑speech features for each entity pair, and classifies the pairs using small scikit‑learn ensembles or compact Graph Attention Networks while keeping the total parameter count under 847 K. On the official HIPE‑2026 Test A set, their best run achieved a macro recall of 0.5142, ranking third in the Efficiency profile and placing mid‑table on Accuracy among all teams. The work also highlights that character distance alone captures most of the classification signal, with additional engineered features sometimes degrading performance.

## Key Contributions  
- Finding 1: Minimum character distance alone captures most of the classification signal; adding further engineered features yields inconsistent gains and can even degrade performance.  
- Finding 2: Document‑grouped cross‑validation is essential on this corpus because pair‑level splits inflate scores by 25–37 percentage points due to entity mentions recurring across documents, a data‑leakage effect that grouped CV removes.  
- Finding 3: Their lightweight pipeline (dependency graph + proximity/POS features) can reach high recall while staying under the 847 K parameter budget.

## Methodology  
The authors parse English, French, and German newspaper articles to build a document‑level dependency graph. From each parse they generate all possible person–place entity pairs and compute two feature types per pair: (i) the minimum character distance between the mentions, and (ii) part‑of‑speech tags of surrounding tokens. These features are fed into either a small scikit‑learn ensemble classifier or a compact Graph Attention Network (GAT) whose total parameter count is capped at 847 K. The system is evaluated using grouped cross‑validation to prevent leakage from repeated mentions across documents.

## Results  
Their best run achieved a macro recall of 0.5142 and an F1 score around 0.49 on the Test A set. It ranked third in the Efficiency profile among the 17 participating teams, indicating solid performance relative to other approaches while still being mid‑table on overall Accuracy. The model’s inference time is low because it relies on lightweight classifiers and a small GAT architecture.

## Significance  
This work proves that interpretable, model‑free methods can deliver respectable results for person‑place extraction in historical archives where pretrained language models are impractical to deploy at scale. It also clarifies that character distance dominates the signal and stresses the importance of proper cross‑document evaluation to avoid artificial score inflation.

## Related Concepts  
Person‑place relations, dependency graphs, proximity features, part‑of‑speech features, scikit‑learn ensembles, Graph Attention Networks (GAT), HIPE‑2026 shared task, cross‑document evaluation, data leakage.
