---
title: Defense-in-Depth for LLMs: Evaluating Memory Gates Against Activation-Induced and Memory-Induced Sycophancy
published: 2026-10-05T21:16:06Z
authors: Ritvij Sharma, Russell Dlugosz, Ryan Zhou, Maheep Chaudhary
url: http://arxiv.org/abs/2610.07403v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Defense-in-Depth for LLMs: Evaluating Memory Gates Against Activation-Induced and Memory-Induced Sycophancy

## Abstract
Long-term memory allows Large Language Models (LLMs) to maintain personalized context across interactions, but retrieved user history can induce memory-induced sycophancy, causing models to favor stored user beliefs over objective evidence. Existing defenses primarily operate on retrieved context and are rarely evaluated jointly with internal behavioral bias. We introduce a $2 \times 2$ defense-in-depth framework separating internal activation steering from external memory handling. We extract sycophancy steering directions from 100 paired prompts and evaluate four open-weight models across 10 steering coefficients and five memory-defense configurations on MemSyco-Bench (answers for all 1,550 items; defense conditions judged on a fixed 250-item subsample), with three LLM judges. Three of the five configurations are new (rewriting every memory, a Router Gate that keeps, rewrites, or drops each memory, and dropping all memory); the other two are MemSyco's baselines. Selective Router Gate filtering preserves substantially more of MemSyco's average accuracy than complete memory removal, and this separation persists when the models are steered toward sycophancy. On Llama 3.1 8B with Router Gate, mild inverse steering ($α= -1.5$) lowers judge-averaged sycophancy from 35.80% to 31.32% while average accuracy moves from 43.99% to 43.31%; this reduction has the same direction under all three judges but is not statistically significant (paired $p = 0.08$ to $0.63$ on 149 items). External memory filtering is the part of the design that holds up; our data do not show that inverse steering adds to it.

## Metadata
- **Published**: 2026-10-05T21:16:06Z
- **Authors**: Ritvij Sharma, Russell Dlugosz, Ryan Zhou, Maheep Chaudhary
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07403v1)