---
title: AuthorityLens: Rethinking LLM-Based Agent Systems Through the Lens of Authority
published: 2026-09-26T08:53:11Z
authors: Shaojin Chen, Huihao Jing, Wun Yu Chan, Wenbin Hu, Jiaxing Li, Wu Pandy Pui Ching, Kshitij Bhatia, Xinlei He, Haoran Li, Yangqiu Song
url: http://arxiv.org/abs/2609.32378v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AuthorityLens: Rethinking LLM-Based Agent Systems Through the Lens of Authority

## Abstract
LLM-based agents are increasingly deployed with authority over consequential resources and decisions in real systems. These agents often operate alongside human and LLM-based participants who hold different forms of authority. Yet workflow roles, permission settings, and review mechanisms do not necessarily reflect the authority realized in practice. We introduce AuthorityLens, a framework for measuring a system's authority structure. Starting from an authority portfolio, we evaluate a system along three dimensions: what the system is authorized to do (System Authority), how much joint participation is required to exercise that authority (Authority Separation), and how much authority each participant holds (Principal Authority). We derive these measurements from the minimal combinations of participants sufficient to realize each outcome across admissible runtime states. We apply AuthorityLens to Codex, OpenCode, and Gemini CLI across 13 operating configurations over a common portfolio of agent operations. We find that nominal configurations do not map cleanly onto realized authority. In Codex, Full Access changes System Authority only marginally while substantially concentrating authority in the executing Assistant. OpenCode's Build and Plan configurations have the same System Authority and Authority Separation despite different workflows and root-level permissions. In Gemini CLI, model-based review increases Authority Separation without changing System Authority. Principal Authority further distinguishes authority replication from authority separation: spawned or delegated agents can become alternative holders of the same authority without increasing the required joint participation. Together, these results demonstrate that AuthorityLens provides a unified framework for measuring and comparing realized authority structures across agent systems.

## Metadata
- **Published**: 2026-09-26T08:53:11Z
- **Authors**: Shaojin Chen, Huihao Jing, Wun Yu Chan, Wenbin Hu, Jiaxing Li, Wu Pandy Pui Ching, Kshitij Bhatia, Xinlei He, Haoran Li, Yangqiu Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32378v1)