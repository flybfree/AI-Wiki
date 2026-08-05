# Summary: 2026-07-23_16-47-39Z_ArtificialEpanorthosis_Whylargelanguagemodelsoveru.md
Saved: 2026-07-23 21:02
Source: 2026-07-23_16-47-39Z_ArtificialEpanorthosis_Whylargelanguagemodelsoveru.md
Model: None

---

## Summary  
The paper investigates why large language models systematically overuse the classical rhetorical figure epanorthosis—the self‑correction of a specimen phrase such as “This is not a course. It is a journey of transformation.”—and proposes an Epanorthosis Index to quantify its prevalence relative to human usage across different genres. It argues that this bias originates from training data dominated by promotional prose and reinforcement‑learning‑from‑human‑feedback (RLHF) preferences for emphatic, confident phrasing rather than the left‑to‑right generation process itself. The authors develop a lightweight mitigation framework using low‑rank adaptation (LoRA) adapters, showing that simple instruction prompts can cut the figure by half to three‑quarters or remove it entirely with a scaling coefficient that restores human rates. Their work aims to calibrate model output to human expectations per genre rather than eliminating the figure altogether.

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 54 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Models systematically overuse epanorthosis, especially in formal oratory and Italian text, where density is roughly twice the human baseline.  
- [Finding 2] The Epanorthosis Index reveals mis‑calibration across genres: overshoot in argumentative writing, undershoot in informal question‑and‑answer exchanges, while matching humans in journalistic and encyclopedic prose.  
- [Finding 3] Lightweight LoRA adapters can reduce epanorthosis density by 50 % to 75 % or nearly eliminate it, with a tunable scaling coefficient that brings the model’s output back onto the human rate.

## Methodology  
The authors first compile large corpora of human‑generated text spanning multiple genres and apply Fontanier’s classification to compute epanorthosis density. They then generate model outputs on these same prompts and compare them to the human baseline using the Epanorthosis Index, which is defined as the ratio of model‑generated epanorthosis events to the expected human rate for each genre. To mitigate the bias, they train lightweight LoRA adapters on a short instruction dataset that explicitly discourages the figure; the adaptation’s strength is scaled so that the resulting output aligns with the target human rate.

## Results  
On three instruction‑tuned model families (small, medium, large), the mis‑calibration pattern holds: oratory and Italian text show roughly twofold overshoot, while informal Q&A writing undershoots. In contrast, argumentative essays, journalism, and encyclopedic prose match human rates closely. Applying a one‑line LoRA adapter reduces epanorthosis density by about 50 % to 75 %, and a supervised fine‑tuning adapter can drive it down to near zero; the scaling coefficient of the adapter is adjusted so that the final index equals the human baseline for each genre.

## Significance  
If large language models continue to write as if they were machines, users may lose trust in their outputs or be misled by unnatural phrasing. By providing a quantitative metric (the Epanorthosis Index) and practical mitigation tools, this research helps preserve the natural, human‑like style that makes AI assistance useful across domains.

## Related Concepts  
- Epanorthosis: a rhetorical figure of self‑correction.  
- RLHF: reinforcement learning from human feedback.  
- LoRA adapters: low‑rank adaptation for lightweight fine‑tuning.  
- Epanorthosis Index: a density metric relative to human usage.  
- Genre calibration: aligning model output with human expectations per text type.
