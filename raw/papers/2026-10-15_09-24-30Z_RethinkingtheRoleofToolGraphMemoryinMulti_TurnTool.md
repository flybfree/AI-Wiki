---
title: Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use
published: 2026-10-15T09:24:30Z
authors: Uiji Hwang, Richeng Xuan, Taeuk Kim
url: http://arxiv.org/abs/2610.21571v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use

## Abstract
Large language model (LLM) agents solve complex tasks by calling external tools over multiple turns. Recent work has proposed tool graph memory, which stores past experience as tool transitions to guide subsequent selection. However, it remains unclear whether this component consistently improves agents' tool use or undermines it. We evaluate tool graph memory on nine models and two benchmarks, finding that it seldom improves significantly over baselines, and that its gains, where present, cost over twice the LLM calls. The memory's guidance is often incorrect, and random or no guidance retains most of the gain, implying that the benefit stems from extra computation rather than the memory itself. Moreover, even with the correct next tool suggested, many failures remain, such as giving up without a tool call. Storing the same experience instead as textual insights outperforms tool graph memory with almost no extra LLM calls. This suggests that memory serves better as a soft prior than as a prescription of the next tool, leading to a more effective and generalizable solution.

## Metadata
- **Published**: 2026-10-15T09:24:30Z
- **Authors**: Uiji Hwang, Richeng Xuan, Taeuk Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21571v1)