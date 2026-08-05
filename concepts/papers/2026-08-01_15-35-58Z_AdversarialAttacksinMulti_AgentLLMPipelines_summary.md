# Summary: 2026-08-01_15-35-58Z_AdversarialAttacksinMulti_AgentLLMPipelines_Unveil.md
Saved: 2026-08-03 20:30
Source: 2026-08-01_15-35-58Z_AdversarialAttacksinMulti_AgentLLMPipelines_Unveil.md
Model: None

---

## Summary  
The paper investigates structural vulnerabilities in multi‑agent LLM pipelines where adversarial attacks propagate across agents due to the absence of boundary verification, creating implicit trust assumptions that are not adversarially robust. It identifies four distinct attack families—content injection, agent impersonation, plan deviation, and memory poisoning—and demonstrates that these failures arise from pipeline architecture rather than model capability alone.

## Semantic links
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 4 title terms overlap; 17 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 5 title terms overlap; 121 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- Finding 1: Multi‑agent pipelines inherit implicit trust assumptions that generate distinct attack surfaces (content injection, agent impersonation, plan deviation, memory poisoning).  
- Finding 2: Attack success correlates with pipeline structure, not model capability, indicating the vulnerability is fundamentally architectural.  
- Finding 3: The authors operationalize these failure modes in a controlled multi‑agent setting and evaluate them across GPT‑5‑mini, Claude Sonnet 4.5, and Kimi K2.5 under identical configurations.

## Methodology  
The researchers analyze annotated production traces from the GAIA and SWE‑Bench benchmarks to map how adversarial inputs travel through agents. They construct synthetic pipelines with the same configuration for each model, inject crafted prompts that exploit boundary gaps, and measure success rates while tracking propagation depth. The evaluation isolates the effect of pipeline structure on attack outcomes.

## Results  
Across all three models, attacks succeed in benign deployments with success rates ranging from 30 % to 78 %, depending on pipeline depth. The effect is consistent regardless of model size or capability, confirming that the vulnerability stems from the pipeline architecture itself. No existing evaluation framework captures these failures.

## Significance  
This work shows that security for agentic AI must be designed at the pipeline level, not merely within individual models. It calls for boundary verification primitives to enforce explicit validation of content, identity, intent, and state integrity as data cross inter‑agent boundaries. The findings motivate a shift toward robust, architecture‑aware defenses.

## Related Concepts  
Multi‑agent LLM pipelines; adversarial attacks; boundary verification; implicit trust assumptions; attack surfaces; pipeline‑level defenses; memory poisoning; plan deviation; content injection; agent impersonation.
