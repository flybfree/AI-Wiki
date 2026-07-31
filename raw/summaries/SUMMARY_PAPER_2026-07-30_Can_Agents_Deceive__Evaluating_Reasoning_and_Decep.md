---
title: Can Agents Deceive? Evaluating Reasoning and Deception in ParliamentBench using a Social Deduction Game
url: http://arxiv.org/abs/2607.28146v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_12-54-17Z_CanAgentsDeceive_EvaluatingReasoningandDeceptionin.md
generated_at: 2026-07-30 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ParliamentBench, an open-source benchmark built on the Secret Hitler social deduction game to test large language model agents in deception and reasoning tasks. Experiments with 16 LLMs across thousands of simulated matches show that top models perform well while weaker ones fail even basic random baselines. Deception consistency is a problem, with most models retaining deceptive personas below 50% throughout games.

## Key Takeaways
- Frontier models such as GPT‑5.4 and Grok 4.1 Fast achieve high performance in both cooperative and deceptive roles, forming a strong top‑four cluster.
- Many LLMs cannot sustain deception across an entire game; retention drops below 50%, indicating instability in maintaining a consistent false identity.
- The weakest models perform worse than random chance (33%) and simple algorithmic baselines (45%), highlighting a gap between capability and reliability.

## Context
Social deduction games like Secret Hitler are used to probe human social dynamics, but extending them to AI agents reveals new challenges. This work contributes a standardized benchmark that can be applied across diverse LLM families, fostering fair comparison of reasoning and deception abilities in high‑stakes environments.

## Implications
For developers deploying LLMs in medical or legal systems, the findings warn that deceptive behavior may emerge unexpectedly, risking patient safety or legal misinterpretation. The benchmark encourages industry to prioritize consistency testing alongside performance metrics to mitigate hidden risks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28146v1)
