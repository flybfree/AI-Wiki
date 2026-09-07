---
title: AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems
published: 2026-09-04T08:30:36Z
authors: Qi Zhang, Yanlin Chen, Wenchao Xiao
url: http://arxiv.org/abs/2609.04871v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems

## Abstract
Improving an industrial recommender is an iterative research-and-engineering process rather than a direct path from idea to deployment. In \textbf{DASHEN, NetEase's gaming-community app}, algorithm engineers typically identify promising directions from research papers, technical reports, and prior production experiments; reproduce or adapt the underlying methods; implement them in the production codebase; and evaluate the resulting models through training and offline experiments. Promising candidates are then advanced to online A/B tests, and those demonstrating robust gains are submitted to Launch Review---the internal gate for full-traffic rollout. Large language models (LLMs) can assist with individual stages of this workflow, but the overall process remains human-dependent without a harness that can reliably coordinate them across long-running, often multi-day experimental cycles. We present \textbf{AutoLR}, initially built as \textbf{Auto Launch Review} and later extended upstream into an autonomous research-to-launch harness. AutoLR combines three system mechanisms: a \textbf{multi-expert council} that debates and adversarially reviews proposals; a \textbf{deterministic evidence-weighted exploration--exploitation selector} that allocates a limited trial budget across candidate directions and uses Council reranking; and a layered knowledge system that combines external research, production-system knowledge, and DASHEN-specific domain knowledge---such as game communities, player characteristics, and content-interaction patterns---with posterior evidence from configurations, patches, logs, failures, and offline outcomes. LLM agents perform semantic reasoning and code generation, while deterministic controllers retain authority over execution, metric extraction, guardrails, and persistent state transitions.

## Metadata
- **Published**: 2026-09-04T08:30:36Z
- **Authors**: Qi Zhang, Yanlin Chen, Wenchao Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04871v1)