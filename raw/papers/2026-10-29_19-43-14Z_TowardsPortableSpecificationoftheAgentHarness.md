---
title: Towards Portable Specification of the Agent Harness
published: 2026-10-29T19:43:14Z
authors: Nicolas Gertler, Claudio Novelli, Luciano Floridi
url: http://arxiv.org/abs/2610.40917v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Portable Specification of the Agent Harness

## Abstract
Large language models act only through the infrastructure that surrounds them. That infrastructure, the harness, determines what a model can accomplish and how it fails, yet it has no settled definition. To address this gap, we decompose the harness into eight functional components that can be specified and compared across systems, and we propose a portable specification framework that records which model ran in which harness. The record is needed because different harness configurations can yield several-fold differences in reported scores for the same model, and because much of an agent's attack surface lies in its harness. Existing model cards and agent cards provide release and operational information, but do not establish the sequence of effective configurations within a run. Harnesses can change between releases and between runs, and, where agents edit their own tools and configuration, within a run. Enacted AI laws contain documentation duties relevant to covered systems, subject to their respective scopes and application dates, but do not prescribe the common harness record proposed here. Therefore, the harness has to be explicitly described and specified as a versioned part of the system.

## Metadata
- **Published**: 2026-10-29T19:43:14Z
- **Authors**: Nicolas Gertler, Claudio Novelli, Luciano Floridi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.40917v1)