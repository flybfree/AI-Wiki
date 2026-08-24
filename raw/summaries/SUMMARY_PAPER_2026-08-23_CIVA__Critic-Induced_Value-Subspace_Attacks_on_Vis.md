---
title: CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents
url: http://arxiv.org/abs/2608.21114v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_13-58-56Z_CIVA_Critic_InducedValue_SubspaceAttacksonVisualWo.md
generated_at: 2026-08-23 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CIVA, a white‑box causal attack on visual world‑model agents that exploits the low‑dimensional value subspace learned by the agent’s own critic to degrade performance while preserving temporal coherence. Experiments show CIVA beats five recent methods and causes up to 26.07% reward loss in DMC walker walk with minimal temporal variation.

## Key Takeaways
- The attack focuses on a low‑dimensional value subspace induced by the victim’s own critic, allowing targeted perturbations that affect only critical dynamics.
- CIVA extracts this subspace offline via critic‑guided PGD and SVD, then smooths coefficients with an exponential moving average for online application.
- The approach keeps optimization cheap and temporally coherent, resulting in low TempAbs of 0.646.

## Context
Visual world‑model agents rely on recurrent latent states that are resistant to simple frame‑wise attacks, yet they remain vulnerable to value‑sensitive manipulations. This work demonstrates that even robust architectures can be compromised when the attacker leverages the internal critic’s learned subspace.

## Implications
For practitioners, CIVA highlights the need for defenses that protect against value‑subspace attacks rather than only frame‑level perturbations. The method could inform future research on secure reinforcement learning and robust world modeling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21114v1)
