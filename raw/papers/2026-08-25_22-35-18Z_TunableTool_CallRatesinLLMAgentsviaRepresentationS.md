---
title: Tunable Tool-Call Rates in LLM Agents via Representation Steering
published: 2026-08-25T22:35:18Z
authors: Yuqi Chen, Vincent Siu, Yang Liu, Dawn Song, Chenguang Wang
url: http://arxiv.org/abs/2608.25198v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tunable Tool-Call Rates in LLM Agents via Representation Steering

## Abstract
Deciding whether to call a tool is a core competence of an LLM agent, and a costly one to get wrong: needless calls add latency, accrue cost, and may trigger irreversible side effects, while missing calls leave the model confidently wrong on questions it could only answer through tool-calls. Models manage this balance poorly, both over-using and under-using tools. Existing methods such as post-training and prompt engineering are expensive and difficult to modify at inference time. We show that whether an instruction-tuned model calls a tool can be controlled by a single linear direction in its residual stream, extracted without any training from the model's own tool-use preference signal and turned into an inference-time intervention with no prompt change. Adding the direction with strength $α$ moves the call rate monotonically from near $0\% $ to over $90\%$ while keeping calls well-formed. The steering works in both directions: dialing it down suppresses calls, and dialing it up induces new calls that land precisely on the questions the model cannot answer from its own knowledge. We also show that the direction generalizes to unseen tools with strength comparable to each tool's own direction and without favoring any specific tool choice. With live tool execution, a single sweep of the steering traces a cost/accuracy Pareto frontier and nearly doubles open-domain QA accuracy ($0.29 \! \rightarrow \! 0.56$); the same recipe transfers across a diverse range of models spanning dense, MoE, and multimodal architectures, without any training. Our code is publicly available at https://github.com/YuqiChen4188/Steering-Tool-Use-Propensity.

## Metadata
- **Published**: 2026-08-25T22:35:18Z
- **Authors**: Yuqi Chen, Vincent Siu, Yang Liu, Dawn Song, Chenguang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25198v1)