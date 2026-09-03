---
title: How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation in LLM Agents for Production Decision-Making
url: http://arxiv.org/abs/2609.01660v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-08-31_19-11-47Z_HowFastDoAgentsRot_AnEmpiricalStudyofLong_HorizonD.md
generated_at: 2026-09-02 20:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how quickly LLM agents degrade in production decision‑making tasks, revealing a systematic drop in success that is tied to the number of steps rather than model size or context length. Experiments across nine models and three real systems show that task success follows a geometric decay with a per‑step reliability parameter that never reaches 1, guaranteeing eventual failure after roughly sixteen steps on agentic loops.

## Key Takeaways
- Task success decays geometrically with each step, driven by a single reliability parameter that rises with model scale but saturates below one, leading to inevitable collapse at long horizons.  
- The effect is most pronounced on the genuine agentic tool‑use task, where all models, including large proprietary systems, drop from near‑perfect success to near zero within sixteen steps across 10,664 trajectories.  
- Context window length has a weaker impact than step count; bounding context steepens decay (logit slope -0.69 vs -0.44), disproving the “lost‑in‑the‑middle” hypothesis.

## Context
The study highlights a gap between benchmark performance and real‑world deployment, where short horizons mask long‑term reliability issues. As LLM agents become more integrated into workflows, understanding this degradation curve is essential for reliable system design.

## Implications
Teams must adopt horizon‑aware evaluation and allocate reliability budgets instead of relying on aggregate pass rates. Ignoring step‑level decay can lead to silent failures in production, undermining trust in agentic automation at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01660v1)
