# Summary: 2026-07-24_07-00-32Z_SmallVision_LanguageModelsKnowWhenTheyAreWrongButC.md
Saved: 2026-07-26 21:43
Source: 2026-07-24_07-00-32Z_SmallVision_LanguageModelsKnowWhenTheyAreWrongButC.md
Model: None

---

## Summary  
The paper investigates whether small vision‑language models can reliably signal when they are uncertain under realistic photographic degradations such as compression, camera shake, and poor lighting. It finds that the confidence the model expresses in natural language is essentially useless for error detection, whereas its internal token‑level probability provides a strong, consistent uncertainty measure. The study compares two open‑weight VLMs—Qwen2‑VL‑2B‑Instruct and SmolVLM‑Instruct—across six degradations at three severity levels using 3,800 predictions. This work demonstrates that small models possess usable self‑knowledge but cannot translate it into a reliable verbal confidence statement.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 29 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Verbalized confidence in both Qwen2‑VL and SmolVLM remains near constant (mean ≈ 0.87–0.90) across all conditions, yielding AUROC values around chance level (0.39–0.75), indicating it does not improve error detection.  
- [Finding 2] The model’s own mean token probability separates correct from incorrect answers with high AUROC scores (0.92–0.99 for Qwen2‑VL and 0.54–0.92 for SmolVLM), showing it can reliably signal uncertainty.  
- [Finding 3] Under severe underexposure, both models’ accuracy plummets (Qwen2‑VL: 0.99→0.22; SmolVLM: 0.97→0.42) while verbalized confidence barely changes and internal error detection collapses to chance.

## Methodology  
The authors evaluate two small open‑weight VLMs across six realistic photographic degradations (e.g., JPEG compression, motion blur, low‑light) at three severity levels. For each prediction they compute two confidence signals: the model’s natural‑language confidence score and the mean probability of the tokens it generated for its answer. The study records 3,800 predictions to quantify performance.

## Results  
Verbalized confidence is almost invariant (≈ 0.87–0.90) and provides only marginal improvement in AUROC (≈ 0.5), essentially at chance. Internal token probability, however, yields strong separation: Qwen2‑VL reaches AUROC 0.92–0.99; SmolVLM reaches 0.54–0.92. Accuracy drops sharply under severe underexposure (Qwen2‑VL from 0.99 to 0.22, SmolVLM from 0.97 to 0.42), yet both confidence signals remain flat and internal error detection also degrades to chance.

## Significance  
The findings reveal that small VLMs encode a useful uncertainty measure internally but fail to convey it through their verbal output, especially when hardware constraints limit model size. This suggests that for real‑world deployment where only token‑level probabilities are feasible—such as in low‑light or severely degraded images—the internal confidence should be trusted over the stated confidence.

## Related Concepts  
- Vision‑language models (VLMs)  
- Uncertainty signals and calibration  
- Token‑level probability as a confidence measure  
- Image degradation (compression, blur, low light)  
- AUROC (area under the receiver operating characteristic curve)  
- Self‑knowledge in AI systems
