# Summary: 2026-07-23_05-30-45Z_ChemicalChain_of_ThoughtFunctionsasaHallucination_.md
Saved: 2026-07-24 02:31
Source: 2026-07-23_05-30-45Z_ChemicalChain_of_ThoughtFunctionsasaHallucination_.md
Model: None

---

## Summary  
The paper investigates why chain‑of‑thought (CoT) reasoning in chemical language models produces hallucinations, i.e., fabricated structural claims that are not present in the input molecules. It shows that these hallucinations are not merely artifacts of answer generation but stem from a shared scratchpad function across model families. By analyzing attribution and perturbing SMILES drafts, the authors reveal that CoT can be causally load‑bearing even when verbal statements are inert. Consequently, CoT should not be taken as evidence of faithful reasoning.

## Key Contributions  
- [Finding 1] The hallucination problem is widespread across four reasoning model families and twelve chemistry tasks, yet it remains largely independent of answer correctness.  
- [Finding 2] A shared scratchpad function exists in model‑specific forms: Chem‑R uses fragmented SMILES drafts, ether‑0 relies on structural sketches, and ChemDFM‑R emphasizes scaffold, positional, and naming cues.  
- [Finding 3] Perturbing the SMILES sketch in Chem‑R degrades generation, demonstrating that the draft is a load‑bearing component of the reasoning trace.

## Methodology  
The authors employed attribution analysis on model outputs to identify which linguistic components contribute to each answer. They also conducted controlled perturbations: replacing or removing fragments of the SMILES string in Chem‑R and ether‑0 models while keeping the verbal claim constant, then measured impact on final generation. This dual approach allowed them to separate hallucination from faithful reasoning.

## Results  
Experiments across twelve tasks revealed that correct answers frequently co‑occur with fabricated structural claims absent from any input molecule. Attribution studies showed that the scratchpad function is consistently activated regardless of answer accuracy. When SMILES drafts were altered, generation quality dropped sharply, indicating that these drafts are essential for model behavior even when the final claim is unchanged.

## Significance  
These findings challenge the assumption that CoT provides a faithful explanation of reasoning and highlight that hallucinations can arise from internal scratchpad mechanisms rather than answer errors. The paper advocates for process‑level supervision that monitors intermediate representations, not just final predictions, to improve reliability in chemical AI systems.

## Related Concepts  
- Chain-of-Thought (CoT) prompting  
- Hallucination in language models  
- Attribution analysis  
- SMILES string generation  
- Model‑specific scratchpad functions
