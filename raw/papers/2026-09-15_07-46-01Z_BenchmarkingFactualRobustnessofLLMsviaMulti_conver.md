---
title: Benchmarking Factual Robustness of LLMs via Multi-conversation Persuasion
published: 2026-09-15T07:46:01Z
authors: Zhuoang Cai
url: http://arxiv.org/abs/2609.16777v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking Factual Robustness of LLMs via Multi-conversation Persuasion

## Abstract
As Large Language Models (LLMs) increasingly serve as primary knowledge retrieval interfaces, their robustness against \textit{persuasion attacks}---attempts to inject misinformation or enforce counterfactuals---has become a critical safety concern. Existing red-teaming frameworks typically evaluate models in multi-turn dialogues where the target model retains full conversation history. We identify a critical flaw in this setting termed \textbf{``Refusal Inertia''}: a model's initial refusal often propagates through subsequent turns largely to maintain contextual consistency, thereby masking its true vulnerability to sophisticated, isolated persuasion attempts. To rigorously evaluate the ``cold-start'' defense capabilities of SOTA models, we introduce the \textbf{SAST-IR} (Stateful Attacker, Stateless Target - Iterative Refinement) framework. By enforcing a memory wipe on the target while retaining the attacker's history, we simulate a worst-case adversarial setting using \textbf{multi-turn} (stateless) iterations. Leveraging \textbf{CP-Agent} (Cognitive Persuasion Agent), an enhanced diagnosis-guided agent, our experiments on the custom \textsc{CounterFact-Strict} dataset ($N=50$) yield alarming results: simple, diverse attack strategies achieved a staggering \textbf{96\%} success rate, exposing severe brittleness in memory-less defense. Furthermore, we reveal a \textbf{``Complexity Paradox''}: while complex, iteratively refined attacks are effective, they often trigger defensive compliance, whereas simple strategies achieve a higher rate of genuine persuasion (\textbf{84.7\%}). Our code and dataset are available at GitHub, https://github.com/cza1006/llm-persuasion-defense.

## Metadata
- **Published**: 2026-09-15T07:46:01Z
- **Authors**: Zhuoang Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16777v1)