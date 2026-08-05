# Summary: 2026-07-15_15-22-11Z_ASelf_EvolvingAgentforLongitudinalPersonalHealthMa.md
Saved: 2026-07-23 23:43
Source: 2026-07-15_15-22-11Z_ASelf_EvolvingAgentforLongitudinalPersonalHealthMa.md
Model: None

---

## Summary  
HealthClaw is a self‑evolving agent architecture designed to manage personal health longitudinally, treating each encounter in isolation as most current systems do. The system separates immutable safety rules and medical knowledge from private longitudinal memory that stores profile facts, reusable procedures, and episodic traces. After every episode an induction process decides whether the profile should be updated, a procedure revised, or the trace retained. This modular design enables continual personalization while preserving safety and privacy.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 5 title terms overlap; 121 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 4 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- The separation of shared safety rules from private longitudinal memory yields a 45.7 % answer‑accuracy rate on longitudinal support probes compared with only 0.2 % using current‑query prompting.  
- HealthClaw generates higher‑quality, privacy‑aware answers and produces fewer unsafe disclosures than both baselines in 100 privacy‑focused probes.  
- The offline biomedical benchmark shows a mean absolute gain of 27.0 percentage points on the primary task metric, with seven gains remaining significant after false‑discovery‑rate correction.

## Methodology  
The authors approached the problem by constructing an agent that continuously updates its support as a user’s routines, preferences, measurements and risk profiles evolve. HealthClaw stores shared safety rules and medical knowledge separately from private longitudinal memory containing profile facts, reusable procedures, and episodic traces. After each episode an induction step evaluates whether the profile should be updated, a procedure revised, or the trace kept; otherwise it is excluded. Evaluation was performed on a synthetic year‑long benchmark together with nine 200‑case biomedical tasks, generating 900 longitudinal support probes and 100 privacy probes.

## Results  
Across 900 longitudinal support probes, answer accuracy rose from 0.2 % to 45.7 %, while prompt‑side context exposure dropped by 71.7 % relative to full‑history prompting. In the 100 privacy probes, HealthClaw achieved higher privacy‑aware answer quality and fewer unsafe disclosures than both baselines. Offline biomedical tasks yielded a mean absolute gain of 27.0 percentage points in the primary metric; after false‑discovery‑rate correction, seven of these gains remained statistically significant.

## Significance  
This work demonstrates that a governed, self‑evolving memory can dramatically improve personal health agents’ accuracy and safety while respecting user privacy—a critical gap for long‑term health management. By continuously adapting to changing routines and preferences, HealthClaw offers a scalable foundation for personalized longitudinal care, though its clinical impact remains unproven and requires prospective evaluation.

## Related Concepts  
- Longitudinal memory  
- Self‑evolving agents  
- Personal health management  
- Safety rule separation  
- Privacy‑aware generation  
- Synthetic year‑long benchmarking  
- False‑discovery‑rate correction
