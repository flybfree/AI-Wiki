---
title: CSPF: A Constrained Shared-Private Fusion Method for Non-Verifiable Preference Evaluation
url: http://arxiv.org/abs/2607.20862v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_02-39-11Z_CSPF_AConstrainedShared_PrivateFusionMethodforNon_.md
generated_at: 2026-07-23 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CSPF, a constrained shared‑private fusion method that learns to combine hidden‑state representations from heterogeneous reward models using pairwise human preference data. The authors demonstrate that CSPF outperforms single‑expert, scalar‑score multi‑expert, and rubric‑judge baselines on LM-Arena target‑domain adaptation and PPE out‑of‑distribution preference evaluation.

## Key Takeaways
- CSPF decomposes each expert signal into a shared component and an expert‑private component, enabling alignment while preserving complementary viewpoints.  
- The method is trained under pairwise human‑preference supervision, allowing the fusion to respect diverse evaluative criteria.  
- Across benchmark tasks, CSPF achieves the best performance among all evaluated reward‑model strategies.

## Context
The challenge of evaluating non‑verifiable AI tasks lies in the lack of explicit labels and the need for robust preference models that can generalize across domains. Existing approaches often rely on simple aggregation or scalar scores, which may miss nuanced preferences. CSPF addresses this by leveraging latent representations that capture both commonalities and task‑specific nuances.

## Implications
For practitioners developing preference evaluation systems, CSPF offers a practical framework to integrate multiple frozen reward models without sacrificing interpretability. The approach can be applied to downstream tasks such as model selection, dataset curation, and user satisfaction assessment where diverse expert signals coexist.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20862v1)
