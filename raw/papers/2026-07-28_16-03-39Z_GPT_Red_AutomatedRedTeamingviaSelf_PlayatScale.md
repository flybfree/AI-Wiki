---
title: GPT-Red: Automated Red Teaming via Self-Play at Scale
published: 2026-07-28T16:03:39Z
authors: Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal, Sam Toyer, Dylan Hunn, Stephanie Lin, Yuxin Wen, Xiangyu Qi, Christopher Wolff, Zizhao Wang, Milad Nasr, Sicheng Zhu, Chuan Guo, Juan Felipe Cerón Uribe, Kaiwen Wang, Aiden Low, Kai Xiao, Kai Chen
url: http://arxiv.org/abs/2607.26115v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GPT-Red: Automated Red Teaming via Self-Play at Scale

## Abstract
We introduce \textbf{GPT-Red}, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs. The goal of this model is to evaluate and improve the robustness of our production systems. To this end, we use it to adversarially train GPT-5.6, our most robust model to prompt injections to date. To create GPT-Red, we design a scalable self-play algorithm where the model is tasked with attacking a diverse population of simultaneously-trained defender agents. We train the model on realistic red-teaming environments using compute on the same scale as some of our largest RL post-training runs, making it the single-largest LLM safety training run ever documented. GPT-Red excels at red-teaming: it reliably breaks our past models up to GPT-5.5, it finds more successful attacks than human red-teamers, and it generalizes to held-out environments, defender models, and harnesses. In the future, we expect that as we improve the robustness of each new GPT model, it will in turn will provide better learning signal for \textit{even stronger} red-teamer agents, thus unlocking a self-improvement flywheel.

## Metadata
- **Published**: 2026-07-28T16:03:39Z
- **Authors**: Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal, Sam Toyer, Dylan Hunn, Stephanie Lin, Yuxin Wen, Xiangyu Qi, Christopher Wolff, Zizhao Wang, Milad Nasr, Sicheng Zhu, Chuan Guo, Juan Felipe Cerón Uribe, Kaiwen Wang, Aiden Low, Kai Xiao, Kai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26115v1)