---
title: AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety
published: 2026-10-14T02:13:29Z
authors: Chenxu Wang, Xiaoyu Wen, Han Qi, Ziyuan Zhou, Cheng Jin, Chaochao Lu, Qiaosheng Zhang
url: http://arxiv.org/abs/2610.19422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety

## Abstract
Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce unsafe actions. Adversarial co-evolution has emerged as an effective approach to strengthening LLM safety, but existing work primarily focuses on language-level safety or indirect prompt injection in web tasks. In this paper, we introduce AgentSafeEvo, a co-evolutionary reinforcement learning framework for agent safety built on an attacker-defender game spanning diverse tasks and attack types. The attacker learns to construct adversarial agent tasks that expose weaknesses in the defender's tool use, while the defender learns to complete tasks safely under these attacks. We further introduce learnability-guided task weighting, which uses within-task defender-reward variability to adjust each task's contribution to attacker and defender updates. Extensive experiments on agent safety and general capability benchmarks demonstrate that our method improves adversarial robustness while maintaining general agent capabilities.

## Metadata
- **Published**: 2026-10-14T02:13:29Z
- **Authors**: Chenxu Wang, Xiaoyu Wen, Han Qi, Ziyuan Zhou, Cheng Jin, Chaochao Lu, Qiaosheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19422v1)