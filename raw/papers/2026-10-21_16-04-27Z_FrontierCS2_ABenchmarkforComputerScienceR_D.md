---
title: FrontierCS 2: A Benchmark for Computer Science R&D
published: 2026-10-21T16:04:27Z
authors: Qiuyang Mang, Wenhao Chai, Runyuan He, Dongruixuan Li, Zihan Zheng, Yujun He, Xuanyi Zhou, Hao Wang, Siddhant Ray, Bo Peng, Ruyi Ji, Shuo Yang, Haocheng Xi, Boru Chen, Xinyang David Han, Melissa Pan, Mayank Mishra, Boxi Yu, Sijia Liu, Kerem Akillioglu, Yi Pan, Zirui Wang, Mert Cemri, Diogo Antunes, Yichuan Wang, Aiwei Ivy Zhang, Zhenyang Chen, Qizheng Zhang, Kaiyuan Liu, Wenyuan Huang, Sherry Ruan, Shu Liu, Dacheng Li, Zerui Cheng, Zeyu Shen, Shang Zhou, Hanfei Chen, Yuzhong Zhang, Bohan Lyu, Qu Ao, Han Zheng, Chonghe Jiang, Jingzhuo Hu, Xiaokun Chen, Kunjun Li, Zhiqing Zhong, Haoye Tian, Tong Zhao, Yunzhong He, Hanchen Li, Ofir Press, Jiantao Jiao, Kunle Olukotun, Karthik R. Narasimhan, Jingbo Shang, Koushik Sen, Matei Zaharia, Alex Dimakis, Ion Stoica, Joseph E. Gonzalez, Alvin Cheung
url: http://arxiv.org/abs/2610.29932v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FrontierCS 2: A Benchmark for Computer Science R&D

## Abstract
Can LLM agents make contributions to frontier computer science R&D? We introduce FrontierCS 2, a benchmark of 48 open-ended tasks. We take a paper and the code its authors released and delete the paper's contribution. The deleted code becomes the human reference that sets the bar. Earlier open-ended benchmarks give each agent a problem statement and grade one program after the run. FrontierCS 2 places the agent inside a research environment. The agent inherits a working repository and may submit a patch at any point. For each patch, a judge returns a development-suite score but keeps the evaluator, the held-out final suite and the reference private, and grades the final submission on that suite against the reference. The tasks span 13 domains, from machine-learning systems and high-performance computing to databases, security and robotics. Beyond these 48 tasks, FrontierCS 2 keeps a private set of more than 100 tasks, to be announced in the future. We evaluate 12 agents. The best one is Claude Opus 5.5, passing 58% of its runs. No run passes on 16 tasks. A higher score is not the same as a pass: most runs that beat the reference on the combined final score still fall short on some metric or workload. On a shared capability scale for agents and tasks, the median task is roughly as difficult as what the strongest agent can handle.

## Metadata
- **Published**: 2026-10-21T16:04:27Z
- **Authors**: Qiuyang Mang, Wenhao Chai, Runyuan He, Dongruixuan Li, Zihan Zheng, Yujun He, Xuanyi Zhou, Hao Wang, Siddhant Ray, Bo Peng, Ruyi Ji, Shuo Yang, Haocheng Xi, Boru Chen, Xinyang David Han, Melissa Pan, Mayank Mishra, Boxi Yu, Sijia Liu, Kerem Akillioglu, Yi Pan, Zirui Wang, Mert Cemri, Diogo Antunes, Yichuan Wang, Aiwei Ivy Zhang, Zhenyang Chen, Qizheng Zhang, Kaiyuan Liu, Wenyuan Huang, Sherry Ruan, Shu Liu, Dacheng Li, Zerui Cheng, Zeyu Shen, Shang Zhou, Hanfei Chen, Yuzhong Zhang, Bohan Lyu, Qu Ao, Han Zheng, Chonghe Jiang, Jingzhuo Hu, Xiaokun Chen, Kunjun Li, Zhiqing Zhong, Haoye Tian, Tong Zhao, Yunzhong He, Hanchen Li, Ofir Press, Jiantao Jiao, Kunle Olukotun, Karthik R. Narasimhan, Jingbo Shang, Koushik Sen, Matei Zaharia, Alex Dimakis, Ion Stoica, Joseph E. Gonzalez, Alvin Cheung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.29932v1)