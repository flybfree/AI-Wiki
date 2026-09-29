---
title: From Attack Success to Attack Severity: Counterfactual Memory Attacks on LLM Agents
published: 2026-09-28T02:11:56Z
authors: Mingxi Zou, Langzhang Liang, Zhuo Wang, Yiyang Zhao, Lizhen Qu, Zenglin Xu
url: http://arxiv.org/abs/2609.34132v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Attack Success to Attack Severity: Counterfactual Memory Attacks on LLM Agents

## Abstract
As LLM agents increasingly rely on persistent memory for long-horizon and personalized behavior, they can retain and reuse information across interactions, but this also creates a lasting channel through which malicious memory writes can influence future behavior. Persistent-memory attacks are typically evaluated by whether they succeed, yet successful attacks can leave persistent states with substantially different downstream consequences. We study this severity as a distinct attack-design objective and formalize it with counterfactual memory regret (CMR), the paired increase in expected downstream loss relative to clean memory. We introduce MemHarm, which predeclares a finite class of sparse, grounded semantic edits, evaluates candidates through the normal agent memory interface using offline paired-loss feedback, and certifies resolved selections within that class. Compared with attack-success optimization, CMR-guided selection produces substantially larger downstream loss while retaining most of the success-rate gain. Across two agent benchmarks and diverse memory designs, MemHarm attains the highest CMR point estimates among the evaluated general attacks on identical support. Factor-removal interventions link this harm to the selected semantic factor, and native-agent deployments verify the write-to-fresh-process attack path.

## Metadata
- **Published**: 2026-09-28T02:11:56Z
- **Authors**: Mingxi Zou, Langzhang Liang, Zhuo Wang, Yiyang Zhao, Lizhen Qu, Zenglin Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34132v1)