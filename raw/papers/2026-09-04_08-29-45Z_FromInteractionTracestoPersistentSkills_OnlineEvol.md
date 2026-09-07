---
title: From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents
published: 2026-09-04T08:29:45Z
authors: Longtao Hu, Xiao Liang, Linchao Zhu
url: http://arxiv.org/abs/2609.04869v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents

## Abstract
Computer-use agents can execute increasingly complex tasks in graphical interfaces, but their interaction experience is typically transient: procedural knowledge acquired from one rollout is not systematically retained, refined, and reused in later tasks. Existing skill libraries provide external procedural knowledge, yet their incremental value over the same agent operating without skills, as well as their longitudinal dynamics under repeated interaction, remain insufficiently characterized. We present an online skill-evolution framework that converts interaction trajectories and evaluator feedback into a persistent, versioned library of reusable procedures. Each iteration executes against a frozen library snapshot, and evidence-guided skill updates become available in subsequent iterations without changing model parameters. We compare the full evolving-library system with a configuration-matched empty-library control across four OSWorld application domains under the same fixed action-generation and GUI-grounding stack, task sets, and iteration horizons. Following a five-iteration empty-library warm-up, Full attains a higher post-warm-up mean evaluator score in all four observed domain runs, with mean differences ranging from 5.7 to 18.6 percentage points and domain-dependent temporal stability. In GIMP, provenance-aware analysis reveals retrieval across task-of-origin boundaries and revision churn, where repeated accepted edits fail to recover the originating task. These findings characterize evolving skill libraries as auditable, shared procedural memory that can improve a fixed computer-use stack, while showing that their benefits are conditional and repeated revision does not guarantee recovery. Code is released at https://github.com/LongtaoHu/Skill-Evo4GUI.

## Metadata
- **Published**: 2026-09-04T08:29:45Z
- **Authors**: Longtao Hu, Xiao Liang, Linchao Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04869v1)