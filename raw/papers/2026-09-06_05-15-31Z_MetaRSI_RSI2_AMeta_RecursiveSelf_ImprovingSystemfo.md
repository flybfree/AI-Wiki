---
title: MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves
published: 2026-09-06T05:15:31Z
authors: Zihan Tan, Leixin Sun, Zitong Shi, Yitao Liu, Jiajun Wu, Nathaniel Brooks, Jiaru Qian, Xiaoran Shang, Suyuan Huang, Yi Ding, Yangxu Liao, Mukai Li, Qiushi Sun, Shudong Liu, Xuankun Rong, Xiaohang Yu, Zhuo Chen, Hejia Geng, Chenxin Li, Aozhou Wang, Zengji Tu, Robert Tang, Yuxin Zhan, Eric Jiang, Yuxin Wu, Jianqing Zhang, Xiao Liang, Fang Wu, Haochi Zhang, Alexander Marlow, Guancheng Wan
url: http://arxiv.org/abs/2609.06396v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves

## Abstract
Recursive self-improvement (RSI) lets a system improve the model-building machinery from its own failures, so every later model inherits the gain. Yet RSI has been validated almost exclusively on coding and formal benchmarks such as science QA and mathematics. This format bound limits RSI to improvement within a machine-checkable slice, not general capability where questions are open and correctness is settled by argument, replication, or measurement. We argue RSI must next operate across real, diverse scientific, engineering, and meta-scientific domains, not where formal evaluation is merely tractable. To that end we present MetaRSI-v1, where improvement is the scheduled composition of three typed operators over one unified paradigm. Data-RSI amplifies existing competence and marks its boundary; Harness-RSI edits a five-slot scaffold without touching weights; Model-RSI internalizes capability into parameters through bounded training. Sharing one loop kernel and artifact vocabulary, they make data, scaffold, and model changes composable rather than exclusive. A two-axis optimizer jointly decides operator order and each operator's proposal policy, while a meta-level policy revises the schedule across terms. We validate MetaRSI-v1 under the field's standard evaluations, on code and closed-form science, with no external teacher: the target model plays every role in its own loop. MetaRSI-v1 reframes self-improvement from a single-surface edit to a composition across the full model-production pipeline, opening two paths: a model route internalizing capability through training, and a harness route leaving weights untouched and thus extending self-improvement to any model reachable through an interface, with Data-RSI redefined as the shared substrate feeding both. The framework further yields refutable laws on where loops exist, how operators compose, and what supervision buys.

## Metadata
- **Published**: 2026-09-06T05:15:31Z
- **Authors**: Zihan Tan, Leixin Sun, Zitong Shi, Yitao Liu, Jiajun Wu, Nathaniel Brooks, Jiaru Qian, Xiaoran Shang, Suyuan Huang, Yi Ding, Yangxu Liao, Mukai Li, Qiushi Sun, Shudong Liu, Xuankun Rong, Xiaohang Yu, Zhuo Chen, Hejia Geng, Chenxin Li, Aozhou Wang, Zengji Tu, Robert Tang, Yuxin Zhan, Eric Jiang, Yuxin Wu, Jianqing Zhang, Xiao Liang, Fang Wu, Haochi Zhang, Alexander Marlow, Guancheng Wan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06396v1)