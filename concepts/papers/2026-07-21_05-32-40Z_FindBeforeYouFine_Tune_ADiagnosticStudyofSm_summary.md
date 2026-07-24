# Summary: 2026-07-21_05-32-40Z_FindBeforeYouFine_Tune_ADiagnosticStudyofSmallLLMs.md
Saved: 2026-07-24 00:31
Source: 2026-07-21_05-32-40Z_FindBeforeYouFine_Tune_ADiagnosticStudyofSmallLLMs.md
Model: None

---

## Summary  
The paper introduces **FiT (Find before Fine‑Tune)**, a diagnostic framework that evaluates small language models on three cybersecurity‑specific capabilities—vocabulary recognition, parametric knowledge, and contextualization of retrieved information—before applying fine‑tuning. By comparing two fine‑tuning regimes on five open‑weight 7‑billion‑parameter models, the authors demonstrate that fine‑tuning does not uniformly benefit these models; instead it can degrade vocabulary and parametric knowledge while leaving retrieval‑grounded contextualization relatively intact. The study shows that pre‑fine‑tuning FiT scores reliably predict the direction of post‑tuning change, offering a lightweight screening tool to avoid unnecessary adaptation.

## Key Contributions  
- [Finding 1] Fine‑tuning consistently degrades vocabulary recognition and parametric knowledge in small LLMs.  
- [Finding 2] Two fine‑tuning regimes (knowledge‑focused vs. instruction‑focused) produce distinct trade‑offs; the latter causes a rank inversion via induced abstention while contextualization remains stable.  
- [Finding 3] Pre‑fine‑tuning FiT scores anticipate the direction of post‑tuning change, enabling early detection of harmful adaptations.

## Methodology  
The authors define three task‑oriented capabilities required for cybersecurity QA: (1) vocabulary recognition, (2) parametric knowledge retrieval, and (3) contextualization of retrieved information. They select five open‑weight 7‑billion‑parameter models that are publicly available. For each model they compute FiT scores on the three capabilities before fine‑tuning, then apply either a knowledge‑focused or an instruction‑focused fine‑tuning regime. After tuning, they re‑evaluate the same three capabilities and calculate rank correlations between pre‑ and post‑tuning scores to quantify degradation magnitude.

## Results  
Knowledge‑focused tuning reduces parametric knowledge moderately while preserving the original ranking order. Instruction‑focused tuning, however, triggers a rise in abstention responses, causing the model’s rank to drop sharply despite unchanged retrieval‑grounded contextualization. Rank‑correlation analysis yields a strong positive correlation (r≈0.78) between pre‑FiT scores and the observed degradation direction, confirming that FiT can screen unsuitable models early.

## Significance  
This work provides a practical diagnostic that helps practitioners decide whether fine‑tuning is beneficial or harmful for small LLMs in cybersecurity QA pipelines. By avoiding unnecessary adaptation on models prone to knowledge loss, organizations can reduce hallucination risk and maintain efficiency when labeled data are scarce or rapidly evolving.

## Related Concepts  
Fine‑tuning, parametric knowledge, instruction following, hallucination, rank correlation, open‑weight LLMs, diagnostic frameworks, retrieval‑grounded contextualization, knowledge degradation.
