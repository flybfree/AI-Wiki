---
title: Robust Context-Aware Detection of Malicious Instructions in Text
published: 2026-08-05T21:44:44Z
authors: Buzhao Liu, Xinhang Ma, Yevgeniy Vorobeychik
url: http://arxiv.org/abs/2608.05430v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust Context-Aware Detection of Malicious Instructions in Text

## Abstract
The remarkable instruction-following ability of modern LLMs has enabled their practical use as the minds of agents that can autonomously complete increasingly complex tasks. Therein, however, also lies their vulnerability to attacks which embed malicious instructions in text, common variants of which are known as indirect prompt injection (IPI). A fundamental task in addressing this vulnerability is successful segmentation of a given text into benign and malicious sentences (if any). While a number of approaches for this task have been proposed, no detector combines query-relative detection at the segment level, and none are hardened against adaptive evasion attacks realizable in agentic executions. We address the former limitation by developing an approach for malicious sentence classification that is both context- and query-aware. Next, to harden the resulting classifier against evasion, we present two adversarial training methods. The first is directly adapted feature-space adversarial training (AT) in which evasions are approximated using projected-gradient-based optimization in the embedding space. The second simulates realizable evasion attacks in the AT loop through LLM-based paraphrasing. Crucially, we parametrize both AT variants to facilitate a smooth tradeoff between utility and attack robustness. In extensive experiments using indirect prompt injection benchmarks we show that the proposed approach outperforms state-of-the-art IPI defense baselines under static attacks, while in the case of adaptive attacks, our AT variants provide significantly higher utility, lower attack success rate, and often both. Finally, we show that the best AT parameters can depend intimately on the particular application domain. Consequently, domain-dependent tuning of malicious text detectors is likely necessary in practice. Our code is publicly available at https://github.com/tavia-liu/CAD.

## Metadata
- **Published**: 2026-08-05T21:44:44Z
- **Authors**: Buzhao Liu, Xinhang Ma, Yevgeniy Vorobeychik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05430v1)