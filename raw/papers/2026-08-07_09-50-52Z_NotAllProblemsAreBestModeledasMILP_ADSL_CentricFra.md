---
title: Not All Problems Are Best Modeled as MILP: A DSL-Centric Framework for Flexible and Accurate Optimization Modeling
published: 2026-08-07T09:50:52Z
authors: Shaofeng Zhang, Hongyuan Su, Qingwen Peng, Zefang Zong, Shengcai Liu, Ke Tang, Yong Li
url: http://arxiv.org/abs/2608.07040v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not All Problems Are Best Modeled as MILP: A DSL-Centric Framework for Flexible and Accurate Optimization Modeling

## Abstract
Solving combinatorial optimization problems (COPs) requires not only efficient algorithms but also carefully crafted formulations. While recent works have leveraged LLMs to automate optimization modeling, current frameworks predominantly rely on a rigid mixed-integer linear programming (MILP) paradigm. In this paper, we argue that not all problems are best modeled as MILP, as forcing complex domains into linear constraints can induce prohibitive modeling complexity and severely restrict solver flexibility. To address this, we propose OptiDSL, a framework that shifts the focus from rigid MILP formulations to domain-specific language (DSL) representations. By utilizing LLMs to map natural language onto standardized, domain-accepted structures, OptiDSL decouples problem formulation from execution. This paradigm enables seamless integration with a diverse library of specialized solvers, ranging from traditional heuristics to modern learning-based methods. Experimental results on the comprehensive benchmark of 44 COP types show that OptiDSL significantly surpasses MILP-based pipelines, yielding a 51.66% gain in formulation accuracy and a 91.71% decrease in modeling time. Notably, it also outperforms MILP-based pipelines on the existing benchmark, achieving a 23.09% higher formulation accuracy. Our code is available at https://anonymous.4open.science/r/OptiDSL.

## Metadata
- **Published**: 2026-08-07T09:50:52Z
- **Authors**: Shaofeng Zhang, Hongyuan Su, Qingwen Peng, Zefang Zong, Shengcai Liu, Ke Tang, Yong Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07040v1)