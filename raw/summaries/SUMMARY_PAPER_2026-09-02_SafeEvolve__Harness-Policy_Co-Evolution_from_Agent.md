---
title: SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment
url: http://arxiv.org/abs/2609.02786v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_16-19-54Z_SafeEvolve_Harness_PolicyCo_EvolutionfromAgentExpe.md
generated_at: 2026-09-02 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SafeEvolve, a framework that co‑evolves harnesses and policies using safety experience from on‑policy trajectories. It shows that harness‑policy co‑evolution improves safety without sacrificing utility. Experiments demonstrate stronger safety‑utility tradeoffs than existing baselines.

## Key Takeaways
- SafeEvolve converts trajectory‑level safety evidence into bounded, component‑level updates across safety prompt and hierarchical skills, producing auditable reversible harness artifacts.
- The framework uses a two‑stage SFT‑RL paradigm where harness‑use SFT bootstraps the policy to leverage evolved harness artifacts.
- Harness‑augmented RL shapes autonomous safety behaviors during multi‑step exploration via verifier‑decomposed rewards.

## Context
AI agents interacting with environments rely on both base models and harnesses, creating safety vulnerabilities in responses and execution paths. Existing alignment methods treat harness or policy updates separately, limiting integration of runtime control with intrinsic safety.

## Implications
SafeEvolve offers a practical path for continuous safety improvement as agents operate autonomously. Practitioners can adopt co‑evolution loops to embed safety directly into runtime systems without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02786v1)
