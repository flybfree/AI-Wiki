---
title: SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Personal Information
published: 2026-08-11T09:14:53Z
authors: Junjie Ye, Zhuohui Sheng, Shaofan Liu, Yulun Zhu, Wenjie Fu, Dingwei Zhu, Ming Zhang, Yujiong Shen, Weichao Wang, Xin Zhao, Shihan Dou, Tao Gui, Qi Zhang, Xuanjing Huang, Pluto Zhou
url: http://arxiv.org/abs/2608.10692v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Personal Information

## Abstract
Large language models (LLMs) are increasingly deployed as mobile assistants, where a key challenge is leveraging personal information scattered across multiple applications (apps) to complete user instructions. However, due to the lack of dedicated benchmarks, their capabilities remain poorly understood. To address this gap, we introduce SPIEval, a human-curated benchmark grounded in five cognitive capabilities (i.e., reasoning, disambiguation, integration, preference inference, and multi-intent decomposition). SPIEval comprises 250 tasks spanning 4,335 personal records distributed across 10 apps and supports multi-turn interaction through 21 tools. Analysis shows that the benchmark exhibits diverse scenarios, challenging tasks, scattered information, controllable environments, and verifiable outcomes. We evaluate nine representative LLMs and find substantial room for improvement. The best-performing model, GPT-5.5 (xhigh), achieves only 57.3% accuracy, while the weakest achieves just 16.4%. Further analysis reveals that 79% of failures stem from inaccurate information localization, as LLMs often commit to plausible but incorrect information instead of continuing retrieval for verification. We also find that fewer than 2% of retrieval actions employ advanced search methods and observe substantial variation in search efficiency across models. These findings expose fundamental limitations of current LLM-based mobile assistants and motivate future research in this direction. Data and code are available at https://huggingface.co/datasets/Junjie-Ye/SPIEval.

## Metadata
- **Published**: 2026-08-11T09:14:53Z
- **Authors**: Junjie Ye, Zhuohui Sheng, Shaofan Liu, Yulun Zhu, Wenjie Fu, Dingwei Zhu, Ming Zhang, Yujiong Shen, Weichao Wang, Xin Zhao, Shihan Dou, Tao Gui, Qi Zhang, Xuanjing Huang, Pluto Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10692v1)