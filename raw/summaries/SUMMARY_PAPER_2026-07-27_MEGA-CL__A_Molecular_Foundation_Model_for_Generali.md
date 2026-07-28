---
title: MEGA-CL: A Molecular Foundation Model for Generalizable ADMET Prediction through Graph External Attention and Contrastive Learning
url: http://arxiv.org/abs/2607.24314v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_11-58-56Z_MEGA_CL_AMolecularFoundationModelforGeneralizableA.md
generated_at: 2026-07-27 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MEGA-CL, a foundation graph neural network that combines self‑supervised contrastive learning with external attention and enhanced message passing to predict ADMET properties of small molecules. Across 13 benchmark datasets and 21 tasks, MEGA-CL outperforms state‑of‑the‑art models, achieving clinically relevant accuracy with predictions within a three‑fold error range on clearance and volume of distribution.

## Key Takeaways
- MEGA-CL integrates self‑supervised contrastive learning to capture both local substructures and global inter‑graph relationships while reducing over‑smoothing.  
- The model consistently improves performance across 21 ADMET tasks, especially on challenging regression problems such as clearance (CL) and steady‑state volume of distribution (VDss).  
- In an external test set of 18 novel FDA‑approved compounds, more than half of human liver microsome clearance predictions were within a two‑fold error range.

## Context
This work advances molecular AI by applying contrastive learning to graph neural networks, which is a trend toward self‑supervised pre‑training for drug discovery. The integration of external attention allows the model to leverage broader chemical context beyond local atom interactions, improving generalization to unseen molecules.

## Implications
MEGA-CL can accelerate in‑silico ADMET evaluation, enabling early optimization of drug candidates and reducing reliance on costly experimental assays. Its robust performance suggests a practical tool for pharmaceutical companies seeking faster, more accurate predictions during lead selection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24314v1)
