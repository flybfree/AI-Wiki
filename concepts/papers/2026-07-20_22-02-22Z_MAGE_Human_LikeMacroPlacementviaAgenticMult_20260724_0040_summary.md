# Summary: 2026-07-20_22-02-22Z_MAGE_Human_LikeMacroPlacementviaAgenticMultimodalR.md
Saved: 2026-07-24 00:40
Source: 2026-07-20_22-02-22Z_MAGE_Human_LikeMacroPlacementviaAgenticMultimodalR.md
Model: None

---

## Summary  
MAGE (Macro Placement Agentic Engine) tackles the persistent need for human‑like macro placement in industrial floorplanning by introducing a multimodal multi‑agent framework that refines placements using natural‑language directives and validation criteria rather than data‑driven learning. The system decomposes the task into six phases, employs tournament refinement among candidate solutions, and quantifies human‑likeness through four metrics: notch score, whitespace score, pocket score, and alignment score. Experiments on NanGate45 and GlobalFoundries 12nm designs demonstrate geometric‑mean improvements of 11.1 %–19.3 % in WNS and 70.0 %–74.0 % in TNS over commercial macro placers, with human‑like gains up to 48 % over baselines.

## Key Contributions  
- MAGE introduces a six‑phase multimodal workflow that integrates expert floorplanning knowledge encoded via natural‑language directives.  
- It employs tournament‑style refinement among candidate macro placements, propagating feedback from higher‑quality solutions.  
- Four new metrics—notch score, whitespace score, pocket score, and alignment score—quantify human‑likeness beyond conventional PPA measures.

## Methodology  
The authors encode floorplanning rules and validation criteria in natural language, generate multiple placement candidates, evaluate them with the four human‑like metrics, run a tournament to select the best solutions as feedback, and iteratively refine until convergence. No training on labeled data is required; the process relies solely on structured expert knowledge.

## Results  
Across nine designs, MAGE improves WNS by 11.1 %–19.3 % geometric mean and TNS by 70.0 %–74.0 % compared to commercial macro placers; over the human‑expert baseline it gains 18.3 % in WNS and 72.5 % in TNS while keeping wirelength and power comparable. Human‑likeness scores improve by 6 %–48 % relative to all baselines.

## Significance  
By automating refinement using expert knowledge and providing interpretable metrics, MAGE reduces manual effort, enhances design quality, and offers a transferable framework for new placements without retraining.

## Related Concepts  
macro placement, multimodal reasoning, multi‑agent systems, human‑like design evaluation, floorplanning rules, tournament optimization, natural‑language directives, geometric mean improvement, TNS/WNS metrics.
