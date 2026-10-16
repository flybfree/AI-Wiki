---
title: A Responsibility-Centered Coordination Mechanism for Decentralized Multi-Agent Systems
published: 2026-10-15T04:39:57Z
authors: Thi-Nhung Nguyen, Viet-Thanh Pham, Linhao Luo, Thuy-Trang Vu, Dinh Phung
url: http://arxiv.org/abs/2610.21243v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Responsibility-Centered Coordination Mechanism for Decentralized Multi-Agent Systems

## Abstract
Centralized orchestration provides comprehensive multi-agent coordination but creates bottlenecks in scalability, adaptability, and collective performance. Decentralized approaches alleviate these bottlenecks by distributing coordination across agents, yet often leave responsibility for delegated dependencies and failure recovery unclear. To address this gap, we propose RCM, a responsibility-centered coordination mechanism that leverages commitments to couple task delegation with explicit responsibilities of the involved parties. Through recursive delegation, agents retain their upstream responsibilities while locally orchestrating downstream commitments, thereby preserving accountability across delegation chains, creating a network of local orchestration. We operationalize this mechanism locally through responsibility-constrained decision-making and a responsibility-oriented communication protocol (RCP), enabling agents to autonomously establish, manage, and terminate commitments. As agents act in parallel, their local actions continuously evolve the commitment graph, allowing global coordination to emerge and adapt toward a shared mission without centralized control. Experiments across reasoning, coding, and executable agent environments demonstrate that RCM outperforms strong centralized and decentralized coordination baselines by up to 18.7 points in task performance and 10.2 points in Responsibility, while improving failure and harm detection without task-specific training.

## Metadata
- **Published**: 2026-10-15T04:39:57Z
- **Authors**: Thi-Nhung Nguyen, Viet-Thanh Pham, Linhao Luo, Thuy-Trang Vu, Dinh Phung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21243v1)