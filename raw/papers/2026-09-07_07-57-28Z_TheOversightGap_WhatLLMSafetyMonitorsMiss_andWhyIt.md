---
title: The Oversight Gap: What LLM Safety Monitors Miss, and Why It Is Not Capability
published: 2026-09-07T07:57:28Z
authors: Xin Xu
url: http://arxiv.org/abs/2609.07162v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Oversight Gap: What LLM Safety Monitors Miss, and Why It Is Not Capability

## Abstract
Several properties safety monitors are asked to certify, among them cross-tenant noninterference, sandbagging and evaluation awareness, are 2-safety hyperproperties, witnessed only by two executions. The standard consequence is a binary impossibility: one trace cannot decide them. We replace the binary with a measurement. A tight bound puts the balanced accuracy of any single-trace monitor at $\tfrac12+\tfrac12\,TV(P_0,P_1)$, turning undecidability into a graded detectability frontier and defining an oversight gap: a monitor's shortfall below it. On a leak family with closed-form $TV$, nine LLM monitors are optimal at $TV=0$ but capture little signal as $TV$ grows; at $TV=1$, where a 20-line membership check scores $100\%$, they average $60.9\%$. That shortfall is mostly not capability: naming what to check closes $61\%$ of it while leaving the $TV=0$ control at chance. The same split runs through a $2{\times}2$ factorial: an imagined second run leaves monitors at chance ($50.4\%$) while the same rule on an executed second run reaches $90.0\%$, and a stored oracle without a comparison procedure yields only $68.2\%$. Information and procedure are each necessary and neither is capability. Under nondeterminism, replay tracks a closed-form $k$-replay curve only under the right projection, and a projection frontier shows the resulting dilemma is forced: narrow misses $98.6\%$ of off-channel leaks, broad flags $75.7\%$ of clean traffic, and attainable accuracy decays like $1/(qm)$ in the benign-variation rate and the channel count. Finally, two frontier LLM judges certified an earlier version of our own benchmark as sound while a sign test found a directional bias ($p=2.7\times10^{-5}$) that invalidated three of our findings. Construction validity for hyperproperty benchmarks should be proved mechanically, not audited by models.

## Metadata
- **Published**: 2026-09-07T07:57:28Z
- **Authors**: Xin Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07162v1)