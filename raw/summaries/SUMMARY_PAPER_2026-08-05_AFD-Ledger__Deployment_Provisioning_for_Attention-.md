---
title: AFD-Ledger: Deployment Provisioning for Attention--FFN Disaggregation
url: http://arxiv.org/abs/2608.04502v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_06-39-57Z_AFD_Ledger_DeploymentProvisioningforAttention__FFN.md
generated_at: 2026-08-05 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AFD-Ledger, an offline analytical provisioning system that compares attention‑feed‑forward network (AFD) and collocated MoE language model deployments under identical hardware budgets and service‑level objectives. By jointly optimizing hardware assignment and deployment organization using an analytical execution model and a bounded search, the method reduces exhaustive evaluation needs by up to 83.5% while still identifying the globally optimal deployment.

## Key Takeaways
- AFD-Ledger cuts complete deployment evaluations by 68.8–83.5%, making large‑scale provisioning feasible without sacrificing optimality.
- On three LongCat 2.0 physical deployments, AFD’s throughput matches collocated models within a narrow margin of 6.6% to 9.6%, confirming the analytical model’s accuracy.
- The study reveals that homogeneous AFD only benefits fixed‑budget throughput in a minority of settings; heterogeneous AFD gains depend on hardware complementarity and deployment organization rather than simple device selection.

## Context
MoE language models are increasingly deployed at scale, where efficient resource utilization is critical. Existing research focuses on architectural innovations but often overlooks the interplay between model execution strategies and hardware provisioning. This work bridges that gap by providing a systematic method to evaluate both AFD and collocated deployments under real‑world constraints.

## Implications
For industry practitioners, AFD-Ledger offers a practical tool to decide whether to adopt attention‑feed‑forward disaggregation without exhaustive trial‑and‑error. Practitioners can allocate hardware more effectively, reducing cost while maintaining performance, which is essential for sustainable AI infrastructure planning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04502v1)
