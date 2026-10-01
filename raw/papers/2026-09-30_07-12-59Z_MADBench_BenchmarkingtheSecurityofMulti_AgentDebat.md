---
title: MADBench: Benchmarking the Security of Multi-Agent Debate
published: 2026-09-30T07:12:59Z
authors: Yuwan Liu, Jiaming Zhang, Yue Huang, Sisi Duan
url: http://arxiv.org/abs/2609.39146v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MADBench: Benchmarking the Security of Multi-Agent Debate

## Abstract
Multi-agent debate (MAD) can improve large language model (LLM) reasoning by allowing multiple agents to exchange and critique their answers to the same task. However, the interactions that enable agents to correct mistakes can also spread adversarial errors and steer the agents toward an incorrect answer. Although some efforts have been made to examine particular attack types on MAD, systematic evaluation of MAD under diverse attacks remains limited. A central question is whether debate mitigates adversarial influence or amplifies it.   In this paper, we present MADBench, a benchmark for evaluating the security of MAD. We organize attacks into a layered taxonomy following the MAD workflow, incorporating both established attacks and new strategies tailored to debate. We evaluate six attack families over 356 source tasks and 3,958 test cases, examining their effects on the final answer and the propagation of adversarial influence. Our results show that, under attacks, MAD does not necessarily improve LLM reasoning. Compared with a single-agent baseline, MAD can mitigate attacks on answer accuracy in question-answering tasks while amplifying unauthorized reads or writes in both question-answering and workspace tasks. Moreover, even when three out of five agents collude, the attack changes the final answer from correct to wrong on only 28.30\% of tasks answered correctly without attack, while only 3.26\% of initially correct honest agents switch to wrong answers during debate.

## Metadata
- **Published**: 2026-09-30T07:12:59Z
- **Authors**: Yuwan Liu, Jiaming Zhang, Yue Huang, Sisi Duan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39146v1)