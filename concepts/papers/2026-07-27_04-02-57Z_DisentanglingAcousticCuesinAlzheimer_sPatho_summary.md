# Summary: 2026-07-27_04-02-57Z_DisentanglingAcousticCuesinAlzheimer_sPathologyand.md
Saved: 2026-07-28 00:02
Source: 2026-07-27_04-02-57Z_DisentanglingAcousticCuesinAlzheimer_sPathologyand.md
Model: None

---

## Summary  
The paper investigates how acoustic biomarkers for Alzheimer’s disease differ across languages and genders, focusing on whether diagnostic AI aligns with human perceptual cues. It trains models to predict clinical AD status and listener perception in Mandarin and Greek among male and female speakers, using SHAP interpretability and statistical validation. The study reveals that alignment is significant only in certain subgroups, exposing a population‑specific failure mode of explainable AI. This work calls for demographic auditing of XAI explanations.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- Finding 1: Pathological‑perceptual alignment is statistically significant for Mandarin speakers and female participants but absent for Greek males.  
- Finding 2: Global SHAP explanations mask these subgroup divergences, leading to false confidence in model fairness.  
- Finding 3: The research demonstrates that population‑specific explainability auditing is necessary for equitable deployment of clinical speech AI.

## Methodology  
The authors collected speech samples from bilingual male and female speakers, recording both pathological and normal acoustic cues. They built two parallel models: one predicting Alzheimer’s pathology based on biomarker metrics, another estimating human perceptual scores using psycholinguistic tests. SHAP values were computed for each model to generate global importance maps, which were then compared across demographic subgroups. Statistical significance was assessed with permutation testing.

## Results  
In Mandarin and female speakers, the pathological model outperformed chance and its top features correlated with perception metrics, indicating strong alignment. In Greek males, both models failed to exceed random performance; SHAP explanations showed no meaningful feature importance. The subgroup analysis revealed a clear demographic split in model behavior.

## Significance  
These findings highlight that explainable AI can obscure critical demographic differences, potentially leading to inequitable clinical deployment. By exposing population‑specific failure modes, the work underscores the need for rigorous, subgroup‑aware auditing of XAI tools before real‑world use.

## Related Concepts  
- Alzheimer’s disease biomarkers  
- Acoustic cue extraction  
- Explainable AI (XAI) and SHAP  
- Demographic fairness in machine learning  
- Cross‑lingual perception differences
