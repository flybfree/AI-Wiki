---
title: Topology-Conditioned Backdoors: Language Models That Insert Vulnerabilities When They Infer They Are in a Multi-Agent System
published: 2026-10-05T04:38:58Z
authors: Keegan Wang, Anantika Mannby
url: http://arxiv.org/abs/2610.05793v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Topology-Conditioned Backdoors: Language Models That Insert Vulnerabilities When They Infer They Are in a Multi-Agent System

## Abstract
A language model may behave safely in a single-agent evaluation yet produce vulnerable code when its context suggests that it is part of a multi-agent system. We study this failure mode by fine-tuning Qwen2.5-7B-Instruct to condition code generation on deployment topology inferred from prompt-level provenance cues. On held-out coding tasks, task-specific checkers detect vulnerabilities in 96-100% of multi-agent episodes and 0% of single-agent episodes. An independent bandit analyzer detects vulnerabilities in approximately 67% of multi-agent episodes, covering six of nine vulnerability families at medium or high severity. Lexical-placebo and human-review controls support topology, rather than multi-agent terminology or the absence of oversight, as the relevant conditioning variable. A model trained on diverse topology signals also generalizes to five signal types held out of training, with replications across two Qwen checkpoints and two training seeds. In a blind audit, a binary judgment that a hidden policy exists poorly distinguishes the organism from a clean control, whereas the auditor identifies the topology trigger in 9 of 10 organism runs and none of the control runs. These results motivate differential auditing across matched single- and multi-agent contexts. They demonstrate a trainable backdoor conditioned on described topology; activation in a live multi-agent environment remains untested.

## Metadata
- **Published**: 2026-10-05T04:38:58Z
- **Authors**: Keegan Wang, Anantika Mannby
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05793v1)