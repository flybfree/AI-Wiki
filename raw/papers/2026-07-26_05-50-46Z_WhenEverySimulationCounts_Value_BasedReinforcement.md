---
title: When Every Simulation Counts: Value-Based Reinforcement Learning for Accelerated Photonics Inverse Design
published: 2026-07-26T05:50:46Z
authors: Longying Wen, Feiyang Wu, Jinglin Yu, Chongxian Yuan, Renjie Li, Zhaoyu Zhang
url: http://arxiv.org/abs/2607.23469v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Every Simulation Counts: Value-Based Reinforcement Learning for Accelerated Photonics Inverse Design

## Abstract
Photonic-crystal surface-emitting lasers (PCSELs) can combine high-power operation with narrow-divergence surface emission, but optimizing coupled parameters requires costly full-wave simulations. Deep Q-network (DQN) optimization can reuse simulated transitions to guide edits, yet which value-learning mechanisms remain reliable under tight simulation budgets is unknown. We address this gap by comparing baseline DQN and six value-based variants for a seven-variable PCSEL design under a shared objective, simulator, 83-call budget, and four matched initializations. Beyond endpoints, we analyze sample efficiency, policy behavior, and physical response to separate learning gains from favorable starts or exploratory jumps. Dueling DQN is the only variant to improve all four seeds. Relative to the first evaluated designs, its selected structures increase the mean quality factor () from to (), reduce wavelength error by 64%, and increase upward power by 47%; compared with baseline DQN, they achieve a higher mean under the same budget. Other variants yield no consistent improvement; Double DQN reproduces baseline trajectories, while Rainbow-lite shows high upside but strong seed dependence. These results identify Dueling DQN as the most reliable configuration tested for simulation-budget-limited PCSEL inverse design and provide a reproducible framework for attributing algorithmic gains in scientific optimization. The source code is publicly available at https://github.com/Longying-Wen/PCSEL-RL.

## Metadata
- **Published**: 2026-07-26T05:50:46Z
- **Authors**: Longying Wen, Feiyang Wu, Jinglin Yu, Chongxian Yuan, Renjie Li, Zhaoyu Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23469v1)