---
title: Toward Metacognitive One-Shot Indirect Prompt Injection: Strategy Abstraction Via Outcome-Conditioned Reflection
published: 2026-08-09T16:19:05Z
authors: Sihan Hou, Xinmeng Hou, Zhijun Zhang, Zehao Wang, Xuhong Ren, Sibo Qin, Kuntharrgyal Khysru, Qing Guo
url: http://arxiv.org/abs/2608.08795v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward Metacognitive One-Shot Indirect Prompt Injection: Strategy Abstraction Via Outcome-Conditioned Reflection

## Abstract
Tool-using large language model (LLM) agents are vulnerable to indirect prompt injection (IPI), in which malicious instructions embedded in external observations manipulate subsequent agent decisions and actions. Most existing adaptive attacks rely on repeatedly querying and refining against the target agent, whereas realistic attackers may have only a single opportunity to interact with an unknown target agent. We propose SAVOR (Strategy Abstraction Via Outcome-Conditioned Reflection), which shifts attack adaptation from test-time iteration to offline strategy distillation. SAVOR performs outcome-conditioned reflection over successful and failed trajectories collected from disjoint training environments, validates context-conditioned candidate strategies, and iteratively consolidates them into a reusable strategy memory. At test time, the frozen memory guides the generation of a single payload for each unseen target, requiring only one target-agent query and no target-agent feedback. Across two benchmarks and three victim models, SAVOR attains the highest average attack success rate in all six settings, leading the strongest prior attack by 2.5 to 11.8 points and the same injection channel without strategy learning by 23.1 points on Agent Security Bench, which holds out attacker tools, and 28.6 points on OpenClaw-IPI, an executable benchmark we introduce that holds out attack goals and verifies attacks through tool interactions and execution receipts. A memory learned under one defense also transfers to another.

## Metadata
- **Published**: 2026-08-09T16:19:05Z
- **Authors**: Sihan Hou, Xinmeng Hou, Zhijun Zhang, Zehao Wang, Xuhong Ren, Sibo Qin, Kuntharrgyal Khysru, Qing Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08795v1)