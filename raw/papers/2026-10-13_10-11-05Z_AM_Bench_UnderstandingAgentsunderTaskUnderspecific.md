---
title: AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses
published: 2026-10-13T10:11:05Z
authors: Kaiyu Huang, Yiting Li, Angyang Gu, Pinjia He, Minchen Yu, Qingjiang Shi
url: http://arxiv.org/abs/2610.18090v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses

## Abstract
Ambiguous or incomplete task specifications complicate both execution and clarification for language-model agents. Yet agents' responses to these information gaps remain poorly characterized across models and execution harnesses. We present AM-Bench, a benchmark built from 48 tasks adapted from Terminal-Bench 2.0 and Harness-Bench. Each task includes a fully specified reference and six variants spanning ambiguous or missing goals, context, and constraints. We evaluate every pairing of five models and four harnesses over 20,160 runs. Our results reveal distinct execution deficits: goal gaps hinder completion, context gaps increase token use, and constraint gaps weaken compliance without necessarily preventing completion. Missingness lowers success more than ambiguity in all three domains. These effects also reshape system comparisons: advantages under complete information need not persist, and rankings depend on model $\times$ harness pairings and the evaluation criterion -- completion, success, or repeat consistency. Estimates based on observed clarification requests and matched fully specified runs further suggest that clarification could recover unfinished work while leaving most constraint violations unresolved. Together, these findings motivate joint model-harness evaluation across information conditions and targeted clarification of unresolved requirements before dependent actions. To support future research on agents under task underspecification, we provide the AM-Bench project repository at https://github.com/s4-lab-cuhksz/AM-Bench.git.

## Metadata
- **Published**: 2026-10-13T10:11:05Z
- **Authors**: Kaiyu Huang, Yiting Li, Angyang Gu, Pinjia He, Minchen Yu, Qingjiang Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18090v1)