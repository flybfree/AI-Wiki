---
title: "Summary: Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives"
published: 2026-09-30T03:57:46Z
authors: [Peng Kuang, Haibo Jin, Dehao Wu, Feiyang Deng, Xiaopeng Yuan, Jerry Wang, Haohan Wang]
type: paper-summary
tags: [paper-summary, arxiv, agent-harnesses, test-time-composition]
source_paper: "2026-09-30_03-57-46Z_ComposingTask_specificAgentHarnessesatTestTimewith.md"
---
# Summary: Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives

## Finding
STITCH selects reusable harness primitives from task information and compiles them into task-specific harnesses at test time. The primitives encode mechanisms such as context gathering, tool use, verification, state handling, and termination, with explicit application scope and composition contracts mined from failed trajectories.

The authors report up to 12-point gains over fixed-harness baselines, while test-time composition adds only 2.7% overhead and is reported as 638 times more efficient than generating task-specific harness code from scratch.

## Why it matters
A single global harness can impose the wrong mechanisms on heterogeneous tasks. A library of reusable, constrained primitives offers a middle path between brittle fixed orchestration and risky code generation: adapt the control loop without rewriting executable harness logic during each task.

## Caveat
The benchmark and efficiency claims require independent reproduction across models, primitive libraries, and adversarial tasks. Composition contracts must also be treated as security boundaries when primitives can invoke tools.

## Canonical original paper
[ArXiv: Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives](http://arxiv.org/abs/2609.38912v1)
