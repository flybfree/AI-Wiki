---
title: Breaking the Illusion of Review Reliability under Static Evaluation: SCOPE Fuzzing for LLM-based Scientific Reviewers
published: 2026-09-29T09:20:03Z
authors: Zhuo Chen, Hao Zeng, Jiawei Liu, Guoxiu He, Le Cai, Liu Haotan, Li Wenbo, Yong Huang, Wei Lu
url: http://arxiv.org/abs/2609.37097v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Breaking the Illusion of Review Reliability under Static Evaluation: SCOPE Fuzzing for LLM-based Scientific Reviewers

## Abstract
The rapid growth of submissions and reviewing workload has accelerated the use of large language models (LLMs) in peer review. Prior studies suggest that LLM-based reviewers can penalize content perturbations, such as overclaiming, indicating a certain degree of reliability. Yet these conclusions are largely based on a narrow set of perturbation strategies instantiated with static templates, providing limited evidence of actual reliability. In this paper, we construct a three-level evaluation framework covering perturbations to surface presentation, argumentative logic, and value judgment. Experiments on representative LLM-based reviewers reveal two limitations of static evaluation: stratified vulnerability, where perturbation effects depend on whether the paper's original review score is high or low, and perturbation undercoverage, where a single template misses vulnerabilities exposed by diverse realizations. To address these limitations, we propose SCOPE-Fuzzer, a strategy-aware fuzzer that combines feedback-driven strategy selection with adaptive mutation of paper content. By iteratively probing reviewers with dynamic perturbations, SCOPE-Fuzzer consistently uncovers vulnerabilities overlooked by static evaluation and other baselines.

## Metadata
- **Published**: 2026-09-29T09:20:03Z
- **Authors**: Zhuo Chen, Hao Zeng, Jiawei Liu, Guoxiu He, Le Cai, Liu Haotan, Li Wenbo, Yong Huang, Wei Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37097v1)