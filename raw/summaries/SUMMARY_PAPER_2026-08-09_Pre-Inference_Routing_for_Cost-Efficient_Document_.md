---
title: Pre-Inference Routing for Cost-Efficient Document Field Extraction
url: http://arxiv.org/abs/2608.06607v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_21-34-51Z_Pre_InferenceRoutingforCost_EfficientDocumentField.md
generated_at: 2026-08-09 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes pre‑inference routing to select between a cheap and a strong document extraction model based on predicted difficulty derived from visible features like image quality and layout. Experiments show the router reduces cost by 31‑33% on receipts and 77% on degraded ad‑buy forms while keeping F1 within 0.02 of using only the large model. Routing is ineffective when either condition fails, such as with clean digital invoices or easy‑to‑read nutrition labels.

## Key Takeaways
- The router reduces cost by 31‑33% on receipts and 77% on degraded ad‑buy forms while keeping F1 within 0.02 of the large model’s performance.
- Routing only helps when cheap failures are frequent enough to justify switching, which can be predicted from visible features like image quality and layout.
- A small labeled pilot correctly predicts routing applicability in two cases, indicating that genre determines success rather than router design.

## Context
Document extraction remains a challenge because models must handle varying difficulty levels across genres. Current approaches either use a single heavy model or lack mechanisms to adapt, leading to inefficiencies. This work introduces a lightweight decision layer that can switch models based on cheap signals, aligning with trends toward cost‑aware AI deployment and explainable routing.

## Implications
Practitioners can implement simple bag‑of‑words routers to cut inference costs without sacrificing quality, especially in mixed‑difficulty document sets. The findings suggest that genre classification is a key bottleneck, guiding future research on domain‑specific adaptation of routing strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06607v1)
