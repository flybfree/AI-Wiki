---
title: KMGen: A Skill-based Approach for Synthetic Individual Patient Data Generation
published: 2026-08-23T21:43:01Z
authors: Jalen Jiang, Chufan Gao, Ethan Rasmussen, Stephen Z. Xie, Jimeng Sun
url: http://arxiv.org/abs/2608.22618v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KMGen: A Skill-based Approach for Synthetic Individual Patient Data Generation

## Abstract
Individual patient data (IPD) from clinical trials is the substrate for survival modeling, meta-analysis, and safety research, yet IPD is rarely released. Prior work has addressed only half of this gap: reconstructing Kaplan-Meier (KM) curves from published plots -- typically requiring manual digitization or human-in-the-loop correction -- while offering no mechanism for generating the adverse-event (AE) streams that constitute the other half of a patient record. We introduce KMGen, the first end-to-end framework that (i) fully automates KM curve extraction at accuracy competitive with human-guided tools, and (ii) generates synthetic per-patient AE trajectories from public trial registry records. The extraction stage is a fully automated agentic pipeline -- an agent generates code to extract each step in the KM curve -- achieving a mean Integrated Absolute Error (IAE) of 0.0151 on a 32-plot benchmark spanning clean, edge-case, and adversarial conditions. The IPD generation stage decouples patient archetype extraction from statistical sampling: an LLM distills the trial record into arm-specific statistics, adverse events, patient demographics, and risk multipliers. A mechanistic sampler generates patient events via clinical archetypes, bootstrap rank-correlation coupling to the empirical KM curve (preserving the marginal survival distribution exactly), and cycle-based AE scheduling with an induction/maintenance split. Across three held-out oncology trials spanning an order of magnitude in cohort size and 30 independent regenerations per trial, KMGen achieves mean integrated KM absolute difference $Δ_{\text{KM}}\,{\leq}\,0.051$, sex/ECOG JSD ${\leq}\,0.013$ on 5 of 6 demographic slots, and recovers ${\geq}\,71\%$ of the top-15 AEs by exact MedDRA term under a single fixed parameter set. The pipeline is released as open source at https://github.com/chufangao/kmgen.

## Metadata
- **Published**: 2026-08-23T21:43:01Z
- **Authors**: Jalen Jiang, Chufan Gao, Ethan Rasmussen, Stephen Z. Xie, Jimeng Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22618v1)