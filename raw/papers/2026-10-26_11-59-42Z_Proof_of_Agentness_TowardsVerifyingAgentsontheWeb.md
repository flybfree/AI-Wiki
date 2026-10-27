---
title: Proof-of-Agentness: Towards Verifying Agents on the Web
published: 2026-10-26T11:59:42Z
authors: Zuyao Xu, Xiang Li
url: http://arxiv.org/abs/2610.35288v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Proof-of-Agentness: Towards Verifying Agents on the Web

## Abstract
CAPTCHAs and bot detection have helped protect Web services from automated abuse for decades by distinguishing humans from bots. However, the emergence of LLM-powered agents introduces a new setting: Web services increasingly accommodate agents as legitimate users. Without a way to distinguish agents from other automated clients such as simple bots and scripts, these services risk large-scale automated junk submissions that waste service resources and consume users' attention or tokens. In this paper, we investigate a novel question for today's Web: "How can a Web service obtain evidence that a client is an agent?" We introduce the concept of "Proof-of-Agentness" (PoA), a mechanism for distinguishing agents from other automated clients, motivated by the parallel between human attention and an agent's inference resources. We outline two approaches: active verification through challenge-response and passive analysis of service-visible signals. Eight language models achieve an overall accuracy of 96.5% on our challenges, with an average overhead of 1,647 tokens. For passive analysis, we conduct an IRB-approved user study comparing the Web interactions of twelve human participants and representative Bot and Agent implementations, achieving an average classification accuracy of 95.8% across four classifiers, motivating further study.

## Metadata
- **Published**: 2026-10-26T11:59:42Z
- **Authors**: Zuyao Xu, Xiang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35288v1)