---
title: DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows
published: 2026-08-27T02:36:23Z
authors: Zechun Niu, Yukun Zhao, Jiaxin Zhang, Xu Shen, Jinhua Si, Han Tian, Can Xu, Yunfan Song, Jiaxin Mao, Yansong Gao, Yuchen Li, Jianmin Wu, Lingyong Yan, Shuaiqiang Wang, Dawei Yin
url: http://arxiv.org/abs/2608.26546v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows

## Abstract
Autonomous agents are increasingly adopted to complete complex, multi-tool workflows in real-world settings. However, existing benchmarks typically separate tasks by application or capability and evaluate agents in environments that are cleaner and more stable than those encountered in practice. We introduce DuMateBench, a real-session benchmark reconstructed from anonymized and privacy-screened user sessions collected from a large-scale production agent platform. Each task preserves the relevant pre-solution interaction history, persistent configurations, and workspace state, and is then validated through human verification. The resulting benchmark comprises 200 tasks spanning 8 broad scenarios and 17 fine-grained capability categories, with most tasks requiring multiple capability coordination. We execute these tasks in isolated Docker containers injected with three forms of real-world environmental complexity: Insufficient, Unstable, and Noisy, and assess performance using a hybrid deterministic and LLM-as-Judge evaluation protocol. Experiments across five representative autonomous-agent frameworks paired with four state-of-the-art LLMs reveal substantial gaps in strict task completion. Complementary robustness, efficiency, and diagnostic analyses further show that performance under environmental perturbations is jointly shaped by the capabilities of the LLM and the surrounding agent framework. The code and data are publicly available at https://dumatebench.com/.

## Metadata
- **Published**: 2026-08-27T02:36:23Z
- **Authors**: Zechun Niu, Yukun Zhao, Jiaxin Zhang, Xu Shen, Jinhua Si, Han Tian, Can Xu, Yunfan Song, Jiaxin Mao, Yansong Gao, Yuchen Li, Jianmin Wu, Lingyong Yan, Shuaiqiang Wang, Dawei Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26546v1)