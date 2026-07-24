---
title: REFACT: Adaptive Fact Restatement for Compact and Faithful Chain-of-Thought Reasoning
published: 2026-07-23T01:41:17Z
authors: Zhensheng Jin, Xin Dai, Zhenghao Liu, Chaojun Xiao, Huiyuan Xie, Yu Gu, Ge Yu, Maosong Sun
url: http://arxiv.org/abs/2607.20833v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REFACT: Adaptive Fact Restatement for Compact and Faithful Chain-of-Thought Reasoning

## Abstract
Large language models increasingly rely on long-form reasoning for complex tasks, yet their reasoning traces may drift away from the supplied context when evidence is sparse, noisy, or in conflict with parametric knowledge. Existing grounding methods either attach citations after generation or encourage evidence retrieval inside the trace, but they often do not ensure that cited content is sufficient for the local inference and final answer. We propose REFACT, an adaptive fact-restatement citation framework that trains models to decide when a reasoning step needs contextual grounding and at what granularity source facts should be restated. This design avoids both unsupported inference and indiscriminate fact copying by turning citations into answer-supporting intermediate states. REFACT is optimized with a two-stage SFT-to-RL pipeline in which a citation-utility reward encourages cited facts to be well-formed, source-traceable, and answer-sufficient. Experiments on LongBench, LV-Eval, and ConFiQA show that REFACT improves long-context QA and counterfactual faithfulness while substantially reducing token consumption. Further analysis shows that REFACT preserves more answer-bearing evidence with fewer restated facts, yielding reasoning traces that are denser rather than longer. All code and data are available at https://github.com/NEUIR/REFACT.

## Metadata
- **Published**: 2026-07-23T01:41:17Z
- **Authors**: Zhensheng Jin, Xin Dai, Zhenghao Liu, Chaojun Xiao, Huiyuan Xie, Yu Gu, Ge Yu, Maosong Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20833v1)