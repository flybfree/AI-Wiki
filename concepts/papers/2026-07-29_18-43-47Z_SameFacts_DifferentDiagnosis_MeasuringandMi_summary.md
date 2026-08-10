# Summary: 2026-07-29_18-43-47Z_SameFacts_DifferentDiagnosis_MeasuringandMitigatin.md
Saved: 2026-07-30 20:21
Source: 2026-07-29_18-43-47Z_SameFacts_DifferentDiagnosis_MeasuringandMitigatin.md
Model: None

---

## Summary  
The paper identifies a hidden source of diagnostic error in clinical language models: Narrative Anchoring, where identical clinical facts expressed in different sociolinguistic registers produce divergent outputs despite the absence of any demographic markers. By constructing a fact‑preserving dataset of 1,000 USMLE vignettes rewritten under three distinct personas, the authors demonstrate that this register‑only bias is statistically significant across seven language models. Their key contribution is a structural mitigation called NarrativeShield, which extracts and verifies facts before reasoning, reducing the anchoring gap to near zero while preserving diagnostic stability at a modest accuracy cost.  

## Semantic links
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 4 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/llm-models/OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 4 title terms overlap; 12 backlinks; 4 summary/topic terms overlap
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Narrative Anchoring is defined as a bias where identical clinical facts generate different diagnoses solely due to sociolinguistic register, not demographic information.  
- [Finding 2] A rigorously audited dataset of 1,000 vignettes with three persona rewrites and independent fact‑preservation verification is introduced.  
- [Finding 3] NarrativeShield, a three‑agent pipeline that separates fact extraction from reasoning, cuts the narrative anchoring gap to $-0.004$–$0.037$ and yields the lowest severely unstable decision rate (DSS < 0.8) across all models.  

## Methodology  
The authors created a dataset where each vignette is rewritten into three sociolinguistically distinct personas while guaranteeing that all clinical facts remain unchanged; verification was performed by an unseen model to ensure no leakage. They evaluated seven language models from three architecture families using direct prompting, chain‑of‑thought reasoning, and explicit debiasing instructions. The NarrativeShield pipeline consists of a fact‑extraction agent, a verification agent, and a diagnostic reasoning agent; the first two run before any inference begins.  

## Results  
Across the models, narrative anchoring produced a Gap of 0.064–0.151 (statistically significant). Chain‑of‑thought reasoning reduced the gap partially but often caused accuracy collapse. NarrativeShield achieved a near‑zero Gap ($-0.004$ to $0.037$) and maintained DSS < 0.8, outperforming all other methods in stability while incurring only a modest accuracy trade‑off. A stress test on an untrained base model showed that any debiasing intervention is ineffective unless the model can follow zero‑shot instructions, indicating that instruction‑following ability gates the mitigation.  

## Significance  
Narrative Anchoring reveals that clinical language models are vulnerable to sociolinguistic register rather than explicit demographic cues, a problem that prior bias work has not fully addressed. By separating fact extraction from reasoning and providing a reproducible dataset, the study offers a scalable framework for mitigating this subtle bias in diagnostic AI systems.  

## Related Concepts  
- Narrative Anchoring (register‑only bias)  
- Sociolinguistic register vs. demographic markers  
- Clinical language models / USMLE vignettes  
- Bias mitigation techniques (chain‑of‑thought, explicit instructions)  
- Accuracy‑stability trade‑off in AI reasoning
