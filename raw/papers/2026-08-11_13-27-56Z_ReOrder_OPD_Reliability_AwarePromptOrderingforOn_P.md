---
title: ReOrder-OPD:Reliability-Aware Prompt Ordering for On-Policy Distillation
published: 2026-08-11T13:27:56Z
authors: Ximo Zhu, Ruiqi Liu, Rong Wang, Ping Wu, Xiang Zheng, Wenzhuo Xu, Xubin Yao, Zhiyuan Yan, Bo Li, Jun Gao, Xiaolei Lv
url: http://arxiv.org/abs/2608.10905v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReOrder-OPD:Reliability-Aware Prompt Ordering for On-Policy Distillation

## Abstract
On-policy distillation (OPD) applies token-level teacher supervision to student-generated trajectories, but this supervision is not always reliable. Existing methods use local confidence or teacher-student agreement to weight, filter, or truncate the sampled trajectory. These signals do not directly determine whether the teacher can continue a student prefix to a correct answer, and trajectory-level interventions can conflate one rollout's unreliability with low expected training value of its prompt. We define prompt-level teacher continuation reliability $R$ as the teacher's probability of reaching a correct answer from a student prefix, averaged over prefixes and trajectories induced by the current student. Oracle experiments show that high-$R$ prompts yield larger OPD gains and that descending-$R$ training outperforms random and ascending orders on a fixed prompt pool. Because estimating $R$ requires many teacher continuations, we use the maximum ROUGE-5 F1 between one independent student rollout and verifier-correct same-prompt teacher trajectories. Across ten equal-frequency bins of this actual score, mean $R$ rises monotonically, showing that the proxy separates coarse reliability levels. ReOrder-OPD sorts prompts by the proxy, then draws independent on-policy training trajectories for vanilla OPD. It improves every matched aggregate comparison across Qwen3 and Gemma4 mathematics settings and Qwen3 code settings. Gains in all six FiRe-OPD and ExOPD settings show that prompt ordering complements within-trajectory supervision.

## Metadata
- **Published**: 2026-08-11T13:27:56Z
- **Authors**: Ximo Zhu, Ruiqi Liu, Rong Wang, Ping Wu, Xiang Zheng, Wenzhuo Xu, Xubin Yao, Zhiyuan Yan, Bo Li, Jun Gao, Xiaolei Lv
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10905v1)