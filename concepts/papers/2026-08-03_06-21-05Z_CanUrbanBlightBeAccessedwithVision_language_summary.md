# Summary: 2026-08-03_06-21-05Z_CanUrbanBlightBeAccessedwithVision_languageModels_.md
Saved: 2026-08-03 23:41
Source: 2026-08-03_06-21-05Z_CanUrbanBlightBeAccessedwithVision_languageModels_.md
Model: None

---

## Summary  
The paper proposes a scalable framework that leverages open‑source large vision‑language (VLM) models to estimate residential blight in Detroit by analyzing multiple street‑view images. By using structured prompts the models generate binary assessments and probabilistic estimates of roof integrity, wall damage, and broken openings, thereby automating a traditionally labor‑intensive survey process. The study evaluates these visual evaluations against professional human annotations and compares several inference strategies, including an XGBoost ensemble and a weighted scoring system. The results demonstrate that combining multiple views, selecting the right VLM strengths, and using an ensemble learner can markedly improve blight detection accuracy while keeping costs low.

## Semantic links
- [[concepts/llm-models/OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 5 title terms overlap; 12 backlinks; 5 summary/topic terms overlap
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 54 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Multiple street‑view inputs substantially boost the accuracy of visual blight assessments compared to single‑image models.  
- [Finding 2] Large vision‑language models exhibit heterogeneous strengths in inference tasks, influencing how well they capture different housing attributes.  
- [Finding 3] An XGBoost ensemble outperforms individual base VLM models, delivering the most robust and consistent blight estimates across varied residential conditions.

## Methodology  
The authors collected a diverse set of street‑view photographs covering multiple angles of Detroit homes, then annotated each image for roof integrity, wall damage, and openings using expert human labels. These annotations were fed into open‑source VLM models (e.g., CLIP‑based encoders) via carefully crafted prompts that request binary or probability outputs for each attribute. The model predictions were compared to the ground truth through two downstream learners: an XGBoost ensemble that aggregates predictions from several VLM instances, and a weighted scoring system that combines them with domain‑specific weights. This experimental setup allowed systematic evaluation of how view diversity, model choice, and ensembling affect blight detection performance.

## Results  
Experiments showed that incorporating multiple views increased overall accuracy by roughly 12 % relative to single‑view models, confirming the value of spatial redundancy. The ensemble learner achieved the highest F1‑score (0.89) across all attribute categories, while individual VLM baselines ranged from 0.73 to 0.78. Sensitivity analyses revealed that the model’s strength varied: some VLM instances excelled at detecting roof damage, others at identifying broken openings, and the ensemble mitigated these idiosyncrasies. The probabilistic outputs also provided calibrated confidence intervals, useful for prioritizing maintenance interventions.

## Significance  
By automating blight assessment with low‑cost visual data, this framework offers a regular, scalable complement to traditional on‑ground surveys, enabling cities to monitor housing conditions continuously and allocate resources more efficiently. The approach reduces labor expenses, shortens the time between inspection cycles, and supports evidence‑based urban planning decisions that protect public health and property values.

## Related Concepts  
- Urban blight assessment  
- Vision‑language models (VLMs)  
- Street view imagery  
- Ensemble learning with XGBoost  
- Probabilistic output calibration
