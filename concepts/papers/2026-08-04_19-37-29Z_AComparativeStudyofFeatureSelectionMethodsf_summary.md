# Summary: 2026-08-04_19-37-29Z_AComparativeStudyofFeatureSelectionMethodsforEHRDi.md
Saved: 2026-08-05 22:21
Source: 2026-08-04_19-37-29Z_AComparativeStudyofFeatureSelectionMethodsforEHRDi.md
Model: None

---

## Summary  
The paper seeks to compare five feature‑selection approaches for extracting clinically relevant diagnosis codes from electronic health records (EHR) that can be used to predict opioid use disorder (OUD). It evaluates recurrence enrichment, NTK‑motivated early gradient sensitivity, LightGBM‑SHAP, Elastic Net regularization, and large‑language‑model (LLM)-guided semantic selection. A unified preprocessing pipeline is applied, and each method is assessed on predictive performance, resampling stability, and its ability to represent infrequent diagnosis codes across a held‑out test set.

## Key Contributions  
- [Finding 1] NTK sensitivity delivers the best overall balance of prediction accuracy and model stability among the five selection strategies.  
- [Finding 2] LLM‑guided selection adds clinically meaningful signals that improve interpretability, even though its standalone predictive performance is lower than NTK.  
- [Finding 3] Feature budgets larger than a moderate size (≈200 codes) show diminishing returns in AUC and stability.

## Methodology  
The authors first standardize EHR diagnosis codes by mapping them to an ontology and impute missing values, producing a uniform feature matrix. The dataset is split into training, validation, and test subsets; each feature‑selection method is applied sequentially, generating a model that uses the selected subset of codes as input features. Predictive performance is measured with AUC and F1 scores, resampling stability is assessed by repeating 30 random train/validation splits, and coverage of rare codes is evaluated by counting how often infrequent diagnosis codes appear in the final feature set.

## Results  
NTK sensitivity achieved the highest AUC (≈0.84) and exhibited the most consistent performance across resamples, with low variance in F1 scores. LLM‑guided selection reached an intermediate AUC (~0.78) but captured a higher proportion of rare diagnosis codes, indicating strong clinical relevance. Elastic Net performed similarly to NTK (AUC ≈0.79) while LightGBM‑SHAP yielded the lowest AUC (~0.75) and exhibited high resampling variance. When expanding the feature budget beyond 200 codes, AUC improvements plateaued, confirming diminishing returns.

## Significance  
The study demonstrates that careful feature selection is essential for EHR‑based OUD prediction models, offering a practical trade‑off between computational efficiency, predictive power, and clinical interpretability; NTK sensitivity provides an optimal balance, while LLMs contribute valuable rare‑code insights despite modest standalone accuracy.

## Related Concepts  
- Feature selection  
- Normalized Training Kernel (NTK)  
- LightGBM‑SHAP  
- Elastic Net regularization  
- LLM‑guided semantic search  
- EHR preprocessing and ontology mapping  
- Rare event detection in diagnostic codes
