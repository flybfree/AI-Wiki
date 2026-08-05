# Summary: 2026-07-17_17-55-19Z_EvaluatingOpen_WeightLLMsforGeneratingStructuredTh.md
Saved: 2026-07-19 21:01
Source: 2026-07-17_17-55-19Z_EvaluatingOpen_WeightLLMsforGeneratingStructuredTh.md
Model: None

---

## Summary  
The paper investigates how open‑weight Large Language Models (LLMs) can automatically convert plain‑text descriptions of autonomous‑vehicle (CAV) vulnerabilities into Structured Threat Information Expression (STIX), a standardized format used by security analysts. By mapping CVE entries to STIX domain objects, relationship objects, CWE identifiers, and MITRE ATT&CK techniques, the authors demonstrate that LLMs can generate high‑quality structured threat intelligence, thereby accelerating vulnerability mitigation in connected vehicle ecosystems.

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 54 backlinks; 5 summary/topic terms overlap
- [[concepts/llm-models/2026-07-10_OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 4 title terms overlap; 12 backlinks; 4 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 12 summary/topic terms overlap

## Key Contributions  
- Single‑model configurations achieve F1 scores of 0.94 for SDO generation, 0.63 for SRO generation, and 0.99 for CWE mapping, while complete MITRE ATT&CK mapping remains challenging.  
- Multi‑agent setups using Gemma‑4‑31B and Codestral‑22B reach F1 scores of 0.91 for SDOs and 0.43 for SROs, showing that larger models improve structured output but still struggle with relationships.  
- An analysis of CWE and MITRE ATT&CK co‑occurrences reveals recurring threat patterns in the CAV domain, highlighting how AI‑assisted translation can prioritize defense strategies.

## Methodology  
The authors constructed a dataset called **CAV‑STIXGen**, which pairs each CAV vulnerability description with corresponding STIX domain objects (SDO), relationship objects (SRO), CWE identifiers, and MITRE ATT&CK technique mappings. To evaluate the LLMs, they employed 11 open‑weight models ranging from 4B to 120B parameters across multiple prompting strategies and temperature settings. The evaluation measured generation quality using F1 scores for each mapping task.

## Results  
Single‑model setups delivered SDO F1 = 0.94, SRO F1 = 0.63, CWE F1 = 0.99; MITRE ATT&CK mapping was consistently below 0.70. In the multi‑agent scenario, Gemma‑4‑31B achieved SDO F1 = 0.91 and Codestral‑22B SRO F1 = 0.43. The co‑occurrence analysis identified several CWE‑ATT&CK pairs that recur across CAV CVEs, suggesting systematic threat vectors.

## Significance  
Automating the translation of raw vulnerability text into structured STIX data can dramatically reduce manual effort and improve interoperability among security tools in the transportation sector. By quantifying model performance on a real‑world dataset, the study provides empirical evidence that open‑weight LLMs are viable for generating actionable threat intelligence, supporting faster patching and risk prioritization.

## Related Concepts  
STIX (Structured Threat Information Expression), CVE (Common Vulnerabilities and Exposures), CWE (Common Weakness Enumeration), MITRE ATT&CK framework, Open‑weight LLMs, Autonomous Vehicle vulnerabilities, Structured Threat Information Generation.
