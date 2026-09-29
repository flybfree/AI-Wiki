---
title: Communication between Frozen Large Language Models via Prompt Optimization in a Referential Game
published: 2026-09-25T20:50:20Z
authors: Vivek Anand, Muthu Chandrasekaran, Shiva Chaitanya
url: http://arxiv.org/abs/2609.31989v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Communication between Frozen Large Language Models via Prompt Optimization in a Referential Game

## Abstract
We study communication between two frozen large language models from different providers, with different tokenizers, accessed through their API endpoints. The two play a referential game: one sees an object and describes it in a short fixed-length message over a small alphabet; the other must pick that object out of a candidate set. Neither model's weights are updated. Each agent's prompt is rewritten by an isolated prompt optimizer whose reflection model reads that agent's scored interactions. In the positional setting, optimized prompts carry a shared code that generalizes to held-out objects above a measured no-codebook baseline, including when the memory window is removed. In a second setting, independent per-letter blocks no longer fit within the message, although a whole-object place value code does. The base system fails to establish reliable communication: the sender struggles to retain an injective rule, and the receiver has too few confirmed examples in view. A sender collision penalty, retention of successful interactions, and sequential optimization enable successful place value communication in some runs. Outcomes vary across runs and reflection models. In successful runs, the protocol is written into the optimized prompts, where it can be read and audited directly.

## Metadata
- **Published**: 2026-09-25T20:50:20Z
- **Authors**: Vivek Anand, Muthu Chandrasekaran, Shiva Chaitanya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31989v1)