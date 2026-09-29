---
title: LLMAdBench: A Human Preference Benchmark for Advertising in LLM Responses
published: 2026-09-26T12:14:49Z
authors: Rui Ai, Yuqing Liu, Sitao Qiu, Yun Qiao, Yuhan Wang, Jessica Xiwen Wang, Yiqi Yang, Lihong Huang, Ruiyao Sun, Kaifeng Zhang, Shengze Ding, Jiaqi He, Xinman Wang, Tianhao Gao, Jimmy Qin, Jianghao Lin, Chonghuan Wang
url: http://arxiv.org/abs/2609.32533v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMAdBench: A Human Preference Benchmark for Advertising in LLM Responses

## Abstract
Inserting advertisements (ads) into consumer-facing LLM output is emerging as a new business model, but there is little shared evidence on how such ad insertion should be evaluated or how it affects user preferences. We introduce LLMAdBench, a human-preference benchmark for studying advertising in LLM-generated content. The benchmark isolates a simple but practically important decision: given a user conversation, an LLM response, and a matched advertisement, where should the ad be placed? Our dataset compares pairs of responses that differ only in ad position while holding all other conditions fixed including the user query, base answer, advertisement, and disclosure condition. Human annotators evaluate each pair based on six criteria from both advertiser's and user's perspectives. The resulting benchmark contains more than 18000 human judgments across two disclosure conditions: explicitly labeling the ad as sponsored and merging it into the response without disclosure. We use LLMAdBench to evaluate eight frontier LLMs as preference judges and find that they are not reliable substitutes for human evaluation. Even the most stable models reverse roughly one quarter of their decisions when the presentation order is swapped, agreement across models is low, and their placement preferences differ systematically from those of human annotators. Moreover, LLMAdBench contains substantial learnable signal. In particular, a Qwen3-8B model fine-tuned on the human preferences improves substantially over its base model and outperforms all zero-shot frontier judges on the held-out prediction task. Beyond model evaluation, LLMAdBench provides quantitative evidence on the advertiser-user trade-off and shows that the sponsorship disclosure systematically changes users' preference over ad placement.

## Metadata
- **Published**: 2026-09-26T12:14:49Z
- **Authors**: Rui Ai, Yuqing Liu, Sitao Qiu, Yun Qiao, Yuhan Wang, Jessica Xiwen Wang, Yiqi Yang, Lihong Huang, Ruiyao Sun, Kaifeng Zhang, Shengze Ding, Jiaqi He, Xinman Wang, Tianhao Gao, Jimmy Qin, Jianghao Lin, Chonghuan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32533v1)