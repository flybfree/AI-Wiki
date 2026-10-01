---
title: "Summary: Self-Evolving Harness on Multiple Tasks with the Agent as Its Own Optimizer"
published: 2026-09-29T18:33:27Z
authors: [Qiankai Xu]
type: paper-summary
tags: [paper-summary, arxiv, agent-harnesses, self-improvement]
source_paper: "2026-09-29_18-33-27Z_Self_EvolvingHarnessonMultipleTaskswiththeAgentasItsI.md"
---
# Summary: Self-Evolving Harness on Multiple Tasks with the Agent as Its Own Optimizer

## Finding
The paper presents a self-evolving harness in which the same frozen model first solves tasks and then edits the harness using complete execution records. Evolution spans multiple domains with held-out and out-of-distribution benchmarks rather than optimizing one benchmark-specific harness.

Starting from a 49-line seed harness, the first evolution stage reportedly improves average performance by 4.48 points on in-distribution tasks and 12.64 points on out-of-distribution tasks. Continued evolution on Claw-Eval raises performance from 66.17 to 68.06. Emergent mechanisms include output truncation, history compaction, and independent review.

## Why it matters
The result treats harness design as a trainable, reusable system layer rather than a fixed wrapper around a model. The cross-task gains are especially relevant: they suggest that harness improvements can transfer when evolution is evaluated against diverse tasks, while also making regression control and provenance essential.

## Caveat
The reported results are paper authors' benchmark results and require independent reproduction, especially on task leakage, model dependence, and whether evolved mechanisms remain safe under production tool access.

## Canonical original paper
[ArXiv: Self-Evolving Harness on Multiple Tasks with the Agent as Its Own Optimizer](http://arxiv.org/abs/2609.38372v1)
