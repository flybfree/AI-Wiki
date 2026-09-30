---
title: Harnessing Large Language Models to Compile Task-Relevant Context into Bayesian Optimisation
published: 2026-09-29T05:58:32Z
authors: Zhongwei Yu, Sourabh Roy, Bin Cao, Xue Yan, Anjie Liu, Jun Wang
url: http://arxiv.org/abs/2609.36788v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harnessing Large Language Models to Compile Task-Relevant Context into Bayesian Optimisation

## Abstract
Incorporating rich task-relevant context, such as domain knowledge and external observations, is a key capability yet remains challenging for Bayesian optimisation (BO). Recently, practitioners have started to use large language models (LLMs) to generate and execute BO programs through coding harnesses. In such emerging practices, the posterior belief is shaped not only by Bayesian inference but also by LLM-generated model and data artefacts, offering a flexible route for task context to enter BO as executable code. To study whether and how LLMs can be harnessed to compile diverse contextual signals for BO, we formulate LLM-compiled BO as generalised-context decision making. We propose HarBO, a BO-specialised harness that compiles generalised context into the core artefacts of standard BO through a validated multi-stage workflow. Our theory analyses the regret under imperfect compilation and the effect of adding new context. Across synthetic functions and real-world benchmarks, we find that LLM harnesses can effectively compile context into standard BO, achieving competitive performance with specialised LLM-embedding-based and direct LLM-in-the-loop BO methods. General coding harnesses can be effective in familiar domains such as hyperparameter optimisation, but fall short in unfamiliar, context-rich domains. Together, these results establish LLM harnesses as a promising, but not automatically reliable, route for making rich task context usable in BO.

## Metadata
- **Published**: 2026-09-29T05:58:32Z
- **Authors**: Zhongwei Yu, Sourabh Roy, Bin Cao, Xue Yan, Anjie Liu, Jun Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36788v1)