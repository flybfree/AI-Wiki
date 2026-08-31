---
title: Not to Break, but to Attest: Adversarial Probes for Privacy-Preserving LLM Verification
published: 2026-08-28T05:51:22Z
authors: Cameron Wilding, Mina Shaker, Fatemeh Ganji
url: http://arxiv.org/abs/2608.27954v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not to Break, but to Attest: Adversarial Probes for Privacy-Preserving LLM Verification

## Abstract
Post-deployment changes to large language models can alter behavior while leaving routine outputs largely unchanged, creating a challenge for AI governance when model weights are proprietary. We present a privacy-preserving zk-SNARK-based audit framework that searches for probes designed in the spirit of adversarial examples to amplify logit drift between an approved model and a modified deployment. Our framework explores complementary probe families under different access models. Token-based probes operate in a black-box setting and require only the input interface, tokenizer, and vocabulary. Embedding-based probes require gray-box access to the embedding interface. Stress probes rely on additional interface capabilities but do not require full white-box access to model weights or architecture. This range allows probe selection to balance sensitivity, access requirements, and deployment cost. We evaluate probe constructions across LLM architectures, model-tampering scenarios representative of post-deployment attacks, and GPU platforms. Importantly, our experimental results demonstrate that token-based probes consistently deliver the strongest mean sensitivity across models and GPU platforms, although operating in a black-box setting. Our Groth16 zk-SNARK workflow remains practical as the probe set scales from 1 to 50, where proving time increases from 1.02 to 1.78 seconds, verification remains near 0.84 seconds, and proof size remains constant.

## Metadata
- **Published**: 2026-08-28T05:51:22Z
- **Authors**: Cameron Wilding, Mina Shaker, Fatemeh Ganji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27954v1)