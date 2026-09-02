---
title: Auditing Harness Tampering in Self-Improving Agents
published: 2026-08-30T17:18:56Z
authors: Xing Wang, Xiaoyi Zhang, Jie Shao
url: http://arxiv.org/abs/2609.00069v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Harness Tampering in Self-Improving Agents

## Abstract
Self-improving agents iteratively modify their own harness to push the frontier of their performance. However, such modifications can produce illusory performance gains or compromise integrity constraints such as authorization, provenance, and completeness without genuinely improving capability. We term this phenomenon as harness tampering, which extends the concept from reward and measurement tampering to the full self-improvement lifecycle. To systematically study this problem, we propose a two-axis taxonomy that categorizes each misaligned edit by the harness functional role in which it occurs and the obligation it violates. Then we build an annotated corpus by seeding tampered-benign edit pairs into the real trajectories of self-improving agents. We adapt and benchmark diverse audit methods on tampering classification and localization tasks. Finally we systematically audit real trajectories of self-improving agents. The results demonstrate that harness tampering consistently occurs in real runs from different agents, often persists in the lineage of the best agent, and forms distinct system-specific profiles across the taxonomy.

## Metadata
- **Published**: 2026-08-30T17:18:56Z
- **Authors**: Xing Wang, Xiaoyi Zhang, Jie Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00069v1)