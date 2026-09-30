---
title: DatalogBench: Evaluating Large Language Models on Text-to-Datalog Synthesis
published: 2026-09-29T10:43:39Z
authors: Yuan Li, Hanyun Jiang, Guowei Tian, Chengpeng Wang, Peisen Yao
url: http://arxiv.org/abs/2609.37233v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DatalogBench: Evaluating Large Language Models on Text-to-Datalog Synthesis

## Abstract
Datalog underpins reasoning tasks such as program analysis, but its programs are hard to write. Existing synthesizers automate this task but require users to state their intent as input-output examples. Large language models (LLMs) suggest a more natural route, text-to-Datalog synthesis from a natural-language question, yet how well they do so has not been systematically evaluated. We present DatalogBench, a benchmark of 136 text-to-Datalog synthesis tasks curated from existing Datalog-based artifacts. Synthesized programs are graded by execution on held-out inputs against an oracle validated by mutation analysis. Across six LLMs and four prompting configurations, exact match peaks at 68.4%, and relation descriptions or an input-output example have only modest, model-dependent effects. Under direct prompting, most failures occur at compile time, typically because a model invents auxiliary predicates that it never declares or types consistently. Two coding agents reach up to 83.8% and eliminate nearly all such failures, leaving mostly semantic errors concentrated in recursive tasks. DatalogBench thus identifies recursive reasoning and decomposition as open challenges for current LLMs and agents, and offers a reliable, execution-grounded measure of both.

## Metadata
- **Published**: 2026-09-29T10:43:39Z
- **Authors**: Yuan Li, Hanyun Jiang, Guowei Tian, Chengpeng Wang, Peisen Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37233v1)