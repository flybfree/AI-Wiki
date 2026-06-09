---
title: From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills
published: 2026-05-22T17:59:12Z
authors: Zisu Huang, Jingwen Xu, Yifan Yang, Ziyang Gong, Qihao Yang, Muzhao Tian, Xiaohua Wang, Changze Lv, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Xue Yang, Dongdong Chen, Xiaoqing Zheng, Chong Luo
url: http://arxiv.org/abs/2605.23899v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills

## Abstract
Language agents increasingly improve by reusing \emph{skills} -- structured procedural artifacts distilled from past experience. In particular, \emph{domain-level} and \emph{model-generated} skills are especially promising. They offer fast adaptation within a domain by encoding domain-specific recurring procedures, and they scale beyond labor-intensive hand-crafting. However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail. To close this gap, we build a utility-grounded evaluation framework that provides systematic experimental results across extractors and target agents, covering five diverse agentic task domains. We find that model-generated skills are beneficial on average but exhibit non-trivial negative transfer, and that neither extractors nor targets behave uniformly. A model can be a strong extractor yet a weak consumer, or vice versa, with skill utility independent of model scale or baseline task strength. To explain these patterns, we then dissect each lifecycle stage in depth, analyzing how experience composition shapes skill quality, what properties characterize useful skills, and how the same skill transfers across different consumers. Finally, we translate these findings into a concrete \emph{meta-skill} that guides skill extraction toward the features tied to actual utility, which consistently improves skill quality across domains and substantially reduces negative transfer.

## Metadata
- **Published**: 2026-05-22T17:59:12Z
- **Authors**: Zisu Huang, Jingwen Xu, Yifan Yang, Ziyang Gong, Qihao Yang, Muzhao Tian, Xiaohua Wang, Changze Lv, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Xue Yang, Dongdong Chen, Xiaoqing Zheng, Chong Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23899v1)