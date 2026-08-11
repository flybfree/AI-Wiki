---
title: Measuring the Wrong Thing: Internal Harmfulness Scores Anti-Rank Successful Jailbreaks
published: 2026-08-10T14:05:32Z
authors: Mingyu Luo, Ming Deng, Zilang Qiu, Yiming Cheng, Ci Tao, Xue Tan, Sijin Sun, Yangfu Li, Ping Chen, Jun Dai, Xiaoyan Sun
url: http://arxiv.org/abs/2608.09624v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring the Wrong Thing: Internal Harmfulness Scores Anti-Rank Successful Jailbreaks

## Abstract
Internal safety scores judge a prompt before any text is generated, and they are validated by how well they separate harmful prompts from benign ones. That separation is then read as evidence that the score will also catch the attacks that succeed. Harmful intent is a property of the prompt. Jailbreak success is an outcome produced later by a particular target model, decoding policy, and judge. A filter tuned on a score that measures the wrong quantity spends its false positive budget on attacks that would have failed anyway. In this paper we audit that inference. Attention based measurements are usually read from prompt dependent locations, so a wrapper changes both the content being judged and the place the signal is taken from. We therefore introduce Active Attention Probing, which supplies a fixed content independent measurement coordinate. We pair every base goal with a plain and a wrapped version and generate real completions from the target models. On Llama, wrapping raises harmful generation from 0.05 to 0.27 while harmful intent AUROC falls from 0.936 to 0.803, so the attacks grow more dangerous while the prompts look safer to the score. Among wrapped harmful prompts the outcome AUROC is 0.220, which places the attacks that succeeded below the attacks that failed. Rare token, passive, and detector derived channels reproduce the reversal on the same matched design, and the reversal itself persists across three target models, seven attack families, and two independent judges. Distribution shift then degrades calibration and threshold transfer before it degrades ranking.

## Metadata
- **Published**: 2026-08-10T14:05:32Z
- **Authors**: Mingyu Luo, Ming Deng, Zilang Qiu, Yiming Cheng, Ci Tao, Xue Tan, Sijin Sun, Yangfu Li, Ping Chen, Jun Dai, Xiaoyan Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09624v1)