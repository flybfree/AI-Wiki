---
title: Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives
published: 2026-09-30T03:57:46Z
authors: Peng Kuang, Haibo Jin, Dehao Wu, Feiyang Deng, Xiaopeng Yuan, Jerry Wang, Haohan Wang
url: http://arxiv.org/abs/2609.38912v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives

## Abstract
Agent harnesses govern how large language models (LLMs) gather context, invoke tools, verify results, preserve state, and terminate, largely affecting agent performance. However, the value of each harness mechanism can differ across heterogeneous tasks: a mechanism that improves one task may impose overhead or context distraction on another, leading to the suboptimality of a global harness. We characterize this suboptimality as a mismatch induced by fixed mechanism choices, motivating task-specific harness construction. Nonetheless, generating harness code for each task introduces generation and debugging costs, with execution risks that can compound as more mechanisms are generated. To address those challenges, we introduce Harness Primitives, reusable harness mechanisms with clear application scope and composition contract mined from failed task trajectories. Based on Harness Primitives, we propose STITCH, a framework that Selects suitable primitives given Task Information and compiles them into Task-speCific Harnesses at test time. This separation enables task-specific harnesses without generating or repairing mechanism code at test time. Extensive experiments demonstrate that STITCH not only improves harness adaptability and robustness, but also scales with the primitive library size, boosting task success rates by up to 12 points over fixed harness baselines, surpassing human-designed harnesses like Codex CLI while maintaining a minimal test-time harness composition overhead of only 2.7%, 638 times more efficient than generating task-specific harnesses from scratch. Ultimately, our work demonstrates that building task-adaptive harnesses can be beneficial for completing diverse tasks and that building reusable primitives can be a promising path towards this goal.

## Metadata
- **Published**: 2026-09-30T03:57:46Z
- **Authors**: Peng Kuang, Haibo Jin, Dehao Wu, Feiyang Deng, Xiaopeng Yuan, Jerry Wang, Haohan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38912v1)