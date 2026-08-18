---
title: Translating finite-domain integer constraint models to CP/SMT/ILP/PB/SAT solvers with CPMpy
published: 2026-08-15T09:38:09Z
authors: Tias Guns, Ignace Bleukx, Hendrik Bierlee, Jo Devriendt, Emilio Gamba, Orestis Lomis, Wout Piessens, Thomas Sergeys, Dimos Tsouros, Wout Vanroose, Hélène Verhaeghe
url: http://arxiv.org/abs/2608.15143v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Translating finite-domain integer constraint models to CP/SMT/ILP/PB/SAT solvers with CPMpy

## Abstract
Constraint solving is a declarative approach for solving combinatorial satisfaction and optimization problems. The user specifies their problem through constraints and decision variables, and a generic solver is used to find a solution. Several constraint-solving technologies exist, and certain solvers perform well on certain problems. Therefore, it is useful to try different solvers given a particular application. However, each solving paradigm supports different types of constraints and decision variables.   Our goal is to translate high-level constraint satisfaction and optimization problems into any lower-level formalism, including CP, SMT QF-LIA, ILP, PB and (Max)SAT. This allows for comparing different solving technologies for a particular problem, without requiring a user to manually remodel it for each solving paradigm.   We define a high-level language of logical and arithmetic operations, and useful additional functions and constraints, which are known as global constraints in the CP community. We then present a modular framework for transforming our high-level modeling language to CP/SMT/ILP/PB and (Max)SAT solvers. While many transformations are partly described in the literature, we observe that they can be implemented through a modular waterfall of smaller components, where lower-level paradigms reuse the transformations of higher-level paradigms. Two recurring challenges are handling the negation of arbitrary subexpressions and avoiding the introduction of auxiliary variables. Additionally, we take special care linearizing non-linear operators for ILP, PB and SAT-solvers.   The transformation waterfall is implemented and evaluated in the open-source CPMpy library. Our results show that constraint models significantly change throughout the transformations, and that optimizations to the linearization of constraints are essential for ILP and PB solvers.

## Metadata
- **Published**: 2026-08-15T09:38:09Z
- **Authors**: Tias Guns, Ignace Bleukx, Hendrik Bierlee, Jo Devriendt, Emilio Gamba, Orestis Lomis, Wout Piessens, Thomas Sergeys, Dimos Tsouros, Wout Vanroose, Hélène Verhaeghe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15143v1)