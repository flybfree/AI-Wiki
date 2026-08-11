---
title: IntelliAudit: Using Large Language Models to Evaluate Audit Controls
url: http://arxiv.org/abs/2608.07688v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-07_18-21-06Z_IntelliAudit_UsingLargeLanguageModelstoEvaluateAud.md
generated_at: 2026-08-10 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces IntelliAudit, a retrieval‑grounded multi‑agent system that automates the evaluation of IT audit evidence for compliance controls. The system retrieves relevant artifacts, generates an evidence‑based assessment, and produces auditor‑facing recommendations with citations and missing‑evidence analysis. Evaluation across simulated organizations shows that IntelliAudit supports control interpretation and audit preparation but highlights the need for human oversight to calibrate sufficiency judgments.

## Key Takeaways
- IntelliAudit uses a multi‑agent architecture to retrieve heterogeneous evidence and generate an assessment grounded in retrieved artifacts, moving beyond simple keyword matching.
- The system’s recommendations include cited evidence, rationale, missing‑evidence analysis, and remediation guidance, providing transparent audit support.
- Human oversight remains essential for calibrating sufficiency judgments and preventing overly permissive or restrictive suggestions.

## Context
The paper situates IntelliAudit within the broader AI research agenda of automated decision‑support tools that rely on retrieval mechanisms to handle complex, heterogeneous data. By demonstrating how large language models can integrate evidence retrieval with reasoning, it contributes to the development of systems capable of bridging gaps between policy and operational artifacts in regulated environments.

## Implications
For auditors, IntelliAudit offers a scalable way to surface relevant evidence and structure assessments, potentially reducing manual review time. For industry practice, the findings caution that AI‑driven tools should augment rather than replace human judgment, ensuring audit integrity while enhancing efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07688v1)
