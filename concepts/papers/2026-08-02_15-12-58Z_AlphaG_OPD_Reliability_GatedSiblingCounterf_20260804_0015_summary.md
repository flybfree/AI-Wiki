# Summary: 2026-08-02_15-12-58Z_AlphaG_OPD_Reliability_GatedSiblingCounterfactuals.md
Saved: 2026-08-04 00:15
Source: 2026-08-02_15-12-58Z_AlphaG_OPD_Reliability_GatedSiblingCounterfactuals.md
Model: None

---

## Summary  
AlphaG‑OPD (Reliability‑Gated Sibling Counterfactuals for On‑Policy Distillation in Symbolic Alpha Factor Discovery) tackles a core limitation of symbolic alpha factor discovery: the model scores completed expressions but does not label the structural decisions that generated them. The authors propose an on‑policy distillation framework that converts terminal factor evaluations into local guidance, thereby preserving the diversity and reward proportionality of generative flow networks while addressing sibling actions at intermediate AST states. By separating three distinct decision components—teaching location, reliability gating, and consolidation—the method learns to teach only when sibling comparisons exhibit strong agreement and a positive lower confidence bound, without requiring additional factor evaluations.

## Key Contributions  
- [Finding 1] AlphaG‑OPD introduces a three‑decision structural on‑policy distillation framework that turns terminal factor scores into actionable local guidance for symbolic alpha factor discovery.  
- [Finding 2] The reliability gate evaluates three sibling actions under four shared suffixes, accepting only KL‑bounded targets when winner agreement is high and an empirical lower confidence bound (LCB) remains positive.  
- [Finding 3] Consolidation is achieved through bounded replay, score‑index expiry, and forward‑gradient balancing, allowing the method to retain accepted targets without extra factor evaluations.

## Methodology  
The authors separate three decisions: Component I identifies grammar‑valid sibling actions at partial AST states visited by the current forward policy; Component II applies a reliability gate that checks winner agreement across siblings under four shared suffixes and ensures a positive LCB before admitting a target; Component III consolidates accepted targets using bounded replay, score‑index expiry, and forward‑gradient balancing. Terminal reward, trajectory balance, grammar rules, and factor‑pool constraints remain unchanged. The framework operates entirely within the existing on‑policy distillation pipeline, leveraging sibling counterfactuals to guide structural learning.

## Results  
Across China’s CSI300, CSI500, CSI1000 indices and the U.S. S&P 500, AlphaG‑OPD delivers strong cross‑market performance on multiple random seeds. A four‑arm equal‑physical‑score ablation tests each component: removing teaching location weakens performance; disabling reliability gating reduces robustness; eliminating consolidation hurts long‑term stability. The full method outperforms baseline GFlowNets in both absolute and relative metrics.

## Significance  
AlphaG‑OPD advances on‑policy distillation by making factor learning reliable, context‑aware, and computationally efficient. By gating sibling counterfactuals with a formal reliability criterion, the method reduces unnecessary factor evaluations while preserving gradient information, leading to more stable and generalizable symbolic alpha factors across diverse financial markets.

## Related Concepts  
- On‑policy distillation  
- Symbolic alpha factor discovery  
- Generative flow networks (GFlowNets)  
- Sibling counterfactuals at intermediate AST states  
- KL‑bounded target acceptance  
- Lower confidence bound (LCB) for reliability gating  
- Bounded replay and score‑index expiry  
- Forward‑gradient balancing
