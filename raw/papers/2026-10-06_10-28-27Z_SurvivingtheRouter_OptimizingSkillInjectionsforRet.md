---
title: Surviving the Router: Optimizing Skill Injections for Retrieval and Execution
published: 2026-10-06T10:28:27Z
authors: Haneen Najjar, Luca Scionis, Haritz Puerto, Sahar Abdelnabi
url: http://arxiv.org/abs/2610.08098v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Surviving the Router: Optimizing Skill Injections for Retrieval and Execution

## Abstract
AI agents increasingly rely on modular third-party "skills" that are dynamically selected by skill routers to execute complex tasks. While recent studies highlight the threat of prompt injections embedded in these skills, existing evaluations often assume settings where the malicious skill is already selected for execution. We show that this assumption can substantially overestimate attack success. In realistic multi-skill environments, injected skills must first compete for retrieval, reducing the effective attack success rate (ASR) of existing injections by 87-97%. To address this limitation, we introduce CORSA (Cluster Optimization for Router-Aware Skill Attacks), a router-aware attack that optimizes skill injections for both retrieval and execution across clusters of related tasks. We evaluate skill injection attacks under router-managed multi-skill settings by extending the benchmark introduced by SkillRouter with eight malicious payload categories. CORSA uses successive optimization stages to first improve retrieval and then optimize end-to-end attack success, while we evaluate user utility and injection naturalism separately. Our experiments show that CORSA substantially improves both retrieval and end-to-end attack success over existing skill injections while preserving user utility, and that the resulting attacks transfer across different router architectures and LLM backbones.

## Metadata
- **Published**: 2026-10-06T10:28:27Z
- **Authors**: Haneen Najjar, Luca Scionis, Haritz Puerto, Sahar Abdelnabi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08098v1)