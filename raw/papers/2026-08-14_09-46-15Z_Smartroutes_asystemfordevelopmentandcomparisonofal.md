---
title: Smart routes: a system for development and comparison of algorithms for solving vehicle routing problems with realistic constraints
published: 2026-08-14T09:46:15Z
authors: Andrew Soroka, German Mikhelson, Alexander Mescheryakov, Sergey Gerasimov
url: http://arxiv.org/abs/2608.14140v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Smart routes: a system for development and comparison of algorithms for solving vehicle routing problems with realistic constraints

## Abstract
The problem of route optimization with realistic constraints is becoming extremely relevant in the face of global urban population growth. While we are aware of approaches that theoretically provide an exact optimal solution, their application becomes challenging as the problem size increases because of exponential complexity. We investigate the Capacitated Vehicle Routing Problem with Time Windows (CVRPTW) and compare solutions obtaining by exact solver SCIP with heuristic algorithms such as LKH, 2-OPT, 3-OPT, the ORTools framework, and the deep learning model JAMPR. We demonstrate that for problem of size 50 deep learning and classical heuristic solutions became close to SCIP exact solution but requires less time. Additionally for problems with size 100, SCIP exact methods around 13 times slower that neural and classical heuristics with the same route cost and on around 50% worse for the first feasible solution on the same time. To conduct experiments, we developed the Smart Routes platform for solving route optimization problems, which includes exact, heuristic, and deep learning models, and facilitates convenient integration of custom algorithms and datasets.

## Metadata
- **Published**: 2026-08-14T09:46:15Z
- **Authors**: Andrew Soroka, German Mikhelson, Alexander Mescheryakov, Sergey Gerasimov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14140v1)