---
title: MiniRep: Robust Reputation-Based Aggregation for Multi-Agent Debate
url: http://arxiv.org/abs/2609.39297v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_08-41-08Z_MiniRep_RobustReputation_BasedAggregationforMulti_.md
generated_at: 2026-09-30 22:03
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces MiniRep, a robust reputation-based aggregation framework designed for Multi-Agent Debate (MAD) systems operating under malicious conditions where agents may adaptively exploit trust metrics or corrupt proposals. The authors demonstrate that traditional reputation mechanisms often fail to predict agent behavior on novel tasks due to such adaptive threats, prompting the development of MiniRep to evaluate agents based on both real-time task performance and longitudinal reputation while mitigating dominance by homogeneous response groups. Experimental evaluations across diverse attack scenarios show that MiniRep consistently outperforms conventional aggregation methods and standard reputation approaches, particularly in maintaining accuracy under a wide range of corruption conditions.

## Key Takeaways
- **Reputation Limitations and Attack Taxonomy:** Past performance-based reputation is insufficient for predicting agent behavior on new tasks because malicious agents can adapt their strategies during collaboration; to address this, the authors construct a comprehensive attack taxonomy derived from reputation-system vulnerabilities and software-testing mutation operators, categorizing threats into strategic exploitation of reputation scores and subtle corruption of agent proposals.
- **Dual-Evaluation Mechanism with Diversity Control:** MiniRep improves robustness by assessing agents through a dual lens that combines their immediate behavior on the current task with their historical reputation over time, while simultaneously implementing safeguards to prevent coalitions of agents producing highly similar responses from disproportionately influencing the final aggregated output.
- **Superior Performance Across Attack Vectors:** Extensive experiments on the MATH benchmark reveal that MiniRep surpasses both conventional MAD aggregation techniques and standard reputation-based baselines regardless of attack presence; notably, in a heterogeneous ten-agent configuration, MiniRep achieves state-of-the-art performance across all 28 tested attack conditions, demonstrating exceptional resilience against diverse malicious behaviors.

## Context
As LLM-powered agents increasingly operate in open ecosystems requiring collaborative problem-solving, ensuring the reliability of multi-agent interactions becomes critical for deploying trustworthy autonomous systems. This work addresses a significant gap in agent security by highlighting how reputation mechanisms can be subverted through adaptive behavior and subtle corruption, moving beyond static trust models to dynamic threat assessment in decentralized agentic environments where agents must coordinate under adversarial pressure.

## Implications
For practitioners building multi-agent frameworks, these findings underscore the necessity of integrating dynamic reputation scoring and response diversity checks to defend against sophisticated adversarial attacks that exploit historical trust metrics. Industry initiatives aiming to establish performance leaderboards or secure agentic marketplaces should adopt robust aggregation strategies like MiniRep to maintain system integrity when deploying heterogeneous agent populations capable of malicious adaptation during collaborative tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39297v1)
