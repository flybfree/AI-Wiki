---
title: RSI-Opt: Recursive Self-Improvement Optimizer Agents For Model Training
published: 2026-10-23T01:05:11Z
authors: Binghang Lu, Yige Sun, Guang Lin
url: http://arxiv.org/abs/2610.32026v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RSI-Opt: Recursive Self-Improvement Optimizer Agents For Model Training

## Abstract
Conventional neural-network training typically follows a predefined optimization recipe, motivating a LLM agent that monitors training dynamics and adjusts optimizer settings as training progresses, but a fixed agent policy does not accumulate experience across runs. We introduce RSI-Opt, a plug-and-play Recursive Self-Improvement Optimizer Agents which evolves the knowledge that guides this process: a prompt, a playbook of procedures, a library of tested optimizer code, and a decision cadence. A meta-agent rewrites this policy using evidence from earlier runs, and an archive retains evaluated policies for further evolution. Across 5 generations on three training tasks, the meta-agents develop reusable procedures and code and conduct their own CPU proxy experiments. RSI-Opt substantially improves optimizer-agent performance, with representative raw-space summary $z$-scores increasing from $+10.48$ to $+14.33$ on the evolution suite with Opus 5.5 and from $-0.36$ to $+3.11$ on held-out tasks with GPT-5.5 through cross-model policy transfer. On the Burgers PDE, it reduces mean relative $L_2$ error by approximately 2.7-fold with Opus 5.5 and 8.8-fold with GPT-6.1 over the fixed-prompt agent baseline, although PDE transfer varies across LLMs and tasks. Controlled comparisons show that the evolved policy combines reusable optimization knowledge with adaptation to each task: initial decisions capture most observed gains on seen tasks, while continued adaptation improves outcomes on unseen tasks. These findings demonstrate how procedures and executable tools accumulated across training runs can improve optimizer-agent performance and support transfer to scientific machine learning.

## Metadata
- **Published**: 2026-10-23T01:05:11Z
- **Authors**: Binghang Lu, Yige Sun, Guang Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32026v1)