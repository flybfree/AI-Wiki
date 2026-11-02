---
title: Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems
published: 2026-10-28T20:40:33Z
authors: Zhuoyun Li, Boxuan Wang, Jinwei Hu, Xiaowei Huang, Yi Dong
url: http://arxiv.org/abs/2610.38869v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems

## Abstract
Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments across retrieval, memory, tools, and peer communication. In this paper, we define belief as an engineering abstraction for evidence-based commitments that guide downstream action. Building on this view, we propose the Explicit Belief Multi-Agent System (EB-MAS), which externalizes belief states into a structured substrate, uses belief operators to propose candidate updates, and applies a Cognitive Firewall to bound or reject updates that are weakly evidenced but strongly driven by vulnerability cues. We also discuss the risk of group belief at the group level, including manufactured consensus, collusion, and cascading misinformation, and outline practical integration challenges around grounding, false positives, scalability, and ethical misuse. Therefore, scalable agent safety requires not only better output filtering or stronger base models, but also explicit interfaces for tracing, calibrating, and constraining belief revision at runtime.

## Metadata
- **Published**: 2026-10-28T20:40:33Z
- **Authors**: Zhuoyun Li, Boxuan Wang, Jinwei Hu, Xiaowei Huang, Yi Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.38869v1)