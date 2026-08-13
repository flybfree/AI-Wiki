---
title: Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction
url: http://arxiv.org/abs/2608.11772v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_08-14-45Z_DiagnosisBeforeRecovery_TurningAgentFailuresintoSe.md
generated_at: 2026-08-12 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DARC, a diagnosis‑guided recovery harness that selects repair interventions before applying test‑time fixes. Experiments on ALFWorld, AppWorld, and XBRL Finance show it improves task performance while reducing steps or retrieval budget compared to broad playbooks.

## Key Takeaways
- DARC decides which recovery interventions are admissible based on failure type before any test correction occurs.
- It prunes mismatched interventions from a shared library, preventing invalid actions or missing procedures.
- The causal order of diagnosis then selective evidence spending makes self‑correction context‑efficient rather than prompt expansion.

## Context
Self‑correcting agents often rely on compiler‑like feedback that is absent in many AI domains. Traditional playbooks expand contexts broadly when failures occur, which can introduce errors and waste resources. DARC offers a more targeted approach by aligning recovery with the specific failure mode.

## Implications
For practitioners, DARC provides a practical framework to make failures actionable without inflating context size. In industry settings where reliable agents are critical, this could reduce debugging overhead and improve deployment reliability across diverse task families.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11772v1)
