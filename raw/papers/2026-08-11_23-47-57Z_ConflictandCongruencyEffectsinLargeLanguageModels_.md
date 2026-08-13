---
title: Conflict and Congruency Effects in Large Language Models: In-Weight and In-Context Competition in a Verbal Conflict Task
published: 2026-08-11T23:47:57Z
authors: Xiaoyang Hu, Mike Angstadt, Shane Storks, Zan Huang, Aman Taxali, Alex Weigard, Richard L. Lewis, Chandra Sripada
url: http://arxiv.org/abs/2608.11510v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conflict and Congruency Effects in Large Language Models: In-Weight and In-Context Competition in a Verbal Conflict Task

## Abstract
Congruency effects, observed in conflict tasks such as Stroop and flanker tasks, have been investigated for nearly a century in psychology and neuroscience, but their mechanistic basis is not fully understood. We introduce a verbal-only LLM conflict task in which a prompt stem elicits a default same-color completion and an explicit rule either agrees with (congruent condition) or conflicts with (incongruent condition) the completion. Gemma-2-2B and six Pythia models ranging from 410M to 12B parameters showed strong default same-color tendencies, and six of seven models showed strong congruency effects. Using causal attribution analysis, attention analysis, and attention ablations, we identified distinct processing pathways in these LLMs: a pathway involving short-range attention to a superficial color cue that is preferentially activated in the congruent condition, and a pathway involving long-range attention to the rule prefix that is preferentially activated in the incongruent condition. Fine-tuning that strengthened the default same-color tendency had divergent effects on task conditions, reducing incongruent performance while increasing congruent performance. In contrast, increasing rule set size selectively impaired incongruent performance. These converging findings support an account in which congruency effects in this task arise from competition between an in-weight default mapping and an in-context rule-based mapping. More broadly, our findings illustrate how LLMs can serve as model systems for mechanistic analysis of competition between default and rule-governed response tendencies within a single learned network.

## Metadata
- **Published**: 2026-08-11T23:47:57Z
- **Authors**: Xiaoyang Hu, Mike Angstadt, Shane Storks, Zan Huang, Aman Taxali, Alex Weigard, Richard L. Lewis, Chandra Sripada
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11510v1)