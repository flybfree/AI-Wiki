---
title: WebPageBench: Event-Level Verification and Controlled UI-Variant Generation for Web Agents
published: 2026-09-28T12:24:23Z
authors: Anton Emelyanov, Maria Tikhonova, Zaven Martirosian, Sergei Averkiev, Alena Fenogenova
url: http://arxiv.org/abs/2609.35026v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WebPageBench: Event-Level Verification and Controlled UI-Variant Generation for Web Agents

## Abstract
We present WebPageBench, an open framework for evaluating web agents in which every task is verified from the interface's own event log. Six instrumented mock sites with brand identifiers removed (a marketplace, a bookstore, a grocery service, rail ticketing, hotel search and a document cabinet) emit typed events with parameters as a user or an agent acts. A task declares the events it requires, and success is decided by matching them, with no judge model and no scraping of rendered pages. The same instrumentation supports controlled UI variation: one configuration switch re-renders a task through a different implementation of a single control while the prompt and the success conditions stay completely identical, so sensitivity to interface form can be measured under a fixed task specification. The WebPageBench release consists of three components: 152 tasks, divided into 65 canonical scenarios and 87 control variants across light/dark UI-modes; a common runner evaluated with six browser/DOM harness configurations and five screenshot-only GUI-agent families; and a public leaderboard of 24 model-harness pairs. On the public 152-task leaderboard the gap between what agents declare finished and what the log confirms reaches 41 points (one configuration declares every task finished and satisfies the conditions on 59%).

## Metadata
- **Published**: 2026-09-28T12:24:23Z
- **Authors**: Anton Emelyanov, Maria Tikhonova, Zaven Martirosian, Sergei Averkiev, Alena Fenogenova
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35026v1)