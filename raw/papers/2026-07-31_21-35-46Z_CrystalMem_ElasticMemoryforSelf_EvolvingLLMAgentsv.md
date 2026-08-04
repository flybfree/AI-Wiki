---
title: CrystalMem: Elastic Memory for Self-Evolving LLM Agents via Knowledge Crystallization
published: 2026-07-31T21:35:46Z
authors: Beining Wu, Jun Huang
url: http://arxiv.org/abs/2608.00303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CrystalMem: Elastic Memory for Self-Evolving LLM Agents via Knowledge Crystallization

## Abstract
Memory for self-evolving large language model (LLM) agents is often provisioned as if its byte budget only grows. Cloud platforms, however, adjust quotas with load and cost, and we show that capability does not follow the budget back up: after a squeeze-and-recover cycle, the agent settles below its pre-squeeze level, a gap we call memory hysteresis. The cause is structural. Deletion and one-way compression discard the material needed for later rebuilding, and we prove that any policy that only keeps or drops entries carries a residual-deficit floor. We propose CrystalMem (Crystallized Memory), an elastic memory sidecar that demotes entries across four fidelity states under a crystallization-energy schedule, orders demotions by advantage-weighted influence with dependency coupling, and recovers capability through verified recrystallization under explicit compute and byte caps. Across seven environments, seventeen methods, and six backbones, with multi-tenant serving and a physical edge-cloud deployment, CrystalMem achieves the highest restored capability in every setting and closes the loop left open by every baseline. From a 50% byte budget, CrystalMem matches the strongest budgeted baseline at full provision on every environment; at equal budgets, it leads by +4.6 pp on average.

## Metadata
- **Published**: 2026-07-31T21:35:46Z
- **Authors**: Beining Wu, Jun Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00303v1)