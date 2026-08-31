---
title: The Calls are Coming from Inside the Model: Investigating Probe-based Detection of Tool-Calling Errors in LLMs
published: 2026-08-27T22:26:25Z
authors: Eric Yeats, Brendan Kennedy, Loc Truong, John Buckheit, Jung Lee, Jesse Friedbaum, John Emanuello, Henry Kvinge
url: http://arxiv.org/abs/2608.27750v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Calls are Coming from Inside the Model: Investigating Probe-based Detection of Tool-Calling Errors in LLMs

## Abstract
The hidden states of large language models (LLMs) are known to capture rich information relating to model knowledge and behavior that can be hard to extract from examination of input and output alone. As LLM-based systems increasingly interface with the external world, one area of concern is detecting incorrect or improper use of tools. Motivated by this, we study the effectiveness of using linear probes to detect incorrect tool-calls, measuring probe efficacy across 18 tool-calling LLMs evaluated on the Berkeley Function Calling Leaderboard. Overall, we find that probing is an effective means to catch a range of different tool-calling errors, including errors arising from using an argument that has the wrong value but the correct type, which might not be recorded by standard logging frameworks. Important factors in success include model size, probing layer, and model post-training type. We also show that probes are capable of generalizing to novel types of errors, which is critical in real world deployments.

## Metadata
- **Published**: 2026-08-27T22:26:25Z
- **Authors**: Eric Yeats, Brendan Kennedy, Loc Truong, John Buckheit, Jung Lee, Jesse Friedbaum, John Emanuello, Henry Kvinge
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27750v1)