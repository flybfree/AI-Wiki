---
title: An LLM-Based Agent for Legal Compliance Assessment: Architecture, Memory, and Evaluation in a Canadian and Quebec Context
url: http://arxiv.org/abs/2610.27347v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_22-24-34Z_AnLLM_BasedAgentforLegalComplianceAssessment_Archi.md
generated_at: 2026-10-20 22:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ComplianceAgent, a legal compliance sub-agent embedded within the COMPASS multi-agent framework, designed to automatically assess whether a given text conforms to a body of law. The agent uses a large language model to score texts against a fixed rubric, grounds its reasoning in a reference legal corpus, and triggers a corrective pipeline—including self-healing rewrites, compliance labels, explainability reports, and human escalation—when scores fall below a critical threshold. Evaluated on a corpus of thirteen Canadian, Quebec, international, and municipal legal instruments, the agent achieved perfect separation between conforming and non-conforming texts on a hand-annotated gold standard of fifteen documents, while maintaining score stability under repeated queries and retrieving relevant legal passages with high precision.

## Key Takeaways
- ComplianceAgent operates as one of four evaluation axes within the COMPASS multi-agent framework, which also covers digital sovereignty, carbon impact, and ethics. The compliance axis specifically leverages an LLM to score a target text against a fixed rubric, grounding its judgment in a reference legal corpus rather than relying on fragile keyword-matching rules. This architecture allows the same implementation to be pointed at different reference corpora, making it adaptable across jurisdictions.
- When the agent's score falls at or below a critical threshold, it activates a corrective chain consisting of self-healing rewrites, a compliance label, an explainability report, and escalation to a human reviewer. This multi-step remediation pipeline ensures that non-compliant outputs are not merely flagged but actively corrected and documented, with full transparency into the reasoning process.
- The evaluation methodology combines classification metrics, a repeated-query stability test, retrieval precision, and a composite score, tested against a hand-annotated gold standard of fifteen texts drawn from thirteen legal instruments spanning federal, provincial, international, and municipal sources in the City of Trois-Rivières. The agent separated every conforming text from every non-conforming one, maintained stable scores across repeated queries, and returned relevant passages from the legal index.

## Context
Automated legal compliance checking has long been hampered by the brittleness of keyword-based rules and the slowness of manual review. This paper sits at the intersection of LLM-based reasoning agents, retrieval-augmented generation, and legal informatics, demonstrating how a structured multi-agent architecture can move beyond simple classification toward grounded, explainable, and self-correcting compliance assessment. The Canadian and Quebec evaluation setting is particularly significant because it tests the agent across a genuinely multi-layered legal landscape—federal statutes, provincial codes, international treaties, and municipal bylaws—rather than a single homogeneous corpus, which is a common weakness in prior legal NLP benchmarks.

## Implications
For legal practitioners, compliance officers, and public-sector institutions, ComplianceAgent offers a template for deploying LLM-based agents that are auditable, jurisdiction-aware, and equipped with human-in-the-loop escalation, addressing the trust and accountability gaps that currently limit adoption of AI in regulated domains. For the broader AI research community, the paper contributes a reproducible evaluation protocol—combining gold-standard annotation, stability testing, and retrieval precision—that can be adapted to other legal systems or compliance domains, and it demonstrates that a single agent implementation can be re-pointed at different reference corpora, reducing the engineering cost of deploying compliance tools across jurisdictions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27347v1)
