---
title: Does Deeper Reasoning Compromise Alignment? Revealing and Mitigating of Alignment Collapse in Large Reasoning Models
published: 2026-09-08T03:18:22Z
authors: Yu-Hang Wu, Yu-Jie Xiong, Henghua Zhang, Bairui Zhang, Jia-Chen Zhang, Shaohua Li
url: http://arxiv.org/abs/2609.08186v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does Deeper Reasoning Compromise Alignment? Revealing and Mitigating of Alignment Collapse in Large Reasoning Models

## Abstract
The emergence of Chain-of-Thought (CoT) has established a robust foundation for Large Reasoning Models (LRMs). While deep reasoning is widely believed to enhance safety alignment, the stability of alignment mechanisms under extended reasoning remains underexplored. This paper challenges the prevailing view by revealing a critical vulnerability: Deep Reasoning May Induce Alignment Collapse. To rigorously quantify this phenomenon, we propose the Alignment Loss Rate (ALR) metric. Our experiments demonstrate that as reasoning depth increases, ALR rises significantly, indicating a severe degradation in model robustness against external perturbations. Capitalizing on this instability, a novel jailbreaking paradigm, Reasoning Trap (RT), is proposed. RT induces the model into extended reasoning to amplify the impact of adversarial attacks, leading to a sharp decline in safety capabilities. To elucidate the mechanism behind this collapse, we identify Attention Dilution as the root cause, arising from the competition for attention between the extended reasoning process and the original input. To mitigate this, Reasoning Residual Alignment (RRA), a lightweight defense strategy that dynamically re-emphasizes the input via residual connections integrated with the reasoning process.

## Metadata
- **Published**: 2026-09-08T03:18:22Z
- **Authors**: Yu-Hang Wu, Yu-Jie Xiong, Henghua Zhang, Bairui Zhang, Jia-Chen Zhang, Shaohua Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08186v1)