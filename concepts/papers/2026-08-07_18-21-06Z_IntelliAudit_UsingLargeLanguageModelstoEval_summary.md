# Summary: 2026-08-07_18-21-06Z_IntelliAudit_UsingLargeLanguageModelstoEvaluateAud.md
Saved: 2026-08-10 22:38
Source: 2026-08-07_18-21-06Z_IntelliAudit_UsingLargeLanguageModelstoEvaluateAud.md
Model: None

---

## Summary  
IntelliAudit is a retrieval‑grounded multi‑agent system that uses large language models to evaluate whether heterogeneous organizational evidence satisfies semantic security and compliance controls in IT audits. The paper demonstrates how the system can retrieve relevant artifacts, generate evidence‑grounded assessments, challenge adverse findings, adjudicate disagreements, and produce auditor‑focused recommendations with citations and rationale. By simulating ISO/IEC 27001 environments and gathering expert auditor feedback, IntelliAudit shows promise for supporting audit preparation while highlighting the need for human oversight to calibrate sufficiency judgments.  

## Key Contributions  
- [Finding 1] Retrieval‑grounded multi‑agent system that couples large language models with evidence retrieval to produce structured audit assessments.  
- [Finding 2] The architecture enables automated challenge of adverse findings and adjudication of disagreements, producing a comprehensive recommendation package.  
- [Finding 3] Human oversight remains essential for calibrating sufficiency judgments and preventing overly permissive recommendations.  

## Methodology  
The authors designed IntelliAudit as an end‑to‑end pipeline: (1) ingest a control description and an evidence corpus; (2) employ a vector‑based retrieval engine to locate pertinent artifacts across policies, records, spreadsheets, and operational logs; (3) feed retrieved snippets into a large language model that generates natural‑language reasoning grounded in the evidence; (4) trigger challenge mechanisms when the model’s assessment conflicts with control intent; (5) resolve disagreements via a lightweight adjudication agent; and (6) compile a final auditor‑facing output containing cited evidence, rationale, missing‑evidence analysis, and remediation guidance. The system was instantiated on ISO/IEC 27001 controls and tested across multiple simulated organizations.  

## Results  
Experiments involving expert auditors reviewed IntelliAudit’s outputs and provided audit‑readiness feedback. The system successfully interpreted control intent, generated evidence‑grounded reasoning, and flagged missing artifacts with high precision. However, it occasionally produced overly permissive recommendations that required human correction, indicating a need for calibrated sufficiency judgments. Overall, IntelliAudit demonstrated strong support for control interpretation and audit‑preparation workflows while remaining a decision‑support tool rather than an autonomous certifier.  

## Significance  
IntelliAudit advances the field by showing how large language models can be integrated with retrieval to automate evidence evaluation in complex audits. Its findings underscore that automated systems should complement, not replace, human judgment, ensuring audit integrity and regulatory compliance. The work also provides a template for future research on AI‑assisted audit tools.  

## Related Concepts  
- Large Language Models (LLMs)  
- Audit Controls  
- Evidence Corpus Retrieval  
- ISO/IEC 27001 Compliance  
- Multi‑Agent Systems  
- Sufficiency Judgments  
- Decision‑Support Tools
