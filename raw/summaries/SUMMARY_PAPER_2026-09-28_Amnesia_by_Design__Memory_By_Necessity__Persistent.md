---
title: Amnesia by Design, Memory By Necessity: Persistent State for Document Intelligence
url: http://arxiv.org/abs/2609.32041v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-25_22-12-41Z_AmnesiabyDesign_MemoryByNecessity_PersistentStatef.md
generated_at: 2026-09-28 22:00
model: qwen3.6-35b-a3b
---

## Summary
This survey identifies the "statelessness bottleneck" in modern Document AI, where systems process documents as isolated events without retaining schemas or experience across sessions, a structural limitation that persists despite parameter scaling or retrieval augmentation. It proposes a unifying framework for persistent evidence-grounded document state that converts multimodal evidence into durable, provenance-linked memory to enable continuous improvement and contradiction detection over time. The authors formalize the operations and invariants required for this persistence and introduce a longitudinal benchmark harness with specific metrics to evaluate the benefits, costs, and risks of implementing stateful capabilities.

## Key Takeaways
- Current Document AI architectures are fundamentally stateless functions that begin processing anew for every document, failing to retain schemas, detect contradictions, or carry forward experience; this "statelessness bottleneck" is a structural choice rather than a scale failure, rendering storage and retrieval insufficient without mechanisms to consolidate observations into knowledge.
- The paper introduces a formal framework for persistent evidence-grounded state coupled with document-native structure and provenance, supported by a statefulness audit revealing that ten representative benchmarks coded against eight criteria leave cross-session state evolution untested, highlighting a critical gap in evaluation methodologies.
- A longitudinal benchmark harness is derived featuring five counterfactual metrics—Experience Gain, Cost Efficiency, Memory Harm, Forgetting Fidelity, and Coverage Retention—to comprehensively characterize the benefit, cost, risk, and governability of persistent document state mechanisms, providing tools to measure how systems evolve across documents, sessions, and time.

## Context
As Document AI applications increasingly handle complex workflows involving amendments, multi-page reasoning, and long-term compliance, the inability of systems to maintain context across interactions creates significant operational inefficiencies and error risks. This work challenges the prevailing assumption that scaling models or extending contexts suffices for document understanding, highlighting a structural gap in how systems consolidate observations into actionable knowledge over time rather than treating each

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32041v1)
