---
title: Janus: An Algorithm-Evaluator Co-Evolution Framework for LLM-Driven Discovery under Expensive Evaluation Budgets
published: 2026-08-08T15:31:12Z
authors: Ximeng Liu, Qianlong Wang, Yingming Mao, Annan Li, Yatao Li, Shizhen Zhao, Jianmin Wu, Dawei Yin, Dou Shen
url: http://arxiv.org/abs/2608.08189v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Janus: An Algorithm-Evaluator Co-Evolution Framework for LLM-Driven Discovery under Expensive Evaluation Budgets

## Abstract
LLM-driven program discovery relies on rapid evaluator feedback, but many scientific and engineering tasks require high-fidelity simulations, hardware execution, or physical experiments, making each evaluation expensive. Cheap surrogate evaluators can reduce this cost, yet fixed surrogates are vulnerable to search-induced distribution shift and are difficult to fit reliably from sparse, search-biased labels. We introduce Janus, a framework that uses LLMs to co-evolve target programs and executable proxy evaluators. To address label scarcity, Janus leverages domain knowledge encoded in LLMs to generate task-specific evaluator programs and calibrates them using real outcomes. To mitigate distribution shift, Janus evolves evaluators alongside target programs, selects them using a promotion-aligned objective, and maintains region-conditioned portfolios with online credit updates. Because proxy predictions remain fallible, Janus uses them only to prioritize candidates and requires real validation before candidates can enter the target-program population or update the incumbent. Across five scientific and engineering design tasks, Janus achieves a larger area under the best-so-far improvement curve over the real-evaluation budget and higher final performance than a matched baseline that evolves only target programs. On average, Janus reaches 99/% of the baseline's final improvement with 59.1/% fewer real evaluations. Evolved proxy evaluators also rank promising candidates more accurately than their seed versions. Together, these results extend evaluator-guided LLM discovery from tasks with cheap, scalable feedback to scientific domains where trustworthy evaluation is scarce and expensive.

## Metadata
- **Published**: 2026-08-08T15:31:12Z
- **Authors**: Ximeng Liu, Qianlong Wang, Yingming Mao, Annan Li, Yatao Li, Shizhen Zhao, Jianmin Wu, Dawei Yin, Dou Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08189v1)