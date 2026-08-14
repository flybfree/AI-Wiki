---
title: Labels Are Not Endpoints: Treatment Leakage and Construct Validity in MCP Agent Security Evaluation
url: http://arxiv.org/abs/2608.12880v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_06-44-40Z_LabelsAreNotEndpoints_TreatmentLeakageandConstruct.md
generated_at: 2026-08-13 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how stored labels in a machine‑learning agent’s security evaluation can leak information about the underlying treatment, undermining construct validity. By tracing execution rows to model‑bound requests and comparing two schema treatments, the authors show that fixed behavior changes when treatment metadata is altered. A reconstruction process corrects mislabeled records while preserving legitimate data transfers.

## Key Takeaways
- The historical grader directly used treatment labels to decide ATTACK_SUCCESS or HIJACK_ATTEMPT outcomes, so relabeling would change class predictions and reveal the treatment.
- Reconstruction fixed 58 historical labels to benign completions without altering three protected‑data transfers or an unauthorized forwarding case.
- A dual‑reviewer blind analysis of 96 requests found identical consensus classes but four construct‑boundary cases differed from the locked codebook.

## Context
Security evaluations often treat label storage as a factual representation, ignoring that labels are artifacts of evaluation design. This study highlights how such assumptions can produce misleading attack rates and defense efficacy estimates in AI safety research.

## Implications
For practitioners, this work calls for rigorous integrity checks to prevent label leakage from skewing security metrics. It also suggests developing tools like the Integrity Chain linter to ensure that measurement audits reflect true model behavior rather than evaluation artifacts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12880v1)
