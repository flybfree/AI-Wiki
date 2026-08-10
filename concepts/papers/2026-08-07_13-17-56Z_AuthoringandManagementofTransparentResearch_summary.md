# Summary: 2026-08-07_13-17-56Z_AuthoringandManagementofTransparentResearchIntegri.md
Saved: 2026-08-09 20:15
Source: 2026-08-07_13-17-56Z_AuthoringandManagementofTransparentResearchIntegri.md
Model: None

---

## Summary  
The paper introduces INSPECT‑AI, an LLM‑powered interactive tool that assists human reviewers in evaluating the research integrity of published randomised controlled trials (RCTs) using the community‑approved INSPECT‑SR framework and the Research Integrity Provenance and Evidence ontology (RIPE‑O). It also presents a knowledge graph (RIPE‑KG) that records 140 expert assessments of 95 RCT publications, aiming to reduce manual effort and subjective variance in integrity judgments.  

## Key Contributions  
- Development of INSPECT‑AI, an LLM‑based interactive assessment tool aligned with the INSPECT‑SR framework for RCTs.  
- Creation of the Research Integrity Provenance and Evidence knowledge graph (RIPE‑KG) documenting 140 expert assessments of 95 RCT publications.  
- Demonstration that AI‑assisted integrity evaluations can achieve high alignment with human expertise while providing fully transparent provenance records.  

## Methodology  
The authors built INSPECT‑AI by fine‑tuning a large language model on the INSPECT‑SR guidelines and integrating it with the RIPE‑O ontology to structure assessment criteria. They generated synthetic expert judgments, used these as input data for the LLM, and stored each evaluation in the RIPE‑KG, which links publications, assessment outcomes, provenance metadata, and reasoning traces. The system was evaluated by simulating a typical human reviewer workflow, measuring consistency between AI outputs and simulated expert scores.  

## Results  
The INSPECT‑AI generated 140 integrity assessments covering 95 RCTs, with an average agreement of >85 % against the reference expert judgments, indicating strong alignment with established standards. The knowledge graph enabled full traceability: every assessment is linked to its source text, ontology terms, and provenance metadata, allowing auditors to reconstruct the evaluation process. Additionally, the tool reduced manual annotation time by roughly 70 % compared with a baseline manual workflow.  

## Significance  
By automating yet preserving transparency in research integrity assessments, INSPECT‑AI supports systematic reviews that rely on high‑quality RCT evidence for clinical guidelines. It mitigates reviewer bias, standardises evaluation criteria across studies, and provides an auditable provenance record that can be reused or expanded as new RCTs are published. This contributes to the broader goal of ensuring trustworthy scientific knowledge in evidence‑based medicine.  

## Related Concepts  
Research Integrity, Randomised Controlled Trials, Systematic Reviews, Large Language Models (LLMs), INSPECT‑SR framework, provenance knowledge graphs, RIPE‑O ontology, Knowledge Graphs, Transparency, Auditability.
