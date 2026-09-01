---
title: MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents
published: 2026-08-31T16:05:39Z
authors: Vernon Toh, Navonil Majumder, Zhengyuan Liu, Nancy F. Chen, Soujanya Poria
url: http://arxiv.org/abs/2608.31022v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents

## Abstract
AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities. We address this with MNIST-PRO, a benchmark that isolates agentic perception by converting MNIST digit recognition into a sequential, glimpse-based search task with lookback constraints. We evaluate ten multimodal models across four memory representations, including raw visual history, textual states, structured metric grid maps, and a consolidated visual canvas. While models excel under full observability, partial observability exposes a clear performance gap. We identify three distinct bottlenecks. First, perceptual-state construction and interpretation present a challenge, as agents struggle to integrate fragmented glimpses. Second, agents often stop exploring before they see the full sequence. Third, models often fail to revise early, incorrect beliefs even when faced with subsequent contradictory evidence. These results show that simply acquiring visual evidence is not enough. Agents must also be able to build and update a reliable perceptual state.

## Metadata
- **Published**: 2026-08-31T16:05:39Z
- **Authors**: Vernon Toh, Navonil Majumder, Zhengyuan Liu, Nancy F. Chen, Soujanya Poria
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.31022v1)