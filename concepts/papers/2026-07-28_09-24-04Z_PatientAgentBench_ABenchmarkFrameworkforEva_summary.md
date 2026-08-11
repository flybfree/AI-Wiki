# Summary: 2026-07-28_09-24-04Z_PatientAgentBench_ABenchmarkFrameworkforEvaluating.md
Saved: 2026-07-28 20:22
Source: 2026-07-28_09-24-04Z_PatientAgentBench_ABenchmarkFrameworkforEvaluating.md
Model: None

---

## Summary  
The paper introduces PatientAgentBench, a benchmark framework to evaluate patient‑facing health AI agents that can reason and act on behalf of patients using healthcare tools. It addresses the gap between static medical QA benchmarks and dynamic agentic interactions with simulated patients, providing a reproducible, clinician‑validated evaluation standard. The authors benchmark ten foundation models across four families over 1,200 patient‑agent scenarios, measuring performance across six dimensions via an LLM jury.  

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- Founding PatientAgentBench as a comprehensive benchmark for patient‑agentic health AI.  
- Demonstrating that clinical gaps persist even in top‑performing agents, especially in sustained tool use and emergency handling.  
- Providing a reproducible evaluation protocol with clinician‑annotated data achieving high inter‑rater agreement.  

## Methodology  
The authors designed PatientAgentBench to simulate realistic primary‑care conversations where an agent interacts with a simulated patient using a sandbox of healthcare tools. Each conversation is evaluated by an LLM‑as‑a‑Jury applying six criteria: triage quality, clinical safety, workflow accuracy, tool execution fidelity, crisis resource provisioning, and overall adherence. The jury scores are compared to annotations from licensed clinicians; the benchmark includes 1,200 scenario‑agnostic dialogues across four model families.  

## Results  
Across ten models, pass rates improved from 32 % (weakest) to 88 % (strongest). Clinical safety failures occurred in 7–9 % of cases for top agents, primarily due to unverified tool outputs and missing crisis resources. Workflow accuracy suffered similarly: the strongest agents failed on only a few actions but often omitted critical steps. The overall best score was 4.25 out of 5.  

## Significance  
This work highlights that static medical knowledge benchmarks cannot capture the risks of autonomous patient‑agentic systems, urging the field to adopt dynamic, tool‑using evaluation frameworks. By releasing PatientAgentBench, researchers can systematically assess and improve safety in health AI agents.  

## Related Concepts  
- Foundation models  
- Agentic healthcare AI  
- LLM‑as‑a‑Jury  
- Clinician annotation  
- Tool sandboxing  
- Primary care triage
