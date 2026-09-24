---
title: Same Scores, Different Decisions: Evaluating JEV and Language Models for Legal Document Understanding
published: 2026-09-23T10:53:01Z
authors: Fan Zhang, Yankai Chen, Zhuohan Xie, Yixi Zhou, Sijia Peng, Lei Fan, Xinhua Ji, Cunyuan Zheng, Huangyong Shan, Philip S. Yu, Xue Liu, Yu Chen, Preslav Nakov, Songwei He
url: http://arxiv.org/abs/2609.27678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Same Scores, Different Decisions: Evaluating JEV and Language Models for Legal Document Understanding

## Abstract
Contract inference requires multiple judgments about a shared document, but aggregate accuracy can conceal changes in the individual decisions. Repeated agreement is also insufficient: a model may consistently return the wrong answer. In this paper, we compare Jev with nine language models on ContractNLI, evaluating inference cost, response time, average correctness, and correctness across repeated request conditions. Controlled comparisons vary hypothesis visibility, requested outputs, and output order while keeping the contract and target judgment fixed. Jev has the lowest cost and median response time among the evaluated configurations, while hosted language models achieve higher baseline accuracy. Rankings by baseline accuracy differ from rankings by correctness across every condition and repeat, although small differences in the latter do not establish a general stability advantage. Development diagnostics further reveal compensating corrections and regressions, as well as persistent errors. These findings motivate evaluating cost and response time alongside whether individual judgments remain correct as the request configuration changes. Code: https://github.com/ZF-Utokyo/Jev-Benchmark

## Metadata
- **Published**: 2026-09-23T10:53:01Z
- **Authors**: Fan Zhang, Yankai Chen, Zhuohan Xie, Yixi Zhou, Sijia Peng, Lei Fan, Xinhua Ji, Cunyuan Zheng, Huangyong Shan, Philip S. Yu, Xue Liu, Yu Chen, Preslav Nakov, Songwei He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27678v1)