# Summary: 2026-08-02_03-05-54Z_Interpretablemachinelearningforpredictingsplitting.md
Saved: 2026-08-03 23:58
Source: 2026-08-02_03-05-54Z_Interpretablemachinelearningforpredictingsplitting.md
Model: None

---

## Summary  
The paper aims to develop an interpretable machine‑learning framework that predicts the splitting strength of asphalt concrete and supports data‑driven mixture design. It leverages SHAP analysis to explain model predictions and identify influential variables. A GUI platform integrates prediction with explanations for practical use. This work bridges predictive modeling and interpretability in pavement engineering.  

## Key Contributions  
- The study demonstrates that six machine‑learning models can predict splitting strength, with TabPFN achieving the best performance (RMSE 0.28, R² 0.88).  
- SHAP analysis reveals nine variables contribute to 92 % of average prediction error, highlighting Ag9.5, FT, Ag4.75, AC, and Du as dominant factors.  
- The framework provides quantitative favorable ranges for material parameters (e.g., Ag9.5 <66.8%, Ac <5.4 wt.%) that improve splitting strength.  

## Methodology  
A database of 296 asphalt samples was used; 14 variables were selected covering composition, gradation, and fiber properties. Six models—TabPFN, ANN, SVR, RF, XGBoost, LightGBM—were trained; hyperparameter optimization applied to five using NSGA‑II while TabPFN used default settings.  

## Results  
All models performed satisfactorily on the test set; TabPFN had lowest RMSE 0.28, MAE 0.21, MAPE 18.01 %, MAD 0.14, highest R² 0.88, composite score 0.91. SHAP analysis identified nine dominant variables accounting for 92 % of contribution.  

## Significance  
Providing interpretable predictions enables engineers to make informed mixture decisions and optimize pavement performance without extensive trial‑and‑error.  

## Related Concepts  
splitting strength, machine learning models, hyperparameter optimization, NSGA‑II, SHAP values, feature importance, GUI interface, asphalt concrete composition variables
