---
title: LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28
published: 2026-09-04T12:48:13Z
authors: Wes Sander
url: http://arxiv.org/abs/2609.05093v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28

## Abstract
We present Discovery Loop, a lightweight system that uses a large language model (LLM) to iteratively evolve optimization algorithms. Starting from a simple seed solver, the LLM proposes algorithmic improvements guided by a scoreboard of results and a history of prior ideas. Each candidate is evaluated against an independent verifier; improvements are kept and failures discarded. Applied to the Packomania circle-packing benchmark (csqv: maximize the sum of radii of N variable-radius circles in the unit square), the system improved the best known solutions for 10 values of N in the range 101-114, with gains of 2.4%-5.4% over prior records, all within 15 iterations and at a total LLM cost of $27.72. These results have been independently accepted by Packomania. We describe the method, analyze cost-efficiency dynamics including an adaptive plateau-detection mechanism, and discuss implications for democratizing automated scientific discovery.

## Metadata
- **Published**: 2026-09-04T12:48:13Z
- **Authors**: Wes Sander
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05093v1)