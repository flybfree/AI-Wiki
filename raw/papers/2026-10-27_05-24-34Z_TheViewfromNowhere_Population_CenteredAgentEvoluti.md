---
title: The View from Nowhere: Population-Centered Agent Evolution
published: 2026-10-27T05:24:34Z
authors: Shuo Yan, Ningning Hou, Haoyu He, Haochen Pei, Shang Gao
url: http://arxiv.org/abs/2610.36660v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The View from Nowhere: Population-Centered Agent Evolution

## Abstract
Self-improving AI systems can revise the designs that govern their own behavior. Yet existing approaches center improvement on selected parent agents and their evolutionary experience, leaving the broader population largely underused. We identify a substantial gap between population coverage (i.e., the tasks solved by at least one evolved variant) and the performance of the best individual agent. This gap shows that useful capabilities and diagnostic evidence emerge across the population without being consolidated into its leading agents.   These observations motivate the view from nowhere, a principle for agent evolution: an agent should be improved by interpreting its behavior through population-wide patterns of success, failure, and prior self-modification. We instantiate this principle as Population-Centered Evolution (PCE). PCE distils task records and modification histories from the population into a population block, which captures recurring failures, complementary successes, and the effects of previously attempted modifications to guide improvements to a selected parent's harness.   Under matched models, initial harnesses, and evolution schedules, PCE achieves 72.1% success on SWE-bench Verified and 96.7% on Polyglot, improving over a strong group-evolution baseline by 3.2 and 5.9 percentage points. In our evaluation, PCE reduces the gap between population coverage and best-agent performance by one-third on SWE-bench and closes it on Polyglot. These results suggest that treating the population as evidence--not merely as candidates for selection--provides a complementary principle for agent evolution.

## Metadata
- **Published**: 2026-10-27T05:24:34Z
- **Authors**: Shuo Yan, Ningning Hou, Haoyu He, Haochen Pei, Shang Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36660v1)