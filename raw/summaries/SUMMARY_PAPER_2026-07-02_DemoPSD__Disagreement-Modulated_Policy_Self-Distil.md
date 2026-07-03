---
title: DemoPSD: Disagreement-Modulated Policy Self-Distillation
url: http://arxiv.org/abs/2607.02502v1
type: paper-summary
date: 2026-07-02
source_paper: 2026-07-02_17-58-29Z_DemoPSD_Disagreement_ModulatedPolicySelf_Distillat.md
generated_at: 2026-07-02 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DemoPSD, a framework for on‑policy self‑distillation that addresses leakage and exploration problems in dense token‑level teacher guidance. By using a reverse‑KL barycenter target to blend teacher and student distributions adaptively, DemoPSD mitigates privileged information leakage while preserving the student’s reasoning capacity. Experiments show it outperforms GRPO and SDPO on SciKnowEval across four fields with higher training entropy and better out‑of‑distribution performance.

## Key Takeaways
- The framework replaces dense teacher supervision with a reverse‑KL barycenter that balances learning from the teacher and preserving student exploration, reducing overfitting to in‑domain patterns.  
- Leakage attenuation is provably achieved because the adaptive blending prevents the student from encoding answer‑dependent shortcuts unavailable at test time.  
- Exploration preservation is maintained as the student retains its own reasoning capacity despite dense token‑level distillation.

## Context
On‑policy self‑distillation aims to improve LLMs’ reasoning without costly external data, but traditional methods often sacrifice generalization and exploration due to overfitting to privileged information. DemoPSD’s adaptive blending offers a principled alternative that balances teacher guidance with student autonomy, aligning with trends toward more robust and generalizable model training.

## Implications
For practitioners, DemoPSD provides a practical way to train LLMs for reasoning tasks while avoiding the pitfalls of dense supervision, leading to higher-quality models that generalize across domains. In industry, this reduces reliance on large labeled datasets and enables faster iteration cycles without sacrificing performance or safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.02502v1)
