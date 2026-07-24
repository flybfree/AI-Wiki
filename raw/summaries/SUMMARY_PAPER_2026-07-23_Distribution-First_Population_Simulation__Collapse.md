---
title: Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling
url: http://arxiv.org/abs/2607.18310v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-17_15-45-57Z_Distribution_FirstPopulationSimulation_Collapse_Ca.md
generated_at: 2026-07-23 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the failure of treating each World Values Survey respondent as an independent large language model agent and proposes a distribution‑first approach that corrects for this collapse. Using deterministic verification on Turkish data, it shows that LLM agents overfit to modal defaults, Verbalized Sampling fixes under‑dispersion but creates over‑dispersion, fidelity transfers weakly, and recall attacks contaminate subgroup claims.

## Key Takeaways
- Independent LLM agents reproduce a population distribution with 85% collapse, concentrating responses in four scenarios and yielding an entropy range of 0.77 to 1.46.
- Verbalized Sampling eliminates under‑dispersion (SD‑ratio drops from 0.4–0.56 to 1.26–1.37) but introduces a structural over‑dispersion that is universal across model families.
- In booking tasks, the cheapest default dominates (~80%) and income only slightly modulates comfort choices, indicating weak fidelity transfer.

## Context
The study addresses a growing trend where synthetic populations are built by modeling each individual as an autonomous LLM, which often ignores statistical consistency. This approach risks producing artifacts that mislead downstream applications such as recommendation systems or policy analysis.

## Implications
For practitioners, the paper suggests pre‑assigning population distributions to agents at constant cost rather than generating independent responses, improving reliability without sacrificing performance. It also warns against assuming LLMs can faithfully capture survey data when used independently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18310v1)
