# Summary: 2026-07-28_18-10-33Z_GuideSkill_EvolvingExecutableLLMAgentSkillsforGuid.md
Saved: 2026-07-29 20:17
Source: 2026-07-28_18-10-33Z_GuideSkill_EvolvingExecutableLLMAgentSkillsforGuid.md
Model: None

---

## Summary  
The paper introduces **GuideSkill**, an external reasoning layer that transforms clinical practice guideline text into executable functions capable of returning ordinal diagnostic‑support scores for each condition. It provides two variants: **GuideSkill‑Zero** which loads these functions directly from the guidelines, and **GuideSkill‑Evo** which dynamically evolves skill coverage by training on case‑diagnosis pairs to add missing diagnoses. At inference, an LLM proposes a differential diagnosis, grounds the required features in matched skills, and fuses the executed skill scores with the model’s ranking. This approach overcomes the limitation of traditional Retrieval‑Augmented Generation (RAG) that merely retrieves or absorbs guideline text.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 4 title terms overlap; 17 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- **Executable Skills Framework** – GuideSkill converts guideline content into functions that output ordinal diagnostic‑support scores, enabling systematic rule execution rather than passive retrieval.  
- **Dynamic Skill Evolution** – GuideSkill‑Evo uses case‑diagnosis pairs to refine and expand the skill set, achieving 99.5 % gold‑label coverage compared with 56.5 % for baseline methods.  
- **Robust Accuracy Gains** – Across four benchmarks and backbones, GuideSkill‑Zero improves macro‑average accuracy by 13.45 % over guideline RAG, while GuideSkill‑Evo leads all baselines with a relative gain of 18.49 % and an absolute improvement of 11.16 % on Qwen3.5‑9B without updating the backbone.

## Methodology  
The authors built a two‑stage pipeline: first, they parse clinical guidelines into discrete functions that take patient features as input and output a numeric score for each condition (ordinal support). GuideSkill‑Zero initializes these functions directly from the guideline text. Second, GuideSkill‑Evo fine‑tunes the function set using labeled case‑diagnosis pairs, adding new diagnoses or correcting existing ones. During inference, an LLM generates a differential diagnosis list; for each proposed condition it selects the corresponding skill, executes its scoring function on the patient features, and aggregates the scores with the model’s ranking to produce a final diagnostic recommendation.

## Results  
- **GuideSkill‑Zero**: Macro‑average accuracy ↑ 13.45 % over guideline RAG across four benchmarks (various backbones).  
- **GuideSkill‑Evo**: Achieves the highest macro‑average for every backbone, improves relative to direct inference by 18.49 %, and raises gold‑label skill coverage from 56.5 % to 99.5 %. On Qwen3.5‑9B it exceeds the strongest parameter‑update baseline by 11.16 % without altering the backbone parameters.  
- **Expert Evaluation**: Clinicians deem the generated skills clinically sound and broadly acceptable, indicating reliable rule execution.

## Significance  
GuideSkill demonstrates that external reasoning layers can reliably combine guideline‑derived procedures with case‑specific patterns, offering a model‑agnostic mechanism for improving diagnostic support in real‑world clinical AI. By providing executable skill scores and enabling dynamic evolution of coverage, the framework addresses key limitations of static RAG approaches and paves the way for more trustworthy, guideline‑grounded medical decision‑making systems.

## Related Concepts  
- Clinical practice guidelines (CPGs)  
- Rule extraction from text  
- External reasoning layers / skill modules  
- Differential diagnosis generation  
- Ordinal scoring functions  
- Skill coverage and completeness  
- Retrieval‑Augmented Generation (RAG)  
- Parameter‑update baselines
