---
title: Managing Context and Communication in Distributed Agentic UAV Swarms
published: 2026-10-01T12:30:29Z
authors: Andrea Iannoli, Ivan Zyrianoff, Angelo Trotta, Lorenzo Gigli, Marco Di Felice
url: http://arxiv.org/abs/2610.01569v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Managing Context and Communication in Distributed Agentic UAV Swarms

## Abstract
Unmanned aerial vehicle (UAV) swarms increasingly rely on language-model agents to provide adaptive mission-level reasoning in uncertain environments. Fully distributed control, in which each UAV hosts an independent Small Language Model (SLM), removes reliance on a centralized coordinator but introduces an information-management problem: long-running interaction histories can degrade the reasoning context, while indiscriminate information dissemination increases communication and inference overhead. We address these challenges with a distributed UAV-agent architecture that enables continuous local SLM control through an event-driven reason-act-observe lifecycle. Runtime knowledge is represented as structured atomic notes and organized into core, local, and peer-specific memory. A deterministic interest-aware gossip engine selectively disseminates these notes according to recipient-specific semantic novelty and recency. We evaluate the architecture using ten UAVs in a simulated search-and-rescue mission. Our approach completes all experimental runs, whereas unrestricted flooding messages completes only 70-85\%, and delegating forwarding decisions to the SLM prevents mission completion in every run. Compared with unrestricted flooding, our approach approximately halves inference-token consumption, reduces transmitted data, and achieves lower survivor-count error.

## Metadata
- **Published**: 2026-10-01T12:30:29Z
- **Authors**: Andrea Iannoli, Ivan Zyrianoff, Angelo Trotta, Lorenzo Gigli, Marco Di Felice
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01569v1)