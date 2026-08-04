# Summary: 2026-08-02_15-12-58Z_AlphaG_OPD_Reliability_GatedSiblingCounterfactuals.md
Saved: 2026-08-04 00:12
Source: 2026-08-02_15-12-58Z_AlphaG_OPD_Reliability_GatedSiblingCounterfactuals.md
Model: None

---

## Summary  
The paper tackles the limitation of symbolic alpha factor discovery, which scores completed expressions but does not label the structural decisions that produced them. It proposes AlphaG‑OPD, a structural on‑policy distillation method that converts terminal factor evaluations into local action guidance for generating reliable sibling counterfactuals. The framework separates three decision components: (I) where to teach by exposing grammar‑valid siblings at partial AST states; (II) what is reliable enough to teach via KL‑bounded admission of sibling comparisons; and (III) how strongly and for how long to teach through bounded replay and forward‑gradient balancing without extra evaluations. This approach enables the on‑policy process to learn from the most trustworthy sibling actions while preserving the original factor pool and grammar rules.

## Key Contributions  
- [Finding 1] AlphaG‑OPD introduces a reliability‑gated sibling counterfactual mechanism that turns terminal factor scores into actionable teacher signals for on‑policy distillation.  
- [Finding 2] The method evaluates three siblings under four shared suffixes, admitting a target only when winner agreement exceeds a threshold and an empirical lower confidence bound is positive.  
- [Finding 3] It consolidates accepted targets via bounded replay, score‑indexed expiry, and forward‑gradient balancing, eliminating the need for additional factor evaluations.

## Methodology  
AlphaG‑OPD operates on three intertwined decisions. Component I identifies grammar‑valid sibling actions at intermediate abstract‑syntax‑tree (AST) nodes visited by the current forward policy. Component II assesses reliability by comparing these siblings across four suffix patterns, using a KL‑bounded target admission rule that requires sufficient winner agreement and a positive lower confidence bound. Component III governs consolidation: accepted targets are stored in a replay buffer with score‑indexed expiry, and their influence on the forward policy is balanced via forward gradients without re‑evaluating factors. The downstream components—terminal reward, trajectory balance, grammar rules, and factor‑pool constraints—remain unchanged.

## Results  
Across China’s CSI300, CSI500, CSI1000 indices and the U.S. S&P 500, AlphaG‑OPD achieved strong cross‑market performance on multiple random seeds, outperforming baseline methods that lack reliability gating or full consolidation. The equal‑physical‑score four‑arm ablation tests confirm that each component contributes uniquely to overall distillation quality.

## Significance  
By providing a reliable, local teacher signal derived from sibling counterfactuals, AlphaG‑OPD reduces the need for costly factor evaluations and improves the efficiency of on‑policy learning in symbolic alpha factor discovery. This makes large‑scale factor generation more scalable and adaptable to diverse financial markets.

## Related Concepts  
symbolic alpha factors, on‑policy distillation, generative flow networks (GFlowNets), sibling counterfactuals, KL‑bounded target admission, lower confidence bound (LCB), AST, replay buffer, forward‑gradient balancing.
