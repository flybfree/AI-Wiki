---
title: CAVEAT: Towards Robust Computer-Use Agents in Incentive-Misaligned Environments
published: 2026-09-23T03:00:00Z
authors: Yuxuan Li, Will Epperson, Wesley Deng, Zezhou Huang
url: http://arxiv.org/abs/2609.27273v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CAVEAT: Towards Robust Computer-Use Agents in Incentive-Misaligned Environments

## Abstract
Computer-use agents (CUAs) increasingly act on behalf of users online. What happens when the environments they operate in have incentives that do not align with the user's? In online marketplaces, for example, platforms may favor some products over others, potentially steering agents away from the user's objective. Existing CUA benchmarks cover cooperative settings or explicit attacks, but do not test whether agents preserve user objectives when the environment itself has a stake in the outcome. We introduce CAVEAT, a controlled benchmark spanning nine marketplace environments and a taxonomy of eight common steering mechanisms. Across five model families, agents purchase the user-optimal product in 78.6% of matched-control episodes but only 17.3% when steering mechanisms are enabled. Larger models and increased reasoning improve robustness, but substantial failures persist. Our trajectory analysis and targeted ablations identify three points where steering enters the decision process: (1) agents distort the user's priorities, (2) prematurely narrow the set of alternatives they consider, and (3) commit before resolving decision-relevant evidence. Guided by this diagnosis, we develop CAVEAT-Harness, which directly targets these failure modes and raises user-optimal purchasing by 55.0%. Targeted post-training further improves a smaller open model. These results establish incentive robustness as a distinct challenge for delegated agents, diagnose how it fails, and show that targeted interventions can substantially improve it.

## Metadata
- **Published**: 2026-09-23T03:00:00Z
- **Authors**: Yuxuan Li, Will Epperson, Wesley Deng, Zezhou Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27273v1)