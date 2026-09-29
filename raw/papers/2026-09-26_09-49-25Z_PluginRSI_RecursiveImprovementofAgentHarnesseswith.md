---
title: PluginRSI: Recursive Improvement of Agent Harnesses with Reusable Plugins
published: 2026-09-26T09:49:25Z
authors: Yaorui Shi, Yuchun Miao, Yuxin Chen, Jiayuan Zhang, Yueqing Sun, Xierui Song, Xiang Wang, An Zhang
url: http://arxiv.org/abs/2609.32423v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PluginRSI: Recursive Improvement of Agent Harnesses with Reusable Plugins

## Abstract
The harness surrounding a language model is a central determinant of agent performance. Recent methods optimize harnesses by searching over complete programs, where individual mechanisms are difficult to isolate and reuse. We introduce PluginRSI, which represents a harness as a composition of atomized plugins and organizes harness evolution around these plugins. Individual plugins are improved independently and accumulated in a shared library, then recombined into new harnesses at each iteration. PluginRSI improves over existing harness optimization methods across software engineering, command-line interaction, and question-answering tasks. The resulting harnesses retain their advantage when transferred to other solver models without further optimization. The evolved plugin library accelerates subsequent optimization from the initial harness, which helps faster and higher convergence on unseen tasks. These results show that accumulating reusable mechanisms provides an effective basis for continued harness improvement.

## Metadata
- **Published**: 2026-09-26T09:49:25Z
- **Authors**: Yaorui Shi, Yuchun Miao, Yuxin Chen, Jiayuan Zhang, Yueqing Sun, Xierui Song, Xiang Wang, An Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32423v1)