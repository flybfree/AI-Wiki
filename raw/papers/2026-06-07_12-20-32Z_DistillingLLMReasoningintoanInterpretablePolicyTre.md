---

title: Distilling LLM Reasoning into an Interpretable Policy Tree for Human-AI Collaboration
published: "2026-06-07T12:20:32Z"
authors: Beiwen Zhang, Yongheng Liang, Guowei Zou, Haitao Wang, Hejun Wu
url: http://arxiv.org/abs/2606.08596v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Distilling LLM Reasoning into an Interpretable Policy Tree for Human-AI Collaboration



**Source**: [Original Paper](http://arxiv.org/abs/2606.08596v1)
## Abstract
Constructing efficient and reliable policies to assist humans is indispensable for human-AI collaboration. Existing methods mainly follow two lines of work. Most prior work relies on multi-agent reinforcement learning (MARL) to learn black-box policies, which limits interpretability and raises safety concerns. Recent methods query large language models (LLMs) at each decision step, causing slow responses and high inference costs. We propose Collaboration Policy Tree (Co-pi-tree), a closed-loop method that learns an executable policy tree consisting of a partner-behavior prediction tree and an agent-action selection tree. Co-pi-tree constructs a policy by distilling LLM reasoning into policy tree code. It then evaluates the policy through partner interaction, obtains feedback, and uses natural language to summarize the interaction feedback to improve problematic branches. Experiments in Overcooked-AI show that Co-pi-tree improves average reward by 35.4% over the baseline average, while reducing the number of LLM queries by 77.7% and test-time latency by 97.1%. Project page: https://beiwenzhang.github.io/Co-pi-tree/

## Metadata
- **Published**: 2026-06-07T12:20:32Z
- **Authors**: Beiwen Zhang, Yongheng Liang, Guowei Zou, Haitao Wang, Hejun Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.08596v1)