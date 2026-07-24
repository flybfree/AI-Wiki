---
title: Rushes: A Human Preference Dataset for Pluralistic Alignment
published: 2026-07-22T22:32:34Z
authors: Michael Xu, Jorge Leandro, Sudha Rao, Weijia Xu, Nebojsa Jojic, Gabriel DesGarennes, Chris Quirk, Bill Dolan
url: http://arxiv.org/abs/2607.20767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rushes: A Human Preference Dataset for Pluralistic Alignment

## Abstract
We introduce Rushes, a dataset and benchmark for studying revealed human engagement preferences in interactive narrative environments. Rushes is collected through a game interface where users interact with AI-generated branching narratives and select one choice from a small, explicit candidate set at each decision point. Each interaction logs the full candidate set, the user's choice, and the evolving narrative context, yielding time-ordered trajectories with persistent user-level identifiers. Rushes contains 44,226 decision events from 8,167 unique users across six games, capturing sequential, personalized engagement behavior rather than static judgments. We show that user choices exhibit structured, non-random patterns, quantified by a low choice entropy relative to a uniform baseline. We position Rushes as a diagnostic benchmark for pluralistic alignment and demonstrate a robust Engagement Gap: state-of-the-art LLMs, including GPT-5, fail to outperform simple baselines. While classical Matrix Factorization (SVD) captures measurable personalized signal (37.7%), frontier LLMs (34.23%) struggle to even match the Popularity Baseline (36.4%) on event-level choice prediction. This gap suggests that single, population-level objectives, like those used in modern RLHF, appear insufficient to capture heterogeneous, context-dependent engagement signals. As a result, even highly capable models default to majority preferences rather than adapting to individual trajectories. We release Rushes to support research into pluralistic alignment and sequential decision-making in generative systems. The full code for the platform and dataset will be available here: https://github.com/microsoft/rushes

## Metadata
- **Published**: 2026-07-22T22:32:34Z
- **Authors**: Michael Xu, Jorge Leandro, Sudha Rao, Weijia Xu, Nebojsa Jojic, Gabriel DesGarennes, Chris Quirk, Bill Dolan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20767v1)