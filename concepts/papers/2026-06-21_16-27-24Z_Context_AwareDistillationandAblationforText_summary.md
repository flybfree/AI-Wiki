# Summary: 2026-06-21_16-27-24Z_Context_AwareDistillationandAblationforText2DSL.md
Saved: 2026-06-22 22:00
Source: 2026-06-21_16-27-24Z_Context_AwareDistillationandAblationforText2DSL.md
Model: None

---


## Summary  
The paper extends the Text2DSL project by replacing prompt‑only synthetic generation with a context‑aware distillation framework that leverages a teacher model (DeepSeek‑V4‑Flash) operating under an explicitly defined structured context consisting of a BNF grammar, an API specification, and a closed identifier vocabulary. This approach generates a verified PolkitBench corpus of 10,733 natural‑language‑to‑Polkit‑rule pairs with 100 % AST validity and 99.7 % runtime acceptance. The authors also perform a factorial ablation study on eight structured‑context conditions (C0–C7) to quantify the contribution of each component.  

## Key Contributions  
- Finding 1: The new, harder corpus collapses the baseline mode’s performance (syntax validity drops from 97.6 % to 58.5 %, combined score falls from 0.482 to 0.252) while only marginally degrading the context‑enhanced mode (syntax 98.6 % → 97.4 %, combined 0.801 → 0.750).  
- Finding 2: The full context C7 yields the best absolute results across all metrics, and the strongest partial conditions are C5 (BNF + Vocabulary) and C6 (API + Vocabulary), both of which include the vocabulary component.  
- Finding 3: A Shapley‑style decomposition shows the largest semantic‑quality effect comes from the vocabulary (+0.198), while the greatest structural‑validity effects are attributed to the API (+24.7 pp) and BNF (+22.3 pp).  

## Methodology  
The authors replace prompt‑only generation with context‑aware distillation: a teacher model (DeepSeek‑V4‑Flash) is prompted only with a structured context that includes a BNF grammar, an API specification, and a closed identifier vocabulary. The generated corpus undergoes two‑tier validation—first AST parsing via esprima to ensure syntactic correctness, then runtime acceptance through the production polkitd daemon and the pkcheck client—to guarantee 100 % AST validity and 99.7 % runtime pass rate. This pipeline scales the original PolkitBench set from 4,204 pairs to 10,733 verified examples.  

## Results  
Baseline mode performance deteriorates sharply when using the new corpus, indicating that context‑aware distillation is essential for reliable generation. The context‑enhanced mode shows only slight degradation, confirming that structured context provides a load‑bearing improvement rather than a superficial boost. Among the eight ablation conditions, full context C7 achieves the highest combined score (0.750), while partial conditions lacking the vocabulary perform worse. Shapley analysis quantifies component contributions: vocabulary adds 0.198 to the combined metric, API contributes +24.7 percentage points, and BNF contributes +22.3 pp.  

## Significance  
These findings demonstrate that structured context is a critical enabler of high‑quality Text2DSL generation, shifting the problem from mere prompt engineering to systematic component design. The ablation results provide quantitative guidance for future research on which structural elements are indispensable and how their omission impacts both syntax and semantics. By establishing a scalable verification pipeline and a reproducible ablation framework, the work advances reliable automatic DSL code generation and informs more robust model training strategies.  

## Related Concepts  
Text2DSL, context‑aware distillation, BNF grammar, API specification, closed identifier vocabulary, AST validation (esprima), runtime acceptance (polkitd daemon/pkcheck client), PolkitBench corpus, factorial ablation study, Shapley decomposition, semantic‑quality vs. structural‑validity metrics
