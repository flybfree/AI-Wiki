---
title: ROCS: Request-Oriented Compute Sharing for Efficient Large-Scale Recommendation
published: 2026-07-30T06:33:50Z
authors: Yuxin Chen, Liang Luo, Buyun Zhang, Jian Jiao, Boda Li, Haoyu Wang, Tongyi Tang, Ao Cai, Zijian Shen, Zhengkai Zhang, Wenyi Xie, Ryan Dick, Han Liu, Neng Shi, Bin Yu, Jianbo Xiao, Shuyao Bi, Hongtao Yu, Yuanwei Fang, Zhuoran Zhao, Sijia Chen, Yang Chen, Shuqi Yang, Qianru Li, Zikun Liu, Wei Ling, Sihan Zeng, Longhao Jin, Jiaxin Lu, Yinbin Ma, Jiawei Li, Yichen Ruan, Yong Ler Lee, Birmingham Guan, Zijian Li, Jianbo Sun, Zhengyu Zhang, Zeliang Chen, Xiaohan Wei, Yuchen Hao, GP Musumeci, Venkatesh Ranganathan, Yantao Yao, Chunqiang Tang, Wenlin Chen, Santanu Kolay, Ellie Dingqiao Wen
url: http://arxiv.org/abs/2607.27744v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ROCS: Request-Oriented Compute Sharing for Efficient Large-Scale Recommendation

## Abstract
Modern recommendation models gain prediction quality by scaling feature-interaction and sequence modules, but production cost constraints cap how far systems can scale.   In this work, we propose Request-Oriented Compute Sharing (ROCS), a modeling and inference paradigm that exploits a unique property of recommendation inference: each user request is evaluated against many candidates, while request-side features are shared across candidates. ROCS defers request-candidate interactions as late as possible, isolates candidate-dependent representations, and evaluates substantial portions of the model once per request rather than once per candidate, significantly improving inference efficiency while maintaining or improving prediction quality. To realize this paradigm, we develop Generalized Layer Masking (GLM) to enforce candidate isolation in feature-interaction architectures, and Deep Cross Attention (DCA) to extend request-oriented sharing to sequence architectures. To support efficient GPU deployment, we co-design In-Kernel Broadcast Optimization (IKBO) that significantly accelerates ROCS model execution.   Experiments on public benchmarks show that ROCS consistently improves the quality-efficiency tradeoff across recommendation backbones. On production-scale workloads, ROCS achieves up to a 3x QPS improvement on retrieval models without quality degradation and a 0.5% relative LogLoss improvement with a 50% QPS gain on a short-form video ranking model. ROCS has been deployed across large-scale recommendation systems spanning ads and organic surfaces, retrieval and ranking stages, and more than two orders of magnitude in inference complexity, delivering significant online gains at reduced infrastructure cost.

## Metadata
- **Published**: 2026-07-30T06:33:50Z
- **Authors**: Yuxin Chen, Liang Luo, Buyun Zhang, Jian Jiao, Boda Li, Haoyu Wang, Tongyi Tang, Ao Cai, Zijian Shen, Zhengkai Zhang, Wenyi Xie, Ryan Dick, Han Liu, Neng Shi, Bin Yu, Jianbo Xiao, Shuyao Bi, Hongtao Yu, Yuanwei Fang, Zhuoran Zhao, Sijia Chen, Yang Chen, Shuqi Yang, Qianru Li, Zikun Liu, Wei Ling, Sihan Zeng, Longhao Jin, Jiaxin Lu, Yinbin Ma, Jiawei Li, Yichen Ruan, Yong Ler Lee, Birmingham Guan, Zijian Li, Jianbo Sun, Zhengyu Zhang, Zeliang Chen, Xiaohan Wei, Yuchen Hao, GP Musumeci, Venkatesh Ranganathan, Yantao Yao, Chunqiang Tang, Wenlin Chen, Santanu Kolay, Ellie Dingqiao Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27744v1)