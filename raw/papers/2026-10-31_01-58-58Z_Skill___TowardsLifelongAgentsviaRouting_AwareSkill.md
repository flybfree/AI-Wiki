---
title: Skill++: Towards Lifelong Agents via Routing-Aware Skill Refinement
published: 2026-10-31T01:58:58Z
authors: Hanrong Zhang, Minghao Liang, Jiawei Wu, Yankai Chen, Shicheng Fan, Zhiwei Liu, Enze Ma, Junwei Yuan, Tianyi Wang, Dehai Min, Kening Zheng, Xue Liu, Philip S. Yu
url: http://arxiv.org/abs/2611.00544v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Skill++: Towards Lifelong Agents via Routing-Aware Skill Refinement

## Abstract
Large language model (LLM) agents extend their capabilities with skills, each with a name, a description, and a body. Under progressive disclosure, an LLM router selects skills by name and description alone and loads only the selected bodies. Skill libraries grow continually as users and agents add new skills. Because the router relies on this metadata, a similar new skill can displace an earlier one, breaking previously correct routing even though the earlier skill and the router are unchanged. This routing interference is aggravated for public skills, whose descriptions may not match their bodies. We formulate the problem as lifelong skill routing, a class-incremental continual learning problem. A solution must keep earlier skills selectable without suppressing new ones. Existing approaches fall short, since continually retraining the router risks catastrophic forgetting and rewriting methods either ignore similar skills or require per-skill feedback. We therefore propose Skill++, which rewrites only the name and description of each incoming skill, without router training or labeled data. The new description states what the body supports, how the skill differs from its closest predecessor, and what related work it excludes. As a library grows to 731 skills over ten sessions, Skill++ selects all required skills for 76.3% of queries, versus 36.4% under the original metadata. Across three benchmarks and five LLM routers, it outperforms all compared approaches, and its gains carry over to the Codex CLI agent harness.

## Metadata
- **Published**: 2026-10-31T01:58:58Z
- **Authors**: Hanrong Zhang, Minghao Liang, Jiawei Wu, Yankai Chen, Shicheng Fan, Zhiwei Liu, Enze Ma, Junwei Yuan, Tianyi Wang, Dehai Min, Kening Zheng, Xue Liu, Philip S. Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.00544v1)