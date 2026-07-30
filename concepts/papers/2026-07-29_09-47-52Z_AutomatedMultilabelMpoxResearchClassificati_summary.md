# Summary: 2026-07-29_09-47-52Z_AutomatedMultilabelMpoxResearchClassificationwithE.md
Saved: 2026-07-29 20:31
Source: 2026-07-29_09-47-52Z_AutomatedMultilabelMpoxResearchClassificationwithE.md
Model: None

---

## Summary  
This paper proposes an automated multilabel classification system for Mpox research articles to categorize them into topics such as outbreaks, vaccination, and epidemiology. It evaluates transformer‑based models, particularly BERT, achieving high accuracy scores across micro and macro F1 metrics. The study also integrates SHAP analysis to provide explainable insights into model decisions. By automating this classification, the approach enables rapid information retrieval for researchers, policymakers, and healthcare workers.  

## Key Contributions  
- [Finding 1] BERT achieves 97.05% accuracy, 97.67% micro F1 score, and 96.46% macro F1 score on the dataset of 14,590 Mpox research articles.  
- [Finding 2] SHAP analysis identifies significant word features that drive classification decisions, enhancing model interpretability.  
- [Finding 3] The multilabel framework successfully groups articles into multiple relevant topics simultaneously.  

## Methodology  
The authors approached the problem by constructing a labeled dataset of 14,590 Mpox research papers, each annotated with multiple labels representing outbreak reports, vaccination studies, and epidemiological analyses. They selected transformer models, focusing on BERT as the baseline, and compared it against other classifiers. For interpretability, they applied SHAP (SHapley Additive exPlanations) to compute feature importance across the model’s attention weights.  

## Results  
The experimental results demonstrate that BERT outperforms alternative models in both accuracy and F1 scores, confirming its suitability for multilabel classification tasks involving complex textual data. The SHAP analysis reveals that key lexical patterns related to outbreak terminology, vaccine names, and epidemiological metrics dominate the explanation space, providing transparent justification for predictions.  

## Significance  
This work matters because it streamlines the massive volume of Mpox research literature, allowing stakeholders to quickly locate pertinent studies without manual sifting. By combining high‑performing AI with explainable reasoning, the system supports evidence‑based decision making in public health planning and resource allocation.  

## Related Concepts  
- Multilabel classification  
- Transformer models (BERT)  
- Explainable AI (SHAP)  
- Public health information retrieval  
- Outbreak monitoring
