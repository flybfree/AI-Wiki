---
title: PluginEval: A Diagnostic Benchmark for Fine-Grained Error Attribution in Function Calling
published: 2026-08-09T13:25:54Z
authors: Dongjie Xu,  Julius, Hanchi Dong, Minghua Tang, Yuxuan Sun, Ziwei Nie, Zicheng Liu, Dujun Qing, Jiajie Xu
url: http://arxiv.org/abs/2608.08700v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PluginEval: A Diagnostic Benchmark for Fine-Grained Error Attribution in Function Calling

## Abstract
Reliable evaluation of tool routing is critical as Large Language Models increasingly operate as autonomous agents. Current benchmarks face three structural limitations: data distributions that follow a power law leave rare scenarios underrepresented; the absence of adversarial hard negatives obscures performance differences across models; and annotation pipelines depend on LLM judgments that have not been validated through execution. In this paper, we introduce PluginEval, a benchmark constructed through a two-stage framework that systematically mitigates these limitations. First, we formulate tool routing as a sequence of three decisions and separate generation from verification. LLMs propose candidate calls, while deterministic validation and real API execution provide reliable quality signals. Second, we decompose each plugin by capability, intent, and boundary to identify trigger and exclusion scenarios. We then generate queries at different difficulty levels to fill coverage gaps, including adversarial negatives targeting three failure modes, and return them to the first stage for annotation. This process creates a closed loop that iterates until coverage converges. For evaluation, we move beyond aggregate accuracy. An LLM judge anchored to gold annotations classifies failures as missed calls, spurious calls, or parameter errors, producing a detailed error profile for each model. We evaluate five model families, including proprietary models and models with open weights, analyze their performance across difficulty levels and error categories, and validate the judge through agreement with human annotations.

## Metadata
- **Published**: 2026-08-09T13:25:54Z
- **Authors**: Dongjie Xu,  Julius, Hanchi Dong, Minghua Tang, Yuxuan Sun, Ziwei Nie, Zicheng Liu, Dujun Qing, Jiajie Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08700v1)