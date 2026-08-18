---
title: Hierarchical Agentic Incident Response with Digital-Twin-Validated Attack Inference
published: 2026-08-15T04:01:27Z
authors: Yiran Gao, Juntao Chen, Tao Li
url: http://arxiv.org/abs/2608.15016v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical Agentic Incident Response with Digital-Twin-Validated Attack Inference

## Abstract
Network incident response remains slow and labor-intensive as the defender must infer multi-stage attacks from partial observations and translate recovery decisions into reliable system commands. Decision-theoretic planners provide principled optimization but typically rely on abstract states and predefined actions, while large language model (LLM) agents can reason over operational context but may hallucinate attacks and responses. Toward automating response planning, we present a hierarchical agentic response framework that integrates LLM-based attack inference, rollout planning, and digital-twin validation. A fine-tuned LLM infers the attack progression and affected hosts from security alerts and system measurements. An emulated network digital twin replays the inferred attack and returns discrepancies between predicted and observed effects to calibrate the inference. A separately fine-tuned planning agent uses the rollout planning method to prioritize affected components at the tactical layer. At the operational layer, the planning agent proposes high-level recovery actions, and an execution agent translates selected actions into recovery and verification commands that are validated in the digital twin. We evaluate the framework on a 33-component enterprise-network testbed under three multi-stage attack scenarios. The results show that our framework outperforms frontier-LLM baselines in recovery success rate by 18--31%.

## Metadata
- **Published**: 2026-08-15T04:01:27Z
- **Authors**: Yiran Gao, Juntao Chen, Tao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15016v1)