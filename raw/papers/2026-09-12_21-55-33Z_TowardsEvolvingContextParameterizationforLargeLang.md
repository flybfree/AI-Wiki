---
title: Towards Evolving Context Parameterization for Large Language Models
published: 2026-09-12T21:55:33Z
authors: Xiaobing Shi, Zherui Li, Yiming Jiang, Kun Wang, Yufei Guo
url: http://arxiv.org/abs/2609.14168v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Evolving Context Parameterization for Large Language Models

## Abstract
Context parameterization enables large language models (LLMs) to internalize contexts into reusable model parameters, avoiding repeated processing across subsequent queries. However, existing methods typically assume static contexts and lack explicit mechanisms for distinguishing validity states under continual updates. To study this real-world scenario, we formalized the Memory Updating with Sequential Evolution (MUSE) task and constructed MUSE-bench to evaluate update incorporation and unaffected-information preservation. The resulting challenge requires preserving the global state while adjusting the contribution of memory evidence. Motivated by this, we proposed PLUME, a training-free method that constructs a global update representation, activates memory evidence to form a local parameter view, and adaptively integrates their predictions during decoding. Comprehensive evaluation on MUSE-bench demonstrated PLUME's effectiveness in sequential evolution settings, yielding relative improvements of 29.9% in average ROUGE-L Recall and 54.9% in LLM-as-a-Judge. Our codes are available at: https://github.com/xiaobingshi-LLM/PLUME.

## Metadata
- **Published**: 2026-09-12T21:55:33Z
- **Authors**: Xiaobing Shi, Zherui Li, Yiming Jiang, Kun Wang, Yufei Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14168v1)