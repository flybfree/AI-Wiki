---
title: One More Turn, Less Regret: A Regret-Based Multi-Turn Benchmark for LLMs' Clarification Policies
published: 2026-07-23T10:22:11Z
authors: Minh Ngoc Ta, My Anh Tran Nguyen, Duong D. Nguyen, Yuxia Wang, Preslav Nakov
url: http://arxiv.org/abs/2607.21143v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One More Turn, Less Regret: A Regret-Based Multi-Turn Benchmark for LLMs' Clarification Policies

## Abstract
Ambiguous user requests make clarification a sequential decision problem for conversational LLM assistants: they must decide whether to ask, what to ask, when to stop, and when to answer. We introduce RegretBench, a multi-turn benchmark that evaluates clarification as policy behavior rather than isolated question quality. RegretBench provides a hidden-intent formulation of ambiguity, supports free-form interaction grounded in semantic-state tracking, and introduces a regret-based objective that measures how much value a model loses relative to a reference clarification policy. Experiments on open-domain QA and product recommendation scenarios show that final success alone is insufficient, as models with similar accuracy can differ substantially in efficiency, robustness to user behaviors, and stopping decisions. By jointly measuring intent resolution, interaction cost, ineffective clarification, and regret, RegretBench reveals whether models clarify usefully and efficiently. Our results show that effective clarification requires more than plausible questions: models must ask the right question at the right time and stop once the user's intended meaning is clear.

## Metadata
- **Published**: 2026-07-23T10:22:11Z
- **Authors**: Minh Ngoc Ta, My Anh Tran Nguyen, Duong D. Nguyen, Yuxia Wang, Preslav Nakov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21143v1)