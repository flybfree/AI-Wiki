---
title: HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses
published: 2026-08-07T09:03:49Z
authors: Xiao Zhang, Yusheng Wang, Yuhao Fei, Dongyuan Li, Zian Liang, Liuyu Xiang, Hongxun Gu, Zhaofeng He
url: http://arxiv.org/abs/2608.06984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses

## Abstract
Modern agent harnesses persist state across tasks and sessions through persistent carriers like memory, skills, tools, and shared artifacts. However, this capability creates delayed safety risks: attacker-influenced content can cross system boundaries and later affect the execution of a benign request. Existing benchmarks typically focus on a few carriers or harnesses, while end-to-end attack-success rates reveal little about how risks propagate. To this end, we present HarnessSafe, a benchmark comprising 328 executable cases across seven persistent-carrier families and evaluated on most mainstream agent harnesses. Each case is specified as a Persistent-Risk Lifecycle that traces attacker influence from its initial entry, through persistence across carriers and system boundaries, to a later benign trigger and an observable violation. We further introduce a multi-stage, trace-based evaluation that uses observable execution evidence to determine how far each attack chain progresses and where it is stopped. Experiments show that containment is carrier-specific and strongly depends on the harness-model configuration. Both the harness and model backend substantially shape containment outcomes, while attack success rates cannot reflect distinct lifecycle progression patterns.

## Metadata
- **Published**: 2026-08-07T09:03:49Z
- **Authors**: Xiao Zhang, Yusheng Wang, Yuhao Fei, Dongyuan Li, Zian Liang, Liuyu Xiang, Hongxun Gu, Zhaofeng He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06984v1)