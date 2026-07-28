# Summary: 2026-07-27_15-33-18Z_TRACE_CTI_AuditablePost_ExtractionGovernanceofTTPC.md
Saved: 2026-07-28 00:14
Source: 2026-07-27_15-33-18Z_TRACE_CTI_AuditablePost_ExtractionGovernanceofTTPC.md
Model: None

---

## Summary  
TRACE-CTI introduces a post-extraction governance framework for Cyber Threat Intelligence (CTI) claims that ensures traceable, auditable trust in automated mappings to the MITRE ATT&CK framework. By preserving granular evidence and provenance throughout the extraction process, TRACE-CTI enables operators to make informed, policy-compliant decisions about which mapping outputs are trusted. The system avoids destructive data loss by maintaining versioned trust states and non-destructive revocation histories while integrating multiple generator families into a unified knowledge graph structure.

## Key Contributions  
- [Finding 1] TRACE-CTI transforms individual prediction-level outputs into configuration-level GraphAssertions that encapsulate provenance, validation grounds, and trust decisions without altering the original extraction data.  
- [Finding 2] The framework demonstrates that cross-generator-family setups significantly increase output diversity compared to same-family setups, improving the granularity of corroborated insights in the knowledge graph.  
- [Finding 3] Empirical evaluation reveals a strong trade-off between precision and recall as setup support increases: gold-aligned precision rises from 25.3% to 90.6% with six-setup unanimity, while recall drops from 88.2% to 16.3%, highlighting the need for balanced governance policies.

## Methodology  
The authors approached the problem by designing a modular framework that operates post-extraction on raw CTI reports and their MITRE ATT&CK mappings. They used two public corpora—65 reports with 5,303 sentences—and tested six different generator families across six GraphVersions. Each setup was incrementally ingested to build the knowledge graph, preserving native evidence granularity and complete provenance paths. The system validates only those GraphAssertions that meet policy-compliant criteria, ensuring trust is grounded in verifiable data.

## Results  
The results show that TRACE-CTI successfully maintains auditability across all stages of claim governance. Every trusted output has an active qualifying validation ground, and versioned trust decisions allow for non-destructive review or revocation. Cross-generator-family setups produced 2.8 times more diverse GraphAssertions than same-family ones, suggesting that integrating heterogeneous sources enriches the graph without redundancy. The final graph state answers seven critical questions about provenance, trust, versioning, dependencies, disagreements, and review queues—something minimal flat outputs cannot do.

## Significance  
TRACE-CTI matters because it addresses a critical gap in current CTI workflows: automated mappings lack accountability and traceability. By enabling auditable governance, the framework supports compliance, risk management, and trustworthy decision-making in security operations. The observed precision-recall trade-off underscores that governance is not just about correctness but also about operational balance—a key insight for real-world deployment.

## Related Concepts  
- MITRE ATT&CK framework  
- Cyber Threat Intelligence (CTI) extraction  
- Knowledge graphs and GraphAssertions  
- Post-extraction claim governance  
- Provenance tracking  
- Trust validation grounds  
- Versioned trust states
