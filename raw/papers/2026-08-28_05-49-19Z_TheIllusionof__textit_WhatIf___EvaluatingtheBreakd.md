---
title: The Illusion of $\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs
published: 2026-08-28T05:49:19Z
authors: Yucheng Wang, Yuetian Du, Zhengyi Liu, Rongyu Zhang, Bing Zhao, Boyu Yang, Ming Kong, Lin Qu, Hu Wei, Jie Liu, Qiang Zhu
url: http://arxiv.org/abs/2608.27953v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Illusion of $\textit{What If}$: Evaluating the Breakdown of Counterfactual Reasoning in LLMs

## Abstract
Counterfactual reasoning requires models to reason beyond the observed world and explain how altered conditions propagate through downstream consequences. Existing benchmarks largely target bounded settings with fixed variables or single gold outcomes, overlooking open-domain scenarios requiring causal-process evaluation. To this end, we present $\textbf{WhatIfBench}$, a diagnostic benchmark for open-domain, open-form, long-horizon counterfactual causal reasoning, containing 220 what-if questions across STEM, HSS, and Hybrid scenarios. To evaluate free-form responses, we further propose $\textbf{PRISM}$, which first converts each natural-language explanation into a Response-Derived Semantic Causal Graph of events, states, and mechanisms. On top of this graph, PRISM then jointly applies a Process Metric assessing graph-level causal validity and a Rubric Metric assessing answer-level explanatory adequacy. Evaluating six frontier LLMs with this framework, we find that WhatIfBench remains far from saturated: even the strongest model reaches only a 64.62% final score. Further analysis reveals persistent causal gaps, premise drift, and topology fragmentation, suggesting that fluent counterfactual narratives often mask fragile causal processes. The benchmark, code, and evaluation scripts are available at $\href{https://github.com/zju-gt/WhatIfBench}{WhatIfBench}$.

## Metadata
- **Published**: 2026-08-28T05:49:19Z
- **Authors**: Yucheng Wang, Yuetian Du, Zhengyi Liu, Rongyu Zhang, Bing Zhao, Boyu Yang, Ming Kong, Lin Qu, Hu Wei, Jie Liu, Qiang Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27953v1)