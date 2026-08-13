---
title: MuseCritic: Learning Multi-Aspect Song Rewards through Natural-Language Aesthetic Critiques
published: 2026-08-12T07:49:17Z
authors: Jiabao Zhuang, Changhao Jiang, Hanchen Wang, Jiahao Chen, Zhixiong Yang, Zhenghao Xiang, Yifei Cao, Jiajun Sun, Hui Li, Ming Zhang, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang
url: http://arxiv.org/abs/2608.11755v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MuseCritic: Learning Multi-Aspect Song Rewards through Natural-Language Aesthetic Critiques

## Abstract
Long-form song generation models continue to improve in duration, structural integrity, and acoustic complexity, making reliable aesthetic rewards increasingly important for aligning these models with human preferences. However, reward models for complete songs remain limited, and existing evaluators typically predict scores in a single forward pass without providing readable explanations. We introduce MUSECRITIC, a semi-scalar reward model that generates a natural-language critique covering five aesthetic dimensions and uses it as an intermediate representation to predict continuous reward scores. MUSECRITIC follows a two-stage training pipeline: a teacher model first provides high-quality critiques for supervised fine-tuning, after which the fine-tuned model generates its own critiques for reward learning, mitigating distribution shift between training and inference. On an in-domain test set of 200 SongEval songs, MUSECRITIC reduces macro-averaged mean squared error from 0.2875 to 0.2316 and improves macro-averaged LCC, SRCC, and Kendall's tau to 0.9068, 0.8838, and 0.7178, respectively. On the out-of-domain Music Arena benchmark with 733 preference pairs, it achieves the highest accuracy of 71.35%. Moreover, using MUSECRITIC with GRPO improves Muse-0.6B on all nine aesthetic metrics from SongEval and Audiobox Aesthetics. These results demonstrate that critique-conditioned reward modeling reduces scoring error and provides an effective optimization signal for song generation. The project repository is available at https://github.com/WuqnEl/MuseCritic.

## Metadata
- **Published**: 2026-08-12T07:49:17Z
- **Authors**: Jiabao Zhuang, Changhao Jiang, Hanchen Wang, Jiahao Chen, Zhixiong Yang, Zhenghao Xiang, Yifei Cao, Jiajun Sun, Hui Li, Ming Zhang, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11755v1)