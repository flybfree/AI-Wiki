---
title: Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL
published: 2026-08-18T01:16:02Z
authors: Yunhao Yang, Yuexin Bian, Yunjie Tian, Di Fu, Tianjin Huang, Yuanyuan Shi, Ziang Xiao, Nuno Vasconcelos, Yijiang Li
url: http://arxiv.org/abs/2608.17253v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL

## Abstract
Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its strongest successes still depend heavily on ground-truth supervision (e.g., verifiable reward). Such annotations are costly to obtain and become increasingly scarce as reasoning capabilities advance beyond what humans can reliably evaluate. Self-rewarding RL reduces this dependence by enabling models to derive reward signals from their own completions. However, training solely on self-generated feedback can reinforce existing biases and suboptimal behaviors, reduce response diversity, and ultimately lead to homogenized responses and training collapse. In this work, we show that unsupervised reasoning can emerge through cooperative multi-agent training. We introduce Co-RL, a framework in which multiple decoupled models, sharing no parameters, are simultaneously optimized through RL using rewards derived from their peers. We further show that increasing cohort diversity, through heterogeneous model families, sizes, and rephrased training samples, reduces the correlated errors that drive self-reinforcing feedback loops. This diversity consistently improves reasoning performance, maintains behavioral diversity, and mitigates training collapse. Across text-only and multimodal domains, Co-RL consistently outperforms the base models and prior label-free approaches, while matching or surpassing supervised methods, without access to any ground-truth labels. Concretely, Co-RL yields average gains of 3.0-8.6% across seven text-only benchmarks for LLMs and 2.3-7.2% across four multimodal benchmarks for VLMs. Code is available at https://github.com/DrStranded/Co-RL.

## Metadata
- **Published**: 2026-08-18T01:16:02Z
- **Authors**: Yunhao Yang, Yuexin Bian, Yunjie Tian, Di Fu, Tianjin Huang, Yuanyuan Shi, Ziang Xiao, Nuno Vasconcelos, Yijiang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17253v1)