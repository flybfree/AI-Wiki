# Summary: 2026-07-23_05-30-45Z_ChemicalChain_of_ThoughtFunctionsasaHallucination_.md
Saved: 2026-07-24 02:40
Source: 2026-07-23_05-30-45Z_ChemicalChain_of_ThoughtFunctionsasaHallucination_.md
Model: None

---

## Summary  
The paper investigates the reliability of chain‑of‑thought (CoT) reasoning in chemical language models and demonstrates that hallucinations are pervasive across four model families and twelve chemistry tasks, even when the final answer is correct. It argues that these hallucinated structural claims arise from a shared “scratchpad” function expressed differently in each model—fragmented SMILES drafts in Chem‑R and ether‑0 versus scaffold, positional, and naming cues in ChemDFM‑R. By showing that perturbing the sketch degrades generation, the authors reveal that these drafts are causally load‑bearing even when the verbal claims remain inert. Consequently, CoT is not a faithful explanation nor merely a post‑hoc rationalization but a hallucination‑prone molecular scratchpad.

## Key Contributions  
- [Finding 1] Hallucinations in chemical CoT are widespread and largely independent of answer correctness; correct answers often coexist with fabricated structural claims.  
- [Finding 2] A shared “scratchpad” function exists across model families, manifesting as SMILES drafts (Chem‑R, ether‑0) or scaffold cues (ChemDFM‑R).  
- [Finding 3] Perturbing the SMILES sketch reduces generation quality, indicating that structural drafts are causally load‑bearing even when verbal claims are largely inert.  

## Methodology  
The authors performed attribution analyses on four reasoning model families and twelve chemistry tasks to compare the relationship between generated answers, verbal structural claims, and the underlying SMILES representations. They also introduced controlled perturbations of the sketch (e.g., inserting or deleting fragments) to test whether changes in the draft affect generation output. This dual‑approach—semantic attribution combined with causal manipulation—allowed them to isolate the role of the scratchpad function.

## Results  
Attribution experiments revealed that correct answers frequently accompany fabricated structural claims absent from the relevant molecules, indicating a decoupling between answer correctness and hallucination. The analysis identified three distinct forms of the scratchpad: (1) Chem‑R and ether‑0 rely on fragmented SMILES drafts; (2) ChemDFM‑R emphasizes scaffold, positional, and naming cues. When the SMILES sketch was altered in Chem‑R or ether‑0, model output degraded markedly, confirming that the sketch is a load‑bearing component of generation despite the verbal claim being largely inert.

## Significance  
These findings challenge the assumption that CoT serves as direct evidence of faithful reasoning and highlight that process‑level phenomena—such as hallucination‑prone scratchpads—can persist even when outputs are numerically correct. The work motivates supervision mechanisms that monitor intermediate representations rather than relying solely on answer‑only evaluation, thereby improving robustness in chemical AI systems.

## Related Concepts  
- Chain‑of‑thought prompting  
- Hallucination (AI)  
- Chemical language modeling  
- SMILES representation  
- Scaffold cues and positional information  
- Attribution analysis  
- Causal load‑bearing structures
