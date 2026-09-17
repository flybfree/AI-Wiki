---
title: M-SQE: Multilingual Skill Quality Estimation for Enhancing Language Equality in Agentic Skill Use
published: 2026-09-16T10:36:32Z
authors: Yilun Liu, Shimin Tao, Minggui He, Chenxin Liu, Li Zhang, Chen Liu, Miao Zhang, Jiaxin Guo, Min Zhang, Liqun Deng, Xiaojun Meng, Daimeng Wei
url: http://arxiv.org/abs/2609.18445v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# M-SQE: Multilingual Skill Quality Estimation for Enhancing Language Equality in Agentic Skill Use

## Abstract
Agent skills, reusable procedural documents that extend LLM agents beyond their parametric memory, have become an important interface for deploying agents on real-world tasks. Community-maintained skill libraries built around this interface are growing rapidly. However, this ecosystem remains deeply English-centric: our audit finds that low-resource languages such as Swahili and Hindi have no in-language skill content, so retrieval often returns a skill written in a different language than the query, degrading accuracy and recall. A practical solution is to synthesize in-language skills for retrieval but the quality can be unreliable, so relevance in this setting alone often surfaces a related but unusable candidate. To address this, we propose M-SQE, a post-retrieval Multilingual Skill Quality Estimation framework that scores candidates via a Theory view for intrinsic quality and an Action view for task-grounded utility, unified into a domain-conditioned final score. We evaluate M-SQE across three skill-use domains: general, tool-use, and cultural tasks. Empirically, we build three-layer candidate skill pools mirroring today's ecosystem, where M-SQE's task success exceeds existing baseline's average by at least +3.5 points across three different retrievers. Particularly, M-SQE lifts the lowest-resource languages most (+12.9pp on Hindi and +5.6pp on Swahili) and achieves strong performance across all six culture regions, thereby moving agentic skill use toward linguistic and cultural equality.

## Metadata
- **Published**: 2026-09-16T10:36:32Z
- **Authors**: Yilun Liu, Shimin Tao, Minggui He, Chenxin Liu, Li Zhang, Chen Liu, Miao Zhang, Jiaxin Guo, Min Zhang, Liqun Deng, Xiaojun Meng, Daimeng Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18445v1)