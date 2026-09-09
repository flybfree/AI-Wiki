---
title: TrojanWorld: Backdooring World-Model Agents via Imagination Steering
published: 2026-09-07T05:14:10Z
authors: Wenkai Huang, Siyuan Liang, Gaolei Li, Yiming Li, Tianhao Peng, Jianhua Li, Dacheng Tao
url: http://arxiv.org/abs/2609.07051v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TrojanWorld: Backdooring World-Model Agents via Imagination Steering

## Abstract
World models increasingly serve as the predictive core of model-based reinforcement learning agents, enabling them to simulate future dynamics and reason over imagined trajectories before acting. Their substantial training demands make pretrained world models attractive for distribution and reuse, exposing downstream systems to model supply chain threats. Backdoor attacks offer a targeted and stealthy means of exploiting such supply chains, yet their threat to interactive world-model agents remains largely unexplored. To fill this gap, we present TrojanWorld, a backdoor framework for world-model agents that induces attacker-specified behavior by steering internal imagination. A physical object placed in the scene acts as the trigger, enabling deployment-time activation through the agent's native observation pipeline without digitally manipulating the observation stream. To achieve effective, stealthy, and persistent control, TrojanWorld combines Decision-Reflective Induction to steer trigger-conditioned imagination toward attacker-specified actions using decision feedback, Clean Behavior Anchoring to preserve trigger-free predictive and behavioral fidelity, and Causal Propagation to sustain the induced preference along subsequent trajectories after the trigger disappears. Together, these mechanisms establish an end-to-end attack chain from physical perception through corrupted imagination to malicious action selection. Experiments with the TD-MPC2, DreamerV3, and R2-Dreamer systems across the DeepMind Control, MetaWorld, MyoSuite, and RoboDesk benchmarks show that under trigger activation, TrojanWorld achieves a target-action deviation as low as 0.026 while retaining at least 98.8% of the corresponding clean performance. Even after trigger removal, the compromised agent can remain trapped in the induced behavioral trajectory, continuing to execute attacker-specified actions.

## Metadata
- **Published**: 2026-09-07T05:14:10Z
- **Authors**: Wenkai Huang, Siyuan Liang, Gaolei Li, Yiming Li, Tianhao Peng, Jianhua Li, Dacheng Tao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07051v1)