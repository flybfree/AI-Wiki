---
title: First Make It Playable, Then Make It Good: Staged Interaction Learning for Small Dialogue-Game Agents
url: http://arxiv.org/abs/2608.27672v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-27_19-58-06Z_FirstMakeItPlayable_ThenMakeItGood_StagedInteracti.md
generated_at: 2026-08-30 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Qwen-GuidePlay-2B, a 2‑billion‑parameter language model designed for dialogue‑game interaction. The authors fine‑tune the base model through three stages: supervised fine‑tuning on only successful Playpen trajectories, weighted turn‑level fine‑tuning, and teacher‑guided fine‑tuning that corrects formatting and evaluates examples. The final model achieves a clemscore of 57.12 and a statscore of 42.68.

## Key Takeaways
- Imitating full trajectories helps with playability by providing complete successful game paths.
- Turn‑level fine‑tuning and teacher‑guided fine‑tuning improve decision‑making and raise the overall score beyond the base model.
- Procedurally heavy methods such as replay‑repair or hard‑example mining did not produce benefits, indicating that small models can excel with careful curation rather than aggressive changes.

## Context
The work tackles a key challenge in AI for interactive games: how to scale language models while maintaining high performance on metrics like clemscore and statscore. It shows that training strategies are more impactful than raw model size, especially when resources are limited.

## Implications
For developers creating small dialogue‑game agents, the results suggest that focused data curation and staged fine‑tuning can deliver substantial gains without requiring massive compute budgets. This approach is practical for industry deployment where efficiency matters as much as performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27672v1)
