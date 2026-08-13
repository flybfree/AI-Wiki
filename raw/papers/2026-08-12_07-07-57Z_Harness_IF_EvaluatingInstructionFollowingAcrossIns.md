---
title: Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents
published: 2026-08-12T07:07:57Z
authors: Zining Huang, Haoran Que, Hong Zeng, Ge Zhang, Zuo Wang, Jin Chen, Haodong Wang, Zhongfei Hou, Changxin Pu, Shen Yan, Wenhao Huang
url: http://arxiv.org/abs/2608.11727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents

## Abstract
When a coding agent obeys a rule, it may simply have been going to do that anyway. Existing instruction-following benchmarks cannot tell the difference: they concentrate rules in the user turn, while coding-agent benchmarks emphasize final task success. We introduce Harness-IF, which scores operational rules one at a time from execution evidence: 60 realistic multi-turn coding items drawn from a 642-rule library, 256 rules receiving verdicts, placed on the five configurable surfaces a deployed agent reads. To separate compliance from coincidence we introduce Against-Prior Accuracy (AP-Acc), which scores only rules labeled as opposing unprompted defaults, observed by re-running tasks with the rule withheld across nine probe builds and curated otherwise. Across 12 frontier models, accuracy spans 72.1-85.9% and AP-Acc 66.1-78.6%; every model is worse on against-prior rules, by 3.6 to 7.4 points (mean 5.81), and the direction survives a common-support analysis with item-clustered intervals. Aggregate scores therefore overstate compliance by a model-specific margin: prior control leaves the top build unchanged and exchanges three adjacent rank pairs. A counterbalanced conflict pilot on nine separate builds adds a second result: pooled precedence does not follow prompt depth, with system prompts, project files, and user instructions ahead of tool and skill descriptions.

## Metadata
- **Published**: 2026-08-12T07:07:57Z
- **Authors**: Zining Huang, Haoran Que, Hong Zeng, Ge Zhang, Zuo Wang, Jin Chen, Haodong Wang, Zhongfei Hou, Changxin Pu, Shen Yan, Wenhao Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11727v1)