---
title: AERIS: Offline Policy Improvement for Multi-UAV Integrated Sensing and Communication
url: http://arxiv.org/abs/2608.25477v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_07-47-38Z_AERIS_OfflinePolicyImprovementforMulti_UAVIntegrat.md
generated_at: 2026-08-26 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces AERIS, an offline policy improvement framework for multi‑UAV ISAC that balances communication, sensing and safety without online risky trials. It uses STAR‑CRDT to apply trustworthy local actions derived from global logs, achieving a 29.3% gain over baselines.

## Key Takeaways  
- The framework learns from fixed flight logs under centralized training while each UAV acts locally, allowing team‑level effects to be assessed without online trial‑and‑error.  
- STAR‑CRDT performs support‑aware local action rectification and distills only trusted improvements into the decentralized actor, providing an offline‑support policy improvement guarantee.  
- Experiments show a 29.3% increase in main ISAC objective return, plus gains of 3.4%, 4.8% and 69.1% in communication sum rate, sensing pass rate and margin, while collision risk drops by 54.2%.

## Context  
Multi‑UAV ISAC is a core component of the envisioned 6G network where simultaneous sensing and communication must be coordinated under stochastic mobility. Traditional methods suffer from global optimization bottlenecks or unsafe online learning, highlighting the need for safe offline policy refinement.

## Implications  
This work demonstrates that centralized training with decentralized execution can yield significant performance improvements without compromising safety, offering a scalable approach for future ISAC deployments. Practitioners can adopt AERIS to design robust policies that maximize utility while minimizing risk in real‑world UAV fleets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25477v1)
