---
title: Multi-Granular Rationale-Guided Molecular LLM for Property Prediction
url: http://arxiv.org/abs/2608.10480v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_04-50-33Z_Multi_GranularRationale_GuidedMolecularLLMforPrope.md
generated_at: 2026-08-11 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MR-MoL, a multi‑granular rationale‑guided molecular language model that directly surfaces the substructural contributions of GNN‑derived scores to property prediction. By ranking and tagging influential fragments as evidence, the model improves performance across eight MoleculeNet benchmarks compared with both generalist and task‑specific models.

## Key Takeaways
- The method extracts GNN attentions from each substructure, masks them, and ranks them into a rationale that includes Murcko scaffolds, BRICS fragments, and functional groups.  
- The rationale is presented as direction‑tagged evidence read alongside the SMILES sequence and molecular graph, not merely as additional context.  
- Five diagnostics demonstrate that the model’s predictions change with the rank, direction, and substructure of the rationale, confirming it learns from the internal attributions.

## Context
Molecular property prediction relies heavily on large language models that process molecules via SMILES or graphs, yet the causal role of individual substructures remains hidden. Recent retrieval‑augmented approaches use external data, but MR-MoL innovates by generating internal rationales directly from learned GNN scores.

## Implications
This approach can be adopted by drug discovery teams to interpret model outputs and prioritize structural modifications that drive property changes. By providing transparent, graded evidence of substructural influence, it bridges the gap between black‑box predictions and actionable chemistry insights.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10480v1)
