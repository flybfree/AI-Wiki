# Summary: 2026-07-24_14-51-28Z_Interiorinterpretabilitywithattentionrollout_contr.md
Saved: 2026-07-26 21:52
Source: 2026-07-24_14-51-28Z_Interiorinterpretabilitywithattentionrollout_contr.md
Model: None

---

## Summary  
The paper proposes interior interpretability, a propagation‑based view of how features interact inside Transformers, and applies it to attention rollout as a stochastic operator. It leverages Dobrushin contraction theory to reveal that rollouts with small Dobrushin coefficients behave like rank‑one matrices driven by normalized column sums, yielding interpretable propagation profiles. The study demonstrates that these profiles grow stronger with model depth in a metabolomic age prediction task and differ between trained versus randomly initialized models. While the method highlights attention‑mediated feature propagation, it is not intended as a causal attribution framework.  

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A rollout operator with a small Dobrushin coefficient is quantitatively close to a rank‑one stochastic matrix whose common row equals its normalized column sums.  
- [Finding 2] The contraction strength of attention rollouts increases with the depth of Transformers in the metabolomic age prediction experiment.  
- [Finding 3] Trained and randomly initialized models exhibit distinct propagation profiles, indicating that initialization influences feature interaction dynamics.  

## Methodology  
The authors treat attention rollout as a row‑stochastic matrix encoding how each token’s representation propagates to subsequent layers. By computing the Dobrushin coefficient—a measure of contraction— they assess how much information is lost across layers. Classical Dobrushin theory provides bounds on the distance between stochastic matrices, allowing them to approximate the rollout by a rank‑one matrix and extract its normalized column sums as a structural descriptor.  

## Results  
Theoretical analysis shows that small Dobrushin coefficients imply near‑rank‑one behavior, which simplifies interpretation. Experimentally, models trained for age prediction show increasing Dobrushin contraction with depth, confirming the theoretical link. Random initialization yields flatter profiles, suggesting alternative propagation pathways. Comparisons with PCA and GradientExplainer approximations to SHAP reveal that only highly ranked variables align locally; global rankings diverge, underscoring the diagnostic rather than causal nature of attention rollout.  

## Significance  
Interior interpretability bridges feature attribution and model architecture, offering a quantitative way to diagnose how attention mechanisms propagate information. The Dobrushin‑based analysis provides a novel theoretical tool for evaluating non‑linear stochastic operators in deep networks, which could guide more robust and interpretable model design.  

## Related Concepts  
- Attention rollout (row‑stochastic operator)  
- Dobrushin contraction theory  
- Rank‑one approximation  
- Feature propagation profiles  
- Stochastic matrix analysis  
- SHAP approximations
