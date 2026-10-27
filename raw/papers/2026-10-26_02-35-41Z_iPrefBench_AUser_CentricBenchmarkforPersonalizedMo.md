---
title: iPrefBench: A User-Centric Benchmark for Personalized Mobile Use Agents
published: 2026-10-26T02:35:41Z
authors: Yuting Ning, Ruijia Cheng, Sushobhan Ghosh, Peitong Duan, HungShi Lin, Abhishek Sundararajan, Shreyash Pandey, Huan Sun, Jeffrey Nichols, Eldon Schoop
url: http://arxiv.org/abs/2610.34735v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# iPrefBench: A User-Centric Benchmark for Personalized Mobile Use Agents

## Abstract
An agent that truly knows and acts on behalf of its user has been a long-standing promise of AI assistants. Computer-use agents bring this promise within reach by capably executing fully specified tasks across apps. However, real-world user requests are often underspecified. To act correctly for the particular user, an agent must infer some missing information from the user's activity history and ask for other information that only the user can provide, without making unsupported assumptions or burdening the user with unnecessary questions. We present iPrefBench, a benchmark for evaluating the infer and ask capabilities of personal mobile-use agents in an executable iOS environment with an interactive simulated user. Grounded in a coherent persona with 3,051 past activity events, iPrefBench comprises 130 underspecified user tasks across 26 apps. Each omitted user-dependent requirement is, by construction, either history-inferable or ask-only. iPrefBench evaluates personalized mobile agents on both whether agents complete tasks correctly for the user (i.e., personalized task completion) and whether they seek user input when necessary (i.e., user-agent interaction). Evaluation of 7 frontier agents reveals a substantial gap between execution and personalization. Agents achieve high action completion scores (up to 91.6%) but low full task success (up to 47.7%) because personalization lags behind. They especially struggle with ask-only information, failing to request enough necessary information. Our findings highlight a challenge for personalized agents in knowing what to infer and when to ask. We hope that iPrefBench can serve as a valuable testbed for building agents that know their user and work with them.

## Metadata
- **Published**: 2026-10-26T02:35:41Z
- **Authors**: Yuting Ning, Ruijia Cheng, Sushobhan Ghosh, Peitong Duan, HungShi Lin, Abhishek Sundararajan, Shreyash Pandey, Huan Sun, Jeffrey Nichols, Eldon Schoop
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34735v1)