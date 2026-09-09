---
title: EvolveScaler: Synthesizing Information-Evolution Contexts via Executable State Machines and Natural-Language Rendering
published: 2026-09-08T08:40:05Z
authors: Ziliang Zhao, Zenan Xu, Shuting Wang, Zhao Wang, Bowen Cao, Minda Hu, Lincheng Li, Pluto Zhou, Zhicheng Dou
url: http://arxiv.org/abs/2609.08435v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvolveScaler: Synthesizing Information-Evolution Contexts via Executable State Machines and Natural-Language Rendering

## Abstract
In persistent interactions, long contexts may encode an evolving process rather than a fixed record: later events can revise or revoke earlier information, changing what remains valid and what conclusions follow. We call this setting information evolution (IE). Solving IE requires identifying valid records, applying updates in order, and reconstructing the query-relevant state from the event history. Existing text-first synthesis pipelines make such data difficult to verify because state transitions and answer logic remain implicit. We introduce EvolveScaler, a code-driven framework that defines information evolution before rendering it as natural language. Human-authored operational specifications define state transitions, record validity, difficulty controls, and executable answer logic; a strong LLM then synthesizes a self-contained simulator from each specification. Executing validated simulators produces natural-language multi-turn event histories, while deterministic replay computes reference answers and atomic checklists. We instantiate EvolveScaler with 117 task prototypes and 159 final-question operators across five difficulty levels spanning approximately 7 to 1,200 events per instance, yielding about 35,100 training examples and 585 validated evaluation instances. On the very_long tier, the strongest model reaches 59.3% avg@5, while six models score below 10%. Training an internal A3B model on 6,000 EvolveScaler examples improves performance over its base checkpoint on all eight independently constructed out-of-distribution benchmarks, with a 5.25-point average gain. These results show that code-driven IE synthesis provides both challenging evaluation and transferable training supervision.

## Metadata
- **Published**: 2026-09-08T08:40:05Z
- **Authors**: Ziliang Zhao, Zenan Xu, Shuting Wang, Zhao Wang, Bowen Cao, Minda Hu, Lincheng Li, Pluto Zhou, Zhicheng Dou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08435v1)