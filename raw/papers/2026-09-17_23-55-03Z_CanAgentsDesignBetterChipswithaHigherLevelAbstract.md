---
title: Can Agents Design Better Chips with a Higher Level Abstraction?
published: 2026-09-17T23:55:03Z
authors: Zijian Ding, Yang Zou, Yizhou Sun, Jason Cong
url: http://arxiv.org/abs/2609.21157v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Agents Design Better Chips with a Higher Level Abstraction?

## Abstract
Large Language Model (LLM) agents are increasingly being explored for chip design, but most existing approaches operate directly at RTL. We ask whether agents can design better chips by leveraging higher-level abstractions. We compare Direct RTL Design, Agent-based HLS Design, Post-Compiler HLS Refinement, and Post-HLS RTL Refinement, and combine Agent-based HLS Design with Post-HLS RTL Refinement as Agent-based HLS with RTL Refinement (AHRR). We use FPGAs as a practical, easy-to-deploy platform for end-to-end evaluation, but note that the design-flow tradeoffs we study are largely independent of the target technology. Across a diverse 11-tasks benchmark suite, AHRR achieves a 2.6$\times$ geometric-mean speedup over Direct RTL Design across our benchmark suite. Case studies show that HLS distills design knowledge into abstractions that agents can leverage, while RTL refinement recovers lower-level optimization opportunities. Together, these results make AHRR a promising workflow for agentic chip design. The code and evaluation artifacts are available at https://github.com/ZijD/AHRR.

## Metadata
- **Published**: 2026-09-17T23:55:03Z
- **Authors**: Zijian Ding, Yang Zou, Yizhou Sun, Jason Cong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21157v1)