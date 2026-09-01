---
title: BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks
published: 2026-08-31T12:59:33Z
authors: Pradyumna Shyama Prasad, Meiri Anto, Leon Eshuijs, Julian Moncarz, Kaustubh Kislay, Juan J. Vazquez
url: http://arxiv.org/abs/2608.30724v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks

## Abstract
LLM agents are increasingly used to run autonomous ML experiments, iterating on target metrics with little human oversight. Prior work has documented reward hacking in these environments, bringing into question the validity of produced research and the broader safety case for AI R&D. Existing benchmarks do not measure exploits that live in the data or the modeling task itself. We introduce BAITBENCH, a suite of three synthetic tabular ML tasks that each contain a shortcut that allows agents to inflate the public test score but fail on a hidden test set. Since the shortcut is optional and using it breaks no stated rule, BAITBENCH measures how often models exploit the shortcut to achieve inflated scores. Across seven frontier agents scored by our two-stage judge pipeline, 57.1% of runs exhibit reward hacking, with five of seven above 50%. Agents cheat even under a second condition where they are prompted not to -the mean cheating rate remains above 50%. We release BAITBENCH, along with the judge implementation, and an annotated dataset of transcripts containing reward hacks as a testbed for evaluating reward-hacking mitigations head-to-head.

## Metadata
- **Published**: 2026-08-31T12:59:33Z
- **Authors**: Pradyumna Shyama Prasad, Meiri Anto, Leon Eshuijs, Julian Moncarz, Kaustubh Kislay, Juan J. Vazquez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30724v1)