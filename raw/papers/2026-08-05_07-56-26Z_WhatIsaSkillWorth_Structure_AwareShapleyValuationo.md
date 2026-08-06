---
title: What Is a Skill Worth? Structure-Aware Shapley Valuation of Agent Skills
published: 2026-08-05T07:56:26Z
authors: Tao Li, Junfeng Liu, Qinghua Zhao, Yifan Li, Lei Wang, Bo Shao, Xuejun Liu, Linjun Shou
url: http://arxiv.org/abs/2608.04562v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Is a Skill Worth? Structure-Aware Shapley Valuation of Agent Skills

## Abstract
Agent skills are increasingly optimized by automated feedback loops, producing long structured artifacts whose internal value remains unclear. We study skill valuation: assigning credit to the internal units of a fixed skill, such as rules, examples, scripts, and heuristics, under a fixed agent and held-out task distribution. Skill valuation differs from data or prompt-span valuation because skill units are structured: they may depend on other units, belong to a document hierarchy, trigger agent behavior, and consume limited prompt context. We introduce SkillSV, a structure-aware Shapley-style framework for skill valuation. SkillSV compiles a skill into units, dependencies, and hierarchy, so that only valid counterfactual skills are evaluated. It uses paired deletion and length-neutral padding to separate content value from context cost, and estimates the resulting values with a rollout-budgeted estimator for noisy agent evaluations. On four agentic benchmarks, we assess the faithfulness, actionability, and explanation of SkillSV: it recovers unit interactions, preserves aggregate skill lift, and guides safe pruning and compression.

## Metadata
- **Published**: 2026-08-05T07:56:26Z
- **Authors**: Tao Li, Junfeng Liu, Qinghua Zhao, Yifan Li, Lei Wang, Bo Shao, Xuejun Liu, Linjun Shou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04562v1)