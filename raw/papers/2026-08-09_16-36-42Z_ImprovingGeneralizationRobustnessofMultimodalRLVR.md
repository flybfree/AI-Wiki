---
title: Improving Generalization Robustness of Multimodal RLVR
published: 2026-08-09T16:36:42Z
authors: Pengfei Zhou, Zhiwei Tang, Xiaopeng Peng, Chenrui Zhou, Lama Moukheiber, Yixing Ma, Bin Xu, Jiajun Song, Zhenglin Wan, Wangbo Zhao, Jiasheng Tang, Bohan Zhuang, Fan Wang, Yang You
url: http://arxiv.org/abs/2608.08802v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving Generalization Robustness of Multimodal RLVR

## Abstract
Reinforcement Learning with Verifiable Rewards (RLVR) makes Multimodal Large Language Models more accurate, but the gains are brittle: simply paraphrasing a question or changing the prompt template can degrade them, which challenges reliable deployment in high-stakes scenarios like medical VQA. We trace this to two issues of the standard RL objective. First, the binary verifier conflates format with content, so the reward signal cannot tell a wrong answer apart from a misformatted one. Second, the training distribution covers only a thin slice of the real-world prompts that the model might meet at deployment, so policies that perform well on the training distribution can behave differently under unseen prompts during test. Both failures call for a robust post-training method that helps the policy cover a broader distribution of semantically equivalent prompts, and we identify two measures that help achieve this objective: separating format from semantics in the reward, and applying policy invariance across perturbed prompts with equivalent semantics. We therefore propose Prompt-Invariant RLVR (PIRL), consisting of a dynamic trinary reward and a consistency regularizer based on an embedding-space adversary. Under stress testing, PIRL's average accuracy on benchmarks drops by only $\le 1\%$, where GRPO drops ~3%. On dynamic evaluation, PIRL also achieves the smallest performance drop.

## Metadata
- **Published**: 2026-08-09T16:36:42Z
- **Authors**: Pengfei Zhou, Zhiwei Tang, Xiaopeng Peng, Chenrui Zhou, Lama Moukheiber, Yixing Ma, Bin Xu, Jiajun Song, Zhenglin Wan, Wangbo Zhao, Jiasheng Tang, Bohan Zhuang, Fan Wang, Yang You
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08802v1)