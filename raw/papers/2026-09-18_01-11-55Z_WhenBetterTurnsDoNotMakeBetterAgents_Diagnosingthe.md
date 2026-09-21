---
title: When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success
published: 2026-09-18T01:11:55Z
authors: Md Tahmid Rahman Laskar, Xue-Yong Fu, Gundeep Singh, Karol Chang, Kevin Sanders, Shi Zong, Tania Habib, Julien Bouvier Tremblay, Shayna Gardiner, Harsh Saini, Matthias Lee, Elena Khasanova, Quinten McNamara, Shashi Bhushan TN
url: http://arxiv.org/abs/2609.21187v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success

## Abstract
Agent models are frequently evaluated one decision at a time, where the model predicts the next action based on the gold interaction history, which is scored against a reference. We investigate whether improvement under this protocol is predictive of improved autonomous workflow execution. We study pre-SFT and supervised fine-tuned (SFT) Qwen3 models at 4B and 14B parameters and Gemma 3 models at 4B and 12B parameters on multi-turn customer-support workflows. We find that SFT consistently improves text-turn success, and that overall next-turn success increases for every model under gold-history evaluation. However, these improvements do not transfer to autonomous workflow execution. Tool-specific gains also vary across metrics and models. None of the four SFT models succeeds under holistic workflow evaluation, with strict trajectory completion reaching at most 10.4% workflow success. Our results show that next-turn evaluation is not a reliable proxy for workflow success, motivating separate reporting of text quality, local action correctness, tool execution, and end-to-end task completion.

## Metadata
- **Published**: 2026-09-18T01:11:55Z
- **Authors**: Md Tahmid Rahman Laskar, Xue-Yong Fu, Gundeep Singh, Karol Chang, Kevin Sanders, Shi Zong, Tania Habib, Julien Bouvier Tremblay, Shayna Gardiner, Harsh Saini, Matthias Lee, Elena Khasanova, Quinten McNamara, Shashi Bhushan TN
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21187v1)