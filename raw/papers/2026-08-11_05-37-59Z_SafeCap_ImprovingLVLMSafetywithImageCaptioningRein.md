---
title: SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning
published: 2026-08-11T05:37:59Z
authors: Caoyuan Ma, Wenpu Liu, Weichu Xie, Tian Gu, Shilei Zhao, Lingxi Min, Shuai Dong, Yuqi Xu, Ji Zhao, Ziyue Wang, Wenzheng Chang, Taiqiang Wu, Yongfu Zhu, Wenqi Shao, Yinqiang Zheng
url: http://arxiv.org/abs/2608.10513v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning

## Abstract
Large vision-language models (LVLMs) remain vulnerable to jailbreak attacks that exploit visual inputs to bypass safety alignment inherited from their language backbones. We propose SafeCap, a reinforcement-learning framework that aligns LVLMs through learned self-captioning. SafeCap trains a policy model to first generate a safety-relevant image caption and then produce a final answer; the caption is further optimized by whether it enables a frozen LLM to reach a safety-aligned decision. This caption-mediated objective encourages the policy to expose visual cues relevant to safe response generation rather than relying solely on direct refusal supervision. Across five multimodal safety benchmarks and six vision-utility benchmarks, SafeCap substantially improves aggregate safety performance under its intended DirectCap protocol, with gains of 3.7-19.0 points in safety average across four model settings while maintaining comparable or improved vision utility. Under controlled comparisons on matched backbones and data, SafeCap outperforms safety SFT, DPO, and SafeGRPO, demonstrating the effectiveness of caption-mediated reinforcement learning for multimodal safety alignment.

## Metadata
- **Published**: 2026-08-11T05:37:59Z
- **Authors**: Caoyuan Ma, Wenpu Liu, Weichu Xie, Tian Gu, Shilei Zhao, Lingxi Min, Shuai Dong, Yuqi Xu, Ji Zhao, Ziyue Wang, Wenzheng Chang, Taiqiang Wu, Yongfu Zhu, Wenqi Shao, Yinqiang Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10513v1)