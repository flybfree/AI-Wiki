---

title: 'QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards'
published: "2026-06-02T17:53:04Z"
authors: Rongzhi Zhang, Rui Feng, Zhihan Zhang, Jingfeng Yang, Qingyu Yin, Xin Liu, Zixuan Zhang, Priyanka Nigam, Bing Yin, Tuo Zhao, Chao Zhang
url: http://arxiv.org/abs/2606.03968v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards



**Source**: [Original Paper](http://arxiv.org/abs/2606.03968v1)
## Abstract
Rubric-based RL is a promising route for extending reinforcement learning beyond verifiable rewards, yet existing methods optimize rubrics while treating the query distribution as fixed. We identify a structural bottleneck: rubric quality is constrained by query structure. Open-ended queries yield vague rubrics; naively narrowing them introduces fabricated references that no model can verify, so all responses fail and training receives no reward signal. We present QUBRIC, a framework that co-designs queries and rubrics. Teacher-derived key points ground the rewriting of open-ended queries into scenario-based, evaluable questions. Contrastive rubric generation then turns teacher-policy gaps into query-level criteria, and learnability filtering retains only informative query-rubric pairs for GRPO training. QUBRIC achieves a +5.5 point gain on ArenaHard over the SFT baseline. Trained only on instruction-following data, it further transfers to three held-out benchmarks spanning legal, moral, and narrative reasoning (+6.3 points on average), with improvements concentrated in reasoning-related dimensions. These results provide evidence that co-designing queries and rubrics can make rubric-based RL a practical complement to RLVR beyond strictly verifiable tasks.

## Metadata
- **Published**: 2026-06-02T17:53:04Z
- **Authors**: Rongzhi Zhang, Rui Feng, Zhihan Zhang, Jingfeng Yang, Qingyu Yin, Xin Liu, Zixuan Zhang, Priyanka Nigam, Bing Yin, Tuo Zhao, Chao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.03968v1)