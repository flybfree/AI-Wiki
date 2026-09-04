---
title: Remember and Reweight: Enhancing Multi-Agent Debate with Experience Memory and Confidence Estimation
url: http://arxiv.org/abs/2609.03619v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_10-05-01Z_RememberandReweight_EnhancingMulti_AgentDebatewith.md
generated_at: 2026-09-03 20:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces R²-MAD, a framework that augments multi-agent debate with an experience memory to correct systematic errors. Experiments show consistent improvements over single‑agent and MAD baselines on diverse benchmarks.

## Key Takeaways
- The framework uses an experience memory to retrieve relevant historical evidence when the current consensus is uncertain, preventing amplification of shared misconceptions.
- Per‑agent reliability is estimated from retrieved experiences, producing confidence weights that modulate peer influence in the debate.
- R²-MAD achieves consistent improvements over existing single‑agent and MAD baselines across benchmarks.

## Context
Multi-agent debate aims to boost LLM reasoning by leveraging iterative discussion among agents. However, without mechanisms to counteract shared misconceptions, performance plateaus or worsens as errors propagate. This work addresses that limitation with a memory‑driven intervention.

## Implications
For practitioners, R²-MAD offers a practical way to make debate systems more robust and less prone to consensus errors. In industry applications where reliable decision making is critical, such improvements could lead to safer AI interactions and better alignment outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03619v1)
