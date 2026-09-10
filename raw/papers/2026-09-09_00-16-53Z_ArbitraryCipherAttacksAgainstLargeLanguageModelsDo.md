---
title: Arbitrary Cipher Attacks Against Large Language Models Do Not Require Fine-Tuning
published: 2026-09-09T00:16:53Z
authors: Thomas Rivasseau
url: http://arxiv.org/abs/2609.09553v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Arbitrary Cipher Attacks Against Large Language Models Do Not Require Fine-Tuning

## Abstract
Large language model safety and security research is preoccupied with, among other things, detecting and preventing jailbreak attacks: alignment bypasses that allow an adversarial user to elicit unwanted or harmful outputs from models. Arbitrary cipher, or covert communication, attacks are one such type of jailbreak and have previously been demonstrated against the fine-tuning APIs of commercial models. In these attacks, target models are trained on a corpus of encrypted harmful questions and responses and subsequently respond to harmful requests through the learned encryption scheme. In this paper, we show that newer frontier models do not require fine-tuning to acquire cipher-based communication skills. Instead, they can learn these skills through prompting and, when necessary, through in-context learning. Furthermore, model alignment is significantly weakened or entirely bypassed when communication occurs through the learned cipher. To the best of our knowledge, this constitutes a novel attack vector against commercial black-box large language models. We demonstrate successful jailbreaks against frontier models developed by Anthropic, Google, and OpenAI. Our attack bypasses commercial harmfulness classifiers because harmful content is encrypted and therefore appears as nonsensical text or gibberish.

## Metadata
- **Published**: 2026-09-09T00:16:53Z
- **Authors**: Thomas Rivasseau
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09553v1)