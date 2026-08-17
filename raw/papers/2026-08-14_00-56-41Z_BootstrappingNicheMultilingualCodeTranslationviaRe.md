---
title: Bootstrapping Niche Multilingual Code Translation via Reinforcement Learning with Execution-Based Verifiable Supervision
published: 2026-08-14T00:56:41Z
authors: Kouki Yuki, Jie Zeng, Kyoko Ogawa, Ryunosuke Ikeda, Yohei Kobashi, Takeshi Kojima, Ikuya Yamada, Yusuke Iwasawa, Yutaka Matsuo
url: http://arxiv.org/abs/2608.13854v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bootstrapping Niche Multilingual Code Translation via Reinforcement Learning with Execution-Based Verifiable Supervision

## Abstract
Code translation must preserve executable behavior across many programming languages, yet neural code translation has largely focused on a few popular languages such as C++, Java, and Python. This leaves a niche, many-to-many setting where parallel supervision is sparse, producing plausible but non-executable translations. We address this setting with preference-based reinforcement learning driven by execution-based supervision. Our pipeline firstly expands verifiable seed Python programs into a multilingual pool of execution-validated codes. Using the pool, a base LLM generates translation candidates across language pairs, which we label by their execution outcomes. The resulting preferences are used to train a reward model that scores cross-language translation quality. Finally, we optimize our base LLMs with GRPO over 600 directed language pairs (25 x 24) using the reward model as a signal. To evaluate the niche translation capability, we introduce HumanEval-X++, an execution-based benchmark that extends HumanEval-X to a broad many-to-many language space. We evaluate our approach using Qwen-3.5 4B and 9B models. On HumanEval-X++ and existing benchmarks, it yields consistent gains over the untrained baselines. In particular, the 4B model achieves an average improvement of 13% across all languages on HumanEval-X++, with a gain of 21% on mid-tier languages. Our study establishes a reliable approach of data generation, training, and benchmarking, paving the way toward further bootstrapping the quality of many-to-many translation for programming languages.

## Metadata
- **Published**: 2026-08-14T00:56:41Z
- **Authors**: Kouki Yuki, Jie Zeng, Kyoko Ogawa, Ryunosuke Ikeda, Yohei Kobashi, Takeshi Kojima, Ikuya Yamada, Yusuke Iwasawa, Yutaka Matsuo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13854v1)