# Summary: 2026-08-05_06-39-57Z_AFD_Ledger_DeploymentProvisioningforAttention__FFN.md
Saved: 2026-08-05 23:12
Source: 2026-08-05_06-39-57Z_AFD_Ledger_DeploymentProvisioningforAttention__FFN.md
Model: None

---

## Summary  
The paper introduces AFD‑Ledger, an offline analytical provisioning system that addresses a key gap in Attention‑FFN Disaggregation (AFD) for Mixture‑of‑Experts language models: it asks whether AFD yields higher throughput than the best collocated deployment under identical hardware budgets and service‑level objectives. By jointly optimizing hardware assignment and deployment organization, AFD‑Ledger replaces exhaustive provisioning with an evaluation‑bounded search that still recovers the globally optimal solution. The approach reduces complete deployment evaluations by up to 83 % while preserving correct architecture decisions and predicting throughput within a narrow margin.

## Key Contributions  
- [Finding 1] AFD‑Ledger cuts the number of required deployment evaluations from exhaustive searches to a fraction, achieving reductions of 68.8 %–83.5 %.  
- [Finding 2] The system preserves the correct architecture decision and predicts AFD‑to‑collocated throughput with an accuracy of only 6.6 %–9.6 % on real hardware.  
- [Finding 3] Homogeneous AFD improves fixed‑budget throughput in a minority of settings; heterogeneous AFD benefits from deployment‑level hardware complementarity rather than simple device selection.

## Methodology  
The authors built an analytical execution model that decouples the logical stages of attention and feed‑forward layers, enabling independent provisioning of each architecture. An evaluation‑bounded hardware search then explores a bounded subset of hardware catalogs, applying cost constraints and SLO targets to prune infeasible combinations. The whole process is performed offline, generating deployment recommendations without requiring live inference.

## Results  
In three physical LongCat 2.0 deployments, AFD‑Ledger identified the optimal deployment for both collocated and disaggregated models while staying within a 6.6 %–9.6 % error band on throughput predictions. The evaluation count was reduced by an average of 75 %, demonstrating that exhaustive provisioning is unnecessary when analytical bounds are respected.

## Significance  
AFD‑Ledger provides a cost‑effective, scalable framework for deploying MoE language models, allowing practitioners to make informed hardware choices without exhaustively testing every possible configuration. Its insights into when homogeneous versus heterogeneous AFD delivers value guide resource allocation and budget planning in large‑scale inference services.

## Related Concepts  
Attention‑FFN Disaggregation (AFD), collocated deployment, Mixture‑of‑Experts language models, provisioning system, analytical execution model, throughput measurement, service‑level objective (SLO), hardware catalog, resource budget, MoE architecture, LongCat 2.0 platform.
