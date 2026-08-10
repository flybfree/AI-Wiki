---
title: Policy-Masked Private Experts: Auditable and Reversible Capability Access Control in Sparse MoE Models
url: http://arxiv.org/abs/2608.06690v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_01-39-36Z_Policy_MaskedPrivateExperts_AuditableandReversible.md
generated_at: 2026-08-09 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Policy‑Masked Private Experts, a method that freezes a pretrained sparse Mixture‑of‑Experts model and adds a disjoint expert branch whose public or private pool is selected before routing. The authors demonstrate that this scheme provides an auditable, reversible control over which trained parameters are executed by the forward pass while preserving task utility. Experiments on Qwen3-30B-A3B and DeepSeek-V2-Lite show zero unauthorized private execution across adversarial scenarios and measurable gains in exact tool use.

## Key Takeaways
- The public model can be frozen so that only its public experts are reachable, leaving the private branch untouched; this creates a narrow but testable claim about execution control.  
- In benchmark tests the private expert branch improves exact tool use by 5.0 percentage points with a one‑sided Holm p = 0.03125 and a percentile‑bootstrap 95% CI of [13.3, 29.3], indicating statistically significant benefit.  
- A parameter‑matched LoRA leaves many adapter calls under deny requests, whereas the disjoint expert branch eliminates those calls entirely.

## Context
The paper addresses a growing need for transparent access control in large language models where execution pathways can be manipulated without altering model weights. By separating routing decisions from trained parameters, it offers a way to audit and reverse‑engineer which parts of a model are being used, a capability that is currently limited by opaque compute graphs.

## Implications
For practitioners, Policy‑Masked Private Experts enables reversible, auditable control over trained parameter paths, supporting trustworthy deployment in regulated environments. The approach also highlights the importance of distribution dependence when transferring utility between public and private branches, guiding future research on secure model sharing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06690v1)
