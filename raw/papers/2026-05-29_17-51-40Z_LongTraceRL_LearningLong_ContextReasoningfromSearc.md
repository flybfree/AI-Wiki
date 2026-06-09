---
title: LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards
published: 2026-05-29T17:51:40Z
authors: Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li
url: http://arxiv.org/abs/2605.31584v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards

## Abstract
Long-context reasoning remains a central challenge for large language models, which often fail to locate and integrate key information in extensive distracting content. Reinforcement learning with verifiable rewards (RLVR) has shown promise for this task, yet existing methods are limited by low-confusability distractors and sparse, outcome-only reward signals that cannot supervise intermediate reasoning steps. To address these issues, we introduce \textsc{LongTraceRL}. For data construction, we generate multi-hop questions via knowledge graph random walks and leverage search agent trajectories to build \emph{tiered distractors}: documents the agent read but did not cite (high confusability) and documents that appeared in search results but were never opened (low confusability), producing training contexts that are far more challenging than those built by random sampling or one-shot search. For reward design, we propose a \emph{rubric reward} that uses the gold entities along each reasoning chain as fine-grained, entity-level process supervision. This rubric reward is applied only to responses with correct final answers (positive-only strategy), distinguishing the reasoning quality among correct responses and preventing reward hacking. Experiments on three reasoning LLMs (4B--30B) across five long-context benchmarks demonstrate that \textsc{LongTraceRL} consistently outperforms strong baselines and encourages comprehensive, evidence-grounded reasoning. Codes, datasets and models are available at \href{https://github.com/THU-KEG/LongTraceRL}{https://github.com/THU-KEG/LongTraceRL}.

## Metadata
- **Published**: 2026-05-29T17:51:40Z
- **Authors**: Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.31584v1)