---
title: Partially-Observable Transmission Control for UAV-Enabled Federated Learning in IoT Networks
url: http://arxiv.org/abs/2608.00855v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_20-28-08Z_Partially_ObservableTransmissionControlforUAV_Enab.md
generated_at: 2026-08-03 23:41
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces a packet-level transmission framework for UAV-enabled federated learning in IoT networks that captures interference and errors via the packet delivery ratio (PDR). It formulates a fairness-consensus bilevel optimization to jointly set transmission thresholds and powers, achieving consensus under partial observability. Numerical results show improved FL aggregation compared with baselines.

## Key Takeaways  
- The packet delivery ratio (PDR) is used as a metric for partial update reception, representing the fraction of packets successfully delivered despite buffer overflow, delay violations, and errors.  
- A fairness-consensus bilevel optimization jointly selects transmission thresholds to maximize average PDR while achieving consensus among IoT learners under partial observability constraints.  
- The alternating optimizer consists of a consensus-based threshold controller that drives learners toward a PDR-efficient consensus and a fairness-based power controller that updates powers to improve worst-case PDR and enforce fairness.

## Context  
Federated learning on UAV platforms enables edge intelligence but suffers from interference in shared unlicensed bands, causing unreliable uplink updates. This work addresses the need for reliable packet-level delivery by modeling transmission as Bernoulli-masked events and optimizing network parameters accordingly.

## Implications  
The approach can be applied to any federated IoT deployment where latency and fairness matter, offering a principled method to balance throughput with equitable performance across devices. Practitioners can leverage the alternating FCB optimizer to design robust transmission policies that adapt to real-time interference conditions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00855v1)
