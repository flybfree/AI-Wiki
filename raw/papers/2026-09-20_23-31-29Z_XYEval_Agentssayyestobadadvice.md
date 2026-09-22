---
title: XYEval: Agents say yes to bad advice
published: 2026-09-20T23:31:29Z
authors: Zhengxuan Wu, Yuxuan Li, Oyvind Tafjord, Been Kim
url: http://arxiv.org/abs/2609.23939v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# XYEval: Agents say yes to bad advice

## Abstract
Effective communication between users and AI agents is essential for human-AI collaboration. The XY problem is a well-known communication pitfall where a person asks about their attempted solution rather than their actual problem. We extend prior sycophancy evaluation to the XY problem in agentic settings, evaluating whether agents can resist plausible but misleading suggestions from users and communicate their reasoning. We introduce XYEval, a meta-evaluation framework that can transform an existing benchmark into an XY problem evaluation. We evaluate five models across six diverse benchmark suites. Agents suffer large XY drops under XY mutation across benchmarks, with relative drops reaching up to 46.7%. With $τ^2$-bench, we further show that agent performance drops more when encountering a pedantic user who requires detailed explanations before approving a better solution. Our findings suggest that current agents lack the ability to effectively reason and communicate when facing misleading suggestions. A simple system instruction baseline that encourages awareness of XY problems only offers partial mitigation. Extensive trace analyses provide behavioral insights into how and why these XY drops occur across execution trajectories. Our results show that mitigating the XY problem remains challenging, requiring agents to both recognize user misdirection and clearly communicate the underlying problem.

## Metadata
- **Published**: 2026-09-20T23:31:29Z
- **Authors**: Zhengxuan Wu, Yuxuan Li, Oyvind Tafjord, Been Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23939v1)