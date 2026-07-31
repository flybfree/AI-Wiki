---
title: PlantBGC: Transformer for Plant BGC Discovery via Label-Free Domain Adaptation and Weak Supervision
url: http://arxiv.org/abs/2607.27258v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_03-13-48Z_PlantBGC_TransformerforPlantBGCDiscoveryviaLabel_F.md
generated_at: 2026-07-30 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
PlantBGC proposes a transformer‑based model that transfers supervision from microbial biosynthetic gene clusters to plant genomes, enabling label‑free domain adaptation for BGC discovery. The approach improves detection of known plant BGCs and reduces false positives using weak supervision derived from GO/KEGG annotations.

## Key Takeaways
- PlantBGC achieves token‑level AUC of 0.988 on microbial data and lifts plant recovery to 67.6% (from 29.4%) with full coverage, showing strong detection capability.
- Weak supervision cuts the proxy primary‑like ratio by up to 48.40% using GO annotations and 45.20% using KEGG, indicating effective noise reduction.
- Compared to plantiSMASH, PlantBGC produces more compact loci, with a median length ratio of 0.278 and 93.8% of matched regions being shorter.

## Context
The paper addresses the challenge of discovering plant BGCs in an era where supervised datasets are scarce, highlighting how transformer encoders can model long‑range domain context while leveraging weak supervision for bias correction.

## Implications
This method offers a scalable pipeline for plant metabolic pathway discovery, reducing experimental costs and accelerating research into secondary metabolites. Practitioners can integrate PlantBGC into genome mining workflows to prioritize high‑confidence loci with minimal annotation effort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27258v1)
