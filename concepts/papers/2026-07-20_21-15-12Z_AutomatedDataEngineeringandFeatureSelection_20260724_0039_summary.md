# Summary: 2026-07-20_21-15-12Z_AutomatedDataEngineeringandFeatureSelectionfortheC.md
Saved: 2026-07-24 00:39
Source: 2026-07-20_21-15-12Z_AutomatedDataEngineeringandFeatureSelectionfortheC.md
Model: None

---

## Summary  
This paper proposes an Automated Data Processing (ADP) framework that automatically selects machine‑learning models and feature subsets to predict warpage in fused deposition modeling (FDM). The framework combines reinforcement‑learning‑inspired policy updates with SHAP‑based Explainable AI to evaluate model‑feature pairs across 217 FDM datasets, converging on configurations that maximize predictive accuracy while maintaining stability. By reducing dimensionality through feature importance scores and iteratively updating a Q‑value table, the method achieves higher test‑set AUC (0.9731 vs. baseline 0.9248) and more than a 50 % increase in mean reward compared with using all features. The contribution lies in integrating XAI for feature selection within an RL‑driven optimization loop, offering a scalable pipeline for similar industrial prediction tasks.

## Key Contributions  
- [Finding 1] The ADP framework automatically generates optimal model‑feature combinations by iteratively updating Q‑values guided by SHAP importance scores.  
- [Finding 2] Integration of reinforcement learning with XAI yields a policy that converges to configurations with significantly higher AUC and reward than the full‑feature baseline.  
- [Finding 3] The method reduces dimensionality while preserving predictive performance, enabling faster training and deployment in real‑time FDM monitoring.

## Methodology  
The authors built an episodic reinforcement‑learning loop where each episode trains multiple ML models on both complete feature sets and SHAP‑selected subsets. For every model‑feature pair they compute test AUC and F1‑score, derive a scalar reward, and update Q‑values to prioritize higher‑performing configurations in subsequent episodes. Feature importance from SHAP is used to prune irrelevant variables, producing reduced yet informative datasets that the policy explores. The process repeats across 217 FDM warpage datasets, allowing the system to explore a vast search space efficiently.

## Results  
Experimental results show that the ADP framework improves test‑set AUC from 0.9248 (full features) to 0.9731 after convergence. Mean reward values increase by over fifty percent relative to the baseline full‑feature configuration, indicating both higher accuracy and more stable performance across episodes. The reduction in feature set size is typically modest, preserving most predictive power while cutting computational load.

## Significance  
This work demonstrates that automated data engineering combined with explainable AI can systematically discover superior model‑feature pipelines for industrial prediction problems. By replacing manual feature engineering with a learned policy, manufacturers can obtain more reliable warpage predictions faster, supporting real‑time quality control and reducing scrap rates in FDM printing.

## Related Concepts  
- Reinforcement learning (RL)  
- Explainable AI (XAI) / SHAP  
- Feature selection  
- Q‑learning  
- Fused deposition modeling (FDM) warpage detection
