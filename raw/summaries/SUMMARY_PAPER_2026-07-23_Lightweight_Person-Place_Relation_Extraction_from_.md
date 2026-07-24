---
title: Lightweight Person-Place Relation Extraction from Historical Newspapers with Dependency Graphs and Proximity Features
url: http://arxiv.org/abs/2607.19718v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_03-35-56Z_LightweightPerson_PlaceRelationExtractionfromHisto.md
generated_at: 2026-07-23 23:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a lightweight, interpretable system for extracting person-place relations from historical English, French, and German newspapers without relying on pretrained language models. By constructing document‑level dependency graphs and using proximity and part‑of‑speech features, the authors achieve a macro recall of 0.5142, ranking third in the Efficiency profile while remaining mid‑table in overall accuracy among 17 participants.

## Key Takeaways
- Minimum character distance alone captures most of the classification signal; adding further engineered features can sometimes degrade performance, indicating that argument distance dominates relation extraction.
- Document‑grouped cross‑validation is essential on this corpus because pair‑level splits inflate scores by 25–37 percentage points due to entity mentions recurring across documents, a data‑leakage effect removed by grouped validation.
- The best run reached a macro recall of 0.5142, placing third in the Efficiency profile and mid‑table on Accuracy among all competing teams.

## Context
This work addresses a growing need for efficient, model‑free extraction pipelines that can operate at scale on historical archives where computational resources are limited. It highlights how simple graph‑based representations combined with handcrafted features can still yield respectable performance without the overhead of large language models, underscoring the value of interpretability and parameter efficiency in AI research.

## Implications
For practitioners, the findings suggest that lightweight architectures and careful data handling can be viable alternatives to heavyweight pretrained models when dealing with long‑term textual corpora. The emphasis on document‑level validation also informs best practices for evaluating relation extraction tasks where entity mentions are not isolated across documents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19718v1)
