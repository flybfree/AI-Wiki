---
title: LeakageBench: Document-Level Leakage Risk for Redacting Personally Identifiable Information in Document Images
url: http://arxiv.org/abs/2609.02207v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_07-21-24Z_LeakageBench_Document_LevelLeakageRiskforRedacting.md
generated_at: 2026-09-02 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LeakageBench, a benchmark of 500 document images containing 11,954 GDPR-aligned PII annotations to measure the risk that personal data leaks through OCR or vision‑language pipelines. The study evaluates both generic and specialized detectors using entity‑level F1 scores as well as group‑wise and document‑level leakage metrics. While Code Interpreter improves GPT‑5.5 localization from 0.090 to 0.249, the overall page‑level leakage remains high at 0.968.

## Key Takeaways
- The benchmark demonstrates that even state‑of‑the‑art OCR‑free vision‑language models still miss many PII instances, resulting in a near‑certainty of document‑level leakage.  
- Code Interpreter’s assistance boosts localization accuracy but does not eliminate the majority of unsafe pages, highlighting the gap between component improvements and overall safety.  
- Document‑level metrics reveal that a single missed identifier can render an entire page non‑compliant with GDPR standards.

## Context
Current PII redaction tools focus on text extraction and entity detection, often overlooking the visual layout and contextual cues that make certain identifiers harder to locate. This paper addresses that gap by providing a dataset that captures both direct identifiers and linkage keys across diverse document formats, offering a more realistic evaluation of real‑world leakage risk.

## Implications
For developers deploying redaction pipelines, LeakageBench underscores the need for holistic assessments rather than relying solely on component scores. Practitioners should treat high page‑level leakage as a critical failure mode that must be mitigated to ensure compliance and user trust.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02207v1)
