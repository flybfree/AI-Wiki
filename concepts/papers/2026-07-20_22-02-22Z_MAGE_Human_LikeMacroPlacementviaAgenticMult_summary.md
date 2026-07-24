# Summary: 2026-07-20_22-02-22Z_MAGE_Human_LikeMacroPlacementviaAgenticMultimodalR.md
Saved: 2026-07-24 00:27
Source: 2026-07-20_22-02-22Z_MAGE_Human_LikeMacroPlacementviaAgenticMultimodalR.md
Model: None

---

## Summary  
The paper introduces MAGE, a multimodal multi‑agent framework that refines macro placement in industrial physical design flows by combining expert knowledge encoded in natural‑language directives with iterative agentic reasoning. Its goal is to achieve human‑like macro placements without requiring large labeled datasets or retraining for each new enablement. By decomposing the task into six phases and using a tournament refinement mode, MAGE generates candidate solutions that are evaluated against structured rules and visual checks. The framework also introduces four novel metrics to quantify human‑likeness beyond conventional PPA measures. The approach demonstrates that macro placement can be automated while preserving the nuanced spatial relationships that human designers prioritize.  

## Key Contributions  
- [Finding 1] MAGE achieves geometric‑mean improvements of 11.1%–19.3% in WNS and 70.0%–74.0% in TNS over commercial macro placers on nine designs from NanGate45 and GlobalFoundries 12nm enablements.  
- [Finding 2] On the three NanGate45 designs with human‑expert baselines, MAGE improves WNS by 18.3% and TNS by 72.5%, surpassing both human experts and Hier‑RTLMP while keeping wirelength and power comparable.  
- [Finding 3] The framework transfers to new placement settings without design‑specific retraining, as demonstrated on anonymized netlists, dense rectilinear floorplans, high‑utilization cases, and unseen designs.  

## Methodology  
MAGE follows a six‑phase workflow: (1) parse natural‑language directives into structured floorplan rules; (2) generate macro placement candidates using a multimodal agent that reasons over visual constraints; (3) evaluate each candidate with the four human‑likeness metrics (notch, whitespace, pocket, alignment); (4) select top candidates for tournament refinement; (5) propagate feedback from higher‑quality solutions to lower‑ranking ones; and (6) produce final placement. The agentic reasoning is driven by expert knowledge encoded in language, not learned from data. This workflow is designed to be modular, allowing integration with existing floorplan generation pipelines.  

## Results  
Across the benchmark datasets, MAGE outperforms all baselines: geometric‑mean WNS gain 11.1%–19.3%, TNS gain 70.0%–74.0%; human‑likeness scores improve by up to 48% over Hier‑RTLMP; wirelength and power remain within comparable ranges. Transfer experiments confirm consistent performance on unseen designs, dense layouts, and high‑utilization settings. These gains are achieved without sacrificing wirelength or power budget constraints, which are critical for high‑performance chips.  

## Significance  
By integrating expert‑driven natural language directives with agentic multimodal reasoning, MAGE bridges the gap between human intuition and automated macro placement, reducing reliance on costly manual refinement while preserving design quality. The novel metrics provide a principled way to evaluate human‑like aesthetics, offering a new benchmark for future PPA research. This work provides a scalable alternative to manual placement, potentially reducing design iteration time and enabling more consistent designs across multiple fab lines.  

## Related Concepts  
- Macro placement in physical design  
- Multi‑agent reinforcement learning  
- Natural language instruction parsing  
- Human‑likeness evaluation metrics (notch, whitespace, pocket, alignment)  
- Tournament refinement
