---
title: Over-Defense in Coding Agents Begins at Silent Forks
published: 2026-10-18T01:56:29Z
authors: Hanjun Luo, Xuecheng Liu, Xiucheng Zhang, Zhuoning Xu, Yingbin Jin, Yankai Chen, Xue Liu, Hanan Salam
url: http://arxiv.org/abs/2610.24949v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Over-Defense in Coding Agents Begins at Silent Forks

## Abstract
Language models behind coding agents are post-trained with outcome rewards, and recent methods concentrate credit on the turns that decide the outcome. We find that defensive actions beyond what a task requires escape both. They begin at silent forks, the turns where every next action leads to the same outcome. Such actions leave the success rate unchanged, and frontier models take the disproportionate branch there in up to 91% of decisive actions under implicit budgets. The most direct fix, a checker in the trajectory reward, reaches these forks only through fully proportionate trajectories, leaving 74% of GRPO groups with identical rewards and behavior unchanged. This motivates a rethink of where learning signals belong, namely where behavior diverges, which a behavioral checker can locate and the outcome cannot. Our method, ForkDPO, contrasts a proportionate and a disproportionate action at the same prefix, at silent forks on both sides of the required behavior. On a test set of unseen repositories, it lowers a 4B model's disproportionate behavior from 70.3% to 58.9%, against 67.7% for DPO at randomly chosen turns, establishing behavioral divergence as a learning signal for how agents act beyond whether they finish. The code is publicly available at https://github.com/Astarojth/silent-forks.

## Metadata
- **Published**: 2026-10-18T01:56:29Z
- **Authors**: Hanjun Luo, Xuecheng Liu, Xiucheng Zhang, Zhuoning Xu, Yingbin Jin, Yankai Chen, Xue Liu, Hanan Salam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24949v1)