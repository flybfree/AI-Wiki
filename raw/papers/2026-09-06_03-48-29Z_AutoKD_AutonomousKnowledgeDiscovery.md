---
title: AutoKD: Autonomous Knowledge Discovery
published: 2026-09-06T03:48:29Z
authors: Qinwen Ge, Bo Ni, Haowei Fu, Ngoc N. Tran, Erik Blasch, Tyler Derr
url: http://arxiv.org/abs/2609.06366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoKD: Autonomous Knowledge Discovery

## Abstract
Scientific discovery in data-rich domains is currently constrained by human bandwidth: the growth in the volume and complexity of real-world data far outpaces the rate at which researchers can read, reason, and synthesize. Recent LLM-based multi-agent systems have begun to automate portions of the research cycle, but they target hypothesis generation in settings where validation cannot itself be automated, and each run is one-shot, with no mechanism for findings to accumulate or steer subsequent inquiry. This paper introduces AutoKD, a multi-agent framework for autonomous knowledge discovery that is both computational and cumulative, allowing validated findings to persist and inform subsequent inquiry. Six coordinated LLM agents collaborate in an open-ended discovery loop, where accepted findings are stored in a persistent insight graph that serves as both long-term memory and an exploration-steering mechanism. We evaluate AutoKD on three diverse datasets from two perspectives: Open-ended Quality against published findings, and Conditioned Quality via literature-derived queries. Across both evaluation perspectives, AutoKD covers known findings and surfaces substantive discoveries that complement human-driven research. Our code is available at https://github.com/GeQinwen/AutoKD.

## Metadata
- **Published**: 2026-09-06T03:48:29Z
- **Authors**: Qinwen Ge, Bo Ni, Haowei Fu, Ngoc N. Tran, Erik Blasch, Tyler Derr
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06366v1)