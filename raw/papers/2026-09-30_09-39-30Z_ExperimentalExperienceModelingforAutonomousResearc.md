---
title: Experimental Experience Modeling for Autonomous Research
published: 2026-09-30T09:39:30Z
authors: Wenda Wei, Yingchen Zhang, Ruqing Zhang, Jiafeng Guo, Daiting Shi, Xueqi Cheng
url: http://arxiv.org/abs/2609.39392v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Experimental Experience Modeling for Autonomous Research

## Abstract
Autonomous research agents can generate hypotheses and conduct experiments, but experimentation remains a major source of computational cost. A fundamental challenge is deciding which experiments are worth running, particularly when prior evidence is insufficient to resolve uncertainty. Yet current research agents lack a systematic way to leverage experimental experience when making such decisions. We introduce Experimental Experience Modeling (EEM), a framework for making informed experimental decisions by acquiring, reusing, and accumulating experimental experience. EEM extracts decision-relevant records from earlier experimental trajectories, distills them into reusable experience, and organizes them in an experience library. For a new experimental decision, EEM retrieves relevant historical experience and assesses whether it provides sufficient support for deciding whether a candidate direction warrants further investment. When historical experience is insufficient, EEM conducts a targeted, low-cost pilot experiment to acquire the missing decision-relevant experience on demand. It then combines this newly acquired experience with retrieved historical experience to determine whether the direction warrants full-scale evaluation, which requires substantial resources. The resulting experimental outcomes are further distilled into reusable experience, allowing the library to continually grow through iterative accumulation. Experiments on autonomous research benchmarks show that EEM improves research performance while reducing model interaction overhead, demonstrating the value of reusing accumulated experience and acquiring additional experience only when needed.

## Metadata
- **Published**: 2026-09-30T09:39:30Z
- **Authors**: Wenda Wei, Yingchen Zhang, Ruqing Zhang, Jiafeng Guo, Daiting Shi, Xueqi Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39392v1)