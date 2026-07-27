# Summary: 2026-07-24_13-25-06Z_AnInsightonEvaluationMetricsUndertheImbalancedCase.md
Saved: 2026-07-26 21:50
Source: 2026-07-24_13-25-06Z_AnInsightonEvaluationMetricsUndertheImbalancedCase.md
Model: None

---

## Summary  
The paper investigates how common anomaly detection evaluation metrics—AUROC, AUPR, F1-score, and MCC—behave when the dataset exhibits severe class imbalance. It aims to provide a clear understanding of metric landscapes by visualizing relationships between metric values and true positive/negative rates across different anomaly ratios. By analysing these metric behaviours, the authors offer practical guidance for interpreting and comparing results on imbalanced data. Their contribution is a systematic study that reveals how metric stability varies with imbalance.  

## Key Contributions  
- The paper maps out the metric landscapes of AUROC, AUPR, F1-score, and MCC as functions of true positive rate (TPR) and false negative rate (FNR), revealing distinct preference zones for each metric.  
- It demonstrates that AUROC remains relatively insensitive to imbalance, while AUPR and F1-score become highly sensitive, especially at low anomaly densities.  
- The study provides a visual framework that helps practitioners select metrics appropriate to their specific anomaly ratio.  

## Methodology  
The authors construct synthetic datasets with controlled class imbalance ratios ranging from 95 % normal to 5 % anomalies. For each dataset they compute AUROC, AUPR, F1‑score, and MCC across multiple threshold settings and plot the metric values against TPR/FNR. The visualisations are generated using scatter plots where the x‑axis is TPR, the y‑axis is FNR, and colour indicates the anomaly ratio. This approach allows a unified view of how each metric behaves under varying imbalance.  

## Results  
The results show that AUROC’s curve stays close to the diagonal across all ratios, indicating balanced trade‑off between precision and recall. In contrast, AUPR exhibits a steep drop when anomalies are rare, making it misleading for low‑density cases. F1‑score collapses near zero when true positives are scarce, while MCC remains relatively stable but can be deceptive at extreme imbalances. The visual landscapes confirm that metric choice must align with the expected anomaly prevalence.  

## Significance  
Understanding these behaviours is crucial because practitioners often rely on a single metric without considering dataset imbalance, leading to misinterpretation of model performance. By offering clear visual insights and practical recommendations, this work enhances reproducibility and fairness in anomaly detection evaluation across diverse real‑world scenarios.  

## Related Concepts  
- Class imbalance  
- Anomaly detection  
- AUROC (Area Under the ROC Curve)  
- AUPR (Area Under the Precision‑Recall Curve)  
- F1‑score  
- MCC (Matthews Correlation Coefficient)  
- True Positive Rate (TPR) / False Negative Rate (FNR)
