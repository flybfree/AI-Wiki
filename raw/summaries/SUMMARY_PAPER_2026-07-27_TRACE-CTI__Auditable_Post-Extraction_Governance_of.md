---
title: TRACE-CTI: Auditable Post-Extraction Governance of TTP Claims with Knowledge Graphs
url: http://arxiv.org/abs/2607.24563v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_15-33-18Z_TRACE_CTI_AuditablePost_ExtractionGovernanceofTTPC.md
generated_at: 2026-07-27 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TRACE‑CTI, a framework for governing cyber threat intelligence (CTI) mappings to MITRE ATT&CK after extraction. The study shows that by preserving provenance and validation history, the framework can produce auditable GraphAssertions with high precision when multiple setups are combined.

## Key Takeaways
- TRACE‑CTI retains run-level predictions and aggregates them into configuration‑level GraphAssertions that include full evidence and versioned trust decisions.  
- The system produces ConsensusAssertions that represent corroborated mappings across different generator families, ensuring each trusted assertion has an active qualifying validation ground.  
- Adding more setups from 1 to six increases gold‑aligned precision from 25.3% to 90.6%, while recall drops correspondingly, highlighting the trade‑off between precision and recall.

## Context
The rapid adoption of automated CTI mapping creates a need for trustworthy outputs that can be audited without altering original data. Existing minimal flat outputs lack provenance, making it difficult to verify or revoke individual mappings later.

## Implications
Practitioners can now implement an end‑to‑end governance model that supports compliance and accountability in threat intelligence pipelines. The framework’s ability to answer detailed questions about provenance and trust makes it a valuable tool for security operations centers seeking reliable, auditable CTI integration.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24563v1)
