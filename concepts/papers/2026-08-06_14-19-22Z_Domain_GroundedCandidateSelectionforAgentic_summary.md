# Summary: 2026-08-06_14-19-22Z_Domain_GroundedCandidateSelectionforAgenticImageEd.md
Saved: 2026-08-06 20:45
Source: 2026-08-06_14-19-22Z_Domain_GroundedCandidateSelectionforAgenticImageEd.md
Model: None

---

## Summary  
The paper investigates whether commercial vision‑language models can replace low‑level physics‑informed vision for the challenging task of shadow removal, a problem where paired data are scarce and scene geometry matters. It shows that while direct use of such models yields plausible edits, they also introduce new failure modes like hallucinated objects or material misinterpretation. To address this, the authors propose an agentic candidate‑selection pipeline that grounds its reasoning in fundamental shadow formation physics. Their approach reduces cross‑domain distortion (CDD) by at least 47 % on a benchmark, demonstrating that classic low‑level priors remain useful for steering generation.

## Key Contributions  
- [Finding 1] Direct use of commercial generative editors can produce clean shadow‑free edits but often hallucinates scene content or misreads shadows as material.  
- [Finding 2] An agentic pipeline that samples, filters, and selects candidate edits guided by physics constraints yields higher quality and more consistent results.  
- [Finding 3] Prompting both the generator and evaluator to treat shadows solely as illumination occlusion—i.e., light occlusion caused by geometry—measurably improves CDD.

## Methodology  
The authors built a multi‑stage pipeline: first, the editor generates a guided probe that isolates shadow regions; second, an evaluator screens each candidate for major failures such as object hallucination or material misinterpretation; if failures are detected, the process retries with alternative prompts; third, multiple candidate edits are sampled and filtered using physics‑based constraints (e.g., preserving surface texture); finally, the best candidate that balances shadow removal with scene preservation is selected. This grounding in shadow formation—treating shadows as light occlusion rather than material or structural features—provides a reliable constraint for the selection process.

## Results  
On the ShadowRemovalRefine benchmark, the physics‑oriented pipeline achieves a CDD of 0.0075, which is at least a 47 % reduction compared to the strongest prior method. This improvement reflects lower distortion and higher consistency across edited images, confirming that the candidate‑selection strategy effectively mitigates the model’s hallucination tendencies.

## Significance  
These findings suggest that commercial vision‑language models are powerful but still benefit from physics‑informed low‑level priors; they do not replace such priors but rather complement them. The agentic selection pipeline shows how grounding generative tasks in domain knowledge can produce reliable, high‑quality outputs even when paired data are unavailable.

## Related Concepts  
- Vision‑language models  
- Generative editors  
- Candidate selection  
- Shadow removal  
- Cross‑domain distortion (CDD)  
- Scene preservation  
- Physics grounding  
- Illumination occlusion  
- Multimodal reasoning
