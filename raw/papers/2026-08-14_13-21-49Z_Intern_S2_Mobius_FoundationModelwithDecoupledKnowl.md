---
title: Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning
published: 2026-08-14T13:21:49Z
authors: Kai Chen, Jifeng Ding, Ning Ding, Jiaye Ge, Lixin Gu, Yicheng Gu, Qipeng Guo, Ermo Hua, Haian Huang, Haozheng Hou, Jie Hou, Xiangyu Hong, Che Jiang, Minxi Jin, Cheng Liang, Dahua Lin, Dawei Liu, Kuikun Liu, Chengqi Lv, Haijun Lv, Han Lv, Ningsheng Ma, Biqing Qi, Jianmin Qian, Shiya Su, Youbang Sun, Huanze Tang, Zhongbo Tian, Hanjing Wang, Rui Wang, Ting Wang, Yi Wang, Baiting Wu, Jun Xu, Bowen Yang, Hui Wang, Weida Wang, Haochen Ye, Jiashuo Yu, Shan Yu, Xiaoyi Yu, Qirui Zeng, Qi Zhang, Ming Zhang, Wenwei Zhang, Bowen Zhou, Xinyu Zhou
url: http://arxiv.org/abs/2608.14290v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning

## Abstract
We introduce Mobius-v0, an architecture that comprises a globally shared Memory (FFN) that stores knowledge vectors and multiple Reasoners (Self-Attn) that iteratively achieve compositional reasoning. Using hidden states as cache and carrier, reasoners repeatedly query memory for required knowledge-vectors, while the knowledge is transmitted back to reasoning operators. Through this knowledge-reasoning-separation architecture, Mobius achieves better knowledge compression and reasoning efficiency. Built upon Mobius-v0 architecture: 1) Our 7B model trained-from-scratch achieves similar downstream score as a 7B Transformer baseline with 62.6% of baseline's training data. 2) Our Intern-S2-Mobius, continually-pretrained from Qwen3.5-35B, achieves similar downstream score while delivering nearly 4x end-to-end inference speedup.

## Metadata
- **Published**: 2026-08-14T13:21:49Z
- **Authors**: Kai Chen, Jifeng Ding, Ning Ding, Jiaye Ge, Lixin Gu, Yicheng Gu, Qipeng Guo, Ermo Hua, Haian Huang, Haozheng Hou, Jie Hou, Xiangyu Hong, Che Jiang, Minxi Jin, Cheng Liang, Dahua Lin, Dawei Liu, Kuikun Liu, Chengqi Lv, Haijun Lv, Han Lv, Ningsheng Ma, Biqing Qi, Jianmin Qian, Shiya Su, Youbang Sun, Huanze Tang, Zhongbo Tian, Hanjing Wang, Rui Wang, Ting Wang, Yi Wang, Baiting Wu, Jun Xu, Bowen Yang, Hui Wang, Weida Wang, Haochen Ye, Jiashuo Yu, Shan Yu, Xiaoyi Yu, Qirui Zeng, Qi Zhang, Ming Zhang, Wenwei Zhang, Bowen Zhou, Xinyu Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14290v1)