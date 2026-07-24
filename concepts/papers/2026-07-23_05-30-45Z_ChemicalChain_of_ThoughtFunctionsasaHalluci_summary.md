# Summary: 2026-07-23_05-30-45Z_ChemicalChain_of_ThoughtFunctionsasaHallucination_.md
Saved: 2026-07-24 02:31
Source: 2026-07-23_05-30-45Z_ChemicalChain_of_ThoughtFunctionsasaHallucination_.md
Model: None

---

## Summary  
The paper investigates why chain‑of‑thought (CoT) reasoning in chemical language models often produces hallucinated structural claims that are unrelated to the correct answer. It demonstrates that these hallucinations arise from a “scratchpad” function embedded within the model’s internal representations, which can be manipulated without affecting the final output. The authors conclude that CoT is neither a faithful explanation nor a mere rationalization but a hallucination‑prone scaffold that should not be trusted as evidence of correct reasoning.

## Key Contributions  
- [Finding 1] Hallucinations in chemical CoT are widespread across four model families and twelve tasks, yet they do not correlate with answer correctness.  
- [Finding 2] Attribution analyses reveal a shared scratchpad function: Chem‑R uses fragmented SMILES drafts, while ChemDFM‑R relies on scaffold, positional, and naming cues.  
- [Finding 3] Perturbing the SMILES sketches in Chem‑R degrades generation, indicating that structural drafts can be causally load‑bearing even when verbal claims are inert.

## Methodology  
The authors systematically examined model behavior by (1) collecting responses from four reasoning families on twelve chemistry tasks, (2) performing attribution studies to map which internal cues drive hallucinations, and (3) conducting controlled perturbations of SMILES drafts in Chem‑R to assess causal impact. This multi‑layered approach allowed them to separate the hallucination source from the final answer.

## Results  
Experiments showed that correct answers frequently coexist with fabricated structural statements absent from the molecules. Attribution tests identified distinct scratchpad mechanisms per model, and SMILES perturbations in Chem‑R reduced generation quality, confirming that drafts serve as load‑bearing components. Overall, hallucination rates remained high even when answer scores were perfect.

## Significance  
Treating CoT as direct evidence of faithful reasoning is misleading; the paper motivates process‑level supervision that monitors internal scratchpad states rather than relying solely on answer correctness. This insight can improve model reliability and guide future training objectives in chemical AI.

## Related Concepts  
- Chain-of-Thought (CoT) prompting  
- Hallucination in language models  
- Model attribution analysis  
- SMILES draft generation  
- Scaffold‑based reasoning
