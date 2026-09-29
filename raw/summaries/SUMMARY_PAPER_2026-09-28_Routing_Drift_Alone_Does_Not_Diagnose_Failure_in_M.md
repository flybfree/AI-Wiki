---
title: Routing Drift Alone Does Not Diagnose Failure in Merged MoE LLMs
url: http://arxiv.org/abs/2609.32821v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_17-47-55Z_RoutingDriftAloneDoesNotDiagnoseFailureinMergedMoE.md
generated_at: 2026-09-28 20:56
model: qwen3.6-35b-a3b
---

## Summary
This study examines whether routing drift observed after merging Mixture-of-Experts (MoE) models indicates genuine routing failure or merely reflects benign input shifts across DeepSeekMoE, OLMoE, and Qwen3-MoE architectures. The authors demonstrate that most expert reassignments stem from changes in router inputs rather than parameter modifications, and that restoring source routes fails to reliably improve task performance or predict next-token likelihood gains. They conclude that routing drift alone is insufficient evidence of failure, proposing instead that routing interventions should be evaluated based on recoverable task loss under controlled conditions.

## Key Takeaways
- Routing drift is predominantly caused by input shifts rather than parameter changes; detailed analysis shows that expert reassignments after merging are largely attributed to variations in router inputs at the same layer, indicating that structural alterations in routing behavior do not necessarily imply parameter corruption or degradation.
- Source-informed corrections lack predictive power for performance gains; source-relative routing differences poorly correlate with next-token likelihood improvements, and different expert selections can produce directionally similar mixture outputs, suggesting that Selective Router Repair (SRR) based on source-specialist advantages does not reliably identify beneficial local corrections.
- Routing failure must be operationalized through task-level intervention effects rather than drift metrics; the authors define routing failure as recoverable task loss under specified routing interventions with fixed non-routing parameters, showing that while deliberate router corruption

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32821v1)
