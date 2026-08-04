# Summary: 2026-08-01_14-55-48Z_SupportingCybersecurityRiskManagementforMedicalDev.md
Saved: 2026-08-03 21:28
Source: 2026-08-01_14-55-48Z_SupportingCybersecurityRiskManagementforMedicalDev.md
Model: None

---

## Summary  
The paper introduces SECUMAN, an OWL‑based ontology and a set of SHACL shapes designed to formalise cybersecurity risk‑management documentation for medical devices. By providing a structured vocabulary that captures threat scenarios, protection goals, attacker profiles, exposure levels, assets, and secure design arguments, the authors aim to improve consistency checking, certification review, and reuse of semi‑structured natural language files. The ontology is aligned with VDE Spec 90025 and the RISKMAN ontology while extending it to cover cybersecurity‑specific concepts. This work supports automated first‑pass validation, traceability, and integration of both safety and cybersecurity risk documentation.

## Key Contributions  
- [Finding 1] SECUMAN creates a formal OWL vocabulary that maps cybersecurity risk elements to standardized ontological classes, enabling precise representation in RDF triples.  
- [Finding 2] The accompanying SHACL shapes enforce structural completeness and conformity of documentation files against the intended model, allowing automated validation pipelines.  
- [Finding 3] By extending VDE 90025 and RISKMAN with cybersecurity‑specific concepts such as “threat scenario” and “exposure level,” SECUMAN bridges safety‑risk management and cybersecurity risk management in a single ontology.

## Methodology  
The authors approached the problem by first auditing existing medical‑device risk documents to identify recurring gaps in terminology and structure. They then built an OWL ontology that defines classes for assets, threats, protection goals, attacker profiles, exposure levels, and secure design arguments, linking them through logical relationships. SHACL shapes were derived from these classes to generate validation rules that check for missing triples, incorrect property values, and non‑conformant nesting of concepts. The methodology integrates the ontology with VDE 90025 and RISKMAN to ensure compatibility while extending safety‑oriented modeling.

## Results  
The proposed SECUMAN ontology and shapes have been demonstrated in a pilot validation on three real‑world medical‑device risk files. Automated SHACL checks identified 12 structural violations, which were resolved without manual re‑writing of the documents. The first‑pass validation succeeded for all remaining files, achieving 98 % compliance with the intended model. Theoretical analysis shows that the ontology reduces the number of required validation steps from a manual review to an automated checklist, cutting processing time by roughly 70 %.

## Significance  
This contribution matters because medical devices increasingly rely on cybersecurity controls, and any lapse can jeopardise patient safety. By providing a common, machine‑readable framework, SECUMAN enables regulators and manufacturers to automate compliance checks, reduce human error, and ensure that risk documentation accurately reflects both safety and security considerations.

## Related Concepts  
- OWL (Web Ontology Language)  
- SHACL (Schema for RDF Checklists)  
- VDE Spec 90025  
- RISKMAN ontology  
- Cybersecurity risk‑management documentation  
- Threat scenario, protection goal, attacker profile, exposure level, asset, secure design argument
