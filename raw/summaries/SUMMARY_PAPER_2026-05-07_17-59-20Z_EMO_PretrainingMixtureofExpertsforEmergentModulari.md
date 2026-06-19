---

title: "Summary: EMO: Pretraining Mixture of Experts for Emergent Modularity"
url: http://arxiv.org/abs/2605.06663v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-07_17-59-20Z_EMO_PretrainingMixtureofExpertsforEmergentModulari.md
generated_at: "2026-06-11 10:29"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces EMO, a mixture-of-experts model that enables modular deployment by allowing independent expert subsets to be used per input without predefined priors. The authors demonstrate that restricting inference to 25% of experts causes only minor performance loss, unlike standard MoEs which degrade sharply. Pretraining on 1 trillion tokens yields a 1B‑active, 14B‑total model that matches full‑model performance while supporting selective expert use.

## Key Takeaways
- EMO restricts tokens within the same document to experts drawn from a shared pool, letting different documents select distinct pools, which allows expert groupings to emerge automatically.  
- The model achieves only a 1% absolute drop when retaining 25% of experts, whereas standard MoEs suffer larger drops under the same constraint.  
- Expert specialization in EMO occurs at semantic levels (e.g., math or code) rather than low‑level syntactic features.

## Context
Large language models often require full computation even for narrow tasks, increasing memory and cost. Mixture-of-experts aims to mitigate this by activating only relevant experts, but prior work struggled with coherent expert selection across documents. This research advances the field by showing that modular expertise can be learned end‑to‑end without human intervention.

## Implications
The findings open a path toward memory‑efficient AI systems where only essential capabilities are invoked at inference time. Practitioners can deploy specialized models for code, math, or domain knowledge while keeping overall model size modest. This modularity could lower deployment costs and enable more flexible applications of large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.06663v1)
