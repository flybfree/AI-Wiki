---
title: Editing as Language: Teaching LLM Agents a Grammar for Native Context Editing
published: 2026-10-18T21:48:56Z
authors: Yunlong Deng, Yan Li, Xing Hu, Yida Zhu, Sean Du, Weiyang Liu, Guangyi Chen
url: http://arxiv.org/abs/2610.25550v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Editing as Language: Teaching LLM Agents a Grammar for Native Context Editing

## Abstract
A synopsis in novels folds a story into a few lines; a function in code gathers many steps with a single execution. Context editing is native to language itself. In this paper, we propose the Native Context Editing (NCE) framework, which gives language model agents a grammar for natively editing their own context. By encoding context-editing operations in a grammar of dedicated special tokens, we teach the agents to invoke edits through the language itself. We train agents on iteratively constructed trajectory segments, with each teacher edit conditioned on the evolving context. This establishes context editing as an atomic and inherent capability of LLM agents, enabling them to dynamically modify their context as they generate responses over long-horizon reasoning and interaction. Compared with context-editing methods that learn to generate tool-use code within specific external harness environments, our approach integrates context editing as an internal mechanism of the model's native generation process, enabling better generalization across diverse real-world workflows. On four long-horizon agentic benchmarks (Terminal-Bench 2.0, SWE-bench Verified, SWE-bench Multilingual, and SWE-bench Pro), NCE improves the average task success rate over the base model by 5.6 percentage points for LongCat-Flash-Lite-Sparse and by 4.5 for Qwen3.6-35B-A3B, while reducing average token usage by 36% and 15%, respectively.

## Metadata
- **Published**: 2026-10-18T21:48:56Z
- **Authors**: Yunlong Deng, Yan Li, Xing Hu, Yida Zhu, Sean Du, Weiyang Liu, Guangyi Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25550v1)