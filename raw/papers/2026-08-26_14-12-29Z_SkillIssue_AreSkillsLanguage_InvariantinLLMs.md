---
title: Skill Issue: Are Skills Language-Invariant in LLMs?
published: 2026-08-26T14:12:29Z
authors: Bobby Cheng, Adam Gaber, Zhengyuan Liu, Catherine Arnett, Omer Goldman, Cheston Tan, Leshem Choshen
url: http://arxiv.org/abs/2608.25832v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Skill Issue: Are Skills Language-Invariant in LLMs?

## Abstract
Large language models access knowledge inconsistently across languages, but to what extent do they differ in their skill sets when interacting with different languages? This work quantifies cross-lingual skill inconsistency orthogonally from knowledge and general benchmark performance. We do this via multilingual self-play: two instances of the same model compete in a text-based game, each interacting through a different language interface. Since the model, opponent, rules, state space, and available actions remain fixed, this setting isolates the effect of language on the model's realized behavior. We build a multilingual extension to TextArena and evaluate three open-weight models across eight languages and six games covering spatial reasoning, imperfect information, resource allocation, and repeated interaction. We find that the same model can exhibit markedly different playing strength across languages, with systematic variation in win--loss margins, invalid actions, and strategic tendencies. Detailed analyses reveal language-specific failures in spatial reasoning, card-conditioned decisions, and optimal move selection. In some settings, changing only the intermediate reasoning language recovers much of the lost performance, suggesting that language can affect different stages of the decision process. These results show that skill discrepancies are a measurable major roadblock in the development of truly multilingual models. Better understanding these discrepancies can help us design models that perform more equitably across languages.

## Metadata
- **Published**: 2026-08-26T14:12:29Z
- **Authors**: Bobby Cheng, Adam Gaber, Zhengyuan Liu, Catherine Arnett, Omer Goldman, Cheston Tan, Leshem Choshen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25832v1)