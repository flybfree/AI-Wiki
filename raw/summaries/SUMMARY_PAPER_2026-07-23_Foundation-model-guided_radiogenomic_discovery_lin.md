---
title: Foundation-model-guided radiogenomic discovery linking cancer genomes to cancer scans
url: http://arxiv.org/abs/2607.20583v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_12-20-58Z_Foundation_model_guidedradiogenomicdiscoverylinkin.md
generated_at: 2026-07-23 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This study pairs Evo~2 genome analysis with routine clinical tumor scans to discover gene‑phenotype links without task‑specific training. By correlating per‑gene severity scores from three TCGA cohorts with radiomic features, the authors recover known drivers and uncover 46 novel genes linked to imaging patterns.

## Key Takeaways
- Evo~2 predicts a severity score for each somatic mutation across cRCC, HCC, and BC without any predefined training task.  
- The per‑gene summaries are correlated with radiomic features extracted from paired tumor segmentations while controlling for total mutation burden.  
- In TCGA‑cRCC, the method identifies 46 additional genes at FDR significance that were absent from existing cancer‑gene panels and include Mendelian ciliopathy and cytoskeletal disease genes.

## Context
The work illustrates how large language models can be repurposed as hypothesis‑free discovery engines for biomedical data. By treating genomic information as a natural language, Evo~2 can generate severity scores that reveal hidden relationships between mutations and imaging characteristics, advancing the integration of AI with routine clinical workflows.

## Implications
This approach offers a scalable method to uncover novel gene–imaging associations that conventional driver‑discovery pipelines miss, potentially informing personalized treatment strategies. For researchers and clinicians, it opens new avenues for radiogenomic research without requiring extensive prior knowledge or large annotated datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20583v1)
