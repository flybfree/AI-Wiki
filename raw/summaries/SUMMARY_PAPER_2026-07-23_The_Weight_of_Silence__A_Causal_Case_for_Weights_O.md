---
title: The Weight of Silence: A Causal Case for Weights Over the Scratchpad in Latent Chess Reasoning
url: http://arxiv.org/abs/2607.20952v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_06-18-43Z_TheWeightofSilence_ACausalCaseforWeightsOvertheScr.md
generated_at: 2026-07-23 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether latent reasoning functions as an active scratchpad during reinforcement learning in chess and finds that RL improves legality from 48% to 61% while eliminating checkmate confabulation. A series of causal interventions shows that only exact‑zero corruption harms performance, indicating that RL adds robustness rather than reliance on thought content.

## Key Takeaways
- Legality rises monotonically after RL training, reaching 61% from a 48% baseline, while checkmate confabulation disappears.  
- Causal interventions reveal that exact‑zero vectors cause collapse to 1% pre‑RL versus 9% post‑RL, suggesting robustness is the key effect of RL.  
- The model’s latent thoughts are not actively consulted at inference time; their primary impact is on parameter shaping during training.

## Context
Latent reasoning has been assumed to act as an internal scratchpad in language models, but its role in reinforcement learning remains untested beyond math and logic tasks. This work extends the debate by applying a staged curriculum with RL to chess, a domain where prior latent‑reasoning plus RL recipes have failed.

## Implications
The findings challenge the prevailing view that latent thoughts are consulted during inference, suggesting instead that they influence training dynamics. For practitioners, this implies that robustness to input corruption may be more valuable than direct reliance on thought vectors for improving model behavior after reinforcement learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20952v1)
