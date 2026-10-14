---
title: ReTerm: Recovery Training for Self-Improving Terminal Agents
published: 2026-10-13T14:44:24Z
authors: Wei Xie, Kaituo Feng, Shiming Fu, Yong Liu, Xiangyu Yue, Shuangjia Zheng
url: http://arxiv.org/abs/2610.18484v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReTerm: Recovery Training for Self-Improving Terminal Agents

## Abstract
Terminal agents have shown strong abilities in complex coding tasks. However, they often struggle to recover from errors during long-running execution (e.g., command errors, faulty implementations), eventually leading to task failures. To this end, we present ReTerm, a self-improving terminal agent trained by learning how to recover from its own failed terminal tasks. To support its training, we construct a customized data pipeline and produce ReTerm-10K, a high-quality dataset that provides effective recovery demonstrations for SFT cold start. Furthermore, we propose ReTerm-GRPO, an online RL algorithm that forks from the agent's own failure states to generate multiple independent self-recovery attempts. By learning from whether these attempts successfully complete the task, the agent self-improves through its own recovery experience. Built on Qwen3.5-9B, our ReTerm-9B achieves 34.8% Pass@1 on Terminal-Bench 2.0, improving over the base model by 14.6 points. Further analysis shows that our method achieves consistently higher recovery rates across diverse error categories compared with standard GRPO training. All code, data and model are released at https://github.com/twothsnd/ReTerm.

## Metadata
- **Published**: 2026-10-13T14:44:24Z
- **Authors**: Wei Xie, Kaituo Feng, Shiming Fu, Yong Liu, Xiangyu Yue, Shuangjia Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18484v1)