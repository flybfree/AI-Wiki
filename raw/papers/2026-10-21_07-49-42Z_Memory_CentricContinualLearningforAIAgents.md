---
title: Memory-Centric Continual Learning for AI Agents
published: 2026-10-21T07:49:42Z
authors: Dongfang Li, Zhuoen Chen, Bonian Jia, Zixuan Liu, Zhengxuan Lu, Can Deng, Yukun Shi, Yuhang Meng, Xin Zhang, Jiahe Huang, Fuhao Li, Junmai Wang, Shunyao Wen, Jingjun Sun, Jiaxu Tian, Jiangling Zhang, Zihan Wang, Liangyou Li, Yitong Yao, Shuangyong Song, Beilun Wang, Pengxu Wei, Hanlin Xu, Chang Liu, Yongxiang Li, Baotian Hu, Xiangyang Ji, Min Zhang
url: http://arxiv.org/abs/2610.29357v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory-Centric Continual Learning for AI Agents

## Abstract
Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive retrieval caches, evaluated primarily by whether they can recall stored facts or past interactions. Whether memory can drive genuine continual learning remains an open question. In this paper, we introduce Memory-Centric Continual Learning (MCCL), arguing that memory should be judged by whether it improves future actions, not merely what it retrieves. MCCL has three main parts. First, a three-axis taxonomy organizes memory by where state is stored (substrates), what form it takes (assets), and how it is managed (policies). This defines a two-loop lifecycle that updates memory state in an inner loop while refining management policies in an outer loop based on task feedback. Second, an evaluation protocol measures retention under interference, adaptation to change, and task transfer to isolate genuine behavioral gains from simple context expansion. Third, a memory scaling framework models how agent performance scales with experience, storage capacity, and compute budgets across non-parametric and parametric memory. Together, these components reframe agent memory from passive lookup to continuous learning, offering a principled route toward self-improving autonomous agents.

## Metadata
- **Published**: 2026-10-21T07:49:42Z
- **Authors**: Dongfang Li, Zhuoen Chen, Bonian Jia, Zixuan Liu, Zhengxuan Lu, Can Deng, Yukun Shi, Yuhang Meng, Xin Zhang, Jiahe Huang, Fuhao Li, Junmai Wang, Shunyao Wen, Jingjun Sun, Jiaxu Tian, Jiangling Zhang, Zihan Wang, Liangyou Li, Yitong Yao, Shuangyong Song, Beilun Wang, Pengxu Wei, Hanlin Xu, Chang Liu, Yongxiang Li, Baotian Hu, Xiangyang Ji, Min Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.29357v1)