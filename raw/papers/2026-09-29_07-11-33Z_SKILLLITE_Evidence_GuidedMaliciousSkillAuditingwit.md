---
title: SKILLLITE: Evidence-Guided Malicious Skill Auditing with Compact LLMs
published: 2026-09-29T07:11:33Z
authors: Haoran Ou, Gelei Deng, Xuanye Zhang, Wenbo Guo, Tianwei Zhang, Kwok-Yan Lam
url: http://arxiv.org/abs/2609.36879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SKILLLITE: Evidence-Guided Malicious Skill Auditing with Compact LLMs

## Abstract
As LLM-based agents perform increasingly complex tasks, Agent Skills have emerged as a flexible mechanism for extending their capabilities. An Agent Skill packages task-specific instructions with executable components and auxiliary resources to provide specialized functionalities. However, the growing adoption of third-party Skills introduces a new supply-chain attack surface. Malicious Skills can embed harmful behaviors that abuse agent privileges and compromise the agent execution environment or accessible resources. Although recent LLM-based malicious Skill auditing approaches have achieved promising performance, they often rely on capable commercial LLMs. How to achieve effective auditing with compact, locally deployable LLMs in security-sensitive and resource-constrained settings remains largely unexplored. Our investigation reveals that compact LLMs struggle to identify malicious behaviors hidden in complex Skill packages. This difficulty arises from both the implicit nature of such behaviors and the limited reasoning capacity of compact LLMs. To address these challenges, we propose SKILLLITE, an evidence-guided agentic framework for malicious Skill detection. SKILLLITE effectively extracts security-relevant behaviors and infers the intended functionality from complex Skill packages. It then employs a compact LLM to assess the maliciousness of the Skill based on the observed behaviors and their functional context. Experiments show that SKILLLITE improves malicious Skill detection across different compact LLM backbones and outperforms existing representative auditing baselines. Its effectiveness generalizes to behaviorally confirmed in-the-wild malicious Skills. Meanwhile, SKILLLITE maintains a low inference latency, supporting its practical deployment.

## Metadata
- **Published**: 2026-09-29T07:11:33Z
- **Authors**: Haoran Ou, Gelei Deng, Xuanye Zhang, Wenbo Guo, Tianwei Zhang, Kwok-Yan Lam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36879v1)