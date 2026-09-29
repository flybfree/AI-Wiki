---
title: RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Agents
published: 2026-09-26T18:41:03Z
authors: Jingsong Liang, Shuhao Liao, Shizhe Zhang, Diyuan Hou, Yuxin Cai, Xinjian Deng, Chengyang He, Wenhui Huang, Runjia Tan, Zhidong Wang, Lan Yu, Xuesong Tian, Guillaume Sartoretti, Jie Luo, Yao Mu, Wenjun Wu, Wanhua Li, Chen Lv
url: http://arxiv.org/abs/2609.32862v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Agents

## Abstract
A foundation model should not act in isolation as an embodied agent. Yet, existing methods often optimize individual components of the agent stack, such as memory, context, skills, or action interfaces, rather than treating the supporting system itself as a unified policy. Moreover, interaction alone does not yield self-improvement unless execution experience is converted into persistent, validated system changes. We therefore propose RoboFoundry, the first embodied agentic framework that formulates this process as Self-Evolving System-as-Policy. RoboFoundry diagnoses capability gaps in decision-making and memory management, converts execution traces into validated task-specific system updates, and promotes recurring improvements to the general system. Evolution operates over two complementary surfaces: a context system that manages active internal context and persistent file-system memory, and a hierarchical skill system that organizes atomic skills, reusable compositions, and failure-conditioned recovery. A shared semantic interface separates embodiment-invariant decisions from embodiment-specific execution, allowing evolved system capabilities to transfer across heterogeneous robots. On EmbodiedBench, RoboFoundry achieves state-of-the-art performance, notably improving GPT-5.5 by 27.8%. It also brings Qwen3.7-Plus to near parity with GPT-5.5 (70.3% vs. 72.7%), showing consistent gains from system-as-policy evolution across foundation models. For long-horizon memory, RoboFoundry outperforms all baselines on RoboMemArena by at least 39.0%, even against methods assisted by external foundation models. On LIBERO-PRO, it further outperforms Cap-Agent0 by 243.8%-679.7% across all perturbation types. In real-world deployments, RoboFoundry demonstrates zero-shot transfer and online evolution across robots and tasks, highlighting its potential for fully autonomous embodied agents.

## Metadata
- **Published**: 2026-09-26T18:41:03Z
- **Authors**: Jingsong Liang, Shuhao Liao, Shizhe Zhang, Diyuan Hou, Yuxin Cai, Xinjian Deng, Chengyang He, Wenhui Huang, Runjia Tan, Zhidong Wang, Lan Yu, Xuesong Tian, Guillaume Sartoretti, Jie Luo, Yao Mu, Wenjun Wu, Wanhua Li, Chen Lv
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32862v1)