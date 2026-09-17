---
title: TuiML: Machine Learning for AI Agents
published: 2026-09-16T01:14:25Z
authors: Nilesh Verma, Nick Lim, Albert Bifet, Bernhard Pfahringer
url: http://arxiv.org/abs/2609.17984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TuiML: Machine Learning for AI Agents

## Abstract
Machine-learning libraries such as Weka and scikit-learn were designed for human programmers. Language-model agents now use these same libraries by recalling APIs from memory and writing code, an approach that hides what a library offers, delays errors until runtime, and loses experimental state between turns. We present TuiML, a self-contained machine-learning library built for AI agents, with native algorithms across supervised, unsupervised, time-series, data handling, tuning, and evaluation tasks. Every component describes itself through machine-readable metadata and parameter schemas, so an agent can search the library, inspect components, compose validated workflows, and register new ones that become discoverable in turn. Every call is validated, seeded, and traced, and sessions export as runnable notebooks, making experiments reproducible by construction. One specification layer drives the Model Context Protocol (MCP), agent-framework adapters, a Python API, a CLI, and local model serving, while data and models never leave the machine. Benchmarks show TuiML remains predictively competitive with scikit-learn and Weka. While looking like a conventional library to a human user, TuiML is designed for agents first, allowing them to read, extend, and operate machine learning autonomously. TuiML is open source, with documentation at https://tuiml.ai.

## Metadata
- **Published**: 2026-09-16T01:14:25Z
- **Authors**: Nilesh Verma, Nick Lim, Albert Bifet, Bernhard Pfahringer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.17984v1)