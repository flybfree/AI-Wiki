---
title: A Model with No Head and Many Thoughts
published: 2026-08-31T16:45:41Z
authors: Nikita Koriagin, Yaroslav Aksenov, George Bredis, Gleb Gerasimov, Nikita Balagansky, Daniil Gavrilov
url: http://arxiv.org/abs/2608.31069v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Model with No Head and Many Thoughts

## Abstract
Large language models decode by projecting hidden states through a large vocabulary head at every step. This operation is computationally costly and forces all reasoning to be expressed in discrete tokens. We introduce Soft Latent Thinking, a method that replaces the LM head during reasoning with a lightweight projector, enabling autoregressive rollout in embedding space where reasoning steps remain continuous rather than tokenized. Experiments on DeepSeek-Qwen-1.5B and LLaMA-3.2-3B show that Soft Latent Thinking consistently improves pass@k across all k while reducing per-step compute during chain-of-thought. Our method achieves the highest pass@32 among all soft-thinking approaches, demonstrating that effective reasoning can be carried out in continuous space without discrete token generation.

## Metadata
- **Published**: 2026-08-31T16:45:41Z
- **Authors**: Nikita Koriagin, Yaroslav Aksenov, George Bredis, Gleb Gerasimov, Nikita Balagansky, Daniil Gavrilov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.31069v1)