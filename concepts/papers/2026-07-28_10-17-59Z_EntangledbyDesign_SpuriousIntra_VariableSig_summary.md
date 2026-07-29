# Summary: 2026-07-28_10-17-59Z_EntangledbyDesign_SpuriousIntra_VariableSignalRout.md
Saved: 2026-07-28 22:42
Source: 2026-07-28_10-17-59Z_EntangledbyDesign_SpuriousIntra_VariableSignalRout.md
Model: None

---

## Summary  
The paper introduces spurious routing in tabular in‑context learners where a composite feature mixes the true health signal \(C\) with a systematic artefact \(S\) from hospital equipment, causing the model to route predictions through the artefact regardless of context size and leading to silent failures across hospitals. It proves that this routing is unavoidable for ridge ICL and derives a closed‑form characterisation \(\mathrm{CSR} \propto \rho_S/\rho_C\), empirically observed in TabPFN at \(r=0.979\). The authors also propose two lightweight mitigations—environment‑stratified context construction and S‑swap augmentation—that reduce spurious routing by up to 98.8 % for TabPFN without requiring causal labels.

## Key Contributions  
- Spurious intra‑variable signal routing is unavoidable for ridge ICL regardless of context size.  
- A closed‑form CSR \(\mathrm{CSR} = \rho_S/\rho_C\) quantifies the phenomenon, with empirical values 0.997 (linear ICL) and 0.979 (TabPFN).  
- Environment‑stratified context construction and S‑swap augmentation mitigate spurious routing by up to 98.8 % for TabPFN while increasing causal sensitivity eightfold.

## Methodology  
The authors formalise the composite representation \(X = [C; \alpha S; \eta]\) where \(C\) is the causal health signal, \(\alpha S\) is a hospital‑specific artefact correlated with outcomes through unmeasured confounders such as demographics, and \(\eta\) is noise. They analyse ridge ICL as a linear in‑context learner, showing that because the model cannot disentangle the distinct subspaces of \(C\) and \(S\), it will route predictions toward the spurious signal. Experiments compare this theory against synthetic tabular data simulating hospital artefacts and evaluate both linear ICL and TabPFN.

## Results  
Theoretical CSR values are confirmed: 0.997 for ridge ICL and 0.979 for TabPFN, indicating near‑certainty that the artefact drives predictions. Larger context amplifies spurious routing up to \(1.74\times\) in the high‑spurious corner, where expressive models show a \(+2.22\) CSR gap relative to linear ICL. S‑swap augmentation reduces spurious routing by 74 % (linear) and 98.8 % (TabPFN), while causal sensitivity increases eightfold.

## Significance  
This work reveals a critical flaw in tabular ICLs that can cause silent failures when deployed across environments, highlighting the need for robust signal routing safeguards. The proposed mitigations are lightweight, require only weak environment labels, and do not necessitate knowledge of the causal partition, offering practical solutions to improve reliability without sacrificing performance.

## Related Concepts  
- In‑context learning (ICL)  
- Ridge regression  
- Composite representations  
- Spurious routing  
- Environment‑stratified context construction  
- S‑swap augmentation  
- Causal sensitivity
