---
title: Lymphocyte Mimicry Correction via Region-Level Tissue Reasoning and Unbalanced Optimal Transport
url: http://arxiv.org/abs/2608.17151v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_21-33-55Z_LymphocyteMimicryCorrectionviaRegion_LevelTissueRe.md
generated_at: 2026-08-18 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Loki‑OT, a method that corrects ambiguous cell mimicry by propagating region‑level tissue reasoning to individual cell predictions using unbalanced optimal transport. By leveraging MLLM‑derived density priors and distilling them into a lightweight student classifier, the approach improves accuracy on challenging epithelium‑rich tissues where cells resemble each other morphologically.

## Key Takeaways
- Loki‑OT uses unbalanced optimal transport to reassign ambiguous cell predictions based on surrounding tissue context, reducing patient‑level mean absolute error in the TCGA‑BRCA cohort.  
- The method outperforms fully supervised in‑domain PanopTILs classifiers by achieving lower MAE and higher F1 scores specifically in mimicry tissues.  
- It relies on 278 weak region‑level MLLM estimates from a general‑domain cell foundation model, demonstrating that pretrained features already contain discriminative tissue information.

## Context
Cell mimicry is a persistent challenge for pathology AI because visual similarity masks biological differences. Existing models either ignore context or cannot operate at the single‑cell level, limiting diagnostic reliability. This work bridges that gap by integrating high‑level region reasoning with cell‑level prediction through optimal transport and MLLM priors.

## Implications
For clinicians, Loki‑OT offers a more accurate diagnosis tool that can reduce misclassifications in ambiguous cases. For industry, the approach showcases how pretrained foundation models can be fine‑tuned with lightweight student networks to enhance performance without large labeled datasets. Practitioners can adopt this framework to improve pathology AI systems across various tumor types.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17151v1)
