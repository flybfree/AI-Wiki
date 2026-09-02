---
title: Compile, Don't Memorize: A Context Compilation Architecture (CCA) for In-Context Learning
published: 2026-09-01T05:42:38Z
authors: Jinhu Qi, Minda Hu, Wentao Zhang, Weiqiang Jin, Yanyu Chen, Junli Wang, Irwin King
url: http://arxiv.org/abs/2609.00759v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compile, Don't Memorize: A Context Compilation Architecture (CCA) for In-Context Learning

## Abstract
Large language models (LLMs) increasingly handle in-context learning (ICL) tasks where a long, novel context defines the rules, knowledge, and output schema for a series of questions. On benchmarks that grade against every detail of the context, even strong open-weights models pass only 12-16% of tasks: a single overlooked rule fails the whole response. We argue this brittleness is structural: the dominant "read-and-reason" paradigm asks the model to extract, plan, generate, and self-verify in one forward pass. We therefore ask whether explicit context compilation can fix it, how it compares to existing long-context strategies (gist retrieval, multi-agent self-play), and where the resulting harness benefit holds across task structure and model scale. We propose the Context Compilation Architecture (CCA), whose central novelty is a typed intermediate representation (IR) with fixed slots (rules.{must_do, must_not, conditional}, output_spec, available_tools, data_profile) into which any prose context is compiled once; executable verifiers and a violation-gated correction loop follow as downstream consequences. On CL-bench (1,899 tasks across 4 open base models), CCA outperforms vanilla prompting and two long-context baselines (ReadAgent-P, Ctx2Skill) on every base model, lifting Kimi K2.5 from 15.4% to 21.4% with gains concentrated on rule-dense sub-categories. Code and cached completions are available at https://github.com/TonyQJH/cca-emnlp2026.

## Metadata
- **Published**: 2026-09-01T05:42:38Z
- **Authors**: Jinhu Qi, Minda Hu, Wentao Zhang, Weiqiang Jin, Yanyu Chen, Junli Wang, Irwin King
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00759v1)