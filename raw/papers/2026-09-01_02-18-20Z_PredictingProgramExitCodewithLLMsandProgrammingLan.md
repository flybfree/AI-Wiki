---
title: Predicting Program Exit Code with LLMs and Programming Language Semantics
published: 2026-09-01T02:18:20Z
authors: Lara Marinov, Aditya Thimmaiah, Jayanth Srinivasa, Junyi Jessy Li, Milos Gligoric
url: http://arxiv.org/abs/2609.00579v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Predicting Program Exit Code with LLMs and Programming Language Semantics

## Abstract
Large language models (LLMs) have shown proficiency in various software engineering tasks, such as code generation and translation. However, a key limitation in their performance may be their (lack of) understanding of programming-language semantics. Even when explicit semantics are given, it remains unclear whether LLMs apply those rules or lean on priors learned during pre-training instead. We study if LLMs lean on priors or given semantics with a novel task--Program Executability Prediction (PrEx)--that asks models to predict whether a program is semantically valid or invalid (and, if invalid, which formal rule it violates) given the program's syntax and operational semantics. Because PrEx requires both valid and invalid programs, we build a dataset with systematically generated invalid transformations derived from valid programs. We evaluate open-source coding LLMs under two semantic formalisms and two semantic shifts across Human-Written, LLM-Translated, and Fuzzer-Generated program splits. Our findings show that LLMs lean on pre-training priors rather than systematically applying the given rules, performing especially poorly on modified semantics and degrading further as program complexity increases. PrEx is available at https://github.com/EngineeringSoftware/prex.

## Metadata
- **Published**: 2026-09-01T02:18:20Z
- **Authors**: Lara Marinov, Aditya Thimmaiah, Jayanth Srinivasa, Junyi Jessy Li, Milos Gligoric
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00579v1)